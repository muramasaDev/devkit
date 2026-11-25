# Roadmap

Planned work, ordered by priority. Each item has a done condition. Open an issue to discuss or claim one ([CONTRIBUTING.md](CONTRIBUTING.md)).

## 0.4 Trust and distribution
| # | Item | Done when |
|---|---|---|
| 1 | CI on pull requests | `claude plugin validate .`, `scripts/validate_uiuxpatterns.py`, link check and secret scan pass in GitHub Actions |
| 2 | Repository settings | Description, topics, private vulnerability reporting, secret scanning push protection and `main` protection are on |
| 3 | Tagged release | `v0.4.0` tag and GitHub Release with notes taken from `CHANGELOG.md` |
| 4 | Social preview | `assets/banner.svg` rendered at 1280x640 and set as the repository image |
| 5 | Consistency check for `securecoding` | A script fails when a `SEC-xx` ID is missing from `SKILL.md`, `controls.md`, `kisa-map.md` or the report template |

## 0.5 Content depth
| # | Item | Done when |
|---|---|---|
| 6 | OWASP mapping | Each of the 24 controls lists the matching ASVS requirement, Top 10 category and CWE ID |
| 7 | Stack presets in `kickoff` | Next.js, FastAPI and Spring presets give a concrete auth, session, upload and secrets setup per control |
| 8 | Worked examples | `examples/` holds one small app with a filled `security-architecture.md`, a `security-report.md` with real test results and a screen review |
| 9 | Remaining sources | Oracle Java SE secure coding guidelines read and added to `cloud.md`; every OWASP-derived file compared against the original |
| 10 | Form card scenes | The 9 input form cards in `uiuxpatterns` are matched against screens one by one |

## 0.6 New skills
| # | Skill | Scope |
|---|---|---|
| 11 | `releasecheck` | Pre-release gate: env and secrets, dependency audit, backups, rollback, monitoring, error pages |
| 12 | `apidesign` | Error format, pagination, idempotency, versioning, rate limits, authorization per endpoint |
| 13 | `dbdesign` | Keys, constraints, migrations, soft delete, audit columns, row-level access |
| 14 | `testplan` | Which tests a feature needs: unit, integration, abuse cases, accessibility, load |

## Later
- English translation of skill bodies (translation pull requests welcome)
- Plugin evals with `claude plugin eval` so a skill change shows its effect on real prompts
- Dark-mode variant of the README banner
