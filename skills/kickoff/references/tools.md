# 선택 도구 (승인한 것만 설치)

2026-11-23 및 2026-11-25 에 저장소 README 와 라이선스 문서를 읽고 정리했다 (설치와 실행은 하지 않음). 설치형 도구는 에이전트 설정을 바꾼다.

| 도구 | 쓰는 때 | 설치 명령 (공식) | 설정 변경 | 라이선스 |
|---|---|---|---|---|
| diagram-design | 구성도, 흐름도 등 다이어그램을 HTML 및 SVG 한 파일로 만들 때 | `/plugin marketplace add cathrynlavery/diagram-design` 후 `/plugin install diagram-design@diagram-design` | 플러그인 추가 | MIT |
| graphify | 코드와 문서를 지식 그래프로 만들어 질의할 때 (큰 저장소) | `uv tool install graphifyy` 후 `graphify install` | 어시스턴트 설정 (README 의 훅 동작은 미확인) | Apache-2.0 |
| rea | 자사 납품물이나 허가된 대상의 역공학 점검 | `npx rea-agents setup` | 설정 백업 후 MCP 등록 | MIT (의존 도구 라이선스 별도, 합법 분석 한정 DISCLAIMER 있음) |
| caveman | 에이전트 출력과 읽기량 절감 | `npx @caveman-ai/cli@latest` | 변경 내용을 보여 준 뒤 설치 | Apache-2.0 (이름과 로고는 상표) |
| chrome-devtools-mcp | 화면이 있는 프로젝트에서 에이전트가 실제 Chrome 으로 화면, 콘솔, 네트워크, 접근성 트리, 성능을 확인할 때 (`uiuxpatterns` 검수) | `/plugin marketplace add ChromeDevTools/chrome-devtools-mcp` 후 `/plugin install chrome-devtools-mcp@chrome-devtools-plugins`. 또는 MCP 설정에 `npx -y chrome-devtools-mcp@latest` | 플러그인 또는 MCP 서버 추가. 호출 때 Chrome 이 전용 프로필로 실행됨 | Apache-2.0 |

주의
- graphify 의 PyPI 이름은 `graphifyy` (y 두 개)
- rea 는 권한이 있는 대상에만 쓴다
- 위 설치 명령은 각 저장소 README 기준이며, 실행 전에 최신 README 를 다시 확인한다
- chrome-devtools-mcp: 사용 통계가 기본으로 Google 에 전송된다 (끄기: `--no-usage-statistics`). 성능 도구는 추적한 주소를 CrUX API 로 보낼 수 있다 (끄기: `--no-performance-crux`). 브라우저의 내용이 모델에 노출되므로 민감한 사이트와 로그인한 개인정보 화면을 열지 않는다. 페이지 내용에 섞인 지시문이 모델에 전달될 수 있다. 원격 디버깅 포트를 열면 같은 PC 의 다른 앱이 브라우저를 제어할 수 있다. 기본 동작은 전용 프로필이고 `--autoConnect` 는 평소 쓰는 프로필의 열린 창에 접근하므로 쓰지 않는다
