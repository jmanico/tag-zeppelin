# Agent instructions

@REQUIREMENTS.md
@ARCHITECTURE.md
@SECURITY.md
@DESIGN.md

Every leaf implementation issue MUST follow `REQUIREMENT_TEMPLATE.md`; epic, workstream, and decision issues use concise purpose-specific bodies that link to affected specification IDs and issues.

## Specification maintenance

Author product behavior only in REQUIREMENTS.md, presentation only in DESIGN.md, implementation decisions only in ARCHITECTURE.md, and security controls only in SECURITY.md. Reference the owner instead of repeating its content. Preserve stable IDs; never reuse retired IDs. Keep proposed, approved, and saved-state terminology distinct. Do not introduce functions, fields, or filters outside REQUIREMENTS.md during implementation.

## Repository workflow

- The repository currently contains root-level specifications, the issue template, and the logo. Clone with `git clone https://github.com/jmanico/tag-zeppelin.git` and work from the repository root; documentation edits need no application dependencies.
- There is currently no application source, build target, runnable application, test harness, formatter, or CI configuration. Do not report application tests as passing. When implementation introduces these facilities, record their actual commands here in the same change.
- For documentation changes, run `git diff --check`, review the entire affected specifications, verify local links and ID references, and check that controls and constraints were not lost. Preserve Markdown tables, front matter, and existing ID notation; use the canonical prose sections and token schema of the format reference linked in DESIGN.md; no formatter is configured.
- Use a focused topic branch and a descriptive commit. Open a PR with the resulting behavior/document changes and actual validation evidence. Merge only after review and all configured required checks pass; do not bypass repository protections. No CI jobs currently exist, so document the manual checks in the PR.
- The maintainer owns release evidence. Before release, require the verification in SECURITY.md, acceptance criteria in REQUIREMENTS.md, and native keyboard/accessibility/scaling checks in DESIGN.md. Include database migration/rollback evidence. Record the bounded API workload result; failure blocks service release. No acceptance checks have run yet because implementation does not exist.
