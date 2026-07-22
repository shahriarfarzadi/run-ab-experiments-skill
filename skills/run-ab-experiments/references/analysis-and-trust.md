# Analysis and Trust Reference

Use this reference for post-run analysis, statistical review, or platform
validation. It distills the analysis guidance in Kohavi, Tang, and Xu,
*Trustworthy Online Controlled Experiments* (2020).

## Contents

- [Analysis order](#analysis-order)
- [SRM gate](#srm-gate)
- [A/A validation](#aa-validation)
- [Estimating effects](#estimating-effects)
- [Variance and unit alignment](#variance-and-unit-alignment)
- [Heavy tails and outliers](#heavy-tails-and-outliers)
- [Multiplicity and peeking](#multiplicity-and-peeking)
- [Triggered analysis](#triggered-analysis)
- [Segments and time](#segments-and-time)
- [Interference and external validity](#interference-and-external-validity)
- [Decision classification](#decision-classification)
- [Diagnostic checklist](#diagnostic-checklist)

## Analysis order

Use this sequence:

1. Verify that the user confirmed the context-and-assumptions register and the
   authorized scope. Stop and interview first if not.
2. Update the experiment control board and run the cognitive-load review.
3. Retrieve the pre-registered design and metric definitions.
4. Reconcile assignment, eligibility, exposure, and time windows.
5. Run SRM and other trust guardrails.
6. Stop if trust fails; investigate without interpreting outcome metrics.
7. Compute arm summaries, absolute effects, relative effects, standard errors,
   confidence intervals, and p-values using the correct unit and estimator.
8. Apply the pre-specified stopping and multiple-testing methods.
9. Compare intervals with practical thresholds and organizational guardrails.
10. Inspect time and pre-treatment segments for explanation and generalization.
11. Classify the decision and record limitations.

## SRM gate

Sample Ratio Mismatch tests whether observed assignment counts are compatible
with the planned allocation. Assignment must occur before treatment, so a
material mismatch usually means selection, logging, randomization, trigger, or
pipeline failure. Even a small relative imbalance can be decisive at scale.

Use a chi-square goodness-of-fit test against the planned shares. A strict
threshold such as 0.001 is a common alert default because the null allocation is
known by design. Run:

```bash
python3 scripts/ab_math.py srm \
  --observed 821588 815482 \
  --expected 0.5 0.5
```

If SRM fails:

- Mark the result invalid.
- Do not inspect success metrics except as debugging clues.
- Trace counts from assignment through trigger, exposure, ingestion, joins,
  bot/fraud filters, exclusions, and metric tables.
- Segment the SRM by day, browser/app version, new/returning user, geography,
  device, and intersections with concurrent experiments.
- Check asymmetric rollout start times, cache warmup, client update delays,
  redirects, identity loss, and residual exposure from earlier runs.
- Rerun after correcting the cause unless a principled reanalysis fully restores
  the intended randomized population.

Also run SRM on triggered units. An overall pass with a triggered failure often
reveals a treatment-influenced or asymmetric trigger.

## A/A validation

An A/A test assigns units exactly like an A/B test while serving identical
experiences. Use it to test the platform, metric implementation, data pipeline,
allocation patterns, and assumptions.

For repeated A/A simulations or runs:

- false positives for a metric should occur near alpha;
- continuous-test p-values under the null should be approximately uniform;
- estimated standard errors should match empirical variation;
- arm counts and key totals should reconcile with the system of record;
- assignment should remain balanced under production allocation patterns.

Simulate many assignments by replaying stored pre-experiment data with fresh
hash seeds. Use a uniformity test or diagnostic histogram. A/A failure patterns
can identify:

- underestimated variance from correlated observations;
- insufficient samples for a heavy-tailed metric;
- extreme outliers, sometimes producing mass near p = 0.32;
- discrete rare-event metrics;
- asymmetric caches, hardware, redirects, or allocation sizes;
- carryover from prior experiments.

Passing one 50/50 A/A test does not validate 10/90 allocations, different
hardware pools, new metrics, or changed pipelines. Run continuous A/A monitoring
alongside production experiments.

## Estimating effects

For a mean metric with independent treatment and control units:

```text
absolute effect = treatment mean - control mean
standard error = sqrt(treatment variance / treatment n
                    + control variance / control n)
confidence interval = absolute effect +/- z * standard error
```

Run a transparent calculation with:

```bash
python3 scripts/ab_math.py mean-effect \
  --control-mean 10.0 --control-variance 9.0 --control-n 50000 \
  --treatment-mean 10.2 --treatment-variance 9.4 --treatment-n 50000
```

Always report:

- assigned and analyzed counts per arm;
- arm means or rates;
- absolute effect in natural units;
- relative effect when the control value is nonzero;
- confidence interval and pre-specified p-value;
- practical benefit/harm thresholds;
- relevant guardrail effects.

The p-value is the probability of an effect at least as extreme under the null
model and its assumptions. It is not the probability that the null is true or
the probability that a finding is a false positive.

A confidence interval is generated by a procedure with stated long-run
coverage. Do not say a realized frequentist interval has a 95% probability of
containing the fixed effect. Do not infer significance by comparing separate
arm intervals; calculate the interval of the difference.

## Variance and unit alignment

The simple variance-of-the-mean formula assumes independent units. It is valid
when each observation is the randomization unit or when dependencies are
modeled. Repeated pages, clicks, or events from one randomized user are
correlated.

For ratio metrics such as total clicks / total pageviews with user-level
randomization:

- aggregate numerator and denominator per user;
- estimate the ratio of user-level averages;
- use the delta method, cluster bootstrap, or another user-cluster-aware method;
- do not treat pageviews as independent samples.

For percentile latency and other nonlinear statistics, use a bootstrap or an
appropriate asymptotic estimator clustered at the assignment unit. For tenant,
geo, or network assignment, use the effective randomized cluster count, not the
underlying users, for inference.

Do not form a relative-effect confidence interval by simply dividing the
absolute-effect interval by a random control mean. Use a valid delta-method or
bootstrap estimator for the ratio when the denominator's uncertainty matters.

## Heavy tails and outliers

Revenue, activity, latency, and event-count metrics are often skewed. Large
samples make mean-based normal approximations useful in many cases, but extreme
skew can require very large samples and can inflate variance enough to hide real
effects.

Pre-specify defensible handling:

- remove known non-human or invalid events symmetrically;
- cap each randomized unit's contribution at a domain-based threshold;
- add a binarized, truncated, or log-transformed sensitivity metric when it
  still reflects the decision;
- retain the untransformed business metric for impact accounting where needed;
- use permutation or bootstrap inference when normal approximation is not
  credible.

Never choose the cap or transformation after seeing which setting makes the
treatment significant. Verify new choices through A/A simulations and trusted
historical experiments.

## Multiplicity and peeking

False discoveries accumulate across:

- many metrics;
- variants and pairwise comparisons;
- time points and repeated looks;
- demographic, platform, and behavioral segments;
- repeated experiment iterations;
- alternative filters and estimators.

Apply the pre-specified family-wise error or false-discovery-rate method. For
exploratory dashboards, one pragmatic hierarchy is stricter thresholds for
metrics less plausibly affected: for example 0.05 for predeclared primary
metrics, 0.01 for plausible secondary metrics, and 0.001 for unrelated
diagnostics. This does not replace a formal multiplicity plan for confirmatory
decisions.

With a fixed-horizon design, do not stop because an ordinary p-value crossed a
threshold mid-run. Use a fixed end or a valid group-sequential/always-valid
method with declared decision boundaries.

Treat successive implementation attempts as a search process. Replicate a
selected winning iteration on a fresh or orthogonally randomized population to
reduce winner's-curse and repeated-testing bias.

## Triggered analysis

Triggered analysis removes units that could not experience any difference. It
improves sensitivity only if the trigger is symmetric and independent of the
treatment outcome.

Required checks:

1. Overall SRM passes.
2. Triggered SRM passes.
3. The never-triggered complement behaves like A/A.
4. Triggering persists after first potential exposure.
5. Trigger logic uses pre-treatment or counterfactual conditions.

Report:

- trigger definition and rate;
- arm counts before and after trigger;
- triggered absolute and relative effects;
- overall absolute and relative effects;
- method used to dilute the triggered result.

Do not assume:

```text
overall relative effect = trigger rate * triggered relative effect
```

That equality holds only under special conditions. The safe starting point for
additive metrics is the triggered absolute effect scaled by triggered units and
then divided by the relevant overall control total. Ratio metrics need a
metric-specific derivation. Recompute the metric at the overall population when
possible.

## Segments and time

Use pre-treatment segments such as market, locale, device, platform, tenure,
and account type. Treatment-defined segments can reverse or distort effects
when users migrate between groups.

For each segment claim:

- state whether it was pre-specified or exploratory;
- show units, interval, and multiplicity handling;
- check whether the interaction is statistically supported, not merely whether
  one segment is significant and another is not;
- investigate extreme differences as potential instrumentation or compatibility
  bugs before building a behavioral story.

Avoid pooling periods with different allocation ratios without stratification
or correct weighting. Simpson's paradox can reverse the aggregate direction
when daily traffic or baseline outcome rates differ across ramp stages.

Plot noncumulative day- or cohort-specific effects to detect novelty, primacy,
seasonality, or outages. Check whether the population composition changes over
time before interpreting a trend.

## Interference and external validity

Randomized differences can still be biased when treatment affects control via
social contacts, marketplace inventory, auctions, ad budgets, shared compute,
caches, or shared training data.

Look for first-order actions and downstream responses. Compare estimates under
different exposure levels or isolation schemes. If interference is material,
report the direction of likely bias and use a cluster, geo, time, resource, or
network design for the next run.

Limit claims to the tested:

- population and identity system;
- product surface and implementation version;
- geography, locale, platform, and traffic mix;
- calendar period and exposure duration;
- market or network equilibrium.

Use replication in new populations and periods. For durability, consider a
long-running experiment, stable cohort, post-period analysis, time-staggered
treatments, holdback, or reverse experiment. Each has assumptions and an
opportunity cost.

## Decision classification

Compare the confidence interval with zero and with the predeclared practical
thresholds.

| Evidence | Interpretation | Default action |
|---|---|---|
| Trust gate failed | Causal estimate is invalid | Debug and rerun |
| Interval excludes zero and exceeds benefit threshold; guardrails pass | Statistically and practically beneficial | Ship or proceed with planned ramp |
| Interval excludes zero but stays inside negligible region | Detectable but not worth the cost | Usually do not ship |
| Interval lies within equivalence/negligible region | Evidence of no meaningful effect at the chosen bounds | Stop, simplify, or reprioritize |
| Interval includes meaningful benefit and harm | Underpowered or unstable | Inconclusive; gather more data or redesign |
| Point estimate is promising but interval crosses zero | Benefit is plausible, not established | Replicate or increase power if worthwhile |
| OEC improves but a veto guardrail fails | Tradeoff violates the plan | Do not ship or escalate under predeclared policy |
| Very large or surprising effect | Twyman-style anomaly risk | Verify instrumentation and replicate |

Do not let sunk implementation cost change the statistical result. It may affect
the predeclared practical threshold, but it is not evidence that treatment works.

## Diagnostic checklist

- [ ] The user confirmed the context-and-assumptions register before analysis.
- [ ] The control board has one active decision, at most three current risks,
      a next owner/action, and a low or accepted-medium load rating.
- [ ] The pre-registered plan and exact analysis version are identified.
- [ ] Assignment, exposure, trigger, and outcome windows reconcile.
- [ ] Overall and triggered SRM pass at the declared threshold.
- [ ] Invariants, telemetry fidelity, and data-quality checks pass.
- [ ] No unresolved cross-variant contamination or shared-resource effect exists.
- [ ] Randomization and analysis units are compatible with the variance method.
- [ ] Outlier, bot, missingness, and deduplication rules are symmetric and frozen.
- [ ] Stopping and multiple-testing procedures match the plan.
- [ ] Absolute effects, relative effects, intervals, arm values, and counts appear.
- [ ] Triggered effects are translated correctly to overall effects.
- [ ] Segment and time findings are labeled confirmatory or exploratory.
- [ ] Practical thresholds and every guardrail are included in the decision.
- [ ] Generalization and long-term assumptions are explicit.
- [ ] Surprising findings have a verification or replication plan.
