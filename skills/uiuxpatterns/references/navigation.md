# Navigation (이동 구조)

- 범위: 화면 이동 구조 9종 (NV-01 ~ NV-09) 의 선택 기준 및 접근성 조건
- 참조 이미지: `assets/08-navigation.png`
- 색인: `pattern-catalog.md`

## 유사 패턴 구분
| 헷갈리는 쌍 | 고르는 기준 |
|---|---|
| 하단 탭바 (NV-01) 대 드로어 (NV-03) | 목적지 수 및 빈도로 나눔. 자주 쓰는 소수의 최상위 목적지는 탭바, 많거나 드물게 쓰는 목적지는 드로어. 탭바는 항상 보이고 드로어는 열어야 보임 |
| 하단 탭바 (NV-01) 대 상단 탭 (NV-02) | 탭바는 앱 최상위 이동, 상단 탭은 한 화면 안 분류 (전체, 예약 중, 예약 완료). 두 층을 함께 쓰면 탭바가 위 층, 상단 탭이 아래 층 |
| 페이지네이션 (NV-07) 대 무한 스크롤 (NV-08) | 위치 복귀, 푸터 접근, 탐색 목적이면 페이지네이션. 정해진 목표 없이 훑어보는 피드이면 무한 스크롤 (대안으로 `더 보기` 단추) |
| 브레드크럼 (NV-04) 대 뒤로 가기 (NV-09) | 브레드크럼은 고정된 계층 안 현재 위치를 보이고 상위로 바로 이동, 뒤로 가기는 방금 있던 화면으로 돌아감 (이력) |
| 고정 헤더 (NV-05) 대 플로팅 버튼 (NV-06) | 둘 다 스크롤 중 고정. 고정 헤더는 현재 맥락 및 조건 (칩) 유지, 플로팅 버튼은 화면의 대표 행동 하나 |

## NV-01 하단 탭바 (Tab bar)
- ID: NV-01
- Korean Name: 하단 탭바
- English Name: Tab bar
- Category: Navigation (08)
- Definition: 화면 아래에 항상 보이는, 최상위 목적지 여러 개를 나란히 둔 이동 모음
- Purpose: 앱의 주요 목적지로 한 번에 이동하고 현재 위치를 알림
- User Problem: 주요 목적지를 찾으려고 메뉴를 열거나 여러 번 이동해야 함
- When to Use: 자주 쓰는 소수의 최상위 목적지가 같은 위계일 때; 한 손 조작이 중요한 모바일 앱
- When Not to Use: 목적지가 많거나 드물게 쓸 때 (드로어 NV-03); 한 화면 안 분류 (상단 탭 NV-02); 작업 흐름 중간 단계
- Interaction Behavior: 탭하면 해당 목적지로 이동하고 현재 탭이 강조됨; 이미 선택된 탭을 다시 누르면 그 목적지의 첫 화면으로 돌아감; 화면 이동에도 탭바는 유지
- Required States: 기본; 현재 (원본 이미지: "홈"); 눌림; focus-visible; 알림 뱃지 (FB-09); 비활성은 두지 않음
- Visual Guidelines: 아이콘 및 글자 이름을 함께 둠 (원본 이미지: 홈, 항공권, 예약, MY); 현재 탭을 색만으로 구분하지 않음 (WCAG 1.4.1); 아이콘 대비 3:1 (1.4.11)
- Accessibility: `<nav>` 에 이름 (`aria-label`); 현재 탭에 `aria-current="page"`; 터치 목표 44x44pt (Apple HIG), 48x48dp (Material Design); 아래에 고정된 탭바가 초점 대상을 완전히 가리지 않게 함 (WCAG 2.4.11)
- Responsive Considerations: 데스크톱에서는 사이드바 또는 상단 내비게이션으로 바뀜; 하단 고정은 터치 화면의 한 손 조작에 맞는 배치라 넓은 화면에서는 쓰지 않음
- Implementation Guidelines: 페이지를 이동시키면 링크 목록 (`<nav>` 안 `<a>`) 으로 만들고, 같은 페이지의 패널만 바꾸면 `role="tablist"` 구조를 씀; 본문 하단에 탭바 높이만큼 `padding-bottom` 을 두고, 초점 이동 때 가림은 `scroll-padding-bottom` 으로 막음
- Common Mistakes: 글자 없는 아이콘만 둠; 목적지가 너무 많아 좁아짐; 현재 위치를 색으로만 표시; 탭바 위에 가려진 본문 마지막 항목
- Related Patterns: NV-02, NV-03, NV-09, FB-09
- Reference Image: `assets/08-navigation.png` 하단 탭바 카드: 아래 탭 "홈", "항공권", "예약", "MY", 현재 탭 "홈"

## NV-02 상단 탭 (Top tabs)
- ID: NV-02
- Korean Name: 상단 탭
- English Name: Top tabs
- Category: Navigation (08)
- Definition: 한 화면 안 내용 분류를 가로로 나란히 둔 탭
- Purpose: 같은 화면 안에서 분류를 바꿔 보여줌
- User Problem: 한 목록을 여러 상태 또는 분류로 나눠 보고 싶은데 화면을 옮기고 싶지는 않음
- When to Use: 같은 종류 내용의 분류 (전체, 예약 중, 예약 완료); 분류 수가 적고 이름이 짧을 때
- When Not to Use: 앱 최상위 이동 (하단 탭바 NV-01); 순서가 있는 단계 (LD-05); 분류가 매우 많거나 이름이 김
- Interaction Behavior: 탭을 누르면 아래 패널이 교체; 현재 탭에 밑줄 (원본 이미지); 탭이 넘치면 가로 스크롤; 선택은 즉시 반영
- Required States: 기본; 현재; hover; focus-visible; 눌림; 비활성 (선택 불가 분류); 패널 로딩 중
- Visual Guidelines: 현재 탭을 밑줄 및 글자 굵기로 구분하고 색만으로 구분하지 않음 (WCAG 1.4.1); 글자 대비 4.5:1 (1.4.3); 탭 간 간격은 목표 크기를 확보
- Accessibility: `role="tablist"`, `role="tab"`, `role="tabpanel"` 및 `aria-selected`; 방향키로 탭 간 이동하고 Tab 키는 패널로 이동; 탭 목표 크기 24x24 CSS px 이상 (WCAG 2.5.8)
- Responsive Considerations: 좁은 화면은 가로 스크롤 탭, 넓은 화면은 모두 펼침; 터치는 스와이프로 패널 전환을 더할 수 있으나 탭 선택이 대체 수단
- Implementation Guidelines: 활성 탭만 Tab 순서에 두고 나머지는 방향키로 이동; 패널 전환 시 URL 에 선택 탭을 반영할지는 제품에서 정한다; 패널은 지연 로딩 가능
- Common Mistakes: 탭이 페이지 이동인데 `tab` 역할을 씀; 스와이프만 있고 탭이 없음; 탭이 많아 가로 스크롤 중 일부가 숨음; 현재 탭 표시가 약함
- Related Patterns: NV-01, GS-03, LD-05, FM-03
- Reference Image: `assets/08-navigation.png` 상단 탭 카드: 탭 "전체", "예약 중", "예약 완료", 현재 탭 밑줄

## NV-03 드로어 (Drawer)
- ID: NV-03
- Korean Name: 드로어
- English Name: Drawer
- Category: Navigation (08)
- Definition: 화면 옆에서 밀려 나오는 메뉴 패널
- Purpose: 많은 목적지를 평소에는 숨기고 필요할 때 보여줌
- User Problem: 목적지가 많아 한 줄 탭바에 담기지 않음
- When to Use: 목적지가 많거나 드물게 쓰는 항목 (설정, 도움말); 화면 공간이 부족한 좁은 화면
- When Not to Use: 자주 쓰는 소수의 최상위 목적지 (NV-01 이 나음); 데스크톱 넓은 화면의 주요 목적지; 발견성이 중요한 기능
- Interaction Behavior: 메뉴 단추로 열림; 배경 눌림 또는 닫기 또는 Esc 로 닫힘; 항목을 누르면 이동하고 닫힘; 열림 때 배경은 어둡게 처리 가능
- Required States: 닫힘; 열리는 중; 열림; 닫히는 중; 현재 항목 표시; 항목 눌림
- Visual Guidelines: 열었을 때 본문이 어두워져 메뉴에 집중; 현재 위치 항목을 구분하되 색만으로 하지 않음 (WCAG 1.4.1); 메뉴를 여는 단추 모양은 IC-01
- Accessibility: 열기 단추에 `aria-expanded` 및 이름; 배경을 가리는 형태이면 `role="dialog"`, `aria-modal="true"`, 초점 가두기, Esc 닫기, 닫은 뒤 열기 단추로 초점 복귀; 배경은 `inert`
- Responsive Considerations: 좁은 화면은 접힌 드로어, 넓은 화면은 항상 보이는 사이드바로 바뀜; 데스크톱에서 주요 목적지를 드로어에 숨기지 않음
- Implementation Guidelines: `<nav>` 안에 링크 목록; 모달형은 `<dialog>` 를 쓸 수 있음; 여는 단추 상태 `aria-expanded` 를 열림 및 닫힘에 맞춰 갱신; 입장 움직임은 MO-07
- Common Mistakes: 주요 목적지를 드로어에만 둠; 단추에 글자 없이 아이콘만; 열린 뒤 초점이 본문에 남음; 닫을 때 초점 복귀 없음
- Related Patterns: NV-01, IC-01, FB-04, MO-07
- Reference Image: `assets/08-navigation.png` 드로어 카드: 본문만 보이는 장면 (캡처 시점에 메뉴 미노출)

## NV-04 브레드크럼 (Breadcrumb)
- ID: NV-04
- Korean Name: 브레드크럼
- English Name: Breadcrumb
- Category: Navigation (08)
- Definition: 현재 화면까지의 계층 경로를 단계별로 보여주는 한 줄 이동 표시
- Purpose: 계층 안 현재 위치를 알리고 상위 단계로 바로 이동
- User Problem: 깊은 계층에서 지금 어디인지, 위로 어떻게 올라가는지 알기 어려움
- When to Use: 고정된 계층이 깊은 구조 (지역, 카테고리, 문서); 상위 단계로 자주 이동해야 할 때
- When Not to Use: 계층이 없는 평면 구조; 같은 화면에 여러 경로로 올 수 있어 경로가 일정하지 않을 때; 단계가 하나뿐
- Interaction Behavior: 각 단계를 누르면 그 상위 화면으로 이동; 현재 단계는 누를 수 없는 글자; 경로가 길면 중간을 줄임
- Required States: 기본; hover; focus-visible; 현재 (링크 아님); 줄임 (긴 경로)
- Visual Guidelines: 구분 기호 (원본 이미지: ›) 로 단계를 나눔; 현재 단계는 링크와 모양이 다름; 앞부분을 흐리게 처리하더라도 글자 대비는 4.5:1 (WCAG 1.4.3)
- Accessibility: `<nav>` 에 이름 (`aria-label`) 및 순서 목록 `<ol>`; 현재 단계에 `aria-current="page"`; 구분 기호는 장식이므로 `aria-hidden="true"` 요소로 넣거나 CSS 테두리로 그림 (CSS `content` 로 넣은 글자는 보조기기가 읽을 수 있음)
- Responsive Considerations: 좁은 화면은 바로 위 단계 하나로 줄이거나 가로 스크롤하는 방식을 제품에서 정한다; 터치 목표 크기 확보
- Implementation Guidelines: 경로 데이터를 화면 구조에서 가져와 중복 정의를 피함; 줄임 표시는 접근 가능한 이름을 유지; 구조화 데이터 사용 여부는 제품에서 정한다
- Common Mistakes: 이력 기반 경로를 계층 경로처럼 표시; 현재 단계가 링크; 구분 기호를 보조기기가 낭독; 좁은 화면에서 줄바꿈이 어지러움
- Related Patterns: NV-09, NV-01, NV-05
- Reference Image: `assets/08-navigation.png` 브레드크럼 카드: 경로 "여행 › 일본 › 오사카" ("여행" 및 "일본" 흐림), 제목 "오사카 왕복 항공권"

## NV-05 고정 헤더 (Sticky header)
- ID: NV-05
- Korean Name: 고정 헤더
- English Name: Sticky header
- Category: Navigation (08)
- Definition: 스크롤해도 화면 위에 붙어 있는 제목 및 조건 영역
- Purpose: 목록을 훑는 동안 현재 맥락 및 조건 (필터 칩) 을 유지
- User Problem: 길게 스크롤하면 지금 보는 화면 및 적용된 조건을 잊음
- When to Use: 필터 칩 또는 정렬이 목록과 함께 계속 필요한 화면; 목록 제목을 유지해야 할 때
- When Not to Use: 헤더가 커서 본문 공간을 크게 가릴 때; 가로 방향 낮은 화면; 맥락이 바뀌지 않는 짧은 화면
- Interaction Behavior: 스크롤하면 헤더가 위에 붙고 본문이 아래로 흐름; 아래로 스크롤할 때 줄이거나 숨기고 위로 스크롤할 때 다시 보이는 방식은 제품에서 정한다
- Required States: 일반 위치; 붙음 (stuck); 줄어듦 또는 숨김; 칩 선택 상태; 구분 그림자 (붙었을 때)
- Visual Guidelines: 붙었을 때 본문과 구분되는 경계 또는 그림자; 높이를 작게; 본문과 겹치는 영역의 배경을 불투명하게 해 글자 대비 유지 (WCAG 1.4.3)
- Accessibility: 키보드 초점이 고정 헤더 뒤로 완전히 가려지지 않게 함 (WCAG 2.4.11); 확대 및 가로 화면에서 헤더가 본문을 모두 가리지 않음; 읽기 순서는 헤더 다음 본문
- Responsive Considerations: 좁은 화면 및 낮은 높이에서는 헤더를 줄이거나 칩만 남김; 데스크톱은 상단 내비게이션과 합쳐질 수 있음
- Implementation Guidelines: CSS `position: sticky` 와 `top` 값 사용; 부모 요소의 overflow 설정이 sticky 를 막을 수 있으므로 확인; `scroll-padding-top` 으로 이동 시 가림 방지
- Common Mistakes: 키보드 초점이 헤더에 가려짐; 헤더 높이가 과해 본문이 좁아짐; sticky 가 부모 overflow 때문에 동작하지 않음; 불투명하지 않아 글자가 겹쳐 보임
- Related Patterns: NV-01, NV-08, IC-06, FB-09
- Reference Image: `assets/08-navigation.png` 고정 헤더 카드: 위에 붙은 "항공권" 및 칩 "편도", "서울", 아래로 흐르는 목록 "상품 4", "상품 5"

## NV-06 플로팅 버튼 (Floating action button)
- ID: NV-06
- Korean Name: 플로팅 버튼
- English Name: Floating action button
- Category: Navigation (08)
- Definition: 내용 위에 떠서 스크롤해도 고정되는 원형 대표 행동 단추
- Purpose: 화면의 가장 중요한 행동 하나를 항상 가까이 둠
- User Problem: 새로 만들기 같은 주 행동을 찾으려고 스크롤하거나 메뉴를 열어야 함
- When to Use: 화면에 대표 행동이 하나 분명할 때 (만들기, 추가); 목록 화면의 주 행동
- When Not to Use: 대표 행동이 여럿이거나 없을 때; 이미 하단에 고정된 주 행동 단추가 있는 화면; 목록 마지막 항목을 가릴 때
- Interaction Behavior: 누르면 해당 행동 시작 (만들기 화면 또는 입력); 스크롤해도 같은 자리; 필요하면 스크롤 방향에 따라 숨기고 보임
- Required States: 기본; hover; 눌림; focus-visible; 비활성; 숨김 (스크롤 중)
- Visual Guidelines: 원형 + 모양 (원본 이미지: 오른쪽 아래); 배경과 구분되는 그림자 또는 색; 아이콘 대비 3:1 (WCAG 1.4.11)
- Accessibility: 글자 없는 아이콘이므로 `aria-label` 로 행동 이름 제공; 터치 목표 44x44pt (Apple HIG), 48x48dp (Material Design); 키보드 초점 순서에서 위치가 자연스러움 (WCAG 2.4.3); 초점이 가려지지 않음
- Responsive Considerations: 데스크톱은 글자가 있는 일반 단추로 바꾸거나 페이지 도구 모음으로 옮김; 좁은 화면에서 목록 하단에 단추 높이만큼 여백
- Implementation Guidelines: `<button>` 을 `position: fixed` 또는 sticky 로 배치; 하단 탭바 (NV-01) 와 겹치지 않게 위치를 계산; 안전 영역 여백 고려
- Common Mistakes: 대표 행동이 아닌 보조 행동에 사용; 이름 없는 아이콘; 목록 마지막 항목을 가림; 여러 개를 띄움
- Related Patterns: NV-01, NV-05, FB-05, IC-02
- Reference Image: `assets/08-navigation.png` 플로팅 버튼 카드: 목록 위 오른쪽 아래 원형 + 단추

## NV-07 페이지네이션 (Pagination)
- ID: NV-07
- Korean Name: 페이지네이션
- English Name: Pagination
- Category: Navigation (08)
- Definition: 긴 목록을 쪽 단위로 나누고 쪽 번호로 이동하는 방식
- Purpose: 목록 안 위치를 알고 원하는 쪽으로 직접 이동
- User Problem: 긴 목록에서 위치를 잃고 푸터에 닿지 못하며 같은 자리로 돌아오기 어려움
- When to Use: 탐색 목적 (비교, 특정 항목 찾기); 쪽 위치로 돌아오는 일이 잦을 때; 푸터 정보에 접근해야 할 때
- When Not to Use: 정해진 목표 없이 훑어보는 피드 (무한 스크롤 NV-08); 항목이 적어 한 쪽에 모두 들어감
- Interaction Behavior: 쪽 번호 또는 이전 및 다음으로 이동; 현재 쪽 표시; 이동 뒤 목록 맨 위로 이동하고 URL 에 쪽 번호가 반영됨
- Required States: 현재 쪽 (원본 이미지: 3); 다른 쪽; 이전 및 다음 활성; 첫 쪽에서 이전 비활성; 마지막 쪽에서 다음 비활성; 로딩 중
- Visual Guidelines: 현재 쪽을 모양으로 구분 (색만으로 하지 않음, WCAG 1.4.1); 쪽 번호가 많으면 줄임 표시 규칙을 제품에서 정한다; 간격 확보
- Accessibility: `<nav>` 에 이름 (`aria-label`); 현재 쪽 `aria-current="page"`; 이전 및 다음 단추에 이름; 목표 크기 24x24 CSS px 이상 (WCAG 2.5.8), 터치 44x44pt (Apple HIG)
- Responsive Considerations: 좁은 화면은 이전, 다음, 현재 쪽 위주로 줄임; 데스크톱은 쪽 번호를 모두 노출
- Implementation Guidelines: 각 쪽을 링크 (`<a href>`) 로 만들어 새로고침, 공유, 뒤로 가기에서 같은 쪽이 열리게 함; 쪽 이동 후 초점을 목록 제목으로 옮김; 쪽 수 계산은 서버에서 받음
- Common Mistakes: 쪽 번호를 URL 에 반영하지 않아 뒤로 가기가 첫 쪽으로 돌아감; 이동 뒤 스크롤이 맨 아래에 남음; 작은 목표; 현재 쪽을 색으로만 표시
- Related Patterns: NV-08, NV-05, LD-01, ES-02
- Reference Image: `assets/08-navigation.png` 페이지네이션 카드: "‹ 1 2 3 ›", 현재 쪽 3

## NV-08 무한 스크롤 (Infinite scroll)
- ID: NV-08
- Korean Name: 무한 스크롤
- English Name: Infinite scroll
- Category: Navigation (08)
- Definition: 목록 끝에 가까워지면 다음 항목이 자동으로 이어 불러와지는 방식
- Purpose: 훑어보는 콘텐츠를 끊김 없이 이어 보여줌
- User Problem: 쪽 이동 단추를 반복해서 누르는 번거로움
- When to Use: 정해진 목표 없이 훑어보는 피드 (소셜, 추천); 항목이 서로 비슷하고 순서에 큰 의미가 없을 때
- When Not to Use: 푸터 정보가 필요한 화면 (푸터에 도달할 수 없음); 특정 항목을 찾거나 비교하는 화면; 위치로 돌아와야 하는 화면 (뒤로 가기 후 위치 복원 문제); 키보드 사용자가 많은 업무 화면
- Interaction Behavior: 끝 근처에서 다음 묶음을 불러옴 (원본 이미지: 목록 아래 회전 원); 불러오는 동안 로딩 표시; 실패하면 다시 시도; 더 없으면 끝 표시
- Required States: 대기; 불러오는 중 (LD-01); 추가됨; 실패 (다시 시도); 끝 도달; 빈 목록 (ES-01)
- Visual Guidelines: 불러오는 자리 표시를 목록 끝에 둠; 끝 도달을 문구로 알림; 새 항목이 들어올 때 읽던 위치가 밀리지 않음
- Accessibility: 키보드 사용자는 푸터까지 Tab 을 한참 눌러도 도달하지 못하는 문제가 있으므로 `더 보기` 단추 대안을 둠; 새 항목 추가 시 초점을 옮기지 않고 `role="status"` 로 추가 알림; 불러오는 영역 `aria-busy`
- Responsive Considerations: 모바일은 스크롤이 자연스러워 쓰기 쉽지만 푸터가 필요하면 `더 보기` 단추; 데스크톱은 키보드 및 푸터 접근을 위해 페이지네이션 또는 `더 보기` 단추 우선
- Implementation Guidelines: 스크롤 감시는 IntersectionObserver 같은 네이티브 API; 뒤로 가기 후 위치 복원을 위해 불러온 범위를 URL 또는 이력 상태에 저장; 항목이 쌓이는 만큼 화면 밖 항목 처리 방법을 제품에서 정한다
- Common Mistakes: 푸터에 도달할 수 없음; 뒤로 가기 하면 맨 위로 돌아가 위치를 잃음; 키보드 사용자가 끝까지 도달하지 못함; 로딩 실패 시 대응 없음; 불러오는 중 읽던 위치가 밀림
- Related Patterns: NV-07, LD-01, LD-02, ES-08
- Reference Image: `assets/08-navigation.png` 무한 스크롤 카드: 목록 "상품 4", "상품 5", "상품 6" 아래 회전 원

## NV-09 뒤로 가기 (Back navigation)
- ID: NV-09
- Korean Name: 뒤로 가기
- English Name: Back navigation
- Category: Navigation (08)
- Definition: 방금 있던 이전 화면으로 돌아가는 단추 또는 동작
- Purpose: 안전하게 이전 화면으로 돌아가는 길을 늘 제공
- User Problem: 잘못 들어갔을 때 돌아가는 길이 없으면 막힌 느낌이 듦
- When to Use: 모든 하위 화면 (상세, 설정, 단계 화면); 이전 화면 이름을 함께 보이고 싶을 때
- When Not to Use: 최상위 화면 (탭바의 루트); 모달 닫기 (닫기 단추 사용); 계층 위치가 중요한 경우 (브레드크럼 NV-04 병행)
- Interaction Behavior: 누르면 이전 화면으로 이동하고 이전 화면의 스크롤 위치 및 입력이 보존됨; 브라우저 뒤로 가기와 같은 결과
- Required States: 기본; hover; 눌림; focus-visible; 비활성은 두지 않음; 이전 화면 없음 (단추 숨김)
- Visual Guidelines: 왼쪽 위에 이전 화면 이름과 함께 표시 (원본 이미지: "‹ 상품 상세"); 아이콘만이면 이름 제공; 목표 크기 확보
- Accessibility: `<button>` 또는 `<a>` 에 이름 (`aria-label` 로 이전 화면 이름); 목표 크기 44x44pt (Apple HIG), 48x48dp (Material Design); 돌아간 뒤 초점을 진입 항목으로 복귀 (WCAG 2.4.3)
- Responsive Considerations: 데스크톱은 브라우저 뒤로 가기 단추 및 화면 안 뒤로 가기 단추가 대응 (상위 계층 이동은 NV-04 로 따로 둠); 터치는 가장자리 스와이프 (GS-09) 를 더함
- Implementation Guidelines: 화면 이동을 이력에 맞게 기록해 브라우저 뒤로 가기와 같은 결과를 냄; 불필요한 이력 항목을 쌓아 뒤로 가기가 같은 화면에 머물게 하지 않음; 이전 화면 상태 (필터, 스크롤) 보존
- Common Mistakes: 뒤로 가기 후 목록 위치 및 필터를 잃음; 같은 화면에서 이력만 쌓여 뒤로 가기가 안 먹힘; 이름 없는 화살표만 둠; OS 뒤로 가기와 다르게 동작
- Related Patterns: GS-09, NV-04, NV-01, MO-07
- Reference Image: `assets/08-navigation.png` 뒤로 가기 카드: 왼쪽 위 "‹ 상품 상세"
