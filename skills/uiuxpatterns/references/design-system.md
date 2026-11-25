# Design System Guidelines

- 역할: 기존 디자인 시스템을 찾아 따르는 방법, 디자인 시스템이 없을 때 제안하는 기본 토큰 구조
- 원칙: 특정 스타일을 강제하지 않는다. 기존 값이 있으면 그 값이 정본이고, 아래 구조는 없는 프로젝트에만 제안한다

## 1. 기존 디자인 시스템 탐색 (항상 먼저)

| 찾는 것 | 보는 곳 |
|---|---|
| UI 라이브러리 | `package.json` 등 의존성 목록, import 문 |
| 토큰 | CSS 변수(`:root`, `[data-theme]`), Tailwind 설정 또는 `@theme`, Sass 변수, 테마 객체, 토큰 JSON |
| 공용 컴포넌트 | `components/`, `ui/`, `shared/`, 스토리 파일 |
| 스타일 방식 | CSS Modules, 유틸리티 클래스, CSS-in-JS, 전역 CSS 중 무엇인지 |
| 문서 | 디자인 가이드, README, 스토리북, 디자인 파일 링크 |
| 실제 사용 값 | 기존 화면에서 반복되는 색, 간격, 반지름, 글자 크기 |

- 찾은 결과로 판단: 토큰 및 컴포넌트가 있으면 재사용, 일부만 있으면 빈 곳만 같은 이름 규칙으로 보충, 없으면 2절 구조를 제안
- 토큰 없이 값이 흩어져 있으면 전면 교체하지 않고, 작업 범위에서 쓰는 값만 기존 값에 맞춘다. 토큰 도입은 별도 제안으로 보고한다
- 브랜드 색, 글꼴, 간격을 임의로 바꾸지 않는다. 기존 토큰 값의 대비 미달 등 기준 위반은 값을 바꾸지 말고 근거와 함께 보고한다 (수정 요청을 받은 경우에만 고침). 작업 범위 안에서 새로 만드는 부분은 기준을 충족하는 기존 토큰을 골라 쓴다

## 2. 기본 토큰 구조 (디자인 시스템이 없는 프로젝트)

### 계층
| 계층 | 뜻 | 이름 예 |
|---|---|---|
| Primitive | 값 그 자체 | `--blue-600`, `--space-4`, `--radius-2` |
| Semantic | 쓰임새에 붙인 이름. 컴포넌트는 이 계층만 참조 | `--color-bg-surface`, `--color-text-primary`, `--color-border-default`, `--color-action-primary`, `--color-feedback-error` |
| Component (필요 시) | 한 컴포넌트에만 쓰는 값 | `--button-height-md` |

- 새 토큰은 의미 기반 이름으로 만든다 (`--color-feedback-error` 처럼 쓰임새. `--red` 처럼 값 이름을 컴포넌트에서 직접 쓰지 않음)
- 테마는 Semantic 계층의 값만 바꿔서 만든다

### Visual Foundation
| 영역 | 정할 것 |
|---|---|
| Color System | 중립 단계, 브랜드 단계, 각 단계의 명도 차이가 대비 기준을 충족하는지 |
| Semantic Colors | 배경(surface 단계), 글자(primary, secondary, disabled), 테두리, 행동(primary), 피드백(success, warning, error, info) |
| Typography | 글꼴 묶음, 크기 단계, 줄 높이, 굵기. 본문 크기는 rem 기준 |
| Spacing | 한 가지 기준 단위의 배수 단계 (기준 단위는 프로젝트가 정함) |
| Layout & Grid | 최대 너비, 열, 여백, 컨테이너 |
| Border Radius | 단계 3 ~ 4개 (작은 요소, 카드, 완전 둥근 것) |
| Border & Shadow | 테두리 굵기 및 색, 그림자 단계 |
| Elevation | 겹침 순서(z-index 단계)와 그림자의 대응: 기본, 띄움(카드), 덮개(드롭다운, 시트), 모달, 알림 |
| Iconography | 아이콘 묶음 하나, 크기 단계, 선 굵기. 글자 없는 아이콘 단추는 접근성 이름 필수 |
| Responsive Breakpoints | 중단점 이름 및 값 (`responsive-design.md`) |
| Motion | 지속 시간 단계, 속도 곡선 (`motion.md`). 한 곳에서 정함 |

- 수치(px, ms, 색 값)는 이 스킬이 정하지 않는다. 기존 화면의 값 또는 사용 중인 UI 라이브러리의 기본값에서 가져온다

### Component States
모든 상호작용 컴포넌트는 아래 상태 중 해당하는 것을 정의한다

| 상태 | 정의할 것 |
|---|---|
| Default | 기본 모양 |
| Hover | 포인터를 올렸을 때 (터치 기기에는 없음. hover 에만 있는 정보 금지) |
| Focus | 키보드 초점. `:focus-visible` 로 보이는 표시, 대비 3:1 (WCAG 1.4.11, 2.4.7) |
| Active | 누르는 순간 |
| Disabled | 비활성. 색만으로 구분하지 않음 |
| Loading | 처리 중. 중복 실행 방지 (`loading.md` LD-06) |
| Success | 완료 |
| Warning | 주의 |
| Error | 오류. 색 및 문구 및 아이콘 병행 (`feedback.md` FB-06) |
| Empty | 내용 없음 (`empty-states.md`) |

- 상태는 색 하나로만 구분하지 않는다 (WCAG 1.4.1)
- 화면 단위 상태(로딩, 빈 화면, 오류, 일부 실패, 완료)도 컴포넌트 상태와 별도로 정의한다

### Themes
| 테마 | 방법 |
|---|---|
| Light Mode | 기본 Semantic 값 |
| Dark Mode | Semantic 값만 재정의. `prefers-color-scheme` 및 사용자 선택 반영. 색을 단순 반전하지 않고 대비를 다시 확인 |
| High Contrast | `prefers-contrast: more` 및 `forced-colors: active` 에서 테두리 및 초점 표시가 유지되는지 확인 |
| Project-Specific Themes | 브랜드별 값 묶음을 Semantic 계층에서 교체 |

## 3. 모드 E 산출물
1. Foundation: 위 Visual Foundation 표의 각 영역 값
2. Tokens: Primitive 및 Semantic 토큰 파일 (프로젝트의 스타일 방식에 맞는 형식)
3. Components: 실제로 화면에 쓰이는 것부터 (단추, 입력, 알림 등). 쓰이지 않는 컴포넌트를 미리 만들지 않음
4. Component States: 컴포넌트별 상태 정의
5. Documentation: 토큰 표, 컴포넌트별 쓰는 때 및 쓰지 않는 때
6. Usage Guidelines: 이름 규칙, 새 토큰 및 컴포넌트를 추가하는 절차

## 4. 점검
- 컴포넌트가 Primitive 값이나 직접 쓴 색 값을 참조하지 않는가
- 같은 뜻의 토큰이 두 이름으로 있지 않은가
- 다크 테마 및 고대비에서 글자, 테두리, 초점 표시가 보이는가
- 새로 만든 컴포넌트가 기존 컴포넌트와 역할이 겹치지 않는가

## 5. 중복 컴포넌트 통합 (모드 D)
1. 대상 컴포넌트마다 속성, 모양, 동작(열기 및 닫기 방식, 초점 처리, 크기 종류)을 표로 비교한다
2. 남길 컴포넌트를 정한다 (기존 공용 컴포넌트가 있으면 그것). 차이 나는 동작은 속성으로 보존하거나 사용자 확인을 받아 하나로 정한다
3. 호출하는 곳을 한 곳씩 옮기고 그때마다 빌드 및 해당 화면을 확인한다
4. 호출이 0건이 된 컴포넌트를 지운다
5. 보고에 옮긴 호출 위치, 바뀐 동작(없으면 `없음`), 확인한 화면을 적는다
