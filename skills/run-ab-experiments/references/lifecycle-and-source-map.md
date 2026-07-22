# Lifecycle, Cognitive Load, and Source Map

Use this reference after the context-and-assumptions register is confirmed. It
controls the three modes—Plan, Manage, Interpret—and keeps the workflow anchored
to Ron Kohavi, Diane Tang, and Ya Xu, *Trustworthy Online Controlled
Experiments* (Cambridge University Press, 2020).

## Contents

- [Operating principle](#operating-principle)
- [Cognitive-load review](#cognitive-load-review)
- [End-to-end lifecycle](#end-to-end-lifecycle)
- [Mode 1: Plan](#mode-1-plan)
- [Mode 2: Manage and intervene](#mode-2-manage-and-intervene)
- [Mode 3: Interpret and analyze](#mode-3-interpret-and-analyze)
- [Handoffs and state control](#handoffs-and-state-control)
- [Book chapter map](#book-chapter-map)

## Operating principle

Maintain one source of truth:

1. Context-and-assumptions register: what the experiment means.
2. Experiment plan: what was decided before outcomes.
3. Control board: where the experiment is now and what decision is active.
4. Analysis report: what the trustworthy evidence supports.
5. Institutional record: what happened, why, and what follows.

Do not duplicate these artifacts. Link them. A fact belongs in one authoritative
place; other artifacts reference it.

Work exhaustively behind the scenes but expose only the information needed for
the current gate. Do not discuss analysis while the active decision is launch
readiness. Do not reopen metric design during interpretation unless a flaw makes
the original metric invalid; label any replacement exploratory.

## Cognitive-load review

At the start and end of every lifecycle step, score five dimensions:

| Dimension | 0 — controlled | 1 — manageable | 2 — material |
|---|---|---|---|
| Ambiguity | Definitions and scope are fixed | Minor gaps do not change the gate | Competing meanings or material unknowns |
| Open decisions | One clear decision | Two linked decisions | Several coupled or unowned decisions |
| Evidence complexity | One trusted source | Several reconcilable sources | Conflicting, missing, or high-dimensional evidence |
| Risk | Reversible and bounded | Monitored moderate risk | User, business, validity, ethical, or operational risk is high |
| Dependencies | Inputs and owners ready | One scheduled dependency | Missing owner, approval, system, or critical input |

Add the scores:

- **0–3, low:** proceed through the gate.
- **4–6, medium:** proceed only if validity, safety, ownership, and decision
  rules are resolved; defer the rest explicitly.
- **7–10, high:** do not advance. Reduce load first.

Use this compact user-facing format:

```text
Load: Medium (5/10)
Causes: metric denominator unclear; rollback owner missing
Reduce now: confirm denominator; assign rollback owner
Deferred: long-term holdout design until the primary test passes
```

Reduce load by:

- resolving one definition rather than discussing several downstream effects;
- converting repeated prose into one table or checklist;
- fixing one owner and deadline per action;
- separating safety monitoring from outcome inference;
- limiting the current display to one decision, seven inputs, and three risks;
- deferring future-stage work with an explicit return gate;
- linking formulas and diagnostics rather than restating them;
- using stable labels: assigned, exposed, triggered, analyzed.

Do not reduce load by hiding a material unknown, collapsing distinct
populations, removing guardrails, or presenting an arbitrary default as fact.

## End-to-end lifecycle

Use the stages in order. Return to an earlier stage when a material premise
changes.

| Stage | Active decision | Required gate | Primary artifact | Book basis |
|---|---|---|---|---|
| 0. Discover | Do we understand the request? | User confirms context and assumptions | Context register | Preface; Ch. 1–3, 9 |
| 1. Frame | What decision and hypothesis matter? | Owner, action set, mechanism, practical threshold | Plan | Ch. 1–2 |
| 2. Feasibility and ethics | Should this be tested this way? | Randomization feasible; risk/review acceptable | Plan | Ch. 1, 9–11 |
| 3. Causal design | Who gets what, and what effect is identified? | Population, unit, variants, exposure, interference fixed | Plan | Ch. 12–14, 20, 22 |
| 4. Metrics | What defines success and harm? | OEC/key metrics and guardrails have data contracts | Plan | Ch. 5–7 |
| 5. Statistical plan | What evidence will be decisive? | MDE, variance, power, duration, multiplicity, stopping frozen | Plan | Ch. 17–18, 20 |
| 6. Readiness | Can execution be trusted and reversed? | Instrumentation, A/A, SRM, alerts, rollback pass | Plan/control board | Ch. 4, 12–13, 19, 21 |
| 7. Pre-MPR | Is treatment safe enough to measure? | Safety and trust checks pass at low exposure | Control board | Ch. 15, 21–22 |
| 8. MPR measurement | Is planned evidence accumulating validly? | Stable allocation, batch validity, horizon progress | Control board | Ch. 15–18, 20–21 |
| 9. Post-MPR | Is capacity or long-term learning required? | Primary measurement complete; added phase justified | Control board | Ch. 15, 23 |
| 10. Interpret | Are results valid and decision-relevant? | Trust → effect → practical threshold → guardrails | Analysis report | Ch. 2–3, 17–23 |
| 11. Decide | Which predeclared action follows? | Decision owner accepts evidence and limits | Analysis report | Ch. 2–3, 7 |
| 12. Close and learn | What must be cleaned up and retained? | Code/config cleanup; institutional record complete | Institutional record | Ch. 4, 8, 15, 23 |

At each stage:

1. State current stage and one decision.
2. Run the load review.
3. Check the gate with evidence.
4. Choose proceed, hold, return, stop, or invalidate.
5. Assign the next action and timestamp the transition.
6. State the relevant book chapters in one line.

## Mode 1: Plan

Plan mode covers stages 0–6.

### Required sequence

1. Confirm context and assumptions.
2. Define the decision, owner, deadline, and cost of errors.
3. Define hypothesis and mechanism.
4. Pass ethics and feasibility review.
5. Fix population, exclusions, assignment unit, identity, variants, trigger,
   estimand, and interference treatment.
6. Define OEC/key metrics, organizational guardrails, trust guardrails, and
   diagnostics with exact data contracts.
7. Set practical thresholds before statistical thresholds.
8. Set variance source, MDE, power, allocation, duration, stopping,
   multiplicity, segmentation, and outlier rules.
9. Verify instrumentation, A/A evidence, SRM, real-time safety, ownership,
   rollback, and ramp stages.
10. Freeze the plan and readiness decision.

### Concise plan output

Show:

- readiness: ready / conditionally ready / blocked;
- hypothesis and estimand in one sentence each;
- metric and guardrail table;
- sample/duration/stopping table;
- top three risks;
- unresolved inputs and owners;
- next gate and load review.

Move detailed definitions and formulas to linked appendices. Do not narrate the
same design in multiple forms.

## Mode 2: Manage and intervene

Manage mode covers stages 7–9 and may return to stages 3–6 after a material
change.

### Monitoring lanes

Keep two lanes distinct:

- **Safety/trust lane:** near-real-time; detects crashes, latency, severe user or
  business harm, telemetry failure, SRM, and shared-resource problems. It can
  stop or reduce exposure.
- **Decision lane:** validated batch analysis; follows the frozen horizon or
  sequential design. It determines efficacy and practical value.

Never promote efficacy evidence from the safety lane into the decision lane.

### Every management check

1. Confirm stage, current allocation, experiment version, elapsed time, matured
   units, and next scheduled gate.
2. Review safety, trust, and operational guardrails before outcome trends.
3. Check SRM overall and by relevant ramp period; check telemetry and invariants.
4. Compare evidence only with the predeclared promotion/stop rule.
5. Choose one action: continue, hold, ramp up, ramp down, stop, invalidate and
   restart, or complete measurement.
6. Explain validity impact before acting.
7. Log the action and update the control board.
8. Run the cognitive-load review; defer irrelevant diagnostics.

### Intervention rules

- **Safety failure:** ramp down or stop; protect users before preserving power.
- **Trust failure:** hold; hide outcome scorecards; debug before interpretation.
- **Code or model fix:** create a new version. Do not silently pool pre-fix and
  post-fix data.
- **Allocation change:** retain stage timestamps and analyze with correct
  stratification/weighting; guard against Simpson's paradox.
- **Eligibility or trigger change:** treat as an estimand change; reconfirm
  context and usually restart.
- **Metric/filter/query change:** preserve the original confirmatory analysis;
  label the new version exploratory unless predeclared change control applies.
- **Outcome-driven early stop:** allow only under the declared sequential rule.
- **Restart after exposure:** assess carryover, re-randomization, cookies, model
  learning, and returning-user bias.
- **Concurrent incident or launch:** record affected periods and populations;
  hold or restart if causal isolation is lost.

### Concise management output

```text
State: MPR measurement, day 5 of 7
Validity: At risk — triggered SRM failed
Decision now: Hold allocation
Evidence: triggered counts 48,120 vs 46,903; SRM p = ...
Action: Data owner debugs trigger pipeline by [time]
Load: Medium (4/10); deferred: efficacy metrics until SRM resolves
Book basis: Chapters 15, 20, 21
```

## Mode 3: Interpret and analyze

Interpret mode covers stages 10–12.

### Required sequence

1. **Validity:** reconcile the frozen plan, populations, exposure, ramp history,
   data quality, SRM, invariants, stopping, multiplicity, and interference.
2. **Effect:** report control and treatment values, units, denominators, windows,
   absolute/relative effects, uncertainty, and adjusted inference.
3. **Practical meaning:** compare the entire interval with benefit and harm
   thresholds; include guardrails and total-population impact.
4. **Decision:** apply the predeclared rule. Use only ship, do not ship,
   iterate/replicate, inconclusive, or invalid.
5. **Next action:** assign rollout, rollback, replication, further data,
   long-term measurement, cleanup, and recordkeeping.

### Concise analysis output

Keep the main result to one screen when possible:

```text
Validity: Valid / At risk / Invalid — one reason
Effect: [absolute and relative effect, CI, unit, population, window]
Practical meaning: [threshold comparison and guardrail result]
Decision: [one status]
Next action: [owner, action, deadline]
Load: [rating, cause, reduction/deferment]
Book basis: [chapters]
```

Put supporting metric tables, diagnostics, sensitivity checks, and exploratory
segments below. Do not repeat their numbers in prose. Do not explain standard
statistical concepts unless the user asks or misunderstanding changes the
decision.

## Handoffs and state control

Treat every mode transition as a handoff:

### Plan → Manage

- Freeze plan and version.
- Record readiness result and unresolved accepted risks.
- Assign dashboard, alert, rollback, and gate owners.
- Set the first scheduled management check.

### Manage → Interpret

- Freeze actual ramp and incident history.
- Confirm measurement and maturation completion.
- Identify all deviations from plan before outcomes.
- Lock the analysis version and data cutoff.

### Interpret → Manage or Close

- Convert decision into an explicit ramp, rollback, replication, or cleanup
  action.
- Preserve the analysis and its limitations.
- Do not overwrite the original decision record after follow-up evidence.

Return to discovery and confirmation whenever a new request changes the
decision, population, estimand, metric meaning, or authorized scope.

## Book chapter map

Use these anchors to check that advice remains source-grounded:

| Chapter | Primary contribution to this skill |
|---|---|
| Preface | Trustworthiness, skepticism, and checking unusually strong results |
| 1. Introduction and Motivation | Causality, necessary ingredients, tenets, strategy versus tactics |
| 2. End-to-End Example | Hypothesis, metrics, design, execution, interpretation, practical decisions |
| 3. Twyman's Law and Trustworthiness | Power, p-value misuse, peeking, multiplicity, internal/external validity, Simpson's paradox |
| 4. Platform and Culture | Experiment lifecycle, infrastructure, scaling, organizational process |
| 5. Speed Matters | Deliberate learning experiments and performance guardrails |
| 6. Organizational Metrics | Goal, driver, guardrail, diagnostic metrics; metric formulation and gaming |
| 7. Metrics and OEC | Experiment-suitable metrics, OEC, long-term alignment, Goodhart-style risks |
| 8. Institutional Memory | Experiment records, meta-analysis, organizational learning |
| 9. Ethics | Respect, beneficence, justice, risk, data collection, review processes |
| 10. Complementary Techniques | Logs, human evaluation, UXR, surveys, and triangulation |
| 11. Observational Causal Studies | Alternatives when controlled experiments are infeasible |
| 12. Client-Side Experiments | Client assignment, update/version realities, device/app guardrails |
| 13. Instrumentation | Client/server logs, joining sources, instrumentation culture |
| 14. Randomization Unit | Experience consistency, metric compatibility, user/analysis units |
| 15. Ramping | Speed-quality-risk framework; pre-MPR, MPR, post-MPR, holdout/replication |
| 16. Scaling Analyses | Processing, computation, near-real-time versus batch, scorecards |
| 17. Statistics | t-tests, intervals, normality, errors, power, multiplicity, replication |
| 18. Variance and Sensitivity | Ratio variance, outliers, transformations, CUPED, unit alignment |
| 19. A/A Tests | Platform validation, null distributions, allocation/hardware pitfalls |
| 20. Triggering | Exposure-focused sensitivity, counterfactual triggers, dilution, trigger trust checks |
| 21. SRM and Trust Guardrails | SRM hard gate, causes, debugging, telemetry/cache/cookie invariants |
| 22. Leakage and Interference | Social, marketplace, shared-resource interference and isolation designs |
| 23. Long-Term Effects | Long-running tests, cohorts, post-period, staggered, holdback/reverse designs |

When a recommendation cannot be anchored to this map, label it as external
methodology or a context-specific inference. Do not attribute it to the book.
