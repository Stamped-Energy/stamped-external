# Vision identity lint — fail if live docs teach the withdrawn company.
# Skips: archive/, CHANGELOG.md, .git/
param(
  [string]$Root = (Split-Path $PSScriptRoot -Parent)
)

$ErrorActionPreference = "Stop"
$fail = New-Object System.Collections.Generic.List[string]

$patterns = @(
  @{ Name = "Stamped Energy product"; Regex = "Stamped Energy" },
  @{ Name = "two pillars"; Regex = "(?i)two pillars|two-pillar|Two Pillar" },
  @{ Name = "15-20 percent identity"; Regex = "15\s*[-~]\s*20\s*%|15\s*to\s*20\s*%" },
  @{ Name = "prescriptive energy intelligence"; Regex = "(?i)prescriptive energy intelligence" },
  @{ Name = "ADR-026 live cite"; Regex = "ADR-026-two-pillars|ADR-024-holistic-plant" }
)

$files = Get-ChildItem -Path $Root -Recurse -Include *.md,*.mdc -File | Where-Object {
  $p = $_.FullName
  if ($p -match '\\.git\\|\\archive\\|\\node_modules\\|\\\.cursor\\') { return $false }
  if ($_.Name -eq "CHANGELOG.md") { return $false }
  return $true
}

foreach ($f in $files) {
  $text = Get-Content -Raw -LiteralPath $f.FullName -ErrorAction SilentlyContinue
  if (-not $text) { continue }
  foreach ($pat in $patterns) {
    if ($text -match $pat.Regex) {
      $rel = $f.FullName.Substring($Root.Length).TrimStart('\', '/')
      [void]$fail.Add("$($pat.Name): $rel")
    }
  }
}

$unique = $fail | Select-Object -Unique
if ($unique.Count -gt 0) {
  Write-Host "VISION IDENTITY LINT FAILED ($($unique.Count))"
  $unique | ForEach-Object { Write-Host " - $_" }
  exit 1
}

Write-Host "VISION IDENTITY LINT OK ($($files.Count) files)"
exit 0
