# Changelog

## 0.4.0 (2026-11-25)
- `securecoding`: attack tests 20 to 29 with preconditions, runnable commands, expected results and post-checks; new tests for SQL injection, CSRF, SSRF, login spraying, session fixation, CORS reflection, OS command injection, XXE and deserialization, response over-exposure
- `securecoding`: controls rewritten in SEC order with stack code pairs, search commands, session and OTP values from ASVS 5.0 / OWASP, SSRF and deserialization sections, supply chain, tool matrix, ASVS and API Top 10 mapping, evidence level per control
- `securecoding`: condition to control table, report template with commit, environment, tool versions, `PASS(test)` and `PASS(inspection)`
- `uiuxpatterns`: `defaults.md` (47 default values with source level), `snippets.md` (9 patterns in HTML, React, Vue, browser-run), `korean-flows.md`, state tables for FB and FM patterns, WCAG 2.2 coverage table, Korean e-commerce law mapping for dark patterns, automated check table (axe rules, source regex), one canonical rule for toast, wait time, IME Enter, switch, dialog
- `kickoff`: stack-aware `.gitignore`, `.gitattributes`, conditional `CLAUDE.md.tmpl`, secret-detection hook option, CLI commands with pinned versions
- Repo: `scripts/validate.py` (versions, SEC IDs, test counts, links, forbidden text, secret patterns), CI workflow, `evals/` (12 cases for `claude plugin eval`, not yet run), code of conduct, issue templates, dependabot
- `securecoding` and `uiuxpatterns` ask short multiple-choice questions (3 or fewer, with 'Not sure' and 'Proceed with defaults') only when the answer changes the result; small requests are answered directly
- English copies of core files in `skills/<name>/en/` (SKILL.en.md x3, securecoding templates and attack tests, kickoff template and tools, uiuxpatterns defaults, snippets, Korean flows); `validate.py` checks parity with the Korean originals
- Skill descriptions shortened to 300 characters or fewer; dangling image references removed from pattern files

## 0.3.0 (2026-11-25)
- `uiuxpatterns`: extended terms (components, AI screens, UX laws, performance), web platform feature table, interaction rules, agent UI (event to screen mapping, human approval), real-browser verification in the checklist
- `kickoff`: optional tool chrome-devtools-mcp with privacy notes
- `uiuxpatterns` keyword index renamed to `pattern-keywords.csv`

## 0.2.0 (2026-11-25)
- `securecoding`: 24 controls, 20 attack tests, security design guide and template, KISA mapping, incident cases, Cloudflare / AWS / Oracle Cloud rules
- `kickoff`: asks admin, payment, OTP and AI features, creates the security design doc
- `uiuxpatterns`: glossary merged into one file
- Public release files: README (EN, KO), NOTICE, SECURITY, CONTRIBUTING

## 0.1.0
- Initial plugin: `kickoff`, `securecoding`, `uiuxpatterns`
