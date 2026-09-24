#!/usr/bin/env python3
"""Deterministic 1-factory pilot AWS cost from public Price List offer files (ap-south-1).

No AWS credentials required — uses published offer JSON.
Labels: ACTUAL = from offer file; ESTIMATED = FX conversion only.
Run: python scripts/pricing/pilot-aws-one-factory.py
"""
from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USD_INR = 83.5  # ESTIMATED FX — not a mid-market quote
HOURS = 730
REGION = "ap-south-1"
CACHE = Path(__file__).resolve().parent / ".offer-cache"


def fetch_json(url: str, timeout: int = 300) -> dict:
    CACHE.mkdir(parents=True, exist_ok=True)
    name = url.rstrip("/").replace("https://", "").replace("/", "_")
    path = CACHE / f"{name}.json"
    if path.exists() and path.stat().st_size > 1000:
        return json.loads(path.read_text(encoding="utf-8"))
    req = urllib.request.Request(url, headers={"User-Agent": "stamped-pilot-cost/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = json.load(resp)
    path.write_text(json.dumps(data), encoding="utf-8")
    return data


def on_demand_usd(terms: dict, sku: str) -> float | None:
    od = terms.get("OnDemand", {}).get(sku, {})
    for term in od.values():
        for dim in term.get("priceDimensions", {}).values():
            return float(dim["pricePerUnit"]["USD"])
    return None


def find_ec2_t4g_small(offer: dict) -> float:
    products = offer["products"]
    terms = offer["terms"]
    for sku, p in products.items():
        attrs = p.get("attributes", {})
        if (
            attrs.get("instanceType") == "t4g.small"
            and attrs.get("operatingSystem") == "Linux"
            and attrs.get("tenancy") == "Shared"
            and attrs.get("capacitystatus") == "Used"
            and attrs.get("preInstalledSw") == "NA"
            and attrs.get("regionCode") == REGION
        ):
            usd = on_demand_usd(terms, sku)
            if usd is not None:
                return usd
    raise RuntimeError("EC2 t4g.small not found")


def find_gp3(offer: dict) -> float:
    products = offer["products"]
    terms = offer["terms"]
    for sku, p in products.items():
        attrs = p.get("attributes", {})
        usage = attrs.get("usagetype", "")
        if (
            attrs.get("volumeApiName") == "gp3"
            and "VolumeUsage.gp3" in usage
            and attrs.get("regionCode") == REGION
        ):
            usd = on_demand_usd(terms, sku)
            if usd is not None:
                return usd
    raise RuntimeError("gp3 storage not found")


def find_rds_t4g_small(offer: dict) -> float:
    products = offer["products"]
    terms = offer["terms"]
    for sku, p in products.items():
        attrs = p.get("attributes", {})
        if (
            attrs.get("instanceType") == "db.t4g.small"
            and attrs.get("databaseEngine") == "PostgreSQL"
            and attrs.get("deploymentOption") == "Single-AZ"
            and attrs.get("regionCode") == REGION
        ):
            usd = on_demand_usd(terms, sku)
            if usd is not None:
                return usd
    raise RuntimeError("RDS db.t4g.small not found")


def find_public_ipv4(offer: dict) -> float:
    products = offer["products"]
    terms = offer["terms"]
    for sku, p in products.items():
        attrs = p.get("attributes", {})
        if attrs.get("group") == "VPCPublicIPv4Address" and attrs.get("regionCode") == REGION:
            usd = on_demand_usd(terms, sku)
            if usd is not None:
                return usd
    raise RuntimeError("Public IPv4 not found")


def find_fargate(offer: dict) -> tuple[float, float]:
    products = offer["products"]
    terms = offer["terms"]
    cpu = mem = None
    for sku, p in products.items():
        attrs = p.get("attributes", {})
        if attrs.get("regionCode") != REGION:
            continue
        usage = attrs.get("usagetype", "")
        if "Fargate-vCPU-Hours" in usage and "perCPU" in usage and "Spot" not in usage:
            cpu = on_demand_usd(terms, sku)
        if usage.endswith("Fargate-GB-Hours") or usage.endswith("Fargate-GB-Hours:perGB"):
            if "Spot" not in usage and "ARM" not in usage.upper().replace("FARGATE", ""):
                # Prefer standard (Graviton often has ARM in name — take first non-spot)
                if mem is None:
                    mem = on_demand_usd(terms, sku)
    # Second pass: APS3-prefixed
    if cpu is None or mem is None:
        for sku, p in products.items():
            attrs = p.get("attributes", {})
            usage = attrs.get("usagetype", "")
            if attrs.get("regionCode") != REGION:
                continue
            if usage == "APS3-Fargate-vCPU-Hours:perCPU":
                cpu = on_demand_usd(terms, sku)
            if usage == "APS3-Fargate-GB-Hours":
                mem = on_demand_usd(terms, sku)
    if cpu is None or mem is None:
        raise RuntimeError(f"Fargate rates not found cpu={cpu} mem={mem}")
    return cpu, mem


def find_s3_standard(offer: dict) -> float:
    products = offer["products"]
    terms = offer["terms"]
    for sku, p in products.items():
        attrs = p.get("attributes", {})
        if (
            attrs.get("volumeType") == "Standard"
            and attrs.get("regionCode") == REGION
            and "TimedStorage" in attrs.get("usagetype", "")
        ):
            usd = on_demand_usd(terms, sku)
            if usd is not None:
                return usd
    # fallback any Standard storage
    for sku, p in products.items():
        attrs = p.get("attributes", {})
        if attrs.get("volumeType") == "Standard" and attrs.get("regionCode") == REGION:
            usd = on_demand_usd(terms, sku)
            if usd is not None:
                return usd
    raise RuntimeError("S3 Standard not found")


def main() -> None:
    base = "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws"
    print("Fetching offer files (may take a minute)...", flush=True)
    ec2 = fetch_json(f"{base}/AmazonEC2/current/{REGION}/index.json")
    rds = fetch_json(f"{base}/AmazonRDS/current/{REGION}/index.json")
    vpc = fetch_json(f"{base}/AmazonVPC/current/{REGION}/index.json")
    ecs = fetch_json(f"{base}/AmazonECS/current/index.json")
    s3 = fetch_json(f"{base}/AmazonS3/current/{REGION}/index.json")

    ec2_h = find_ec2_t4g_small(ec2)
    gp3 = find_gp3(ec2)
    rds_h = find_rds_t4g_small(rds)
    ipv4_h = find_public_ipv4(vpc)
    fargate_cpu, fargate_mem = find_fargate(ecs)
    s3_gb = find_s3_standard(s3)

    lines = [
        ("EC2 t4g.small (Mosquitto)", ec2_h * HOURS, f"${ec2_h}/hr ACTUAL"),
        ("RDS db.t4g.small Single-AZ Postgres", rds_h * HOURS, f"${rds_h}/hr ACTUAL"),
        ("EBS gp3 50 GB (RDS share)", gp3 * 50, f"${gp3}/GB-mo ACTUAL"),
        ("Public IPv4 ×1", ipv4_h * HOURS, f"${ipv4_h}/hr ACTUAL"),
        (
            "Fargate 0.25 vCPU / 0.5 GB",
            (0.25 * fargate_cpu + 0.5 * fargate_mem) * HOURS,
            f"cpu ${fargate_cpu}/vCPU-hr mem ${fargate_mem}/GB-hr ACTUAL",
        ),
        ("S3 Standard 5 GB (bills)", s3_gb * 5, f"${s3_gb}/GB-mo ACTUAL"),
        ("CloudWatch Logs ~5 GB ingest", 0.50 * 5, "$0.50/GB ESTIMATED fallback (CW filter flaky)"),
    ]

    total_usd = sum(x[1] for x in lines)
    out = {
        "as_of_utc": datetime.now(timezone.utc).isoformat(),
        "region": REGION,
        "hours_per_month": HOURS,
        "fx_usd_inr": USD_INR,
        "fx_label": "ESTIMATED",
        "lines": [
            {
                "component": name,
                "monthly_usd": round(usd, 4),
                "monthly_inr_est": round(usd * USD_INR, 2),
                "detail": detail,
            }
            for name, usd, detail in lines
        ],
        "total_monthly_usd": round(total_usd, 4),
        "total_monthly_inr_est": round(total_usd * USD_INR, 2),
        "notes": [
            "Infrastructure only — excludes frontier LLM API tokens (main variable cost).",
            "Shared stamped-pilot RDS: one-factory incremental cost may be near-zero for DB if already provisioned.",
            "Do not stand up a second VPC for LNM.",
            "ADR-002 ceiling ₹15–25k/mo is for ≤10 plants; one factory should sit well under that.",
        ],
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
