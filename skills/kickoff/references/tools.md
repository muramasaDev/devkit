# 선택 도구 (승인한 것만 설치)

2026-11-23 및 2026-11-25 에 저장소 README 와 라이선스 문서를 읽고 정리했다 (gitleaks 외에는 설치와 실행을 하지 않음). 설치형 도구는 에이전트 설정을 바꾼다.

명령 형식
- 에이전트는 슬래시 명령(`/plugin ...`)을 실행할 수 없으므로 `claude plugin ...` CLI 형태로 적는다 (`claude plugin --help` 로 `marketplace add`, `install` 하위 명령 확인, Claude Code 2.1.332)
- `@latest` 는 쓰지 않는다. 버전 미고정 원격 실행은 `securecoding` SEC-16(무결성 검사 없는 코드 실행 금지)과 충돌한다. 아래 버전은 2026-11-25 에 npm 레지스트리(`npm view <패키지> version`) 또는 PyPI(`pip index versions`)로 확인한 값이며, 실행 전에 같은 명령으로 다시 확인한다

| 도구 | 쓰는 때 | 설치 명령 (공식, 버전 고정) | 설정 변경 | 라이선스 |
|---|---|---|---|---|
| diagram-design | 구성도, 흐름도 등 다이어그램을 HTML 및 SVG 한 파일로 만들 때 | `claude plugin marketplace add cathrynlavery/diagram-design` 후 `claude plugin install diagram-design@diagram-design` | 플러그인 추가 | MIT |
| graphify | 코드와 문서를 지식 그래프로 만들어 질의할 때 (큰 저장소) | `uv tool install graphifyy==0.9.119` 후 `graphify install` | 어시스턴트 설정 (README 의 훅 동작은 미확인) | Apache-2.0 |
| rea | 자사 납품물이나 허가된 대상의 역공학 점검 | `npx rea-agents@6.10.1 setup` | 설정 백업 후 MCP 등록 | MIT (의존 도구 라이선스 별도, 합법 분석 한정 DISCLAIMER 있음) |
| caveman | 에이전트 출력과 읽기량 절감 | `npx @caveman-ai/cli@4.2.0` | 변경 내용을 보여 준 뒤 설치 | Apache-2.0 (이름과 로고는 상표) |
| chrome-devtools-mcp | 화면이 있는 프로젝트에서 에이전트가 실제 Chrome 으로 화면, 콘솔, 네트워크, 접근성 트리, 성능을 확인할 때 (`uiuxpatterns` 검수) | `claude plugin marketplace add ChromeDevTools/chrome-devtools-mcp` 후 `claude plugin install chrome-devtools-mcp@chrome-devtools-plugins`. 또는 MCP 설정에 `npx -y chrome-devtools-mcp@1.14.0` | 플러그인 또는 MCP 서버 추가. 호출 때 Chrome 이 전용 프로필로 실행됨 | Apache-2.0 |
| gitleaks | 첫 커밋 전 비밀 탐지 훅 (아래 절차) | 아래 절차 | `.git/hooks/pre-commit` 또는 `.pre-commit-config.yaml` 추가 | MIT |

주의
- graphify 의 PyPI 이름은 `graphifyy` (y 두 개)
- rea 는 권한이 있는 대상에만 쓴다
- 마켓플레이스 방식(diagram-design, chrome-devtools-mcp 플러그인)은 버전 고정 방법을 확인하지 못했다 [미확인]. 설치 뒤 `claude plugin list` 로 설치된 버전을 기록한다. diagram-design 저장소 HEAD 는 2026-11-25 에 `67dbb00` (`git ls-remote`)
- 위 설치 명령은 각 저장소 README 기준이며, 실행 전에 최신 README 를 다시 확인한다
- chrome-devtools-mcp: 사용 통계가 기본으로 Google 에 전송된다 (끄기: `--no-usage-statistics`). 성능 도구는 추적한 주소를 CrUX API 로 보낼 수 있다 (끄기: `--no-performance-crux`). 브라우저의 내용이 모델에 노출되므로 민감한 사이트와 로그인한 개인정보 화면을 열지 않는다. 페이지 내용에 섞인 지시문이 모델에 전달될 수 있다. 원격 디버깅 포트를 열면 같은 PC 의 다른 앱이 브라우저를 제어할 수 있다. 기본 동작은 전용 프로필이고 `--autoConnect` 는 평소 쓰는 프로필의 열린 창에 접근하므로 쓰지 않는다

## 비밀 탐지 훅 (gitleaks)

저장소 안의 비밀(키, 토큰)이 커밋되기 전에 막는다. 출처: github.com/gitleaks/gitleaks README 및 `.pre-commit-hooks.yaml`. 최신 태그 `v8.30.1` (2026-11-25, `git ls-remote`). README 에 기능 추가 없이 보안 패치만 받는다는 안내가 있다. 승인받은 뒤 `git init` 이 끝난 저장소에서 하고, 이미 `.git/hooks/pre-commit` 이 있으면 덮어쓰지 않고 사용자에게 알린다.

방법 A. 직접 설치한 gitleaks 를 훅으로 연결
1. gitleaks 설치 (README): `brew install gitleaks`, 또는 Docker 이미지, 또는 릴리스 바이너리. 릴리스 바이너리는 같은 릴리스의 `gitleaks_8.30.1_checksums.txt` 로 sha256 을 대조한다
2. `.git/hooks/pre-commit` 에 아래 두 줄을 쓰고 실행 권한을 준다
```sh
#!/bin/sh
exec gitleaks git --pre-commit --redact --staged --verbose
```
- 시험 결과(2026-11-25, Windows, 릴리스 `gitleaks_8.30.1_windows_x64.zip` sha256 일치): 가짜 AWS 키 및 GitHub 토큰 형태 문자열을 스테이징하고 커밋하면 종료 코드 1 로 커밋이 막힌다. 비밀이 없는 커밋은 통과한다
- 우회: `git commit --no-verify` (쓰지 않는다). `.git/hooks/` 는 저장소에 올라가지 않으므로 클론마다 다시 설치한다

방법 B. `pre-commit` 프레임워크 (팀 공유용 설정 파일 `.pre-commit-config.yaml` 을 저장소에 올릴 수 있음)
1. `pip install pre-commit` (이미 있으면 생략)
2. `.pre-commit-config.yaml`
```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.30.1
    hooks:
      - id: gitleaks
```
3. `pre-commit install`
- 훅 ID `gitleaks` 의 entry 는 방법 A 와 같은 `gitleaks git --pre-commit --redact --staged --verbose`. 건너뛰기: `SKIP=gitleaks git commit -m "..."` (쓰지 않는다)
- `pre-commit install` 로 훅 설치까지 확인했다 (pre-commit 4.7.0). 훅 실행으로 비밀 커밋이 막히는지는 [미실행] (Go 소스를 받아 빌드하는 단계가 280초 안에 끝나지 않아 중단)
