# Contributing

## Repository model
This repository is primarily an auto-synced NeetCode submissions archive with optional curation.

## Submission file rules
- Keep NeetCode naming and hierarchy: `<topic>/<problem>/submission-<n>.<ext>`.
- Preserve historical `submission-*` files by default.
- If you add a refined solution, create a new `submission-<n+1>` instead of rewriting older files.
- Mark the preferred solution in `SOLUTIONS_INDEX.md`.

## Quality bar
- Every Python submission must pass repository validation checks:
  - Syntax must parse.
  - File must contain at least one class or top-level function.
- Favor clarity and correctness over micro-optimizations.
- Keep judge-compatible patterns (e.g., `List` annotations without explicit typing imports) unless a problem specifically requires stricter runtime compatibility.

## Local validation
Run from repository root:

```bash
python tools/validate_submissions.py
```

To validate only changed Python submissions:

```bash
python tools/validate_submissions.py --changed-only --base <base_sha> --head HEAD
```

## CI behavior
- CI validates changed Python submission files on pushes and pull requests.
- Keep changes focused by topic/problem to keep review and validation noise low.

## Incremental cleanup policy
- Prioritize syntax and clearly invalid definitions first.
- Apply style/consistency improvements in small batches by topic.
- Preserve problem history while designating one recommended submission per problem.
