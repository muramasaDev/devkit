Korean original: ../SKILL.md

# Kickoff (project start setup)

At the first step of a project, set the working rules, security baseline, and UI baseline in one pass. Never overwrite existing files. This skill must sit in the same folder (`skills/`) as `securecoding` and `uiuxpatterns`, and the security document templates come from `securecoding`.

Paths below are relative to the kickoff folder (`skills/kickoff/`).

## Language branch
- If the user requests in Korean, use the Korean template (`templates/CLAUDE.md.tmpl`). For any other language, use `en/templates/CLAUDE.md.tmpl`. The language of generated files follows the user's language.
- Security document templates: for English users, use `../securecoding/en/templates/security-report.md` and `../securecoding/en/templates/security-architecture.md`. For Korean users, use the existing paths `../securecoding/templates/...`.
- Tool list: for English users, use `en/references/tools.md`. For Korean users, use `references/tools.md`.
- `templates/gitignore` and `templates/gitattributes` are language-independent. Use the originals in the Korean folder for both languages.

## Condition definitions (conditions are defined only here; the steps below and the templates refer to them by these names)
- **Has UI**: the type in question 2 is "web or app UI"
- **Security scope**: at least one of the following
  - Feature: login, file upload, DB use, admin UI, payment or coupon, verification code, AI feature
  - Type is "server or API"
  - Data handled is "personal or confidential data present"
  - The manifest (`package.json`, `pyproject.toml`, `pom.xml`, etc.) has external dependency entries
- **Security docs created**: Security scope applies, and step 3 actually created the `docs/security/` documents or they already exist

## Steps
1. **Check current state**: check whether it is a git repository, whether `CLAUDE.md`, `.gitignore`, `.gitattributes`, and `docs/` already exist, and whether a manifest exists. Do not touch existing files; only propose differences
2. **Ask about project nature** (multiple choice via the `AskUserQuestion` tool. One call allows up to 4 questions, so split into two rounds. Do not ask about items whose answer is already evident; fill empty slots with the next item)
   - Round 1 (4 questions)
     - Type: web or app UI / server or API / data processing script / library or CLI
     - Data handled: personal or confidential data present / none
     - Deployment: internet / closed network / undecided
     - Features A (multi-select): login / file upload / DB use / admin UI
   - Round 2
     - Features B (multi-select, 3 items): payment or coupon / verification code / AI feature
     - Stack (multi-select, only when the manifest does not tell): Node / Python / Java / .NET. Others (Go, etc.) are taken as free-text input
   - If neither Features A nor Features B has a selection, features are "none"
3. **Create files** (only the missing ones; keep the order below)
   1. If not a repository, run only `git init`. Connect a remote and push only when the user asks
   2. `.gitignore`: copy only the `# [기본]` block (the default block; the heading is Korean in the original file) from `templates/gitignore`, plus the stack blocks matching the stack answers (or the manifest): `# [Node]`, `# [Python]`, `# [Java]`, `# [.NET]`, `# [Go]`. If the file already exists, propose only the missing lines
   3. `.gitattributes`: copy `templates/gitattributes`. If there is no `*.sh` and no plan to run on Linux or containers, delete the `*.sh` line and the comment before it
   4. Security docs: if **Security scope** applies, check that the following exist, relative to the kickoff folder: `../securecoding/templates/security-report.md` and `../securecoding/templates/security-architecture.md` (for English users, `../securecoding/en/templates/security-report.md` and `../securecoding/en/templates/security-architecture.md`, per the language branch)
      - If they exist, copy them to `docs/security/security-report.md` and `docs/security/security-architecture.md` respectively. In `security-architecture.md`, fill only the fields answerable from the step 2 answers (roles, payment, AI) and leave the rest as `TBD`. Tell the user to fill in this document with them before writing feature code
      - If they do not exist, write "`securecoding` not installed" in the closing report and skip this step (**Security docs created** does not apply)
   5. `CLAUDE.md`: create it from `templates/CLAUDE.md.tmpl` (see "How to fill `CLAUDE.md`" below). Create it last, because it needs the results of `.gitignore` and the security docs
      - If the user requests in Korean, use `templates/CLAUDE.md.tmpl`; for any other language, use `en/templates/CLAUDE.md.tmpl`. The language of the generated file follows the user's language
4. **Recommend skills to apply**
   - If **Has UI**, `uiuxpatterns` (mode A before design, mode C after implementation)
   - If **Security scope**, `securecoding` (design phase before the first feature code, attack scenario tests after feature implementation). If not installed, do not recommend it; report as in step 3.4
5. **Propose optional tools** (`references/tools.md`; for English users, `en/references/tools.md`). Mention only those that fit the project's nature, with the name and a one-line purpose, and run the official install command only for those the user approves. Never install without approval
   - Secret detection hook (gitleaks): propose before the first commit. If approved, follow the procedure in `references/tools.md` (English users: `en/references/tools.md`)
6. **Verify generated results** (actually run these before reporting)
   - Check that every path `CLAUDE.md` points to (`docs/...`, etc.) actually exists. If a path does not exist, delete or fix that line
   - Check that no placeholder starting with `{` remains in `CLAUDE.md`
   - Check with `git check-ignore .env` that `.env` is ignored. If it is not, propose adding an `.env` line to `.gitignore`
7. **Closing report**: files created, files skipped with reasons (e.g. "`securecoding` not installed"), the step 6 check results, and a one-line next action

## How to fill `CLAUDE.md`
- `{project name}`: the repository folder name
- Type, data handled, main features, deployment: the step 2 answers as given. List selected features separated by commas, or "none" if there are none. If there is no answer, use `TBD`
- Condition lines: each line is prefixed with `{only if Has UI}`, `{only if Security scope}`, `{only if Security docs created}`, or `{only if .env ignore confirmed}`. If the condition holds, delete only the prefix and keep the line; if it does not hold, delete the whole line
  - `.env ignore confirmed`: only when `git check-ignore .env` succeeded (exit code 0) after step 3.2
- `{command}` (test, build): find it in the manifest. Do not read the code; if not found, use `TBD`
  - `package.json`: the `test` and `build` entries in `scripts`. Write them with the runner matching the lock file (`npm run`, `pnpm`, `yarn`)
  - `pyproject.toml`, `requirements.txt`: if a `pytest` config or `tests/` exists, test is `pytest`. Build is `python -m build` only when `pyproject.toml` has a build config
  - `Makefile`: if `test` and `build` targets exist, `make test` and `make build`
  - `pom.xml`: `mvn test`, `mvn package`. `build.gradle`: `gradle test`, `gradle build`
  - `*.sln` or `*.csproj`: `dotnet test`, `dotnet build`. `go.mod`: `go test ./...`, `go build ./...`. `Cargo.toml`: `cargo test`, `cargo build`
- Notes section: leave empty (keep only the guide comment from the template)
- If an existing repository already has `CLAUDE.md` (including output of the built-in `/init`), use it as the base and do not overwrite it. Propose only the template working rules that are missing. For an existing repository without `CLAUDE.md`, first ask the user whether to leave code structure and command documentation to `/init`. Kickoff handles only the working rules, `.gitignore`, `.gitattributes`, and the security documents

## Rules to keep
- Questions are multiple choice, 4 or fewer per call
- Installable tools can change agent settings, so tell the user which settings change before installing
- Do not fill values by guessing. If unknown, leave `TBD`
