# Accessibility Guidelines

- 목표: WCAG 2.2 Level AA
- 역할: 구현 및 검수 때 확인할 항목. 패턴별 세부는 각 카테고리 파일의 Accessibility 항목
- 괄호 안 번호는 WCAG 2.2 성공 기준

## 필수 검토 항목

| 영역 | 확인할 것 | 확인 방법 |
|---|---|---|
| 문서 기본 (점검 첫 항목) | `<html lang="ko">` 가 있고 화면 언어와 맞음 (3.1.1). 기본 템플릿(Next.js, Vite 등)이 `lang="en"` 으로 시작하는 경우가 많아 한국어 서비스에서 가장 먼저 본다. 화면마다 다른 `<title>` (2.4.2). 반복 블록 건너뛰기 링크 또는 랜드마크 (2.4.1). 입력 칸 값을 바꾸거나 초점을 받을 때 자동으로 화면 이동이나 제출이 일어나지 않음 (3.2.2, 3.2.1). 도움말 및 문의 수단은 여러 화면에서 다른 내용에 대한 상대 순서가 같음 (3.2.6). 링크 글자가 목적을 설명 (2.4.4), 제목 및 레이블이 내용을 설명 (2.4.6), 반복되는 이동 구조의 순서가 같고 (3.2.3) 같은 기능은 같은 이름 (3.2.4). 입력 칸에 `autocomplete` 로 용도 지정 (1.3.5) | 소스 검색 (`quality-checklist.md` 13절), 접근성 트리 |
| Semantic HTML | 단추는 `<button>`, 이동은 `<a href>`, 제목 단계 순서, 랜드마크(`<header>`, `<nav>`, `<main>`, `<footer>`), 목록 및 표 요소 사용 (1.3.1) | 코드 확인, 접근성 트리 |
| Keyboard Navigation | 모든 기능을 키보드로 수행 (2.1.1), 키보드 함정 없음 (2.1.2), 복합 위젯은 화살표 키 이동 | Tab, Shift+Tab, Enter, Space, Esc, 화살표로 직접 조작 |
| Focus Management | 초점 순서가 읽는 순서와 같음 (2.4.3), 대화 상자를 열면 안으로 이동하고 닫으면 연 요소로 복귀, 화면 전환 후 초점 위치 지정, 고정 헤더 등이 초점 요소를 완전히 가리지 않음 (2.4.11) | 키보드 조작 |
| Visible Focus | 초점 표시가 보임 (2.4.7), `outline: none` 만 두지 않음, 표시의 대비 3:1 (1.4.11) | 키보드 조작, 코드 검색 |
| Accessible Labels | 입력에 연결된 `<label>` (3.3.2), 글자 없는 단추에 `aria-label`, 이미지 대체 글 (1.1.1), 보이는 글자가 접근성 이름에 포함 (2.5.3), 이름 및 역할 및 값 (4.1.2) | 접근성 트리, 자동 검사 |
| Color Contrast | 글자 4.5:1, 큰 글자 3:1 (1.4.3), UI 요소 및 그래픽 3:1 (1.4.11), 색만으로 정보 전달 금지 (1.4.1) | 아래 `대비 판정` 절, 대비 측정 도구 |
| Screen Reader Support | 상태 변화를 초점 이동 없이 알림: `role="status"` 또는 `role="alert"` (4.1.3), 로딩 영역 `aria-busy`, 펼침 상태 `aria-expanded`, 현재 위치 `aria-current` | 아래 `스크린 리더 확인 절차` 표 |
| Error Identification | 오류 필드를 글로 식별 (3.3.1), 고치는 방법 제시 (3.3.3), `aria-invalid` 및 `aria-describedby`, 법적 및 금융 제출은 확인 또는 되돌리기 (3.3.4) | 잘못된 값으로 제출 |
| Touch Target Size | 최소 24x24 CSS px (2.5.8). 터치 화면은 플랫폼 지침 44x44pt (Apple HIG), 48x48dp (Material Design) 권장 | 요소 크기 측정 |
| Reduced Motion | `prefers-reduced-motion: reduce` 에서 움직임을 줄이거나 끔, 5초 넘게 자동으로 움직이는 내용은 멈춤 수단 (2.2.2), 1초에 3번 넘게 번쩍이지 않음 (2.3.1) | OS 설정을 켜고 확인 |
| Responsive Layout | 320 CSS px 너비에서 가로 스크롤 없이 사용 (1.4.10), 글자 200% 확대 (1.4.4), 글자 간격 조정 시 잘림 없음 (1.4.12), 화면 방향 고정 금지 (1.3.4) | 브라우저 확대 및 좁은 창 |
| Pointer 대안 | 다중 접점 및 경로 제스처에 단일 포인터 대안 (2.5.1), 드래그에 단일 포인터 대안 (2.5.7), 누르는 순간이 아니라 뗄 때 실행 (2.5.2) | 제스처 없이 같은 기능 수행 |
| 시간 제한 | 시간 제한은 끄거나 늘릴 수 있음 (2.2.1). 자동으로 사라지는 알림에 꼭 필요한 정보나 유일한 행동을 두지 않음 | 흐름 확인 |
| 인증 및 재입력 | 같은 과정에서 이미 입력한 정보를 다시 요구하지 않음 (3.3.7), 인증에 인지 기능 시험만 두지 않음 (3.3.8), 붙여넣기 및 비밀번호 관리자 허용 | 가입 및 로그인 흐름 |

## 대비 판정
- 큰 글자는 18pt 이상, 또는 굵게 14pt 이상이다. CJK 글꼴은 동등한 크기로 본다 (확인: WCAG 2.2 Contrast (Minimum) 정의)
- CSS px 환산: 18pt 는 24px. 굵은 14pt 는 약 18.5px (확인: Understanding 문서가 1pt = 1.333px 로 환산해 약 18.5px 로 표기. 14 x 4/3 로 계산하면 18.67px). 경계에 걸리면 큰 글자로 보지 않고 4.5:1 로 판정한다 (일반)
- 계산한 값은 반올림하지 않는다. 4.499:1 은 4.5:1 에 미달이다 (확인: Understanding 문서 원문 예시)
- 측정 도구: Understanding 문서가 정보용으로 든 것은 Colour Contrast Analyser, Luminosity Colour Contrast Ratio Analyser, Colour Contrast Check, Colors On the Web Color Contrast Analyzer 이다 (보증 아님). 자동 검사는 axe `color-contrast` (`quality-checklist.md`). 배경 이미지, 그라데이션, 겹친 면 위의 글자는 자동 검사가 못 재는 경우가 있어 직접 잰다 (일반)
- 측정 결과에는 두 색 값, 글자 크기 및 굵기, 비율(소수 둘째 자리 이상)을 적는다

## 스크린 리더 확인 절차
`스크린 리더로 확인함` 만 적지 않고 아래 절차와 기대 결과로 판정한다.

| 흐름 | 절차 | 기대 결과 |
|---|---|---|
| 저장 알림 | 값을 입력하고 저장 단추를 활성화 | `저장했어요` 가 1회 낭독되고 초점은 저장 단추에 남는다 (4.1.3) |
| 입력 오류 | 필수 칸을 비우고 제출 | 칸 이름과 오류 문구가 함께 낭독된다 (3.3.1). 같은 문구가 두 번 낭독되지 않는다 |
| 대화 상자 | 열기, 닫기 | 열면 대화 상자 이름이 낭독되고 뒤쪽 내용은 읽히지 않는다. 닫으면 초점이 연 단추로 돌아온다 |
| 로딩 | 목록 불러오기 | 시작과 완료가 각각 1회 낭독되고 스피너 자체는 소리를 내지 않는다 |

판정은 조합별로 따로 적는다. 한 조합만 돌렸으면 나머지는 `미검증` 이다.

| 조합 | 대상 | 확인 범위 |
|---|---|---|
| NVDA + Chrome | Windows 데스크톱 | 이름만 확인 (NVDA: Windows 용 무료 오픈소스 화면 낭독 프로그램, NV Access) |
| VoiceOver + Safari (iOS) | iPhone, iPad | 이름만 확인 |
| TalkBack + Chrome | Android | 이름만 확인 |
| 센스리더 | 국내 현장 도구 (Windows 화면 낭독 프로그램) | 이름과 용도만 확인 (국내 서비스 접근성 안내 문서가 센스리더 기준으로 설명하는 사례 확인). 버전별 동작은 미확인 |

- 최소 데스크톱 1조합과 모바일 1조합을 돌린다 (일반). 낭독 문구는 도구 및 버전마다 다르므로 `기대 결과` 는 낭독 횟수, 초점 위치, 이름 포함 여부로 판정하고 문장 전체의 일치로 판정하지 않는다 (일반)
- 환경 칸에 도구 버전, 브라우저 버전, 기기 및 OS 버전을 적는다 (`templates/ui-audit.md`)

## WCAG 2.2 A 및 AA 성공 기준 대비 (번호와 이름은 W3C WCAG 2.2 원문 목차에서 확인, 2026-11-25)
- 총 55개 (A 31, AA 24). 4.1.1 Parsing 은 2.2 에서 삭제되어 목록에 없다 (확인)

| 이 파일 | 성공 기준 |
|---|---|
| 본문 표 및 패턴별 표에 항목 있음 (31) | 1.1.1 Non-text Content, 1.3.1 Info and Relationships, 1.3.4 Orientation, 1.4.1 Use of Color, 1.4.3 Contrast (Minimum), 1.4.4 Resize Text, 1.4.10 Reflow, 1.4.11 Non-text Contrast, 1.4.12 Text Spacing, 1.4.13 Content on Hover or Focus, 2.1.1 Keyboard, 2.1.2 No Keyboard Trap, 2.2.1 Timing Adjustable, 2.2.2 Pause, Stop, Hide, 2.3.1 Three Flashes or Below Threshold, 2.4.3 Focus Order, 2.4.7 Focus Visible, 2.4.11 Focus Not Obscured (Minimum), 2.5.1 Pointer Gestures, 2.5.2 Pointer Cancellation, 2.5.3 Label in Name, 2.5.7 Dragging Movements, 2.5.8 Target Size (Minimum), 3.3.1 Error Identification, 3.3.2 Labels or Instructions, 3.3.3 Error Suggestion, 3.3.4 Error Prevention (Legal, Financial, Data), 3.3.7 Redundant Entry, 3.3.8 Accessible Authentication (Minimum), 4.1.2 Name, Role, Value, 4.1.3 Status Messages |
| `문서 기본` 행에 추가 (11) | 1.3.5 Identify Input Purpose, 2.4.1 Bypass Blocks, 2.4.2 Page Titled, 2.4.4 Link Purpose (In Context), 2.4.6 Headings and Labels, 3.1.1 Language of Page, 3.2.1 On Focus, 3.2.2 On Input, 3.2.3 Consistent Navigation, 3.2.4 Consistent Identification, 3.2.6 Consistent Help |
| 이 파일에 항목 없음 (13) | 1.2.1 Audio-only and Video-only (Prerecorded), 1.2.2 Captions (Prerecorded), 1.2.3 Audio Description or Media Alternative (Prerecorded), 1.2.4 Captions (Live), 1.2.5 Audio Description (Prerecorded), 1.3.2 Meaningful Sequence, 1.3.3 Sensory Characteristics, 1.4.2 Audio Control, 1.4.5 Images of Text, 2.1.4 Character Key Shortcuts, 2.4.5 Multiple Ways, 2.5.4 Motion Actuation, 3.1.2 Language of Parts |

- `항목 없음` 의 기준은 해당 기능(동영상, 음성, 단축키, 모션 입력, 다국어 본문)이 화면에 있을 때 WCAG 원문으로 직접 점검한다. 항목이 없다고 해서 충족이 아니다
- 이 파일의 `본문 표` 문구는 각 기준을 요약한 것이며, 판정 문구를 원문과 대조한 기준은 2.2.1, 1.4.10, 1.4.12, 2.4.1, 2.4.2, 3.1.1, 3.2.2, 3.2.6, 4.1.3 에 한한다. 나머지는 원문 대조 전이다 (`미확인`)

## ARIA 사용 원칙
- 기본 HTML 요소로 되는 것은 ARIA 를 쓰지 않는다. `<div role="button">` 보다 `<button>`
- 역할을 붙이면 그 역할의 키보드 동작도 구현한다 (예: `role="tablist"` 는 화살표 키 이동)
- 보이는 상태와 ARIA 상태 값(`aria-expanded`, `aria-selected`, `aria-checked`, `aria-invalid`)을 항상 같게 유지한다
- 장식 아이콘은 `aria-hidden="true"`, 뜻이 있는 아이콘은 대체 글
- 기존 프로젝트에 접근성 처리가 된 컴포넌트(자체 또는 사용 중인 라이브러리)가 있으면 새로 만들지 않고 그것을 쓴다

## 패턴별로 자주 빠지는 것
| 패턴 | 빠지는 것 |
|---|---|
| FB-01 Toast, FB-02 Snackbar | 상태 메시지 역할, 자동 닫힘 전에 읽을 시간, 스낵바 행동의 키보드 접근 |
| FB-04 Modal dialog, FB-05 Bottom sheet | 초점 가두기, Esc 닫기, 닫은 뒤 초점 복귀, 배경 `inert` |
| FB-07 Tooltip | 키보드 초점에서도 표시, Esc 로 닫기, 포인터를 툴팁 위로 옮겨도 유지 (1.4.13) |
| LD-02 Skeleton, LD-01 Spinner | 로딩 중 및 완료를 스크린 리더에 알림 |
| LD-08 Optimistic update | 실패하여 되돌릴 때의 알림 |
| NV-08 Infinite scroll | 키보드로 목록 끝 및 푸터 도달, 새 항목 추가 알림 |
| GS 전체 | 제스처 없이 같은 기능을 하는 보이는 수단 |
| IC 전체 | 글자 없는 아이콘 단추의 접근성 이름 및 펼침 상태 |
| AI-02 Streaming response | 글자 단위로 읽히지 않게 완료 시점에 알림, 정지 단추의 키보드 접근 |

## 검증의 한계 (보고에 구분해 적는다)
- 자동 검사 도구는 일부 기준만 잡는다. 통과가 AA 충족을 뜻하지 않는다
- 코드만 읽고 확인한 항목은 `코드 확인`, 실제 키보드 및 스크린 리더로 확인한 항목은 `실사용 확인` 으로 구분한다
- 확인하지 못한 항목은 `미검증` 으로 적는다
