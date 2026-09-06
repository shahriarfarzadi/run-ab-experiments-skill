# Experiment-to-Business-Case Reference

Use this reference after the experiment's trust gates pass when a decision
depends on scaled impact, costs, capacity, opportunity cost, or a comparison of
rollout scenarios. It is industry-neutral: obtain all domain values and metric
mappings through the confirmed context-and-assumptions register.

This decision-accounting layer complements the experimentation method. Do not
attribute its accounting conventions or scenario formulas to Kohavi, Tang, and
Xu unless the source map explicitly does so.

## Contents

- [Prerequisites](#prerequisites)
- [Input contract](#input-contract)
- [Translate the causal effect](#translate-the-causal-effect)
- [Build scenarios](#build-scenarios)
- [Construct the value ledger](#construct-the-value-ledger)
- [Targeted and conditional interventions](#targeted-and-conditional-interventions)
- [Uncertainty and break-even](#uncertainty-and-break-even)
- [Decision gate](#decision-gate)
- [Audit checklist](#audit-checklist)

## Prerequisites

Do not build a decision case from an invalid causal estimate. First establish:

- a passed or explicitly bounded experiment-validity assessment;
- the estimand and its randomization and analysis units;
- arm values, absolute effect, uncertainty interval, population, and window;
- the decision owner, available actions, and practical thresholds;
- accepted limits on external validity and outcome maturation.

If trust fails, use outcome data only to diagnose the failure. If evidence is
inconclusive, a scenario model may quantify the value of more information, but
must not present the point estimate as established impact.

## Input contract

Classify every input:

| Class | Examples | Required treatment |
|---|---|---|
| Experiment evidence | Absolute effect, interval, eligible units | Preserve unit, population, and time window |
| Observed operating input | Current volume, adoption, capacity | Record source and as-of period |
| Domain value | Value or cost per outcome | State basis, timing, and owner |
| Working assumption | Future take-up or persistence | Label and vary in sensitivity analysis |
| Unknown | Cannibalization or downstream harm | Show decision consequence and verification path |

Do not mix counts of assigned units, exposed units, actors, transactions,
events, or outcomes. If the experiment measures actors with at least one
outcome, do not call the estimate a transaction count. Convert only with a
measured or explicitly assumed relationship.

## Translate the causal effect

Prefer the absolute effect in natural units:

```text
incremental outcomes
= target eligible units
x expected exposure or adoption share
x absolute causal effect per exposed or assigned unit
```

Match the scale factor to the estimand. An intention-to-treat effect already
contains non-exposure and non-compliance in the tested assignment policy; do
not multiply it by an additional take-up factor unless the target policy differs.

For a triggered effect, translate through the tested trigger population and
recompute overall impact whenever possible. Do not multiply a relative effect
by a trigger rate without a metric-specific derivation.

Record differences between the test and target rollout:

- eligible population and composition;
- exposure, adoption, and compliance;
- duration, recurrence, maturation, and persistence;
- treatment intensity and implementation version;
- capacity, equilibrium, interference, and displacement.

Treat extrapolation beyond the tested range as an assumption, not another
experiment result.

## Build scenarios

Name a baseline and construct only decision-relevant alternatives. Depending on
the decision, scenarios may include status quo, full rollout, targeted rollout,
staged rollout, a conditional policy, a different treatment, or no action.

For each scenario reconcile mutually exclusive populations:

| Population | Units | Experience or policy | Expected outcomes | Value/cost treatment |
|---|---:|---|---:|---|
| Unaffected |  |  |  |  |
| Existing-policy participants |  |  |  |  |
| New treatment recipients |  |  |  |  |
| Displaced or cannibalized units |  |  |  |  |

The population rows must sum to the scenario's target population unless an
explicitly named group is out of scope.

## Construct the value ledger

Use components rather than one unexplained blended value:

```text
absolute scenario value
= sum(volume_i x per-unit benefit_i)
- sum(volume_j x per-unit variable cost_j)
- incremental fixed costs
- downstream harms or externalities valued for the decision
```

Then compare with the same scope and period:

```text
incremental value = scenario value - baseline value
```

Keep separate:

- cash receipts and cash costs;
- accounting revenue and expense;
- contribution before shared overhead;
- fixed and variable costs;
- lost revenue or displaced value;
- opportunity cost;
- capacity, quality, trust, safety, or fairness consequences that are not
  credibly monetized.

Never describe a positive absolute value as an improvement when incremental
value versus baseline is negative. Never count a transfer between internal
parties as new total value without naming the chosen organizational boundary.

When an outcome is purchased by sacrificing value, report:

```text
cost per incremental outcome
= -incremental value / incremental outcomes
```

Use this only when incremental value is negative and incremental outcomes are
positive. Compare it with an owner-approved willingness-to-pay threshold.

## Targeted and conditional interventions

For a policy applied only after a condition, separate:

1. units that complete the desired behavior before eligibility;
2. eligible units that would complete it later without intervention;
3. eligible units that receive or notice the intervention;
4. recipients whose behavior changes because of it;
5. recipients whose existing behavior is merely subsidized or displaced;
6. eligible units that do not respond.

Response or click-through is not incremental impact. Estimate the counterfactual
behavior of responders from random assignment when available. Otherwise label
natural progression and cannibalization as explicit assumptions and show a
range.

Charge variable cost only when the corresponding service or resource is
actually consumed. Charge communication or delivery cost to all units that
incur it, not only responders.

## Uncertainty and break-even

Propagate two types of uncertainty separately:

- **causal uncertainty:** use the experiment interval or an appropriate
  posterior/distribution for the effect;
- **business uncertainty:** use sourced ranges for volume, adoption, value,
  cost, persistence, displacement, and capacity.

At minimum show downside, central, and upside cases without presenting them as
equally likely unless probabilities are justified. Identify which input can
reverse the decision.

Useful break-even forms include:

```text
required incremental outcomes
= incremental cost / value per incremental outcome

required absolute effect
= required incremental outcomes / applicable target units

maximum acceptable unit cost
= gross incremental value before that cost / units consuming the cost
```

Derive the formula for the actual ledger rather than forcing an inapplicable
template. Use simulation when effects and inputs interact nonlinearly.

## Decision gate

Return one status:

- **proceed:** validity passes and the decision case clears practical,
  operational, and veto thresholds across the accepted uncertainty range;
- **proceed with limits:** a targeted or staged policy contains material risk
  and has explicit monitoring or stop conditions;
- **do not proceed:** incremental value or a veto guardrail fails;
- **inconclusive:** plausible business outcomes cross the decision boundary;
- **invalid:** experiment trust fails, so the causal business case is unusable.

A decision owner may knowingly choose growth, learning, safety, access, quality,
or another nonfinancial outcome over incremental financial value. Record that
tradeoff and its threshold; do not relabel the financial result.

## Audit checklist

- [ ] Experiment trust gates pass before causal scaling.
- [ ] The effect, scale, and value ledgers use compatible units and windows.
- [ ] Actors, transactions, events, and outcomes remain distinct.
- [ ] Baseline and alternatives cover the same organizational boundary.
- [ ] Scenario populations reconcile without double counting.
- [ ] Absolute and incremental value are both reported.
- [ ] Cash cost, accounting cost, and opportunity cost are separate.
- [ ] Natural progression, displacement, and cannibalization are addressed.
- [ ] Causal and business uncertainty are not collapsed into a point estimate.
- [ ] Break-even values and the decision-reversing assumptions are visible.
- [ ] Nonfinancial guardrails remain in the decision even when not monetized.
- [ ] The final recommendation names an owner, action, and verification gate.
