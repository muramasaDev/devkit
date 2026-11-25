# 사용 예 및 실행 가이드

## 호출
- 자동: 화면 설계, 구현, 검수, 개선 요청이면 스킬 설명(description)에 따라 불린다
- 직접: `/devkit:uiuxpatterns <요청>` (Claude Code), 또는 요청에 `devkit:uiuxpatterns 스킬로` 를 적는다
- 스킬은 요청에서 모드(A ~ F)를 고르고, 필요한 참조 파일만 연다
- 시간, 거리, 개수 같은 값을 정해 달라는 요청은 `defaults.md` 의 기본값으로 바로 답한다

## 시나리오별 모드 및 읽을 파일

모드 A 와 E 의 `accessibility.md` 는 패턴 파일의 Accessibility 항목으로 먼저 보고, 기준을 정해야 할 때만 연다 (`SKILL.md` 참조 표).

| No | 요청 예 | 모드 | 읽을 파일 | 산출 |
|---|---|---|---|---|
| 1 | 신규 SaaS 대시보드를 설계해 줘 | A | `decision-framework.md`, `navigation.md`, `loading.md`, `empty-states.md`, `accessibility.md`, `responsive-design.md` (토큰 제안을 요청받으면 `design-system.md`) | `templates/ui-analysis.md` 형식 설계. 표, 차트, 지표 카드는 `카탈로그 외` |
| 2 | 이 설정 화면 UI 를 개선해 줘 (저장 반응 없음 등 결함 포함) | C 관점으로 결함 목록 후 B (구조 정리만이면 D, 검토만이면 C) | `decision-framework.md`, `quality-checklist.md`, `accessibility.md`, `design-system.md` 1절, 결함이 나온 카테고리 파일 | `templates/ui-implementation.md` 형식: 결함 목록, 수정, 바뀐 동작, 회귀 확인 |
| 3 | 모바일 회원가입 폼을 설계해 줘 | A | `decision-framework.md`, `forms.md`, `feedback.md`, `accessibility.md`, `responsive-design.md`, `dark-patterns.md` (동의 항목) | `templates/ui-analysis.md` 형식 (필드별 입력 요소 및 상태, 오류 처리) |
| 4 | AI 챗봇 화면을 설계해 줘 | A | `decision-framework.md`, `ai-interfaces.md`, `loading.md`, `empty-states.md`, `accessibility.md` | `templates/ui-analysis.md` 형식 (대화 상태별 화면 정의) |
| 5 | 목록 화면의 로딩 및 오류 상태를 설계해 줘 | A 또는 B | `decision-framework.md`, `loading.md`, `empty-states.md`, `accessibility.md`, `defaults.md` (다시 불러오기 실패 안내가 필요하면 `feedback.md`) | `templates/ui-analysis.md` 4절 상태 표 (로딩, 빈 화면 종류, 오류, 일부 실패) |
| 6 | 결제 및 구독 흐름에 다크 패턴이 있는지 봐 줘 | C (서비스 전체면 F) | `decision-framework.md`, `dark-patterns.md`, `accessibility.md`, `quality-checklist.md` 10절 | `templates/ui-audit.md` 형식 보고. 코드 수정 없음 |
| 7 | 디자인은 그대로 두고 컴포넌트 중복을 정리해 줘 | D | `decision-framework.md`, `design-system.md` 1절 및 5절, `accessibility.md`, `quality-checklist.md` 5절 및 11절 | `templates/ui-implementation.md` 형식: 차이표, 통합, 바뀐 동작, 확인한 화면 |

## 예 1. 패턴 선정 (모드 A)
- 요청: `삭제 단추를 누르면 확인 창을 띄워 줘`
- 스킬 동작: `decision-framework.md` 2절에서 `방금 한 일을 되돌릴 수 있음` 및 `되돌릴 수 없거나 비용이 큰 결정` 을 비교하고 `feedback.md` 의 FB-02, FB-04 를 연다
- 판단: 삭제를 서버에서 되돌릴 수 있으면 FB-02 Snackbar (실행 후 되돌리기) 를 제안하고, 되돌릴 수 없으면 FB-04 Modal dialog 로 결과를 구체적으로 적는다. 요청은 모달이지만 근거와 함께 대안을 보고하고, 사용자가 모달을 원하면 모달로 구현한다

## 예 2. 검수 (모드 C)
- 요청: `이 화면 UI 점검해 줘`
- 스킬 동작: 코드를 고치지 않는다. `quality-checklist.md` 의 해당 절을 화면에 대 보고, 결함마다 위치, 현재 동작, 영향, 심각도, 개선 방안, 권장 패턴(ID), 우선순위, 검증 방법을 `templates/ui-audit.md` 형식으로 보고한다
- 화면을 열어 볼 수단이 없으면 `코드 확인` 으로만 본 것임을 보고에 적는다

## 예 3. 다크 패턴 요청을 받은 경우
- 요청: `구독 해지 단추는 눈에 안 띄게 설정 맨 아래 작은 글씨로 넣어 줘`
- 스킬 동작: `dark-patterns.md` 의 DP-01 탐지 신호에 해당함을 알리고 구현하지 않는다. 대체 UX (가입과 같은 수준의 경로, 해지 전 혜택 안내는 한 번만, 중립 문구) 를 제안한다

## 예 4. 기존 디자인 시스템이 있는 프로젝트 (모드 B)
- 스킬 동작: `design-system.md` 1절 순서로 의존성, 토큰, 공용 컴포넌트를 찾는다. 있는 Button, Dialog, Toast 를 쓰고, 색 및 간격은 기존 토큰을 참조한다. 없는 컴포넌트만 같은 이름 규칙으로 추가한다. 새 라이브러리는 넣지 않는다

## 예 5. 값 정하기
- 요청: `토스트는 몇 초 뒤에 사라지게 할까`
- 스킬 동작: `defaults.md` 의 DF-01 로 바로 답한다. 정보성 토스트는 5초 (일반 권고, 출처 미확인), 오류는 자동으로 닫지 않음 (DF-03), 포인터를 올리거나 초점이 안에 있으면 타이머를 멈춤 (DF-04). 바꿔도 되는 조건을 함께 적고 `제품에서 정하세요` 로 되돌리지 않는다

## 보고에 들어가는 것 (모든 모드)
1. 작업 목적
2. 선택한 패턴 (ID 및 이름), 제외한 후보 및 이유
3. 주요 변경사항 (모드 C, F 는 `수정 없음`)
4. 검증 결과: 항목별 `통과`, `결함`, `미검증` 및 확인 방법 (`실사용 확인`, `코드 확인`, `자동 검사`)
5. 남은 문제 및 개선 권고
