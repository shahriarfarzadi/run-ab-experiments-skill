# Experiment plan: [name]

## Status and ownership

- Experiment ID:
- Decision owner:
- Product/engineering owner:
- Data owner:
- Reviewers: experimentation / privacy / security / ethics / legal as needed
- Status: draft / approved / ramping / measuring / stopped / completed
- Readiness: ready / conditionally ready / blocked
- One active decision:
- Current gate:
- Cognitive load: low / medium / high — [cause]
- Experiment control board:
- Book basis: Chapters
- Planned dates:
- Links: specification / code / dashboard / metric definitions / prior tests

## Confirmed context and assumptions

- Context-and-assumptions register:
- Confirmed by:
- Confirmation date:
- User-approved unknowns or limitations:
- Material context changes after confirmation:

If material context changed, revise the register and obtain confirmation again
before completing this plan.

## Decision and hypothesis

- Decision this experiment informs:
- Available actions: ship / do not ship / iterate / replicate / other
- Hypothesis:
- Mechanism:
- Target population:
- Smallest effect worth acting on:
- Cost and downside assumptions:

## Population and causal estimand

- Eligibility:
- Exclusions:
- Trigger condition:
- Unit of randomization:
- Unit of analysis:
- Stable identifier and persistence:
- Estimand in words:
- Analysis window:
- Attribution/maturation window:
- External-validity boundary:

## Variants and assignment

| Variant | Exact experience | Version | Planned share | Fallback |
|---|---|---|---:|---|
| Control |  |  |  |  |
| Treatment |  |  |  |  |

- Assignment algorithm and seed/version:
- Exposure event:
- Concurrent-experiment policy:
- Carryover/contamination controls:
- Interference mechanism and mitigation:

## Metrics

| Metric | Role | Formula/unit | Population/window | Direction | Practical threshold | Source/owner |
|---|---|---|---|---|---:|---|
|  | OEC/primary |  |  |  |  |  |
|  | organizational guardrail |  |  |  |  |  |
| SRM | trust guardrail | observed versus planned unit counts | assigned and triggered | pass | p >= [threshold] | assignment logs |

For every metric, link or append its exact numerator, denominator, joins,
deduplication, missingness, bot/fraud handling, capping, and version.

## Statistical plan

- Framework and test:
- Sidedness:
- Alpha:
- Power target:
- Baseline and source period:
- Variance and randomization unit:
- Absolute/relative minimum detectable effect:
- Required units per arm and total:
- Expected eligible and triggered traffic per day:
- Planned duration and weekly-cycle coverage:
- Confidence interval:
- Multiple-testing family and correction:
- Variance estimator for ratio/clustered/nonlinear metrics:
- Fixed-horizon or sequential stopping rule:
- Missing-data and outlier rules:
- Confirmatory segments:

## Ramp and monitoring

| Phase | Treatment exposure | Minimum time/units | Promotion checks | Automatic stop |
|---|---:|---:|---|---|
| Team/internal |  |  |  |  |
| Small production |  |  |  |  |
| Maximum-power measurement |  |  |  |  |
| Capacity ramp |  |  |  |  |
| Optional holdout/replication |  |  |  |  |

- Near-real-time safety metrics:
- Alert owners and channels:
- Rollback procedure:
- Peak-capacity validation:

## Integrity and instrumentation

- [ ] Assignment, exposure, trigger, and version events are logged.
- [ ] Unit IDs join outcomes without unexpected one-to-many expansion.
- [ ] Control and treatment instrumentation is symmetric.
- [ ] SRM runs overall, by ramp stage, and in triggered analysis.
- [ ] Telemetry fidelity, missingness, duplicates, cache, and runtime invariants exist.
- [ ] A/A validation covers this allocation, unit, metric, and pipeline.
- [ ] Experiment restart and residual-exposure rules are defined.

## Ethics, privacy, and user risk

- Expected participant benefit and possible harms:
- Deception or behavioral manipulation:
- Sensitive, identifiable, or linkable data:
- User expectations, notice, consent, or opt-out:
- Fair distribution of risk and benefit:
- Data minimization, access, retention, audit, and incident response:
- Required review and approval:

## Decision rules

- Ship when:
- Do not ship when:
- Guardrail vetoes:
- Declare inconclusive when:
- Declare invalid when:
- Replicate when:
- Long-term follow-up when:

## Open issues before launch

| Issue | Why it matters | Owner | Due date | Status |
|---|---|---|---|---|
|  |  |  |  |  |

- Deliberately deferred:
- Return gate for deferred work:

## Institutional record after completion

- Actual dates, allocation changes, and incidents:
- Final report:
- Decision and rationale:
- Screenshots/artifacts:
- Follow-up experiments:
- Cleanup owner and deadline:
