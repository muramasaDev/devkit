# 선택 도구 (승인한 것만 설치)

2026-11-23 저장소 README 와 라이선스 문서를 읽고 정리했다 (설치와 실행은 하지 않음). 설치형 도구는 에이전트 설정을 바꾼다.

| 도구 | 쓰는 때 | 설치 명령 (공식) | 설정 변경 | 라이선스 |
|---|---|---|---|---|
| diagram-design | 구성도, 흐름도 등 다이어그램을 HTML 및 SVG 한 파일로 만들 때 | `/plugin marketplace add cathrynlavery/diagram-design` 후 `/plugin install diagram-design@diagram-design` | 플러그인 추가 | MIT |
| graphify | 코드와 문서를 지식 그래프로 만들어 질의할 때 (큰 저장소) | `uv tool install graphifyy` 후 `graphify install` | 어시스턴트 설정 (README 의 훅 동작은 미확인) | Apache-2.0 |
| rea | 자사 납품물이나 허가된 대상의 역공학 점검 | `npx rea-agents setup` | 설정 백업 후 MCP 등록 | MIT (의존 도구 라이선스 별도, 합법 분석 한정 DISCLAIMER 있음) |
| caveman | 에이전트 출력과 읽기량 절감 | `npx @caveman-ai/cli@latest` | 변경 내용을 보여 준 뒤 설치 | Apache-2.0 (이름과 로고는 상표) |

주의
- graphify 의 PyPI 이름은 `graphifyy` (y 두 개)
- rea 는 권한이 있는 대상에만 쓴다
- 위 설치 명령은 각 저장소 README 기준이며, 실행 전에 최신 README 를 다시 확인한다
