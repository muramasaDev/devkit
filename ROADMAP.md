# Roadmap

Open items, ordered by priority. Each has a done condition. Open an issue to discuss or claim one ([CONTRIBUTING.md](CONTRIBUTING.md)).

## Done in 0.4.0
CI workflow, `scripts/validate.py`, 9 eval cases (written, not run), ASVS 5.0 and API Top 10 mapping, 29 runnable attack tests, `defaults.md`, `snippets.md`, `korean-flows.md`, stack-aware `.gitignore`. Details in [CHANGELOG.md](CHANGELOG.md).

## 0.5 Evidence and trust
| # | Item | Done when |
|---|---|---|
| 1 | Run the evals | `claude plugin eval . --runs 3` scores with and without the plugin are in `CHANGELOG.md`; failing cases lead to skill fixes |
| 2 | Source check of `[요약 확인]` items | Each control marked `[요약 확인]` is compared against the original page and re-tagged `[원문]` or corrected |
| 3 | `defaults.md` sources | The 42 rows marked "general recommendation, source unverified" get a primary source or stay labelled |
| 4 | Law text | Article numbers of the Korean e-commerce dark-pattern rules are checked against the statute text, not press coverage |
| 5 | Run the code | `snippets.md` React and Vue examples compile; `controls.md` stack examples run in a scratch project; commands marked `[미실행]` are run |
| 6 | Repository settings | Description, topics, private vulnerability reporting, secret scanning push protection and `main` protection are on |
| 7 | Tagged release | `v0.4.0` tag and GitHub Release with notes from `CHANGELOG.md` |

## 0.6 Reach
| # | Item | Done when |
|---|---|---|
| 8 | English skill text | `SKILL.md` x3, `templates/`, `attack-tests.md` first; layout decided in [CONTRIBUTING.md](CONTRIBUTING.md); `validate.py` checks the same IDs in every language |
| 9 | Worked example | `examples/` holds one small app with a filled `security-architecture.md`, a `security-report.md` with real results and a screen review |
| 10 | Stack presets in `kickoff` | Next.js, FastAPI and Spring presets give auth, session, upload and secrets setup per control |
| 11 | Other sources | Oracle Java SE secure coding guidelines read into `cloud.md`; Azure and GCP rules added; KISA 2023 edition checked |
| 12 | Form card scenes | The 9 input form patterns in `uiuxpatterns` are matched against reference screens |

## 0.7 New skills
| # | Skill | Scope |
|---|---|---|
| 13 | `releasecheck` | Pre-release gate: env and secrets, dependency audit, backups, rollback, monitoring, error pages |
| 14 | `apidesign` | Error format, pagination, idempotency, versioning, rate limits, authorization per endpoint |
| 15 | `dbdesign` | Keys, constraints, migrations, soft delete, audit columns, row-level access |
| 16 | `testplan` | Which tests a feature needs: unit, integration, abuse cases, accessibility, load |
