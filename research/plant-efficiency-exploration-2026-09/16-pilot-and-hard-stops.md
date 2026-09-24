# Pilot 1 and where each hard stop lives

**Date:** 2026-09-24
**Status:** The first decision family on the coarse architecture.
**Authority:** [`09-stamped-founder-vision.md`](09-stamped-founder-vision.md) §13. Shape: [`14-coarse-architecture.md`](14-coarse-architecture.md).

## The family

Confirmed machine idle with extra loads still on. One owner. One card. Primary domain: energy. A recovered machine-minute, if shown, is a separate time section. The two effects are not added together.

Configured task class: operational. L4's language model selects the ops-head role from the configured set. L5 names the person on that shift.

Autonomy for this family: human only. It is not an autonomy class.

## Path

1. L1 reads the machine-state and auxiliary-load tags the edge path already accepts.
2. L2 stores them with provenance, freshness, and the condition key.
3. L3 emits one idle-load finding with a verification plan. A second detector on the same condition key merges into that finding.
4. L4 retains a world fact for the condition, recalls the plant bank, reflects a cited proposal, runs the cross-section check and the constraint gate, and emits or withholds. The calculator owns any rupee figure. Jev is not called.
5. L5 opens the card, assigns the ops head, and waits for accept, edit, reject, or defer. It then runs the verification plan.
6. L6 shows the one card, the domain sections, and the autonomy setting, which stays off.
7. L4 retains a short learning fact. The card body is not stored.

Exit, from `09`: cards repeat; a named role closes assign, act, and verify; peers accept the evidence format; rejection and no-change are recorded; the team can say what is measured, confirmed, modeled, or unknown.

The template lane runs only when the agent cannot emit a valid, cited, constraint-checked proposal.

Bills are context. They are not the verification source.

## Measurement and verification

The boundary is the auxiliary circuit the card names. The standard is IPMVP retrofit isolation, as summarized by [FEMP](https://stage.energy.gov/cmei/femp/measurement-and-verification-options-federal-energy-and-water-saving-projects) and [BEDES](https://bedes.lbl.gov/source/ipmvp).

- **Option B.** Both the load and the idle interval are measured inside that boundary. The effect may be labeled Measured and the card may close as verified.
- **Option A.** The key parameter is measured and the other is estimated. The estimate stays Modeled. The card must not call the whole effect verified.
- **Option C.** A plant-level or shared feeder meter. Wrong boundary for this card. It cannot close the auxiliary-load effect as verified.
- **Option D.** Calibrated simulation. Not the verification path.

Machine state still has to show idle. A load movement on a running machine is a different condition.

## Hard stops

- **No equipment write.** L1 has no write path. This card asks a person to act.
- **No invented rupee.** L3 and L4 use the calculator. A model tier never becomes a rupee field.
- **No outranking a known constraint.** The constraint is entered in L6 by a named plant owner, stored in L2, and read by L4's constraint gate.
- **No silent master-data, dispatch, quality, or maintenance action.** Those classes do not exist. L5's default is that every class is off. This pilot enables none.
- **Unverified close does not teach success.** `learning_eligible` is false without a verification result or an explicit reason. The plant bank may record that evidence was missing. It may not record that the loads were confirmed off.

Withhold stays off the customer card. Staff can see the trace.
