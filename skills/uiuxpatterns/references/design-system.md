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

- 수치(px, ms, 색 값)는 기존 값이 우선이다. 기존 화면의 값 또는 사용 중인 UI 라이브러리의 기본값이 있으면 그것을 쓰고, 아무 값도 없는 프로젝트만 바로 아래 `기본 토큰 값` 을 시작값으로 쓴다

### 기본 토큰 값 (기존 값이 전혀 없을 때의 시작값)
- 근거 표기: `계산` 은 WCAG 상대 휘도 정의로 직접 계산한 대비비(2026-11-25, Python, 임계값 0.04045 (WCAG 2.2 정의. 이전 값 0.03928 과 24쌍 결과 같음), 소수 둘째 자리 표기. 판정은 반올림하지 않은 값), `확인` 은 원문, `일반` 은 관용 값이며 규격이 아니다
- 브랜드가 정해지면 색 단계(brand)만 교체하고, 교체한 값은 아래 표의 사용 칸 기준으로 대비를 다시 계산한다

| 토큰 | 값 | 근거 |
|---|---|---|
| 간격 `--space-1` ~ `--space-16` | 4, 8, 12, 16, 24, 32, 48, 64px (0.25, 0.5, 0.75, 1, 1.5, 2, 3, 4rem). 이름 번호는 4px 배수 | 일반 |
| 글자 크기 `--text-xs` ~ `--text-3xl` | 0.75, 0.875, 1, 1.125, 1.25, 1.5, 2rem (12, 14, 16, 18, 20, 24, 32px). 본문은 1rem, 입력 칸 글자는 16px 이상 | 일반 |
| 줄 높이 | 본문 1.6, 제목 1.3, 한 줄 라벨 1.25 (단위 없는 값) | 일반 |
| 반지름 | `--radius-1` 4px, `--radius-2` 8px, `--radius-full` 9999px | 일반 |
| z-index | `--z-base` 0, `--z-raised` 10, `--z-overlay` 100 (드롭다운, 시트), `--z-modal` 200, `--z-toast` 300 | 일반 |
| 모션 시간 및 곡선 | `defaults.md` 의 DF-13 (짧음 100ms, 보통 300ms, 김 500ms) 및 DF-14 (곡선 4종) 를 그대로 쓴다. 토큰 이름 예: `--duration-short`, `--duration-medium`, `--duration-long`, `--ease-standard`. 값을 이 파일에서 따로 정하지 않는다 | `defaults.md` 의 근거 열 참조 |

중립 및 브랜드 색 단계 (대비는 흰색 `#FFFFFF` 및 다크 바탕 `neutral-900` 위의 값):

| 단계 | 값 | 흰색 위 | 다크 바탕 위 | 쓰는 곳 |
|---|---|---|---|---|
| neutral-50 | `#F8F9FA` | 1.05 | 16.92 | 연한 바탕, 다크 글자 |
| neutral-100 | `#F1F3F5` | 1.11 | 16.04 | 바탕 |
| neutral-200 | `#E4E7EB` | 1.24 | 14.38 | 구분선(정보 없는 장식) |
| neutral-300 | `#CBD2D9` | 1.53 | 11.69 | 구분선, 다크 보조 글자 |
| neutral-400 | `#9AA5B1` | 2.50 | 7.13 | 글자 및 입력 테두리에 쓰지 않음(3:1 미달) |
| neutral-500 | `#6B7785` | 4.56 | 3.91 | 입력 테두리, 안내 문구 |
| neutral-600 | `#52606D` | 6.46 | 2.76 | 보조 글자 |
| neutral-700 | `#3E4C59` | 8.81 | 2.02 | 본문 보조 |
| neutral-800 | `#1F2933` | 14.76 | 1.21 | 본문, 다크 띄운 바탕 |
| neutral-900 | `#121820` | 17.84 | 1.00 | 주 글자, 다크 바탕 |
| brand-300 | `#85B4FF` | 2.11 | 8.47 | 다크 테마의 행동 색 |
| brand-500 | `#2F7BEA` | 4.08 | 4.37 | 큰 글자 및 아이콘(3:1)만. 일반 글자 4.5:1 미달 |
| brand-600 | `#1F63CC` | 5.65 | 3.16 | 라이트 테마의 행동 색, 링크, 초점 표시 |
| brand-700 | `#184FA6` | 7.76 | 2.30 | 눌림 |

- 의미 색 (라이트, 흰색 위): success `#1B7A3E` 5.38, warning `#8A5A00` 5.93, error `#C0262D` 5.90, info는 brand-600 5.65. 다크 바탕 위: success `#5FD38A` 9.49, warning `#F2B84B` 9.97, error `#FF8A8F` 7.89, info는 brand-300 8.47
- 흰 글자 대 brand-600 배경 5.65, 흰 글자 대 error 배경 5.90 (단추 글자 4.5:1 충족). 다크 띄운 바탕 `neutral-800` 위: 주 글자 neutral-50 14.00, 보조 neutral-300 9.67, brand-300 7.01, 입력 테두리 neutral-500 3.23 (3:1 충족)
- 색 하나로 상태를 구분하지 않는다 (WCAG 1.4.1). 이 표의 대비는 글자 대 바탕 한 쌍의 값이며 겹친 면이나 그림자 위에서는 다시 잰다

```css
:root {
  --space-4: 1rem; --text-md: 1rem; --radius-2: 8px;
  --duration-medium: 300ms; --ease-standard: cubic-bezier(0.2, 0, 0, 1);
  --color-text-primary: #121820; --color-border-input: #6B7785; --color-action-primary: #1F63CC;
}
```

### 한글 글자 규칙
| 항목 | 규칙 | 근거 |
|---|---|---|
| 줄바꿈 | `word-break: keep-all` 로 단어(어절) 중간에서 끊지 않고 공백에서 줄을 바꾼다. 공백 없이 긴 문자열(주소, 이메일, URL)은 `overflow-wrap: anywhere` 를 함께 두어 칸 밖으로 넘치지 않게 한다. `word-break: break-word` 는 MDN 에 deprecated 로 표기되어 쓰지 않는다 | 확인 (MDN word-break: keep-all 은 CJK 텍스트에 단어 분리를 쓰지 않음, break-word 는 deprecated 표기). 조합 이유는 일반 |
| 웹폰트 서브셋 | 한글 웹폰트는 `@font-face` 의 `unicode-range` 로 나누어 둔다. 페이지가 범위 안 글자를 쓰지 않으면 그 조각은 내려받지 않는다. 한글 음절 블록은 `U+AC00-D7AF` | `unicode-range` 동작은 확인 (MDN). 한글 범위 값은 일반 (MDN 에 예시 없음) |
| 글꼴 표시 | `font-display: swap` (block 기간이 매우 짧고 swap 기간이 무한. 글꼴이 늦어도 대체 글꼴로 먼저 보임) | 정의는 확인 (MDN font-display). 선택은 일반 |
| 대체 글꼴 | `font-family: <프로젝트 글꼴>, "Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans KR", system-ui, sans-serif`. 웹폰트 로딩 실패 및 지연 때 한글이 깨지지 않게 | 일반 |
| 줄 높이 | 한글 본문 1.6, 제목 1.3. 사용자가 줄 높이를 글자 크기의 1.5배로 바꿔도 잘림이 없어야 한다 | 1.4.12 수치는 확인 (WCAG 2.2). 1.6 은 일반 |
| 줄 길이 | 한글 본문 `max-inline-size: 40em` 안팎 (한 줄 약 40자). `modern-web.md` 의 `본문 줄 길이 80자 이내` 는 라틴 문자 기준이고 한글은 글자 폭이 약 1em 이라 같은 80자를 쓰면 80em 이 되어 너무 길다 | 일반 (규격 아님. 실화면에서 확인) |
| 숫자 | 금액 및 수량 열은 `font-variant-numeric: tabular-nums` 로 자릿수를 맞춘다 | 일반 |

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
