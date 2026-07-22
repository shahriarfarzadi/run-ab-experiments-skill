# Experiment Design Reference

This is an operational distillation of Ron Kohavi, Diane Tang, and Ya Xu,
*Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*
(Cambridge University Press, 2020). It summarizes the source; it does not
replace it. The authoring pass used the PDF for page-level extraction and the
EPUB to cross-check chapter structure and terminology. The skill is
self-contained; recipients do not need either book file to use it.

## Contents

- [The causal contract](#the-causal-contract)
- [Decision and hypothesis](#decision-and-hypothesis)
- [Population, eligibility, and triggering](#population-eligibility-and-triggering)
- [Randomization and analysis units](#randomization-and-analysis-units)
- [Variants and interference](#variants-and-interference)
- [Metric architecture](#metric-architecture)
- [Practical and statistical sensitivity](#practical-and-statistical-sensitivity)
- [Duration and stopping](#duration-and-stopping)
- [Instrumentation and assignment](#instrumentation-and-assignment)
- [Ramping](#ramping)
- [Ethics and data](#ethics-and-data)
- [Pre-launch checklist](#pre-launch-checklist)

## The causal contract

An online controlled experiment estimates a causal effect by randomly assigning
eligible units to a control experience or one or more treatment experiences.
The analysis is trustworthy only when these conditions are plausible:

- Assignment is random and stable.
- Every eligible unit has a known probability of entering each variant.
- Potential outcomes for a unit are not changed by other units' assignments,
  unless the design and analysis model that interference.
- Exposure, outcomes, and exclusions are measured comparably across variants.
- The analysis respects the assigned unit and the pre-specified stopping rule.
- The tested population, implementation, and period match the intended claim.

Use an experiment only when there are enough units, the intervention can be
implemented safely, the outcome can be measured, and the organization can act
on the result. When random assignment is infeasible, switch to an explicitly
observational design and weaken causal claims.

## Decision and hypothesis

Start with the decision, not the dashboard.

Define:

1. The decision and decision owner.
2. The proposed intervention and exact control.
3. The target population.
4. The hypothesized mechanism.
5. The expected direction and outcome.
6. The smallest effect worth acting on.
7. The launch, rollback, maintenance, and opportunity costs.
8. The actions available for positive, negative, neutral, inconclusive, and
   invalid evidence.

A useful hypothesis is falsifiable and names the metric and population. Example:

> For signed-in buyers who begin checkout, moving delivery estimates above the
> payment form will increase completed orders per eligible buyer by at least 1%
> without degrading refund rate, checkout latency, or support contacts beyond
> their pre-specified guardrails.

Do not use “users will like it” or “conversion will improve” as the complete
hypothesis. Record why the mechanism should change behavior so diagnostics can
distinguish an implementation failure from a failed idea.

## Population, eligibility, and triggering

Define eligibility before assignment where possible. Include:

- geography, locale, platform, version, account state, age or policy limits;
- new versus existing users;
- bots, employees, test accounts, and fraud handling;
- overlapping experiments or mutually exclusive layers;
- the date/time boundary and late-arriving events;
- identity rules across devices, cookies, login IDs, and shared accounts.

Use triggered analysis when many assigned units could not encounter any
difference between variants. Trigger on potential exposure, not on an outcome.
Examples include reaching checkout for a checkout change, receiving a weather
answer for a weather-card change, or producing different outputs between old
and new recommendation models.

Trustworthy triggering rules:

- Evaluate the same trigger logic for every variant.
- Base eligibility attributes on pre-treatment state.
- For model or coverage changes, generate the counterfactual when feasible and
  trigger when the actual and counterfactual experiences differ.
- Once a unit triggers, retain it for the remaining analysis window.
- Include all subsequent outcomes that the exposure might affect.
- Run SRM on triggered units.
- Analyze the never-triggered complement; it should resemble an A/A test.
- Report both the triggered effect and the overall population effect.

Do not filter to purchasers, clickers, adopters, survivors, or other groups
whose membership treatment can change. That is post-treatment selection bias.
Use intention-to-treat based on original assignment.

## Randomization and analysis units

Common units include event/page, query, session, user, account, tenant,
advertiser, geographic region, time block, and network cluster.

Choose the unit using two questions:

1. What level is needed for a consistent experience?
2. At what level are the decision metrics defined?

Prefer the randomization unit to equal the analysis unit. It may be coarser than
the analysis unit if the variance method handles within-unit correlation. It
must not be finer than a required user-level outcome: page-level randomization
cannot identify a coherent user-level retention effect when each user receives
a mix of variants.

User-level randomization is the default for visible product changes because it
preserves experience and permits longitudinal outcomes. Prefer a stable signed-
in ID when cross-device consistency matters. A cookie or device ID may be
necessary for pre-login flows, but document churn and privacy implications.
Avoid IP address except when infrastructure constraints leave no alternative;
it inconsistently represents individuals and organizations.

Use a deterministic, high-quality hash of stable unit ID, experiment namespace,
and seed. Verify independence across concurrent layers. Version assignments and
log the version with every exposure.

## Variants and interference

Specify each variant as an implementable contract:

- code, model, content, and configuration version;
- intended behavioral difference;
- eligibility and fallback behavior;
- assignment and exposure event;
- server, client, cache, or model-training side effects;
- data-quality and capacity expectations.

Avoid asymmetric redirects, logging, or execution paths. A redirect imposed
only on treatment changes latency and bot behavior and can contaminate variants
through bookmarks or shared links.

Interference violates the assumption that one unit's outcome depends only on
its own assignment. Look for:

- social messages, invitations, co-editing, or network effects;
- marketplace inventory, auctions, surge pricing, and shared budgets;
- shared CPU, memory, caches, queues, or rate limits;
- shared model-training data;
- carryover across sessions, time blocks, or sequential experiments.

Mitigations include splitting shared resources, randomizing by geo or time,
network-cluster or ego-centric designs, edge-level analysis, and measuring the
downstream ecosystem value of actions. These designs trade bias for variance;
state the remaining interference and effective sample size.

## Metric architecture

### Business taxonomy

- **Goal metric:** the durable outcome the organization ultimately values.
- **Driver metric:** a sensitive, actionable leading indicator believed to
  cause movement in the goal.
- **Organizational guardrail:** a constraint that protects users, operations,
  or the business while optimizing another outcome.
- **Trust guardrail:** an invariant or data-quality signal used to decide
  whether experiment results are valid.
- **Diagnostic metric:** evidence used to explain a key metric, not to define
  success post hoc.

### Experiment metric requirements

Every decision metric should be:

- measurable during the experiment;
- attributable to a variant;
- sensitive enough for the available units and duration;
- timely enough for the decision;
- aligned with long-term value;
- interpretable and actionable;
- resistant to gaming and known failure modes.

Define each metric as a data contract:

| Field | Required definition |
|---|---|
| Name and role | OEC, primary, secondary, organizational guardrail, trust guardrail, or diagnostic |
| Formula | Numerator, denominator, aggregation, and unit |
| Population | Eligible, assigned, exposed, triggered, or overall |
| Window | Start, end, attribution delay, and late-event rule |
| Direction | Higher, lower, or target range |
| Threshold | Smallest meaningful gain or maximum tolerated harm |
| Source | Events/tables, joins, version, and owner |
| Quality | Bot/fraud logic, deduplication, capping, missingness, and invariants |

Normalize totals by actual sample size. For example, revenue per assigned or
triggered user is generally useful; total revenue is confounded by random
variation in arm size.

Choose the denominator that includes every unit that could be affected and no
unit selected by a treatment-influenced outcome. For a checkout intervention,
users who start checkout can be valid; purchasers alone are not.

### OEC

An Overall Evaluation Criterion makes the tradeoff among key objectives
explicit. It should be measurable in the short term while plausibly causing
long-term strategic value. If a weighted OEC cannot be defended, use a small
set of key metrics and write the decision rules for mixed directions in advance.

Audit every OEC for Goodhart-style gaming. Revenue, clicks, queries, or time on
site can rise while user value falls. Add quality, retention, unsubscribe,
abandonment, or other counter-metrics that capture the failure mode.

A practical starting decision logic is:

- all key metrics nonnegative and at least one meaningful positive: candidate
  to ship if guardrails pass;
- all nonpositive and at least one meaningful negative: do not ship;
- all compatible only with negligible changes: stop or reprioritize;
- meaningful mixed directions: apply the predeclared tradeoff or escalate;
- confidence intervals still include meaningful benefit and harm: inconclusive.

## Practical and statistical sensitivity

Statistical significance asks whether the observed effect is inconsistent with
a null model. Practical significance asks whether the magnitude is worth acting
on. Set the practical boundary first and size the experiment to detect it.

Power depends on effect size, variance, allocation, alpha, and sample size. A
test powered to detect a 10% change may be badly underpowered for 1%. Use
historical variance from the same unit, population, metric definition, and time
window. Default to at least 80% power and a two-sided 5% alpha unless risk and
decision costs justify another predeclared choice.

Improve sensitivity without changing the causal question by:

- using a more stable metric that captures the same value;
- capping, binarizing, or transforming heavy-tailed metrics when the transformed
  quantity still represents the decision;
- triggering on potential exposure;
- using pre-experiment covariates, stratification, post-stratification, or
  CUPED-style adjustment;
- pooling compatible control groups;
- using paired or interleaved designs where appropriate.

Do not optimize sensitivity by filtering on post-treatment behavior, changing
the metric after seeing results, or using a finer randomization unit that breaks
experience consistency or the desired estimand.

## Duration and stopping

Run for at least one complete weekly cycle by default. One-day experiments
overrepresent frequent users and miss weekday/weekend differences. Extend when:

- unique units accumulate slowly;
- seasonality or holidays are material;
- novelty causes an early spike that decays;
- primacy or learning causes a delayed effect;
- metrics need an attribution or maturation window;
- long-term retention or marketplace equilibrium matters.

For fixed-horizon tests, choose the end date before launch and evaluate the
confirmatory result once at that horizon. Ordinary p-values are not valid under
repeated peeking and optional stopping. If continuous decisions are required,
use a pre-specified sequential design with always-valid inference.

Plot cohort- or day-specific effects to diagnose novelty and primacy. Do not
mistake the mechanically changing composition of cumulative users for a time
trend.

## Instrumentation and assignment

At minimum log:

- stable unit ID and assignment time;
- experiment, layer, seed, allocation, and version;
- assigned variant and actual exposure;
- trigger reason and counterfactual difference when used;
- event ID, event time, outcome value, and source version;
- pre-treatment segment dimensions;
- errors, latency, cache, resource use, telemetry fidelity, and fallbacks.

Validate joins and cardinality across assignment, exposure, and outcome logs.
Check for missing, duplicate, delayed, or treatment-dependent data. Confirm that
the same user cannot enter incompatible variants and that restarting an
experiment does not silently mix residual exposure with new assignments.

For a new platform or metric pipeline, run repeated A/A tests. Under a valid
continuous null test, p-values should be approximately uniform and false
positives should occur near the selected alpha. Also reconcile aggregate users,
revenue, or other key measures with the system of record.

## Ramping

Use four conceptual phases:

1. **Pre-maximum-power:** mitigate risk with team, employee, beta, data-center,
   or small-percentage rings; monitor near-real-time safety metrics.
2. **Maximum-power allocation:** collect decision evidence, commonly with a
   balanced control/treatment split; remain for at least a weekly cycle and
   longer for novelty or primacy.
3. **Post-measurement capacity:** optionally increase exposure in short stages
   to verify peak operational load.
4. **Long-term holdout or replication:** use only for a stated question about
   durability, delayed effects, a long-horizon true-north metric, or a surprising
   result.

Stop or ramp down quickly when safety or trust guardrails fail. Do not spend
weeks in low-power ramps attempting to infer an outcome they cannot measure.
After final launch, remove dead branches, defaults, and obsolete experiment
configuration.

## Ethics and data

Assess three principles:

- **Respect:** transparency, truthfulness, autonomy, meaningful choice, and
  special protection where autonomy is limited.
- **Beneficence:** realistic benefits versus physical, psychological, social,
  financial, privacy, and opportunity harms.
- **Justice:** fair distribution of risks and benefits; avoid exploiting a
  convenient or vulnerable population.

Ask:

- Could either arm be shipped to all users under ordinary standards?
- Is there genuine uncertainty, or is one arm known to be materially worse?
- Does the intervention deceive, manipulate relationships, or exploit
  behavioral vulnerabilities?
- What data is necessary, sensitive, identifiable, linkable, or discriminatory?
- What do users reasonably expect about collection and experimentation?
- Who can access the data, for what purpose, for how long, with what audit trail?
- What happens if the data is exposed or the intervention causes harm?
- Is consent, notice, opt-out, expert review, or an ethics/IRB-like process
  required?

Use the organization's current legal, privacy, security, and research-ethics
policies. Applicable laws and product policies are time-sensitive; verify them
from authoritative sources rather than relying on this reference.

## Pre-launch checklist

- [ ] The question-first interview is complete and the user confirmed the
      context-and-assumptions register.
- [ ] The experiment control board shows one active decision, the readiness
      gate, top three risks, next owner/action, and a low or accepted-medium
      cognitive-load rating.
- [ ] Decision, owner, and action set are explicit.
- [ ] Hypothesis, mechanism, and practical threshold are predeclared.
- [ ] Eligibility, exclusions, trigger, population, and estimand are defined.
- [ ] Randomization unit supports experience consistency and all key metrics.
- [ ] Interference, carryover, identity churn, and concurrent tests are handled.
- [ ] Variants and exposure are versioned and instrumented symmetrically.
- [ ] OEC/key metrics, organizational guardrails, trust guardrails, and
      diagnostics have complete data contracts.
- [ ] Historical baselines and variance support the sample-size calculation.
- [ ] Alpha, power, sidedness, multiplicity, variance, and stopping rules are
      frozen.
- [ ] Duration covers a weekly cycle and relevant maturation effects.
- [ ] SRM and real-time safety thresholds have owners and rollback actions.
- [ ] A/A or end-to-end validation supports the platform and metric pipeline.
- [ ] Ethics, privacy, security, and legal review requirements are satisfied.
- [ ] Ramp plan and launch cleanup are defined.
- [ ] The final plan is stored before outcome data is inspected.
