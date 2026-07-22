# Run A/B Experiments

[![Validate](https://github.com/shahriarfarzadi/run-ab-experiments-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/shahriarfarzadi/run-ab-experiments-skill/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/shahriarfarzadi/run-ab-experiments-skill)](https://github.com/shahriarfarzadi/run-ab-experiments-skill/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A question-first Agent Skill for planning, managing, intervening in, and
interpreting trustworthy online controlled experiments.

It turns experiment context into explicit facts, assumptions, unknowns, and
decision gates before analysis begins. It then keeps one control board across
the lifecycle and reviews cognitive load at every step.

## Why this skill exists

Experiment mistakes usually begin before the statistics: an unstated decision,
an ambiguous population, a weak metric, an unlogged exposure, a hidden
interference path, or an improvised stopping rule. This skill makes those
assumptions visible before they can silently determine the answer.

The workflow enforces five behaviors:

1. Ask high-impact questions before planning or analysis.
2. Confirm a context-and-assumptions register before work starts.
3. Separate design, live-operation, inference, and business decisions.
4. Check trust failures such as sample ratio mismatch before reading outcomes.
5. Reduce cognitive load with one active decision, explicit deferrals, and
   concise stage gates.

## General by design

The installable skill contains no company, product, repository, experiment,
dataset, traffic, baseline, metric-catalog, or decision context. It also
contains no personal path, private URL, email, credential, or experiment ID.

All test-specific context must enter through the mandatory interview and then
be classified as a confirmed fact, approved assumption, proposed assumption,
unknown, or contradiction. Generic examples and conventional statistical
values are labeled as examples or proposals; they are never silent defaults.
CI scans the packaged skill for environment-specific and identity-specific
content on every change.

## Install

### Option 1: install directly from GitHub

The open Agent Skills CLI can discover the skill in this repository:

```sh
npx skills add shahriarfarzadi/run-ab-experiments-skill
```

Choose the agents and installation scope when prompted.

### Option 2: clone and use the bundled installer

```sh
git clone https://github.com/shahriarfarzadi/run-ab-experiments-skill.git
cd run-ab-experiments-skill
./install.sh all
```

Install only one harness when preferred:

```sh
./install.sh codex
./install.sh claude
./install.sh agy
```

The installer never overwrites a different installation by default. Use
`--force` only when you want it to move the existing skill to a timestamped
backup and install this version.

| Harness | Global destination | Invocation |
| --- | --- | --- |
| Codex | `$HOME/.agents/skills/run-ab-experiments` | Mention `$run-ab-experiments` |
| Claude Code | `$HOME/.claude/skills/run-ab-experiments` | Run `/run-ab-experiments` or ask naturally |
| Antigravity (`agy`) | `$HOME/.gemini/config/skills/run-ab-experiments` | Ask naturally; inspect with `/skills` |

If a newly created top-level skills directory is not detected, start a new
agent session.

### Install from a release ZIP

Every GitHub release includes a versioned bundle and SHA-256 checksum. Download
both files, verify the checksum, unzip the bundle, and run `./install.sh` from
the extracted directory.

macOS:

```sh
shasum -a 256 -c run-ab-experiments-bundle-v1.2.0.zip.sha256
```

Linux:

```sh
sha256sum -c run-ab-experiments-bundle-v1.2.0.zip.sha256
```

## Use

Start with the decision or situation, even if the context is incomplete:

```text
Use $run-ab-experiments to help us decide whether to launch a redesigned
checkout. We have early results, but the test plan was not documented.
```

The skill intentionally does **not** analyze immediately. Its protocol is:

1. **Interview:** ask only the questions that could change validity or action.
2. **Confirm:** present facts, assumptions, contradictions, and unresolved
   unknowns for explicit approval.
3. **Work:** enter exactly one lifecycle mode after confirmation.

| Mode | Primary output | Gate before proceeding |
| --- | --- | --- |
| Plan | Decision-grade experiment plan | Design, readiness, and load review |
| Manage/intervene | Updated experiment control board | Validity-preserving run decision |
| Interpret/analyze | Trust audit, estimates, and decision | Integrity checks before outcomes |

The included calculator supports transparent fixed-horizon sample-size,
independent-arm mean-effect, and SRM calculations. It is deliberately narrow;
the skill routes clustered, sequential, ratio, percentile, and other advanced
analyses to suitable statistical methods.

```sh
python3 skills/run-ab-experiments/scripts/ab_math.py --help
```

## Repository layout

```text
skills/run-ab-experiments/
├── SKILL.md                 Core protocol and lifecycle routing
├── agents/openai.yaml       Codex interface metadata
├── assets/                  Reusable control-board and report templates
├── references/              Question bank, design, trust, and source map
└── scripts/ab_math.py       Dependency-free transparent calculations
```

Repository-level files provide installation, validation, packaging, release,
security, and contribution workflows. They are not loaded into agent context.

## Validate and package

No third-party Python package is required.

```sh
make validate
make package
```

Validation checks the skill contract, internal links, line budget, calculator,
installer syntax, installation behavior for all three harnesses, placeholders,
and accidental inclusion of book files. Packaging creates a reproducible ZIP
and matching SHA-256 file under `dist/`.

## Method and source

The workflow is an original operational distillation grounded in:

> Kohavi, Ron, Diane Tang, and Ya Xu. *Trustworthy Online Controlled
> Experiments: A Practical Guide to A/B Testing*. Cambridge University Press,
> 2020. [doi:10.1017/9781108653985](https://doi.org/10.1017/9781108653985).

The source map in the skill connects every lifecycle stage to the preface and
all 23 chapters. The repository does not include or redistribute the source
PDF or EPUB.

Current harness conventions were checked against the official
[Codex skill documentation](https://developers.openai.com/codex/skills),
[Claude Code skill documentation](https://code.claude.com/docs/en/skills), and
[Antigravity skill documentation](https://antigravity.google/docs/skills).

This project is independent and is not affiliated with or endorsed by Ron
Kohavi, Diane Tang, Ya Xu, Cambridge University Press, OpenAI, Anthropic, or
Google. It does not replace qualified statistical, legal, privacy, security, or
ethics review.

## Contributing and security

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes. Report
security issues through the process in [SECURITY.md](SECURITY.md), not a public
issue.

Released under the [MIT License](LICENSE).
