# Gestures (제스처)

- 범위: 터치 화면 입력 동작 9종 (GS-01 ~ GS-09) 의 판단 조건 및 데스크톱 대응 수단
- 색인: `pattern-catalog.md`
- 값 정본: `defaults.md` (본문의 DF-nn 은 그 표의 항목 번호)

## 공통 원칙
- 제스처는 보이지 않으므로 같은 기능에 보이는 대체 수단 (단추, 메뉴) 을 둔다
- 다중 접점 및 경로 제스처는 단일 포인터 대안을 둔다 (WCAG 2.5.1)
- 드래그는 단일 포인터 대안을 둔다 (WCAG 2.5.7)

## 유사 패턴 구분
| 헷갈리는 쌍 | 고르는 기준 |
|---|---|
| 스와이프 (GS-03) 대 드래그 (GS-05) | 스와이프는 방향을 주면 화면 단위 (카드, 쪽) 가 넘어가는 동작, 드래그는 손가락을 따라 대상이 움직이고 놓은 위치가 결과가 되는 동작 |
| 밀어서 삭제 (GS-04) 대 길게 누르기 (GS-02) 메뉴 | 한 가지 행동 (삭제) 을 목록에서 빠르게 반복하면 밀어서 삭제, 행동이 여러 개 (복사, 고정, 삭제) 이면 길게 누르기 메뉴 |
| 가장자리 스와이프 (GS-09) 대 스와이프 (GS-03) | 화면 가장자리에서 시작하면 화면 이동 (뒤로), 화면 안에서 시작하면 내용 넘김. 같은 가로 방향이라 시작 위치로 나눔 |
| 핀치 (GS-06) 대 두 번 탭 (GS-07) | 둘 다 확대 계열. 핀치는 접점 2개로 배율을 연속 조절, 두 번 탭은 접점 1개로 배율을 단계 전환 |
| 탭 (GS-01) 대 길게 누르기 (GS-02) | 탭은 기본 동작 실행, 길게 누르기는 보조 행동 메뉴. 길게 누르기에만 있는 기능은 두지 않음 |

## GS-01 탭 (Tap)
- ID: GS-01
- Korean Name: 탭
- English Name: Tap
- Category: Gestures (06)
- Definition: 화면의 한 지점을 짧게 눌렀다 떼는 동작
- Purpose: 항목 열기, 단추 실행, 선택 같은 기본 동작을 일으킴
- User Problem: 무엇이 눌리는 요소인지, 눌렀을 때 반응이 있는지 알기 어려움
- When to Use: 모든 주 동작의 기본 입력; 카드 및 목록 항목 열기; 다른 제스처로만 가능한 기능의 대체 수단
- When Not to Use: 되돌릴 수 없는 동작을 탭 한 번에 즉시 실행; 목표가 작거나 붙어 있어 오탭이 잦은 배치
- Interaction Behavior: 누르는 동안 눌림 표시; 목표 안에서 떼면 실행; 목표 밖으로 벗어나 떼면 취소
- Required States: 기본; hover (마우스); 눌림; focus-visible; 비활성; 실행 중
- Visual Guidelines: 눌리는 요소임이 모양으로 드러남 (단추 모양, 밑줄, 화살표); 카드 전체가 목표면 카드 전체에 눌림 표시; 색만으로 구분하지 않음 (WCAG 1.4.1)
- Accessibility: 터치 목표 44x44pt (Apple HIG), 48x48dp (Material Design), 최소 24x24 CSS px (WCAG 2.5.8); 키보드로 같은 동작 (2.1.1); 이름 및 역할 제공 (4.1.2)
- Responsive Considerations: 데스크톱은 마우스 클릭이 대응; hover 및 키보드 초점 상태를 추가; hover 에만 나타나는 정보는 터치에서 보이지 않으므로 두지 않음
- Implementation Guidelines: 카드 전체가 목표면 `<a>` 또는 `<button>` 하나로 감싸고 안에 다른 대화형 요소를 중첩하지 않음; `<div>` 에 click 만 다는 구현 금지; 눌림 표시는 `:active`, 키보드 표시는 `:focus-visible`
- Common Mistakes: `<div>` 에 click 핸들러만 달아 키보드 및 보조기기가 쓰지 못함; 눌림 표시 없음; 인접 목표 간격 부족; 탭 한 번에 결제 같은 확정 동작
- Related Patterns: GS-02, GS-07, FB-04, NV-01
- Reference Image: 장면: 탭 카드: 항목 카드 "오사카 왕복 항공권"

## GS-02 길게 누르기 (Long press)
- ID: GS-02
- Korean Name: 길게 누르기
- English Name: Long press
- Category: Gestures (06)
- Definition: 화면의 한 지점을 떼지 않고 일정 시간 눌러 두는 동작
- Purpose: 항목에 대한 보조 행동 메뉴 (복사, 고정, 삭제) 를 열거나 선택 모드로 진입
- User Problem: 목록 항목마다 단추를 두면 화면이 복잡해지는데, 보조 행동은 필요함
- When to Use: 한 항목에 보조 행동이 여러 개일 때; 단추를 항목마다 두기 어려운 밀집 목록; 숙련 사용자의 지름길
- When Not to Use: 이 동작만이 유일한 진입일 때; 주 행동; 처음 쓰는 사용자가 반드시 해야 하는 기능
- Interaction Behavior: 누르고 있으면 기준 시간 뒤 메뉴가 뜸; 기준 시간은 0.5초이며 플랫폼이 값을 제공하면 그 값을 따름 (DF-08); 메뉴 밖 탭 또는 Esc 로 닫음
- Required States: 누르는 중 (진행 표시); 메뉴 열림; 선택 항목 강조; 취소 (기준 시간 전에 뗌)
- Visual Guidelines: 메뉴가 대상 항목 가까이에 뜨고 대상이 강조됨; 삭제는 빨강 및 글자를 함께 사용 (WCAG 1.4.1); 메뉴 항목 대비 4.5:1 (1.4.3)
- Accessibility: 같은 메뉴를 여는 보이는 단추 (더 보기, IC-02) 를 둠; 키보드의 컨텍스트 메뉴 키 또는 Shift+F10 으로 열림; 메뉴는 `role="menu"`, 여는 단추에 `aria-haspopup="menu"` 및 `aria-expanded`
- Responsive Considerations: 데스크톱은 마우스 오른쪽 클릭 메뉴가 대응; 항목 옆 더 보기 단추를 상시 노출하거나 hover 시 노출 (초점에도 노출)
- Implementation Guidelines: 누르는 동안 브라우저 기본 메뉴 및 텍스트 선택이 겹치지 않게 처리; 손가락이 일정 거리 움직이면 길게 누르기를 취소하고 스크롤로 넘김; 메뉴를 닫으면 초점을 대상 항목으로 되돌림
- Common Mistakes: 메뉴가 유일한 진입이라 발견 불가; 누르는 중 아무 표시 없음; 스크롤과 충돌; 삭제를 확인 및 되돌리기 없이 즉시 실행
- Related Patterns: GS-04, IC-02, FB-05, FB-02
- Reference Image: 장면: 길게 누르기 카드: "여행 준비 메모" 위에 뜬 메뉴 "복사", "고정", "삭제"(빨강)

## GS-03 스와이프 (Swipe)
- ID: GS-03
- Korean Name: 스와이프
- English Name: Swipe
- Category: Gestures (06)
- Definition: 손가락을 화면 위에서 한 방향으로 쓸어 넘기는 동작
- Purpose: 카드, 쪽, 사진 같은 나란한 화면 단위를 다음 또는 이전으로 넘김
- User Problem: 같은 자리에서 여러 내용을 보려 할 때 단추를 반복해서 누르는 부담
- When to Use: 가로로 나란한 카드 묶음; 사진 갤러리; 쪽 단위 온보딩
- When Not to Use: 모든 항목을 비교해야 하는 내용 (한꺼번에 보이는 목록이 나음); 화면 가장자리 시작 동작이 필요한 곳 (GS-09 와 충돌)
- Interaction Behavior: 손가락을 따라 이동하다 놓으면 가까운 단위에 맞춰 멈춤; 첫째 및 마지막 단위에서 더 넘기면 멈춤 표시; 놓는 기준은 단위 폭의 절반을 넘으면 다음 단위이고 빠르게 튕기면 거리와 상관없이 다음 단위 (DF-10)
- Required States: 현재 위치; 이동 중; 처음 및 끝; 읽기 중단 (자동 넘김이 있을 때); 쪽 표시 (예시 화면은 점 3개)
- Visual Guidelines: 다음 카드 일부를 걸쳐 보여 넘길 수 있음을 알림; 쪽 표시 점은 현재 쪽을 색만으로 구분하지 않음 (1.4.1); 점 대비 3:1 (1.4.11)
- Accessibility: 경로 제스처이므로 이전 및 다음 단추 또는 눌러서 이동하는 쪽 표시를 둠 (2.5.1); 5초 넘게 자동으로 넘어가면 멈춤 수단 (2.2.2); 키보드 좌우 방향키 이동
- Responsive Considerations: 데스크톱은 이전 및 다음 단추, 키보드 방향키, 트랙패드 가로 스크롤이 대응; 넓은 화면은 카드 여러 장을 한 번에 보여 넘김을 줄임
- Implementation Guidelines: 가로 스크롤 영역과 CSS scroll-snap 으로 구현하면 기본 스크롤 접근성이 유지됨; 영역에 이름 (`aria-label`) 을 줌; 넘김 단추는 `<button>`
- Common Mistakes: 스와이프만 있고 단추가 없음; 쪽 표시가 눌리지 않음; 세로 스크롤과 방향 충돌; 자동 넘김을 멈출 수 없음
- Related Patterns: GS-05, GS-09, NV-02, MO-07
- Reference Image: 장면: 스와이프 카드: 가로로 넘기는 카드 묶음 및 쪽 표시 점 3개

## GS-04 밀어서 삭제 (Swipe to delete)
- ID: GS-04
- Korean Name: 밀어서 삭제
- English Name: Swipe to delete
- Category: Gestures (06)
- Definition: 목록 항목을 옆으로 밀어 숨은 행동 단추 (삭제) 를 드러내는 동작
- Purpose: 목록에서 한 가지 행동 (삭제) 을 항목 단위로 빠르게 처리
- User Problem: 항목마다 삭제 단추를 두면 목록이 복잡하고, 별도 화면에서 지우면 단계가 많음
- When to Use: 이메일, 알림, 일정 같이 같은 행동을 반복하는 목록; 삭제를 되돌릴 수 있을 때
- When Not to Use: 되돌릴 수 없는 삭제; 항목에 가로 스와이프 의미가 이미 있을 때; 행동이 여러 개일 때 (GS-02 메뉴가 나음)
- Interaction Behavior: 항목이 왼쪽으로 밀리며 오른쪽에 빨간 "삭제" 가 드러남; 드러난 단추를 탭하면 실행; 반대로 밀거나 다른 곳 탭 시 닫힘
- Required States: 기본; 미는 중; 단추 노출; 삭제 중; 삭제됨 (되돌리기 가능); 실패
- Visual Guidelines: 단추는 글자 "삭제" 를 포함하고 빨강만으로 의미를 전하지 않음 (1.4.1); 글자 대비 4.5:1 (1.4.3); 밀린 항목과 단추 경계가 분명함
- Accessibility: 경로 제스처이므로 같은 삭제를 하는 보이는 수단 (더 보기 메뉴, 편집 모드) 을 둠 (2.5.1); 키보드 및 보조기기에서 삭제 접근 가능; 삭제 결과 `role="status"` 로 알림
- Responsive Considerations: 데스크톱은 항목 옆 삭제 단추, hover 시 노출 (초점에도 노출), 선택 후 Delete 키가 대응
- Implementation Guidelines: 삭제 후 되돌리기 (스낵바, FB-02) 를 제공하고 실제 삭제는 되돌리기 시간이 지난 뒤 처리; 세로 스크롤을 막지 않도록 가로 방향이 확정된 뒤에만 항목을 움직임; 시작 위치는 화면 가장자리에서 띄움
- Common Mistakes: 밀기 외 수단 없음; 되돌리기 없음; 한 번 밀어 즉시 삭제됨; 세로 스크롤 중 항목이 흔들림; 가장자리 뒤로 가기와 충돌
- Related Patterns: GS-02, GS-09, FB-02, IC-02
- Reference Image: 장면: 밀어서 삭제 카드: 목록 항목이 왼쪽으로 밀리고 오른쪽에 빨간 "삭제" 노출

## GS-05 드래그 (Drag)
- ID: GS-05
- Korean Name: 드래그
- English Name: Drag
- Category: Gestures (06)
- Definition: 대상을 누른 채 끌어 다른 위치에 놓는 동작
- Purpose: 순서 바꾸기, 위치 옮기기, 값 조절 같은 연속 이동
- User Problem: 순서나 위치를 단추로 한 칸씩 바꾸면 느리고, 놓일 곳을 가늠하기 어려움
- When to Use: 순위 목록 (예시 화면: 3순위 삿포로 항목을 2순위 위로 옮김); 칸반 같은 영역 간 이동; 크기 및 위치 조정
- When Not to Use: 이동 거리가 먼 목록 (스크롤과 함께 끌기 어려움); 드래그가 유일한 수단일 때; 단순 선택
- Interaction Behavior: 손잡이를 누르면 항목이 들림; 끄는 동안 놓일 자리를 표시; 놓으면 확정; 취소 수단 (Esc 또는 원위치 놓기) 을 둠
- Required States: 기본; 손잡이 hover 및 초점; 들림; 이동 중 (놓일 자리 표시); 놓음; 취소; 실패
- Visual Guidelines: 손잡이를 보이게 둠; 들린 항목은 그림자 또는 크기로 구분; 놓일 자리는 선 또는 빈칸으로 표시; 표시 대비 3:1 (1.4.11)
- Accessibility: 단일 포인터 대안 필수 (2.5.7): 위로 및 아래로 단추 또는 순서 입력; 키보드로 항목 선택 후 방향키 이동; 이동 결과 `role="status"` 로 알림; 손잡이 단추에 `aria-label`
- Responsive Considerations: 데스크톱은 마우스 드래그가 대응하며 키보드 이동 및 순서 단추 병행; 터치는 손잡이로만 시작해 스크롤과 구분
- Implementation Guidelines: Pointer Events 로 마우스 및 터치를 한 코드로 처리; 끌기 영역에 CSS `touch-action` 을 지정해 스크롤과 충돌을 막음; 자리 옮김 뒤 초점이 이동한 항목에 남게 함
- Common Mistakes: 드래그만 있고 단추 대안이 없음; 손잡이가 없어 스크롤과 구분 불가; 놓일 자리 미표시; 이동 결과를 보조기기에 알리지 않음
- Related Patterns: GS-03, GS-04, FM-07, MO-03
- Reference Image: 장면: 드래그 카드: 손잡이가 있는 항목 "3순위 삿포로" 가 들려 "2순위 후쿠오카" 위로 이동

## GS-06 핀치 (Pinch)
- ID: GS-06
- Korean Name: 핀치
- English Name: Pinch
- Category: Gestures (06)
- Definition: 손가락 두 개를 화면에 대고 벌리거나 오므리는 동작
- Purpose: 이미지, 지도 같은 내용을 확대 및 축소
- User Problem: 작은 화면에서 세부를 보려면 배율을 자유롭게 바꿔야 함
- When to Use: 이미지, 지도, 도면, 문서 미리보기처럼 세부를 살피는 내용
- When Not to Use: 확대할 이유가 없는 일반 본문; 핀치만이 유일한 확대 수단일 때; 한 손 사용이 전제인 화면
- Interaction Behavior: 두 접점 거리에 비례해 배율 변화; 접점 사이 중심을 기준으로 확대; 놓으면 배율 유지; 최소 1배, 최대 4배 (DF-11)
- Required States: 기본 배율; 확대 중; 최대 및 최소 도달; 이동 (확대 후 끌기); 원래 배율 복귀
- Visual Guidelines: 확대된 상태에서 현재 위치를 알 수 있게 함 (축소판 또는 안내); 확대 단추에 현재 배율 한계를 반영 (최대일 때 비활성)
- Accessibility: 다중 접점 제스처이므로 확대 및 축소 단추 같은 단일 포인터 대안 (2.5.1); 키보드 + 및 - 키; 단추 목표 크기 24x24 CSS px 이상 (2.5.8)
- Responsive Considerations: 데스크톱은 확대 및 축소 단추, 키보드 +, -, 마우스 휠 조합이 대응; 트랙패드 핀치는 브라우저 기본 확대와 겹치므로 확대 대상 영역 안에서만 가로채고 영역 밖은 브라우저 확대에 맡김 (DF-11)
- Implementation Guidelines: 확대 영역에 CSS `touch-action` 을 지정해 브라우저 기본 핀치와 구분; 페이지 전체 확대를 막는 viewport 설정은 두지 않음; 두 접점 이벤트는 Pointer Events 로 추적
- Common Mistakes: 핀치만 있고 단추가 없음; 페이지 전체 확대를 금지; 확대 후 이동 불가; 배율을 되돌릴 방법 없음
- Related Patterns: GS-07, GS-05, LD-07, MO-08
- Reference Image: 장면: 핀치 카드: 이미지 대각선 양 끝의 접점 2개

## GS-07 두 번 탭 (Double tap)
- ID: GS-07
- Korean Name: 두 번 탭
- English Name: Double tap
- Category: Gestures (06)
- Definition: 같은 지점을 짧은 간격으로 두 번 연속 탭하는 동작
- Purpose: 이미지를 확대했다가 원래 크기로 되돌리는 빠른 보조 동작
- User Problem: 한 손으로 확대하고 싶은데 핀치는 두 손가락이 필요함
- When to Use: 이미지 및 지도의 확대 전환; 숙련 사용자의 지름길
- When Not to Use: 주 기능; 두 번 탭에만 있는 기능; 탭 한 번에 이미 다른 동작이 있어 지연이 생기는 요소
- Interaction Behavior: 두 번 탭하면 단계 배율로 전환, 다시 두 번 탭하면 원복; 탭 한 번과 구분하느라 한 번 탭 반응이 늦어질 수 있음
- Required States: 기본; 확대됨; 전환 중; 첫 탭 대기; 비활성 (더 이상 확대 불가)
- Visual Guidelines: 두 번 탭할 수 있다는 단서가 따로 없으므로 확대 단추를 함께 노출; 전환은 짧은 움직임으로 위치 변화를 이해시킴 (MO-08)
- Accessibility: 눈에 보이지 않는 동작이므로 같은 기능 단추 필수; 시간 간격이 짧아 어려운 사용자가 있으므로 대안 제공 (2.5.1 취지); 키보드 +, - 키
- Responsive Considerations: 데스크톱은 두 번 클릭이 대응; 더불어 확대 단추 및 키보드; 두 번 클릭 시 텍스트가 선택되지 않게 처리
- Implementation Guidelines: 요소에 CSS `touch-action: manipulation` 으로 브라우저 두 번 탭 확대를 끔; 첫 탭 지연이 문제면 한 번 탭 동작이 없는 영역에만 사용
- Common Mistakes: 두 번 탭만으로 좋아요 같은 기능 제공; 한 번 탭 반응이 느려짐; 단추 없음; 브라우저 기본 확대와 충돌
- Related Patterns: GS-01, GS-06, MO-08, LD-07
- Reference Image: 장면: 두 번 탭 카드: 이미지 영역 (동작 중간 장면)

## GS-08 당겨서 새로고침 (Pull to refresh)
- ID: GS-08
- Korean Name: 당겨서 새로고침
- English Name: Pull to refresh
- Category: Gestures (06)
- Definition: 목록 맨 위에서 아래로 당겼다 놓아 내용을 다시 불러오는 동작
- Purpose: 최신 내용을 사용자가 직접 요청
- User Problem: 목록이 오래된 것인지 알 수 없고 새로고침 위치를 찾기 어려움
- When to Use: 시간순으로 갱신되는 목록 (특가, 피드, 알림); 모바일 앱형 화면
- When Not to Use: 자동 갱신이 충분한 화면; 입력 중인 폼; 목록이 아닌 화면; 맨 위가 아닌 위치에서의 당김
- Interaction Behavior: 맨 위에서 당기면 표시가 따라 내려옴; 기준 거리를 넘고 놓으면 새로 불러옴; 기준 거리는 80px (DF-09); 새 항목이 맨 위에 추가됨
- Required States: 대기; 당기는 중; 놓으면 갱신됨 (기준 도달); 갱신 중; 완료 (새 항목 수 표시); 변경 없음; 오류
- Visual Guidelines: 당기는 정도를 표시가 보여줌; 완료 후 새 항목을 맨 위에 보임 (예시 화면은 "새 특가 3개"); 오류는 ES-08 또는 인라인 문구
- Accessibility: 경로 제스처이므로 새로고침 단추를 둠 (2.5.1); 완료 결과를 `role="status"` 로 알림; 갱신 중 영역 `aria-busy`
- Responsive Considerations: 데스크톱은 새로고침 단추 또는 키보드 F5, 자동 갱신이 대응; 마우스 휠로 당기기는 지원하지 않음
- Implementation Guidelines: 브라우저 기본 새로고침과 겹치면 CSS `overscroll-behavior` 로 조정; 스크롤 위치가 맨 위일 때만 동작; 갱신 중 중복 요청을 막음
- Common Mistakes: 단추 대안 없음; 변경이 없을 때 아무 응답 없음; 스크롤 중간에서 작동; 갱신 후 읽던 위치를 잃음
- Related Patterns: LD-01, LD-09, ES-08, GS-03
- Reference Image: 장면: 당겨서 새로고침 카드: 목록 맨 위에 "새 특가 3개" 항목

## GS-09 가장자리 스와이프 (Edge swipe)
- ID: GS-09
- Korean Name: 가장자리 스와이프
- English Name: Edge swipe
- Category: Gestures (06)
- Definition: 화면 가장자리에서 시작해 안쪽으로 쓸어 이전 화면으로 돌아가는 동작
- Purpose: 한 손으로 뒤로 가기를 하되 상단 단추까지 손을 뻗지 않음
- User Problem: 큰 화면에서 왼쪽 위 뒤로 가기 단추가 손에서 멀음
- When to Use: 상세 화면에서 목록으로 돌아갈 때; 계층 이동 후 뒤로 가기
- When Not to Use: 화면 가장자리에서 시작하는 자체 동작을 만들 때 (OS 의 뒤로 가기 제스처와 겹침); 되돌아갈 곳이 없는 최상위 화면
- Interaction Behavior: 가장자리에서 안쪽으로 밀면 현재 화면이 손가락을 따라 밀리고 이전 화면이 드러남; 놓는 기준에 따라 돌아가거나 취소; 기준은 플랫폼 기본값을 따름
- Required States: 대기; 진행 중 (이전 화면 노출); 완료 (이전 화면); 취소 (원위치)
- Visual Guidelines: 상세 화면이 목록 위로 겹치고 밀려 나가는 모양 (예시 화면: "특가 목록" 위로 옆에서 겹친 상세 화면); 이전 화면 위치를 유지
- Accessibility: 보이는 뒤로 가기 단추 (NV-09) 를 둠 (2.5.1); 키보드 및 보조기기에서 뒤로 가기 접근 가능; 이동 후 초점을 이전 화면의 진입 항목에 되돌림 (2.4.3)
- Responsive Considerations: 데스크톱은 브라우저 뒤로 가기 단추 및 화면 안 뒤로 가기 단추가 대응; 가장자리 동작은 제공하지 않음
- Implementation Guidelines: OS 및 브라우저에 이미 있는 뒤로 가기 동작을 자체 구현하지 않고 이력이 화면 이동과 맞도록 함; 가장자리 시작 영역에는 가로 스와이프 (GS-03, GS-04) 를 두지 않음
- Common Mistakes: OS 뒤로 가기와 겹치는 자체 가장자리 동작; 보이는 뒤로 가기 단추 없음; 돌아간 뒤 목록 위치 및 초점 소실; 이력이 화면 이동과 어긋남
- Related Patterns: NV-09, GS-03, GS-04, MO-07
- Reference Image: 장면: 가장자리 스와이프 카드: "특가 목록" 화면 위로 상세 화면이 옆에서 겹친 장면
