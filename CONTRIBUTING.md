# Contributing

Contributions that improve experimental validity, decision clarity, source
traceability, portability, or cognitive-load management are welcome.

## Before opening a change

1. Search existing issues and pull requests.
2. Open an issue first for a material workflow, statistical, or compatibility
   change.
3. Keep the skill focused on online controlled experiments. Put user-facing
   repository guidance at the repository root, not inside the skill folder.
4. Cite the book chapter or another primary source for substantive method
   changes. Do not copy copyrighted passages into the repository.

## Development

Fork the repository, create a focused branch, and make the smallest coherent
change. The project requires POSIX `sh` and Python 3, with no third-party Python
dependencies.

Run the full local check before opening a pull request:

```sh
make validate
```

If the change affects distribution, also build and inspect the release bundle:

```sh
make package
unzip -l dist/run-ab-experiments-bundle-v*.zip
```

## Skill design rules

- Preserve the mandatory question-first and explicit-confirmation gates.
- Keep `SKILL.md` below 500 lines and route detail through direct references.
- Keep frontmatter limited to `name` and `description` for portability.
- State each fact once; avoid motivational prose and repeated summaries.
- Treat conventional statistical defaults as proposals, not hidden choices.
- Update the source map when a method or lifecycle rule changes.
- Add or update deterministic checks for scripts and installer behavior.

## Pull requests

Use a clear title and explain the problem, the behavioral change, validation
performed, source-book impact, and cognitive-load impact. Keep unrelated
changes in separate pull requests.

By contributing, you agree that your contribution is licensed under the MIT
License.
