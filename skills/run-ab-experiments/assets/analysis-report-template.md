# Experiment analysis: [name]

## Confirmed context and authorization

- Context-and-assumptions register:
- Confirmed by:
- Confirmation date:
- Authorized artifacts, queries, metrics, populations, and periods:
- User-approved unknowns or limitations:
- Material context changes after confirmation:

If material context changed, stop, revise the register, and obtain confirmation
again before interpreting results.

## One-screen conclusion

- **Validity:** valid / at risk / invalid — [one reason]
- **Effect:** [absolute and relative effect, CI, unit, population, window]
- **Practical meaning:** [benefit/harm threshold and guardrail comparison]
- **Decision:** ship / do not ship / iterate or replicate / inconclusive / invalid
- **Next action:** [owner, action, deadline, next gate]
- **Cognitive load:** low / medium / high — [cause and reduction/deferment]
- **Book basis:** Chapters

Do not repeat these numbers below. Use the detailed sections only as evidence.

## Plan and data

- Experiment ID and pre-registered plan:
- Variants and versions:
- Actual start/end and allocation changes:
- Eligibility, trigger, randomization unit, and analysis unit:
- Analysis version, query/code, data cutoff, and owner:
- Deviations from plan:

## Trust gate

| Check | Result | Threshold | Evidence | Consequence |
|---|---|---|---|---|
| Assignment reconciliation | pass/fail |  |  |  |
| Overall SRM | pass/fail | p >=  | observed vs expected counts |  |
| Triggered SRM | pass/fail/N/A | p >=  |  |  |
| Never-triggered complement | pass/fail/N/A | A/A-like |  |  |
| Telemetry fidelity and missingness | pass/fail |  |  |  |
| Invariant metrics | pass/fail |  |  |  |
| Contamination/carryover | pass/fail |  |  |  |
| Shared-resource/interference risk | pass/fail |  |  |  |

If a required trust check fails, stop here, mark the outcome **invalid**, and
document the debugging and rerun plan.

## Exposure and sample

| Variant | Assigned units | Exposed units | Triggered units | Analysis units |
|---|---:|---:|---:|---:|
| Control |  |  |  |  |
| Treatment |  |  |  |  |

- Trigger rate:
- Planned versus actual power/MDE:
- Weekly-cycle, seasonality, and maturation coverage:

## Confirmatory results

| Metric | Role | Control | Treatment | Absolute effect [CI] | Relative effect [CI] | Adjusted p | Practical threshold | Decision read |
|---|---|---:|---:|---:|---:|---:|---:|---|
|  | OEC/primary |  |  |  |  |  |  |  |
|  | guardrail |  |  |  |  |  |  |  |

- Statistical test and variance estimator:
- Multiple-testing and stopping procedure:
- Triggered-to-overall impact method:

## Diagnostic evidence

- Mechanism metrics:
- Time/cohort trend and novelty/primacy:
- Pre-specified segment interactions:
- Outlier and sensitivity analyses:
- Runtime, cache, and capacity signals:

Label every unplanned metric, segment, filter, or model as exploratory and state
the enlarged search space.

## Decision application and next action

- Predeclared rule applied:
- Metric tradeoff or guardrail consequence not already shown above:
- Action, owner, deadline, and verification gate:
- Launch/ramp or rollback instruction:
- Replication, long-term follow-up, or cleanup:

## Limits and deferred questions

- Remaining uncertainty that could change the decision:
- Generalization limit across users, platforms, markets, or time:
- Interference or long-term assumption:
- Deliberately deferred analysis and its return gate:

## Institutional record

- Final dashboard and analysis links:
- Incidents and deviations:
- Screenshots/artifacts:
- Lessons for metrics, platform, or future ideas:
- Owners and due dates for follow-up:
