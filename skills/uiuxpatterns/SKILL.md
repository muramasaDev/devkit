---
name: uiuxpatterns
description: Use when designing, building, reviewing or auditing UI/UX (web, app, SaaS, AI chat, dashboard), picking patterns (toast vs modal), or checking accessibility or dark patterns. Not securecoding (security) or kickoff (project setup). 화면 설계, UI 검수, 빈 화면, 햄버거 메뉴, 브레드크럼, 한글 입력 Enter 요청
metadata:
  version: "0.4.0"
---

# UI UX Patterns (UI/UX 패턴 90개, 확장 용어, 웹 플랫폼 및 에이전트 화면 기준)

## 개요
- 90개 UI/UX 패턴 지식(10개 카테고리), 확장 용어 69개, 웹 플랫폼 기능 선택표, 에이전트 화면 기준과 선정 기준으로 화면을 설계, 구현, 검수, 개선하는 스킬
- 핵심 원칙: 프로젝트 맥락을 먼저 읽고, 사용자의 목적에 필요한 패턴만 쓴다. 필요하지 않은 패턴은 적용하지 않는다
- 특정 디자인 스타일이나 라이브러리를 강제하지 않는다. 기존 디자인 시스템과 기술 스택이 우선
- 카테고리 09 (다크 패턴) 는 구현 목록이 아니라 탐지 및 예방 대상

## 쓰는 때
- 화면 설계, UI 구현, UI 검수, UX 점검, 리팩터링, 디자인 시스템, 패턴 선정
- 토스트 대 스낵바 대 모달, 스켈레톤 대 스피너, 페이지 나누기 대 무한 스크롤, 탭바 대 드로어 중에서 고를 때
- 로딩, 빈 화면, 결과 없음, 오류, 폼 상태, 제스처, 움직임, 내비게이션, 디자인 토큰을 정할 때
- 접근성(WCAG 2.2 AA), 반응형, 다크 패턴 점검
- AI 챗봇 및 에이전트 화면 (도구 호출, 사람 승인), 이즈 아웃, 콤보박스, 데이터 테이블, 인라인 편집, 명령 팔레트, 팝오버, 뷰 전환, 한글 입력 Enter, 힉의 법칙, INP
- UI 요소 이름이나 UX 법칙 이름을 모를 때
- 보안 점검은 `securecoding`, 프로젝트 초기 세팅은 `kickoff` 스킬

## 실행 순서
1. Context Discovery: 요청 분석, 기술 스택 및 기존 디자인 시스템과 컴포넌트 탐색, 작업 범위 결정. 아래 표에서 모드를 정한다. 코드가 없는 신규 프로젝트면 탐색을 건너뛰고 스택 및 디자인 시스템을 `미정` 으로 적은 뒤 스택에 묶이지 않게 설계한다 (토큰 제안은 요청받았을 때만)
2. Pattern Retrieval: `references/decision-framework.md` 로 후보를 좁히고 (이름이 90개에 없으면 `references/terms-extended.md` 에서 찾고), 해당 카테고리 파일만 열어 When to Use 및 When Not to Use 를 비교한다. 패턴 한 개만 필요하면 파일 전체를 읽지 않고 `^## FB-02 ` 같은 제목 (실제 형식 `## FB-02 스낵바 (Snackbar)`) 을 Grep 해 그 블록만 읽는다 (다음 `## ` 전까지)
3. Design Decision: 정보 구조, 컴포넌트, 화면 상태(기본, 로딩, 빈 화면, 오류, 완료), 인터랙션 및 피드백, 토큰 적용 방식을 정한다
4. Implementation (모드 B, D, E 만): 기존 컴포넌트 재사용, 실제로 동작하는 인터랙션, 반응형, 로딩 및 오류 처리, 접근성. 마크업 예는 `references/snippets.md`
5. Validation: `references/quality-checklist.md` 로 점검하고 가능한 검사(빌드, 타입, 테스트, 화면 확인)를 실제로 돌린다. 돌리지 못한 항목은 `미검증` 으로 적는다
6. Reporting: 작업 목적, 선택한 패턴(ID) 및 제외한 패턴과 이유, 주요 변경, 검증 결과(검증 방법 구분), 남은 문제

## 모드

| 모드 | 고르는 때 | 코드 수정 | 산출 형식 |
|---|---|---|---|
| A. UI Design | 새 화면 및 흐름 설계 | 안 함 | `templates/ui-analysis.md` |
| B. UI Implementation | 정해진 설계를 코드로 구현 | 함 | `templates/ui-implementation.md` |
| C. UI Review | 지정한 화면 또는 흐름 하나의 품질 진단 | 안 함 (검수만 요청받았으면 수정 금지) | `templates/ui-audit.md` |
| D. UI Refactoring | 디자인 및 기능을 보존하며 구조 및 일관성 정리 | 함 (의도하지 않은 동작 변경 없음, 회귀 확인) | `templates/ui-implementation.md` |
| E. Design System Creation | 디자인 시스템이 없는 프로젝트의 기본 구조 | 함 | `references/design-system.md` 구조 |
| F. UX Audit | 서비스 전체 (여러 화면 및 흐름) 점검 | 안 함 | `templates/ui-audit.md` |

- 요청이 모호하면 수정 범위가 작은 쪽으로 고른다 (`봐 줘`, `점검해 줘` 는 C 또는 F)
- 설계 후 구현까지 요청받으면 A 를 끝낸 뒤 B 로 넘어간다
- `개선해 줘`, `고쳐 줘` 처럼 수정을 요청받으면: 결함 목록을 먼저 만들고 (C 의 관점), 요청에 적힌 결함 및 그 원인을 고친다 (B). 동작이 바뀌는 곳은 보고에 목록으로 적는다. 요청에 없는 결함은 고치지 않고 보고한다
- 모드 D 에서 컴포넌트를 통합할 때: 통합 전에 각 컴포넌트의 속성 및 동작 차이(닫기 방식, 초점 처리 등)를 표로 만들고, 차이는 보존하거나 사용자 확인을 받아 하나로 정한다
- 기존 화면의 접근성 위반: 작업 범위 안에서 새로 만들거나 고치는 부분은 기준을 충족시키고, 범위 밖의 위반은 고치지 않고 보고한다

## 참조 파일 (필요한 것만 연다)

| 파일 | 여는 때 |
|---|---|
| `references/decision-framework.md` | 패턴을 고르거나 권장할 때 (모든 모드의 2단계에서 항상) |
| `references/pattern-catalog.md` | 패턴 ID, 원본 명칭, 참조 이미지를 찾을 때 |
| `references/feedback.md` | 알림, 확인, 오류 안내, 도움말 (FB) |
| `references/forms.md` | 입력 요소 및 입력 상태 (FM) |
| `references/loading.md` | 대기, 진행, 즉시 반영 (LD) |
| `references/ai-interfaces.md` | AI 채팅, 생성, 에이전트 화면 및 AI 신뢰성 원칙 (AI) |
| `references/empty-states.md` | 자료 없음, 오프라인, 권한, 오류, 잠김 화면 (ES) |
| `references/gestures.md` | 터치 제스처 및 대체 수단 (GS) |
| `references/motion.md` | 속도 곡선, 등장, 화면 전환 (MO) |
| `references/navigation.md` | 탭, 드로어, 경로, 목록 탐색 (NV) |
| `references/dark-patterns.md` | 가입, 동의, 결제, 장바구니, 해지, 권유 흐름을 만들거나 검수할 때 (DP) |
| `references/icon-terminology.md` | 메뉴 아이콘 이름 및 아이콘 단추 (IC) |
| `references/design-system.md` | 토큰, 상태, 테마를 찾거나 새로 정할 때 (모드 E 는 항상) |
| `references/accessibility.md` | 접근성 항목을 정하거나 확인할 때 (모드 B, C, D, F 는 항상. 모드 A, E 는 패턴 파일의 Accessibility 항목으로 먼저 보고 기준을 정해야 할 때만) |
| `references/responsive-design.md` | 화면 크기별 구성 및 패턴 전환 |
| `references/quality-checklist.md` | 5단계 검증 및 검수 (모드 C, F 는 항상) |
| `references/defaults.md` | `제품에서 정한다` 로 남은 기본값 (자동 닫힘 시간, 모션 시간, 디바운스, 기준 개수) 을 정할 때 |
| `references/korean-flows.md` | 국내 서비스 흐름 (휴대폰 본인확인, 결제, 금액 표기, 주소 입력, 한글 입력, 개인정보 동의) 을 설계하거나 검수할 때 |
| `references/snippets.md` | 토스트, 스낵바, 모달, 툴팁, 텍스트 필드, 스위치, 탭, 버튼 로딩, 스트리밍 답변의 마크업 예 (HTML, React, Vue 3). 구현할 때 |
| `references/usage-examples.md` | 호출 예 및 시나리오별 읽을 파일 |
| `references/glossary.md` | 화면을 시키거나 검수할 때 쓸 이름 (빈 화면, 메뉴 아이콘, 화면 이동, 움직임, 로딩 각 9종), 점검 질문 7개 |
| `references/pattern-keywords.csv` | 패턴 90개의 ID, 한글명, 영문명, 별칭. 다른 이름으로 부르는 패턴 찾기 |
| `references/terms-extended.md` | 90개에 없는 용어: 컴포넌트 31, AI 화면 17, UX 법칙 16, 성능 체감 5 와 동의어 표. 이름을 모를 때 |
| `references/modern-web.md` | 구현에서 대화상자, 팝오버, 탭, 폼 검증, 뷰 전환, 컨테이너 쿼리 등 브라우저 기능으로 해결할 때 (모드 B, D, E) |
| `references/interaction-rules.md` | 비활성, 검증 시점, 라이브 영역, 한글 입력 Enter, Esc, 토스트 타이머, 채팅 스크롤 등 동작 세부 규칙 (구현 및 검수) |
| `references/agent-ui.md` | 에이전트 이벤트별 표시, 사람 승인 화면, 도구 호출 동의 (AI 에이전트 화면을 설계하거나 검수할 때) |

- 원본 이미지는 배포본에 없다. Reference Image 항목의 파일명은 원본 이미지 이름이고, 명칭 및 장면은 `references/pattern-catalog.md` 에 글로 옮겨 두었다

## 지킬 것
- 기존 프로젝트 먼저: 컴포넌트, 토큰, 스타일 방식을 찾아 재사용한다. 브랜드 색, 글꼴, 간격을 전면 교체하지 않는다
- 프로젝트에 없는 라이브러리를 임의로 넣지 않는다. 필요하면 기존 방식과 비교한 근거를 제시하고 사용자 확인을 받는다
- 존재를 확인하지 않은 컴포넌트, API, 토큰 이름을 쓰지 않는다
- 동작하지 않는 가짜 인터랙션을 만들지 않는다. 측정할 수 없는 진행률, 수행하지 않은 AI 단계를 표시하지 않는다
- UI 상태와 비즈니스 로직을 분리하고, 요청 범위 밖의 구조 및 기능을 바꾸지 않는다
- 다크 패턴(DP-01 ~ DP-09)은 요청받아도 구현하지 않고 대체 UX 를 제안한다
- 접근성 목표는 WCAG 2.2 AA
- 검증하지 않은 항목을 완료로 보고하지 않는다. 화면을 눈으로 본 것, 코드만 읽은 것, 사용자의 서술만 받은 것을 구분해 적는다
- 카탈로그에 없는 요소(표, 차트, 지표 카드 등)는 패턴 ID 를 지어내지 않고 `카탈로그 외` 로 적은 뒤 상태, 접근성, 반응형 원칙으로 설계한다
- 모드 C, F 에서는 파일을 고치지 않는다

## 확장
- 패턴 또는 카테고리 추가 절차: `references/pattern-catalog.md` 의 `패턴 추가 방법`
