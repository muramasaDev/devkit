# Contributing

## Before a pull request
- Run `python scripts/validate.py` (`python3` or `py` on macOS, Linux, Windows). CI runs the same script
- Run `claude plugin eval . --case '<skill>/*'` for the skill you changed (cases in `evals/`)
- Run `claude plugin validate .` if Claude Code is installed
- Keep each `description` at 300 characters or fewer and open `/skills` to confirm no truncation warning
- Keep LF line endings (`.gitattributes` enforces it)

## Content rules
- Short, factual bullets. No guesses and no expected-effect claims
- Tag evidence in `securecoding`: `[원문]` source page read, `[KISA]` guide read, `[일반]` not verified. Add the source URL and the date read
- Do not copy source text. Summarize and link
- Never mark a test PASS unless it was run
- No private, company or personal data. No secrets or `.env` files
- New third-party material: add it to `NOTICE.md` with its license

## Translations
Skill text is Korean. Translations go in `skills/<name>/<lang>/` with the same relative paths as the originals (`SKILL.md` becomes `SKILL.<lang>.md`), no frontmatter (so it is not read as a skill), the same IDs, code blocks and table rows, and a `Korean original:` pointer on the first line. `scripts/validate.py` checks IDs and code blocks of every `en/` file against its original. Untranslated references stay Korean and are marked `(Korean for now)`.
