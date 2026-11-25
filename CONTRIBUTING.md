# Contributing

## Before a pull request
- Run `python scripts/validate_uiuxpatterns.py`
- Run `claude plugin validate .` if Claude Code is installed
- Keep LF line endings (`.gitattributes` enforces it)

## Content rules
- Short, factual bullets. No guesses and no expected-effect claims
- Tag evidence in `securecoding`: `[원문]` source page read, `[KISA]` guide read, `[일반]` not verified. Add the source URL and the date read
- Do not copy source text. Summarize and link
- Never mark a test PASS unless it was run
- No private, company or personal data. No secrets or `.env` files
- New third-party material: add it to `NOTICE.md` with its license

## Translations
Skill text is Korean. English or other translations are welcome as new files next to the originals, with the same evidence tags.
