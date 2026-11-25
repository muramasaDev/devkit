# Optional tools (install only those approved)

Compiled on 2026-11-23 and 2026-11-25 from repository READMEs and license documents (nothing was installed or run except gitleaks). Installable tools change agent settings.

Command format
- Agents cannot run slash commands (`/plugin ...`), so commands are written in `claude plugin ...` CLI form (subcommands `marketplace add` and `install` checked with `claude plugin --help`, Claude Code 2.1.332)
- Do not use `@latest`. Unpinned remote execution conflicts with `securecoding` SEC-16 (no code execution without an integrity check). The versions below were checked on 2026-11-25 against the npm registry (`npm view <package> version`) or PyPI (`pip index versions`); recheck with the same command before running

| Tool | When to use | Install command (official, version pinned) | Settings changed | License |
|---|---|---|---|---|
| diagram-design | Making diagrams (architecture, flow, etc.) as a single HTML and SVG file | `claude plugin marketplace add cathrynlavery/diagram-design`, then `claude plugin install diagram-design@diagram-design` | Plugin added | MIT |
| graphify | Building a knowledge graph from code and documents and querying it (large repositories) | `uv tool install graphifyy==0.9.119`, then `graphify install` | Assistant settings (the README's hook behavior is unverified) | Apache-2.0 |
| rea | Reverse-engineering audit of our own deliverables or authorized targets | `npx rea-agents@6.10.1 setup` | Back up settings, then register MCP | MIT (dependent tools have separate licenses; DISCLAIMER limits use to lawful analysis) |
| caveman | Reducing agent output and reading volume | `npx @caveman-ai/cli@4.2.0` | Show the changes, then install | Apache-2.0 (name and logo are trademarks) |
| chrome-devtools-mcp | In projects with a UI, when the agent checks the screen, console, network, accessibility tree, and performance in a real Chrome (`uiuxpatterns` review) | `claude plugin marketplace add ChromeDevTools/chrome-devtools-mcp`, then `claude plugin install chrome-devtools-mcp@chrome-devtools-plugins`. Or in the MCP settings, `npx -y chrome-devtools-mcp@1.14.0` | Plugin or MCP server added. Chrome is launched with a dedicated profile on each call | Apache-2.0 |
| gitleaks | Secret detection hook before the first commit (procedure below) | Procedure below | `.git/hooks/pre-commit` or `.pre-commit-config.yaml` added | MIT |

Notes
- The PyPI name of graphify is `graphifyy` (two y's)
- Use rea only on targets you are authorized to analyze
- For the marketplace route (the diagram-design and chrome-devtools-mcp plugins), no way to pin a version was found [unverified]. After installing, record the installed version with `claude plugin list`. The diagram-design repository HEAD on 2026-11-25 was `67dbb00` (`git ls-remote`)
- The install commands above follow each repository's README; recheck the latest README before running
- chrome-devtools-mcp: usage statistics are sent to Google by default (disable with `--no-usage-statistics`). The performance tools may send traced URLs to the CrUX API (disable with `--no-performance-crux`). Browser content is exposed to the model, so do not open sensitive sites or logged-in screens with personal data. Instructions embedded in page content may reach the model. Opening a remote debugging port lets other apps on the same PC control the browser. The default behavior uses a dedicated profile; `--autoConnect` reaches open windows of your everyday profile, so do not use it

## Secret detection hook (gitleaks)

Blocks secrets (keys, tokens) inside the repository before they are committed. Sources: the github.com/gitleaks/gitleaks README and `.pre-commit-hooks.yaml`. Latest tag `v8.30.1` (2026-11-25, `git ls-remote`). The README states that only security patches are accepted, with no new features. Do this only after approval, in a repository where `git init` is done. If `.git/hooks/pre-commit` already exists, do not overwrite it; tell the user.

Method A. Wire a self-installed gitleaks as the hook
1. Install gitleaks (README): `brew install gitleaks`, or the Docker image, or a release binary. For a release binary, check the sha256 against `gitleaks_8.30.1_checksums.txt` from the same release
2. Write the following two lines to `.git/hooks/pre-commit` and make it executable
```sh
#!/bin/sh
exec gitleaks git --pre-commit --redact --staged --verbose
```
- Test result (2026-11-25, Windows, release `gitleaks_8.30.1_windows_x64.zip`, sha256 matched): staging strings shaped like a fake AWS key and a GitHub token and committing blocks the commit with exit code 1. A commit with no secrets passes
- Bypass: `git commit --no-verify` (do not use). `.git/hooks/` is not pushed to the repository, so reinstall on each clone

Method B. `pre-commit` framework (the config file `.pre-commit-config.yaml` can be committed to the repository for team sharing)
1. `pip install pre-commit` (skip if already installed)
2. `.pre-commit-config.yaml`
```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.30.1
    hooks:
      - id: gitleaks
```
3. `pre-commit install`
- The entry of hook ID `gitleaks` is the same as method A, `gitleaks git --pre-commit --redact --staged --verbose`. Skip: `SKIP=gitleaks git commit -m "..."` (do not use)
- Hook installation via `pre-commit install` was verified (pre-commit 4.7.0). Whether the hook run blocks a secret commit is [not run] (the step that fetches and builds the Go source did not finish within 280 seconds and was stopped)
