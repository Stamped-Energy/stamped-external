# Improve report template (Track C)

> Internal only — developers. Generated monthly by the Improve job ([stamped-improve-pipeline-spec.md](./stamped-improve-pipeline-spec.md), [ADR-025](../decisions/ADR-025-improve-loop-step-06.md)).  
> Do **not** auto-apply UI changes; implement approved items as plant-scoped L6 config.

```markdown
# Improve report — {{plant_id}} — {{yyyy-mm}}

## 1. Closure summary
| Metric | Value |
| Acted / done / verified | |
| Deferred | |
| Rejected | |
| Disputed | |
| Closure rate (30d) | |

## 2. Followed vs ignored contrast
| Dimension | Followed skew | Ignored skew |
| decision_class | | |
| waste_category | | |
| template_id | | |
| owner_role | | |
| effort | | |
| order_conflict | | |

## 3. Negotiation themes
| Tag / reason_code | Count | Notes |
| order_deadline | | |
| production_constraint | | |

## 4. Evidence challenges
| Chart / evidence type | Challenge count |

## 5. Friction hotspots (L6)
| Route / module | Signal |

## 6. Suggested UI tweaks (human review)
- [ ] …

## 7. Suggested L6 config pins
- nav_pins: …
- rx_card_extra_columns: tradeoff | order_impact
- default_department_filter: …

## 8. Track A / B drafts attached
- calibration_patch: draft | none
- preference_profile_version: draft N
```
