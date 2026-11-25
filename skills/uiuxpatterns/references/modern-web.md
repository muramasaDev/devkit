# Modern Web Platform Guide (웹 플랫폼 기능 선택표)

- 역할: 구현 (모드 B, D, E) 에서 직접 만들지 않고 브라우저 기능으로 해결할 수 있는 UI 를 고르는 표
- 쓰는 법: 만들려는 UI 의 줄을 찾아 `쓰는 기능` 과 `규칙` 을 따른다. 기존 프로젝트가 라이브러리를 쓰면 그 규칙이 우선이고, 이 표는 라이브러리가 하는 일을 점검하는 기준으로 쓴다
- 지원 상태는 이 문서에 적지 않았다. 쓰기 전에 MDN 호환성 표와 Baseline 상태를 확인하고, 지원이 부족한 기능은 대체 방안을 함께 둔다
- 확인 표기: `읽음` 지침 본문 확인, `앞부분` 앞부분만 확인, `요지` 설명문 및 관련 지침에서만 확인. 근거 경로는 Chrome 의 modern-web-guidance 저장소 `guides/` 기준 (2026-11-25 읽음)
- 요약이며 원문이 아니다. API 이름과 속성 이름은 그대로 적었다

## 1. 오버레이와 열기
| UI | 쓰는 기능 | 규칙 | 근거 | 확인 |
|---|---|---|---|---|
| 모달 대화상자 (차단형 확인, 입력, 파괴 동작) | `<dialog>` + `showModal()` 또는 `command="show-modal"` | `role="dialog"`, `aria-modal`, 포커스 가두기, Esc 처리를 직접 만들지 않는다. 파괴 동작 확인은 취소 단추에 `autofocus`. 수동 ARIA 는 네이티브 `<dialog>` 를 쓸 수 없는 사용자 정의 대화 상자일 때만 (DF-07). 닫기 방식은 `closedby` (`any`, `closerequest`, `none`). 취소 단추는 `requestClose()`. 메뉴, 툴팁, 토스트는 dialog 가 아니라 popover | ui-components/dialog | 읽음 |
| 모달 뒤 배경 스크롤 | `dialog:modal { overscroll-behavior: contain }` 및 `dialog::backdrop { overflow: hidden; overscroll-behavior: contain }` 를 둘 다 둔다. `::backdrop` 의 `overflow` 기본값이 `visible` 이라 `overflow: hidden` 이 없으면 `overscroll-behavior` 가 무시된다 | `html`, `body` 에 `overflow: hidden` 또는 `position: fixed` 를 쓰지 않는다 | ui-behaviors/prevent-page-scroll-under-modal-dialog | 요지 |
| 선언형 열기 | `commandfor` + `command` (`show-modal`, `close`, `request-close`, `toggle-popover`) | 같은 단추에 `popovertarget` 과 `commandfor` 를 함께 쓰지 않는다. 미지원 환경은 기능 감지 후 폴리필 로드 | ui-behaviors/declarative-dialog-popover-control | 읽음 |
| 비모달 오버레이 | `popover` 속성 | `auto` 는 바깥 클릭에 닫히고 `manual` 은 유지. 폴리필 스타일은 `:is(:popover-open, .\:popover-open)` | features/popover | 읽음 |
| 툴팁과 토글팁 | `popover="hint"` + `interestfor` | 컨트롤 자체 설명은 툴팁, `i` 아이콘의 부가 정보는 토글팁, 행동에 꼭 필요한 정보는 화면에 그대로 적는다. 화살표 방향은 `container-type: anchored` 와 `@container anchored()` | ui-behaviors/interest-triggered-tooltips, ui-atoms/position-aware-tooltips | 읽음 |
| 토스트 | `popover="manual"` | 정본은 `feedback.md` FB-01 (DF-01 ~ DF-05). 비필수 결과 알림용이며 즉시 주의가 필요한 알림은 토스트가 아닌 다른 컴포넌트. 이 지침의 기본은 닫을 때까지 유지이고 빈도가 높고 중요도가 낮으면 자동 소멸을 검토하라고 한다. 이 스킬은 정보성에 5초 자동 닫힘을 기본으로 두고 (일반), 오류와 행동이 필요한 알림은 자동으로 닫지 않는다. 쌓기 컨테이너는 한 번에 둘 이상이 불가피할 때만. 초점이 토스트 안 컨트롤에 있으면 타이머를 멈춘다 | ui-components/persistent-toast-notifications | 읽음 |
| 드롭다운 위치 | CSS Anchor Positioning | 뷰포트 충돌 시 자동으로 뒤집힌다 | ui-atoms/viewport-aware-dropdowns | 요지 |

## 2. 탐색과 구조
| UI | 쓰는 기능 | 규칙 | 근거 | 확인 |
|---|---|---|---|---|
| 탭 | `<button>` + `role="tab"` | 초기 상태를 HTML 에 렌더 (선택 안 된 패널은 `hidden`). `hidden="until-found"`, 키보드는 roving tabindex 가 기본 (`navigation.md`), `focusgroup` 은 기능 감지 뒤 점진 적용 (지원 상태는 MDN 호환성 표에서 확인). 포커스를 따라 선택되는 것이 기본. `aria-controls` 는 필요 없다 | ui-components/tabs | 읽음 |
| 사이트 내비게이션 | `<nav>` 하나 | 좁으면 popover, 넓으면 인라인. 고정 중단점 대신 맞는지 측정. `menubar`, `menuitem` 역할을 쓰지 않는다. 하위 메뉴는 button + `aria-expanded`, `<details>` 는 쓰지 않는다 | ui-components/navbar | 읽음 |
| 아코디언 | 인접한 `<details>` | 한 번에 하나만 열리게 하려면 같은 `name`. `summary` 안에 heading 을 넣지 않는다 (일부 스크린 리더가 버림). 화살표 키 탐색을 추가하지 않는다 | ui-components/accordion | 읽음 |
| 접힌 내용 검색 | `<details>`, `hidden="until-found"` | 숨겨도 페이지 찾기와 URL 조각으로 열린다 | ui-behaviors/search-hidden-content | 앞부분 |
| 내비게이션 드로어 | 최상위 레이어 (dialog 또는 `popover="manual"`) + scroll-snap | 열림 위치 2개를 scroll-snap 으로 잡고 `IntersectionObserver` 로 상태를 읽는다. JS transform 보다 스크롤 방식을 선호 | ui-components/navigation-drawer | 앞부분 |
| 반응형 표 | 표 의미 유지 + `position: sticky` 머리글 | 좁은 컨테이너에서 셀을 쌓고 `::before` 로 머리글을 주입. 래퍼에 `tabindex="0"` 과 `role="region"` | ui-atoms/responsive-table | 앞부분 |
| 한 줄 말줄임 | CSS 말줄임 | 전체 글자는 DOM 에 유지하고 표시만 줄인다 (탭, 칩, 표 셀, 파일명) | ui-atoms/single-line-overflow | 앞부분 |

## 3. 폼
| UI | 쓰는 기능 | 규칙 | 근거 | 확인 |
|---|---|---|---|---|
| 입력 검증 시점 | `required`, `type`, `pattern`, `:user-invalid`, `:user-valid` | 제약은 선언으로, 오류 스타일은 상호작용 후에만. `aria-invalid` 는 false 로 시작해 `:user-invalid` 와 함께 true | forms/required-field-feedback, forms/validate-input-after-interaction, accessibility/accessible-error-announcement | 읽음 |
| 폼 구조 | `form`, `search`, `fieldset` + `legend` | 모든 컨트롤에 `name`, 보조 단추는 `type="button"`, select 변경만으로 제출하지 않는다, CSS 로 탭 순서와 다른 시각 순서를 만들지 않는다 | forms/forms | 앞부분 |
| 자동완성 | `autocomplete` 값 | 주소, 결제, 로그인, 가입 폼에 올바른 값을 쓴다 (WCAG 1.3.5). SMS 인증번호 폼은 별도 지침 | forms/autofill-address-form 외, forms/sms-otp-form | 요지 |
| select 꾸미기 | `appearance: base-select`, `::picker(select)`, `<selectedcontent>` | 미지원 브라우저는 OS 기본 드롭다운으로 저하된다. 고정 폭을 지정 | forms/branded-select-styling | 읽음 |
| 스위치 | `<input type="checkbox" switch role="switch">` + label 병기 (DF-28) | 색은 `accent-color`. 포커스 대비 3:1. `switch` 속성은 지원이 한정적이어서 (Chrome, Edge, Firefox 미지원, 해당 지침 확인) 기능 감지 뒤에만 폴리필을 불러온다. 직접 만든 요소는 `role="switch"` 와 `aria-checked`. 브라우저별 낭독 결과는 읽지 못해 적지 않는다 | forms/switch | 읽음 |
| 한글 입력 중 Enter | keydown 에서 `e.isComposing \|\| e.keyCode === 229` 검사 (React 는 `e.nativeEvent.isComposing`) | 조합 중이면 제출하지 않는다 (한글, 일본어, 중국어). 검색 요청은 `compositionend` 뒤, 글자 수 및 `maxlength` 계산은 조합이 확정된 뒤 (DF-27) | forms/ime-safe-enter-submit | 읽음 |

## 4. 움직임
| 용도 | 쓰는 기능 | 규칙 | 근거 | 확인 |
|---|---|---|---|---|
| 화면 전환 | `document.startViewTransition()`, `view-transition-name` | 이름은 한 상태에서 하나씩만. 여러 페이지 사이트는 `@view-transition` 선언, 방향은 `types` 와 `:active-view-transition-type()`. 미지원은 즉시 전환 | ui-behaviors/same-document-transitions, cross-document-transitions | 읽음 |
| 등장과 퇴장 | `@starting-style` + `transition-behavior: allow-discrete` | `transition` 단축형에 넣지 않는다. 최상위 레이어 요소는 `overlay` 도 전환. 퇴장은 숨김 상태로의 전환으로 정의 | ui-behaviors/animate-element-entry-exit, animate-to-from-top-layer | 앞부분 |
| 일반 규칙 | `opacity`, `transform` 만 애니메이션 | 비필수 스크롤 효과는 `animation-timeline: scroll()` 또는 `view()`. reduced-motion 은 사례별로 처리 (전역으로 0.01ms 로 만들지 않는다). 5초 넘게 자동 재생되면 멈추는 수단, 초당 3회 넘는 점멸 금지 | ui-behaviors/motion | 읽음 |
| 스크롤 연동 | `view()` 타임라인 | `@supports ((animation-timeline: view()) and (animation-range: entry))` 로 감지 | ui-behaviors/scroll-entry-exit-effects | 앞부분 |
| 크기 전환 | `interpolate-size: allow-keywords`, `calc-size()` | `height: auto` 전환에 `max-height` 꼼수를 쓰지 않는다 | css/animate-to-intrinsic-sizes | 읽음 |
| 탭 밑줄 이동 | Anchor Positioning | 활성 탭 밑줄을 의사 요소로 옮긴다 | ui-behaviors/anchor-positioning-tab-underline | 앞부분 |
| 스프링 곡선 | `linear()` | 호버, 눌림, 포커스 상태를 구분하고 팝오버는 트리거에서 열리는 모션 | user-experience/natural-interactions | 앞부분 |

## 5. 로딩, 반응형, 시각
| 용도 | 쓰는 기능 | 규칙 | 근거 | 확인 |
|---|---|---|---|---|
| 진행 표시 | `<progress>` | `value` 가 없으면 불확정. 불확정은 스피너를 우선하고 진행 막대의 불확정 표시는 일시적일 때만. reduced-motion 에서 정지 또는 완화 | ui-components/spinner, progress, progress-ring | 읽음 |
| 컨테이너 기준 반응형 | `@container` | 뷰포트 단위는 `dvh`, `dvw`. 입력 장치는 media query 유지. 노치는 `viewport-fit=cover` + safe-area inset | css/responsive-design, user-experience/form-factor-adaptation | 읽음 |
| 터치 목표 | `min-block-size`, padding, `pointer: coarse` | 최소 24x24 CSS px (WCAG 2.5.8), 터치는 44x44. 가로 스와이프는 `touch-action: pan-y` | accessibility/accessibility, user-experience/form-factor-adaptation | 읽음 |
| 다크 모드 | `color-scheme` + `light-dark()` | 전환 토글은 사용자 재정의용. `prefers-color-scheme` 로 다른 색 쌍도 가능 | visual-design/dark-mode | 읽음 |
| 색과 대비 | 토큰 | 일반 글자 4.5:1, 큰 글자 3:1, 컨트롤 경계와 상태 3:1. 색만으로 상태를 나타내지 않는다. Forced Colors 고려. `prefers-contrast: more` 는 필요할 때만 | visual-design/color | 읽음 |
| 글자 | `rem`, 단위 없는 `line-height` | 글자 요소에 고정 `height` 를 주지 않는다 (`min-block-size`). 본문 줄 길이 80자 이내 (라틴 문자 기준, 한글은 `design-system.md` 의 한글 글자 규칙), 양쪽 정렬 지양 | visual-design/typography | 읽음 |
| 접근성 기본 | 네이티브 HTML | 랜드마크, 한 페이지에 `main` 하나, 양수 `tabindex` 금지, `:focus-visible` 과 3:1 포커스 링, 라이브 영역 긴급도 구분, axe-core 와 수동 시험 | accessibility/accessibility | 앞부분 |
| 아이콘 | `<use>` 또는 CSS 아이콘 체계 | 내부를 꾸밀 필요가 있으면 `<use>`. 대비 3:1 | ui-atoms/icons | 앞부분 |

## 6. 아직 읽지 못한 항목 (규칙으로 인용하지 않는다)
- 캐러셀과 scroll-snap 계열, 스와이프 삭제 및 노출, 드래그와 정렬, 컨텍스트 메뉴, 메뉴, 툴바, 브레드크럼, 호버카드, 앱 투어, 카드, 복사 단추, scrollspy
- 본문이 비어 있는 항목: 스켈레톤, 콤보박스, 별점, 트리 뷰, 데이터 그리드, 슬라이더 범위, 클라이언트 라우팅
- 성능, 보안, PWA, 내장 AI 분야는 이 스킬 범위 밖이다 (보안은 `securecoding`)
