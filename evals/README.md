# Evals

Prompt and grader cases for `claude plugin eval`. Each case is `<skill>/<case>/prompt.md` with `graders/criteria.md` (LLM-judged).

```bash
claude plugin eval . --runs 3            # with and without the plugin (baseline arm)
claude plugin eval . --case 'securecoding/*'
```

| Skill | Cases |
|---|---|
| `securecoding` | `login-review`, `coupon-design`, `no-overtrigger`, `asks-scope` |
| `kickoff` | `new-project`, `library-no-ui`, `existing-gitignore` |
| `uiuxpatterns` | `payment-failure`, `korean-enter`, `empty-states`, `asks-region`, `small-no-ask` |

Status: cases written, not yet run. Add scores to `CHANGELOG.md` after a run. `no-overtrigger` should pass without the plugin as well; the others should score higher with it.
