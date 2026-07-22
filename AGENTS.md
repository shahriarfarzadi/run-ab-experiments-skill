# Repository agent rules

## Preserve skill generality

- Keep `skills/run-ab-experiments` independent of any company, product,
  experiment, dataset, repository, metric catalog, traffic profile, or decision
  context.
- Require experiment-specific facts to enter through the skill's mandatory
  question-first interview and confirmed context-and-assumptions register.
- Do not add personal paths, credentials, private URLs, experiment IDs, fixed
  business baselines, organization names, or project-specific metric formulas.
- Keep source-book attribution and clearly labeled generic examples separate
  from user context. Never convert an example into a silent default.
- Run `make validate` after every change to the skill or repository tooling.

## GitHub merge gate

- Never merge a pull request or enable auto-merge without the user's explicit
  approval immediately before the merge action.
- Creating a repository, opening a pull request, pushing a branch, or receiving
  a general request to keep the repository updated does not grant merge
  approval.
- Before asking, provide the pull request number and URL, exact diff summary,
  check status, review status, and unresolved risks.
