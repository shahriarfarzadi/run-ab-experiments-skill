# Discovery Question Bank

Use this reference before any experiment planning, review, calculation, query,
or post-test analysis. Ask adaptively: omit questions already answered, expand
ambiguous answers, and include conditional modules that match the experiment.

## Contents

- [Interview rules](#interview-rules)
- [Core questions for every experiment](#core-questions-for-every-experiment)
- [Planning and pre-launch questions](#planning-and-pre-launch-questions)
- [In-flight management and intervention questions](#in-flight-management-and-intervention-questions)
- [Post-test analysis questions](#post-test-analysis-questions)
- [Platform and methodology audit questions](#platform-and-methodology-audit-questions)
- [Conditional hidden-assumption modules](#conditional-hidden-assumption-modules)
- [Readiness criteria](#readiness-criteria)

## Interview rules

- Open with a brief orientation in this pattern: the decision you understand,
  why context must come first, and permission to answer briefly or write
  `unknown`. Vary the words naturally; do not recite a script.
- Use the voice of an experienced coach working beside the user: calm, warm,
  precise, non-blaming, and focused on helping them reach the next safe gate.
- Ask 12–20 numbered questions in the first response when the prompt has little
  context. Use no more than five short grouped headings so the user can answer
  inline. Mark no more than seven as **Needed now**. Mark the rest as **Answer
  if known**. Defer questions that cannot affect the current lifecycle gate.
- When the prompt is detailed, ask at least five respectful stress-test
  questions about facts that could reverse the design, invalidate the result,
  or change the decision. Direct the rigor toward the design, never the person.
- Ask one main thing per question. Use plain language first; add the technical
  term in parentheses only when useful.
- When a bank entry bundles several related fields, present them as short
  sub-bullets under one numbered topic instead of stacking questions in a long
  sentence.
- Explain why a question matters in one short clause only when the user may
  otherwise dismiss it. Keep the explanation beside the question.
- Accept `unknown`, but record the consequence and how the unknown could be
  resolved. Thank the user through useful handling of the answer, not generic
  praise. Never translate `unknown` into a hidden default.
- Ask for exact definitions, examples, dates, thresholds, and source artifacts.
  Avoid yes/no phrasing when the underlying detail matters.
- Replace blame-oriented wording such as “Why didn’t you define this?” with
  neutral wording such as “What definition was used, and when was it chosen?”
- Do not make the user decode jargon, defend ordinary uncertainty, or absorb a
  lecture before answering.
- Distinguish what was decided before outcomes were visible from what was
  chosen afterward.
- Do not debate or solve the experiment while interviewing.
- After answers arrive, ask a second, narrower round for contradictions and
  decision-critical gaps before creating the assumptions register.
- Do not ask the same fact in different language. Refer to its earlier answer.
- End each question round with a compact progress line: answered, unknown,
  blocking, and deliberately deferred counts. Then state the single next step
  and what the user will receive after it.

Use this shape, adapting the words to the situation:

```text
My current understanding is that this test needs to inform [decision].

We can make this manageable in two passes. For now, brief answers are enough,
and “unknown” is a useful answer—it tells us what must be verified.

Needed now
1. [One decision-critical question]
...

Answer if known
8. [One useful but non-blocking question]
...

Next: I’ll turn your answers into a one-page context and assumptions register
for you to correct before any planning or analysis begins.
```

## Core questions for every experiment

Choose the relevant questions from this core set for both planning and
post-test work.

### Decision and business context

1. What exact decision will this evidence change, and what actions are actually
   available: ship, stop, iterate, choose among variants, change rollout, or
   something else?
2. Who owns the decision, who can veto it, and when must the decision be made?
3. What is the product, business model, user journey, and current pain point?
4. Why is the change expected to work? Describe the behavioral or technical
   mechanism rather than only the desired metric movement.
5. What is the cost of shipping, maintaining, delaying, or incorrectly rejecting
   the change? Are false positives and false negatives equally costly?
6. What prior evidence exists: earlier experiments, observational analysis,
   user research, incidents, competitor examples, or stakeholder intuition?

### Population and experience

7. Who can enter the experiment, and who must be excluded? Include geography,
   language, platform/app version, account state, age/policy restrictions,
   employees, test accounts, bots, and fraud.
8. Are new, existing, anonymous, signed-in, multi-device, shared-account, or
   returning users expected to behave differently?
9. What exactly does control experience, and is it identical to current
   production? What exactly changes in every treatment?
10. Besides the intended feature, what else differs between arms—latency,
    redirects, logging, model execution, cache behavior, content, support,
    pricing, or operational infrastructure?
11. What event proves a unit could first be affected (exposure/trigger), and can
    the treatment itself change whether that event is observed?
12. Can one person's or unit's treatment affect another unit through social
    connections, inventory, auctions, budgets, recommendations, shared compute,
    caches, or model training?

### Identity, assignment, and time

13. What is the proposed or actual randomization unit and stable identifier?
    How persistent is it across devices, sessions, logins, reinstalls, and time?
14. At what unit are outcomes computed? Are repeated events from the same
    randomized unit treated as correlated?
15. How are assignments generated, versioned, logged, and kept stable? Can
    concurrent experiments overlap or steal traffic?
16. What calendar period matters, including weekday/weekend mix, holidays,
    campaigns, billing cycles, seasonality, novelty, learning, and carryover?

### Metrics and decision thresholds

17. What long-term user and business value should improve? What short-term
    metric is supposed to represent it, and why is that relationship causal?
18. For every key metric, what are the exact numerator, denominator, unit,
    population, attribution window, direction, source, and quality filters?
19. Which metric is primary or the OEC, which are organizational guardrails,
    which are trust guardrails, and which are diagnostics only?
20. What is the smallest benefit worth acting on and the largest acceptable harm
    for each veto guardrail? Who approved those thresholds?

### Risk, ethics, and governance

21. What physical, psychological, social, financial, privacy, fairness, or
    opportunity harm could either arm cause?
22. Does the test involve deception, sensitive or identifiable data, vulnerable
    users, high switching costs, differential pricing, or offline consequences?
23. What privacy, security, legal, research-ethics, or policy reviews are
    required? What notice, consent, choice, or opt-out do users have?
24. What data is necessary, who can access it, how long is it retained, and what
    happens if it is exposed or misused?
25. Which documents, schemas, queries, dashboards, screenshots, logs, or raw
    aggregates can the user provide after the assumptions gate is confirmed?

## Planning and pre-launch questions

Ask these in addition to the core questions when designing or reviewing a test.

### Hypothesis and scope

1. Write the current hypothesis in one sentence. Which part is the idea and
   which part is a particular implementation?
2. Is this an experiment for decision, risk containment, learning, metric
   validation, capacity validation, or several of these? Which is primary?
3. What causal effect is wanted: effect of assignment, effect of actual exposure,
   effect among triggered users, or total population impact?
4. What result would falsify the proposed mechanism even if the primary metric
   moved favorably?

### Traffic, sensitivity, and statistics

5. What are the historical baseline, variance or standard deviation, and sample
   period for every decision metric? Do they use the same population and unit as
   the proposed experiment?
6. How many eligible unique randomization units and triggered units arrive per
   day and per complete week? How much traffic is available after other tests?
7. What alpha, power, sidedness, confidence interval, and allocation does the
   decision owner accept? If unknown, which error is more costly?
8. How many treatments and key comparisons exist? Which metrics, segments, and
   looks belong to the confirmatory testing family?
9. Will the test use a fixed end date or valid sequential monitoring? Who can
   stop early, and under exactly which safety or efficacy boundary?
10. Which pre-treatment covariates, stratification, or variance-reduction method
    may be used, and were their definitions frozen before launch?

### Instrumentation and trust

11. Which events record assignment, actual exposure, trigger, outcomes, errors,
    and version? How are missing, duplicate, delayed, bot, fraud, and outlier
    events handled?
12. What is the source of truth, and how will experiment counts and key metrics
    reconcile with it?
13. Has this assignment pattern, metric implementation, and data pipeline passed
    repeated A/A tests? What did the null p-value distribution look like?
14. Which invariants will detect asymmetric telemetry, cache, cookie, latency,
    crash, or resource behavior?
15. How will SRM be checked overall, by ramp stage, and among triggered units?

### Ramp and operations

16. Which internal, beta, geography, data-center, or low-percentage rings will
    contain risk before the maximum-power measurement stage?
17. What near-real-time safety thresholds cause automatic rollback, who receives
    alerts, and how quickly can exposure be removed?
18. What operational capacity must be validated after measurement, and what peak
    period must the ramp cover?
19. Is a holdout, reverse test, or replication needed? What learning justifies
    its user and opportunity cost?
20. Who will remove dead code, obsolete configuration, and experiment logging
    after the final decision?

## In-flight management and intervention questions

Ask these before advising on a running experiment, ramp change, incident,
pause, restart, or early stop. Do not interpret efficacy until the context gate
is confirmed and the experiment is in a valid decision phase.

### Current state and active decision

1. What lifecycle phase is active: internal ring, small production exposure,
   maximum-power measurement, capacity ramp, holdout, paused, or stopped?
2. What single decision is needed now: continue, hold, ramp up, ramp down, stop,
   fix and restart, or complete measurement? Who owns it and by when?
3. What are the current experiment version, population, allocation, stage start,
   elapsed time, and matured assigned/exposed/triggered/analyzed counts?
4. What promotion, stop, rollback, and completion rules were frozen before the
   run? Which rule applies to this decision?
5. Is the current data from the near-real-time safety path or the validated batch
   decision path? What delay and quality difference exists between them?

### Safety, trust, and evidence

6. Which user, business, operational, privacy, fairness, and capacity guardrails
   pass, fail, or remain unknown? Give thresholds and current values.
7. What are the overall and current-stage SRM counts/p-values? If triggering is
   used, what is triggered SRM and the never-triggered complement result?
8. Are assignment, exposure, telemetry, missingness, duplicates, bots, caches,
   cookies, crashes, latency, and shared resources behaving symmetrically?
9. Has anyone inspected outcome metrics? Did that influence allocation, timing,
   stopping, or requested changes?
10. Is the current stage powered and mature enough for its intended decision, or
    is it only a risk-containment stage?

### Changes and incidents

11. What ramp, pause, outage, bug, fix, code/model/config change, data-pipeline
    change, or concurrent launch occurred? Give timestamps and affected units.
12. Would the proposed intervention change the experience, estimand, identity,
    eligibility, trigger, metric, filter, allocation, or analysis version?
13. Could exposure before a fix create carryover through learning, cookies,
    inventory, model training, or returning users?
14. Can the change be isolated as a new version or fresh randomization, or would
    pre-change and post-change data be mixed?
15. What rollback mechanism exists, how quickly acts, and who is available to
    execute and verify it?

### Control and cognitive load

16. Which dashboard, alert, ramp log, incident log, frozen plan, and source of
    truth can be inspected after confirmation?
17. What are the three most material risks or blockers at this gate? Which other
    diagnostics can be deferred safely?
18. Which input, owner, or approval is missing now? What is the consequence of
    acting before it is resolved?
19. When is the next scheduled gate, and what exact evidence must be ready then?
20. What should be written into the permanent intervention and state-transition
    record after this decision?

## Post-test analysis questions

Ask these before opening or interpreting outcome data. Obtain raw aggregates or
data only after the context register is confirmed.

### Original plan versus actual execution

1. Provide the original hypothesis, experiment plan, metric definitions, power
   calculation, and decision rule. Which were timestamped before outcomes were
   visible?
2. What decisions about metrics, filters, windows, segments, or stopping were
   changed after anyone saw interim or final results?
3. What were the exact start and end timestamps, ramp stages, allocation changes,
   pauses, restarts, bug fixes, incidents, and data cutoffs?
4. Were control or treatment already exposed before the stated analysis start?
   Could cookies, learned behavior, models, or inventory carry over?
5. Did any concurrent feature, campaign, outage, model update, release, or policy
   change affect only part of the experiment period or population?

### Population reconciliation

6. For each arm, what are the assigned, exposed, triggered, and analyzed unit
   counts? Explain every transition and loss between them.
7. What allocation was expected at each ramp stage? What are the overall and
   triggered SRM statistics or raw counts needed to compute them?
8. What eligibility, exclusion, bot/fraud, missingness, deduplication, and
   outlier filters were applied? Which were pre-specified, and can treatment
   influence any of them?
9. Did units switch arms, receive both experiences, fail to receive assignment,
   or appear under multiple identifiers?
10. Does the never-triggered complement behave like A/A? If not, what difference
    reached users outside the trigger definition?

### Metrics and inference

11. For each metric, provide its exact definition and role, arm sample sizes,
    means/rates, variance or standard error, and analysis unit. For ratio and
    percentile metrics, provide the variance method.
12. What practical benefit and harm thresholds were chosen before results? If
    none existed, what decision economics can establish them without reference
    to the observed point estimate?
13. What statistical test, alpha, sidedness, interval, multiplicity correction,
    covariate adjustment, and stopping rule were actually used?
14. How often were results inspected, by whom, and did inspection influence
    stopping, extension, ramping, metric choice, or iteration?
15. How many metrics, variants, segments, dates, filters, and repeated experiment
    versions were searched before presenting the reported finding?
16. What was the planned and achieved minimum detectable effect or power at the
    actual analyzed sample size?

### Data integrity and interpretation

17. Which A/A, invariant, telemetry-fidelity, cache, cookie, crash, latency, and
    shared-resource checks passed or failed?
18. Are missing, late, duplicated, censored, or extreme observations balanced by
    arm? Could treatment change logging or classification?
19. What do day-level and stable-cohort effects show? Is there novelty, primacy,
    seasonality, ramp confounding, or Simpson's reversal?
20. Which segment findings were pre-specified? Are claimed segment differences
    supported by an interaction test rather than separate significance labels?
21. Could social, marketplace, inventory, auction, budget, CPU/cache, or model-
    training interference bias control or treatment? In which direction?
22. What claim must generalize beyond the tested users, devices, markets, period,
    or exposure level? What evidence supports that extension?
23. What decision is the user hoping to make from the result, and what outcome
    would cause them to change their current preference?
24. Can the user provide the pre-registered plan, analysis query/code, schema,
    scorecard export, ramp log, and anonymized arm-level aggregates?

## Platform and methodology audit questions

1. What decisions and experiment types must the platform support?
2. Which clients, identity systems, randomization units, and traffic layers exist?
3. How are assignment, exposure, triggering, metric definitions, and versions
   represented and joined?
4. Which tests are automatic hard gates versus informational warnings?
5. How often do SRM, A/A, telemetry, or metric-validation checks fail, and what
   happens to scorecards when they do?
6. How are fixed-horizon, sequential, ratio, percentile, cluster, CUPED, and
   multiple-testing methods implemented and validated?
7. How are ramp histories, incidents, decisions, screenshots, and cleanup stored
   as institutional memory?
8. What permissions, approvals, privacy controls, audit logs, and ethical review
   paths govern experiments and data?
9. Which manual steps create inconsistent definitions or analyst discretion?
10. Provide representative raw artifacts from passed, failed, and surprising
    experiments after the assumptions gate is confirmed.

## Conditional hidden-assumption modules

### Marketplace, auction, ads, or social network

- What scarce resource, counterparty, neighbor, inventory, or budget connects
  treatment and control?
- Can treatment improve itself by making control worse, or dilute itself by
  benefiting control?
- Can resources be split, or should randomization use geo, time, cluster,
  network, advertiser, seller, or market units?
- Does a small ramp estimate the same equilibrium effect as full launch?

### Machine learning, ranking, or recommendations

- Are control and treatment models trained on separate or shared behavior?
- Can both models run to log counterfactual differences without altering latency?
- Are model, feature, training-data, and inference versions frozen and logged?
- Can treatment change who triggers, training labels, exploration, or future
  recommendations?

### Subscription, retention, or long-term behavior

- What is the true long-term outcome and how is the short-term surrogate validated?
- What maturation, renewal, churn, learning, or habituation window is required?
- Is a cohort, holdout, post-period, staggered, or reverse design justified?
- Could identity churn or other launches contaminate long-running comparisons?

### Mobile, desktop, or client release

- Which app/OS versions receive assignment, and how delayed is update adoption?
- Can offline clients, reinstalls, device changes, or crashes create missing
  exposure or asymmetric attrition?
- Are crash, startup, battery, network, and device-health guardrails available?
- Can the treatment be disabled remotely without waiting for another release?

### Pricing, credit, health, safety, or vulnerable users

- Could the experiment create material financial, physical, discriminatory, or
  irreversible harm?
- Is individual consent, expert review, legal approval, or a non-experimental
  alternative required?
- Is differential treatment explainable, fair, and consistent with policy?
- What immediate stop condition protects participants rather than only metrics?

### Geography, language, or culture

- Are translations and treatments behaviorally equivalent across locales?
- Do holidays, payment methods, regulation, network speed, or device mix differ?
- Is allocation balanced within each market, and will analysis stratify ramp
  stages and markets correctly?
- Which populations are excluded from the resulting claim?

## Readiness criteria

Do not create the confirmation register until:

- the decision and owner are known or explicitly marked unknown;
- control, treatments, population, assignment unit, and exposure are defined;
- metric meanings and decision thresholds are known or their absence is accepted;
- planning tasks have traffic/variance/stopping inputs or an agreed plan to get
  them;
- management tasks have current phase, version, allocation, matured counts,
  safety/trust evidence, frozen gate rules, intervention history, and an owner;
- post-test tasks have the original plan, execution history, population counts,
  metric definitions, trust evidence, and inference choices—or explicit user
  acceptance that missing items may prevent a valid conclusion;
- material ethical, privacy, legal, operational, and interference risks are
  surfaced;
- contradictions are listed rather than silently resolved.

After readiness, complete the context-and-assumptions register and wait for the
user's explicit confirmation before any analysis.
