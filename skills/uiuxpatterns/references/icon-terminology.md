# Menu Icon Terminology (메뉴 아이콘 별명)

- 범위: 메뉴를 여는 아이콘 모양의 별명 9종 (IC-01 ~ IC-09) 을 아이콘 단추 관점으로 정리한 용어집
- 참조 이미지: `assets/10-icon-terminology.png`
- 색인: `pattern-catalog.md`

## 검증 메모
- (a) 실무에서 널리 통하는 이름은 햄버거, 케밥 정도이고 나머지는 디자인 커뮤니티 별명이라 사람마다 가리키는 모양이 다를 수 있음
- (b) 와플 및 벤토는 둘 다 3x3 격자를 가리키는 말로 섞여 쓰이며, 원본 이미지에서는 둥근 점 9개가 와플, 네모 점 9개가 벤토
- (c) 도너, 계단, 슬라이더 아이콘은 원본 이미지에서 각각 필터 값, 정렬, 범위 조절 메뉴를 펼치는 장면으로 나옴. 모양과 기능의 대응은 표준이 아니라 원본 이미지의 사용 예
- (d) 팀 안에서는 별명보다 기능 이름 (예: 더 보기 메뉴, 앱 전환, 필터, 정렬) 을 함께 적음

## 유사 패턴 구분
| 헷갈리는 쌍 | 고르는 기준 |
|---|---|
| 햄버거 (IC-01) 대 베지 버거 (IC-07) | 가로줄 3개 대 2개. 원본 이미지 사용 예는 햄버거가 이동 메뉴 (항공권, 혜택, MY), 베지 버거가 설정 및 로그아웃. 한 제품에서 둘을 병용하지 않음 |
| 케밥 (IC-02) 대 미트볼 (IC-03) | 세로 점 3개 대 가로 점 3개. 둘 다 항목 단위 행동 메뉴이므로 한 제품에서 하나로 통일 |
| 와플 (IC-04) 대 벤토 (IC-05) | 둘 다 3x3 격자. 원본 이미지에서 둥근 점은 와플 (혜택, 쿠폰함, 찜 목록), 네모 점은 벤토 (전체 기능, 설정). 별명이 섞여 쓰이므로 한 제품에서 하나만 쓰고 기능 이름 (앱 전환, 바로가기) 을 병기 |
| 햄버거 (IC-01) 대 도너 (IC-06) 대 계단 (IC-08) | 가로줄 모양이 비슷하나 길이가 다름. 줄 길이가 같으면 이동 메뉴, 아래로 짧아지면 필터 값, 어긋나게 놓이면 정렬 (원본 이미지의 사용 예) |
| 도너 (IC-06) 대 슬라이더 아이콘 (IC-09) | 도너는 정해진 값 (편도, 서울, 조식 포함) 을 고르는 필터, 슬라이더 아이콘은 연속 범위 (가격 범위, 평점 범위) 를 조절 |

## IC-01 햄버거 (Hamburger)
- ID: IC-01
- Korean Name: 햄버거
- English Name: Hamburger
- Category: Menu Icon Terminology (10)
- Definition: 같은 길이의 가로줄 3개를 세로로 쌓은 아이콘
- Purpose: 주요 이동 메뉴 (드로어 또는 펼침 목록) 를 여는 단추
- User Problem: 목적지가 많아 화면에 모두 펼치기 어려움
- When to Use: 좁은 화면에서 이동 메뉴를 접어 둘 때 (원본 이미지: 항공권, 혜택, MY); 드물게 쓰는 목적지가 많을 때
- When Not to Use: 데스크톱 넓은 화면에서 주요 목적지를 숨길 때 (발견성이 낮아져 상단 내비게이션 또는 사이드바로 펼침); 자주 쓰는 소수 목적지 (하단 탭바 NV-01)
- Interaction Behavior: 누르면 메뉴 패널이 열리고 단추 상태가 열림으로 바뀜; 다시 누르거나 Esc 로 닫힘; 닫으면 단추로 초점 복귀
- Required States: 닫힘; 열림 (`aria-expanded`); hover; focus-visible; 눌림; 알림 있음 (뱃지 FB-09)
- Visual Guidelines: 줄 3개 길이를 같게; 열린 상태를 닫기(X) 모양 또는 상태 표시로 구분; 아이콘 대비 3:1 (WCAG 1.4.11); 가까이에 글자 `메뉴` 를 둘 수 있음
- Accessibility: `<button>` 에 `aria-label` (예: 메뉴) 이고 별명 `햄버거` 는 쓰지 않음; `aria-expanded` 를 상태에 맞춰 갱신; 목표 44x44pt (Apple HIG), 48x48dp (Material Design), 최소 24x24 CSS px (WCAG 2.5.8)
- Responsive Considerations: 좁은 화면에서만 접고 넓은 화면에서는 주요 목적지를 항상 보이는 내비게이션으로 펼침; 데스크톱에서는 hover 툴팁 (FB-07) 에 기능 이름을 보조 표시
- Implementation Guidelines: 이동 링크 목록을 여는 단추는 `aria-expanded` 로 열림 여부를 알리고 열리는 목록과 연결; 아이콘은 SVG 로 `currentColor` 를 쓰고 접근 가능한 이름은 단추에 둠; 모달 패널이면 초점 가두기
- Common Mistakes: 글자 없는 아이콘만 둠; 데스크톱에서도 주요 목적지를 햄버거 뒤에 숨김; `aria-expanded` 누락; 줄 2개 아이콘과 혼용
- Related Patterns: NV-03, NV-01, IC-07, FB-09
- Reference Image: `assets/10-icon-terminology.png` 햄버거 카드: 가로줄 3개. 펼친 메뉴 "항공권", "혜택", "MY"

## IC-02 케밥 (Kebab)
- ID: IC-02
- Korean Name: 케밥
- English Name: Kebab
- Category: Menu Icon Terminology (10)
- Definition: 점 3개를 세로로 쌓은 아이콘
- Purpose: 한 항목에 대한 행동 메뉴 (더 보기) 를 여는 단추
- User Problem: 항목마다 여러 행동 단추를 두면 목록이 복잡해짐
- When to Use: 목록 항목, 카드, 행 끝에서 보조 행동을 모아 둘 때 (원본 이미지: 수정, 공유, 삭제); 행동이 둘 이상일 때
- When Not to Use: 행동이 하나뿐 (단추 직접 노출); 주 행동 (보이는 단추); 메뉴 안에 이동 메뉴를 넣을 때 (햄버거)
- Interaction Behavior: 누르면 항목 가까이에 행동 목록이 뜸; 항목을 고르면 실행하고 닫힘; 바깥 누름 또는 Esc 로 닫힘
- Required States: 기본; hover; focus-visible; 눌림; 메뉴 열림; 항목별 비활성; 위험 항목 (삭제)
- Visual Guidelines: 점 크기 및 간격을 균일하게; 위험 항목은 빨강 및 글자를 함께 사용 (WCAG 1.4.1); 점이 작아도 눌림 영역을 확보
- Accessibility: `<button>` 에 `aria-label` (예: 더 보기, 목록에서는 항목 이름 포함); `aria-haspopup` 및 `aria-expanded`; 목표 44x44pt (Apple HIG), 48x48dp (Material Design); 메뉴가 닫히면 단추로 초점 복귀
- Responsive Considerations: 모바일에서는 같은 행동을 바텀시트 (FB-05) 로 열 수 있음; 데스크톱은 hover 시 노출하되 초점에도 노출하고 길게 누르기 (GS-02) 대신 오른쪽 클릭 메뉴를 병행
- Implementation Guidelines: 행동 목록은 `role="menu"` 구조 또는 단순 단추 목록으로 만듦; 아이콘은 SVG 이고 단추 영역은 점보다 크게; 메뉴 위치는 화면 가장자리를 넘지 않게 자동 조정
- Common Mistakes: 이름 없는 아이콘만 둠; 목록 항목마다 같은 이름 `더 보기` 여서 구분이 안 됨; 삭제를 즉시 실행 (확인 및 되돌리기 없음); 점이 가로 방향 아이콘과 섞임
- Related Patterns: IC-03, GS-02, FB-05, FB-02
- Reference Image: `assets/10-icon-terminology.png` 케밥 카드: 세로 점 3개. 펼친 메뉴 "수정", "공유", "삭제"(빨강)

## IC-03 미트볼 (Meatballs)
- ID: IC-03
- Korean Name: 미트볼
- English Name: Meatballs
- Category: Menu Icon Terminology (10)
- Definition: 점 3개를 가로로 나란히 놓은 아이콘
- Purpose: 한 항목에 대한 보조 행동 메뉴를 여는 단추 (케밥과 같은 역할의 가로 모양)
- User Problem: 항목 옆에 행동 단추를 모두 두면 공간이 부족하고 눈에 거슬림
- When to Use: 행 끝 또는 카드 모서리에 가로 방향이 더 맞을 때 (원본 이미지: 숨기기, 신고); 한 제품에서 케밥 대신 이 모양으로 통일할 때
- When Not to Use: 같은 제품에 케밥도 있을 때 (모양과 방향을 섞지 않음); 행동이 하나뿐; 로딩 중 표시와 혼동되는 문맥 (점 3개 애니메이션)
- Interaction Behavior: 누르면 행동 목록이 뜸; 항목을 고르면 실행하고 닫힘; 바깥 누름 또는 Esc 로 닫힘
- Required States: 기본; hover; focus-visible; 눌림; 메뉴 열림; 위험 항목 (신고)
- Visual Guidelines: 점 3개의 간격을 균일하게; 위험 항목은 빨강 및 글자를 함께 사용 (WCAG 1.4.1); 로딩 점과 혼동되지 않도록 움직이지 않음
- Accessibility: `<button>` 에 `aria-label` (예: 더 보기); `aria-haspopup` 및 `aria-expanded`; 목표 44x44pt (Apple HIG), 48x48dp (Material Design); 메뉴 닫힘 뒤 초점 복귀
- Responsive Considerations: 터치에서는 바텀시트 (FB-05) 로 열 수 있음; 데스크톱은 hover 시 툴팁 (FB-07) 으로 기능 이름 표시 (초점에도 표시)
- Implementation Guidelines: 단추 안의 SVG 에 접근 가능한 이름을 단추에 둠; 메뉴 구조 및 위치 조정은 케밥과 같음; 제품 전체에서 둘 중 하나만 사용하는 규칙을 디자인 토큰 문서에 적음
- Common Mistakes: 케밥 및 미트볼을 한 제품에서 섞음; 아이콘만 있고 이름 없음; 로딩 표시처럼 보이게 움직임; 신고를 확인 없이 실행
- Related Patterns: IC-02, GS-02, FB-05, FB-07
- Reference Image: `assets/10-icon-terminology.png` 미트볼 카드: 가로 점 3개. 펼친 메뉴 "숨기기", "신고"(빨강)

## IC-04 와플 (Waffle)
- ID: IC-04
- Korean Name: 와플
- English Name: Waffle
- Category: Menu Icon Terminology (10)
- Definition: 둥근 점 9개를 3x3 격자로 놓은 아이콘
- Purpose: 서비스 및 바로가기 모음을 여는 단추 (앱 전환)
- User Problem: 여러 서비스 또는 기능으로 빠르게 건너가는 길이 화면 곳곳에 흩어져 있음
- When to Use: 자주 쓰는 바로가기 몇 개를 격자로 모아 둘 때 (원본 이미지: 혜택, 쿠폰함, 찜 목록); 서비스 간 전환이 필요할 때
- When Not to Use: 주요 이동 메뉴 대체 (햄버거 IC-01 또는 탭바); 같은 제품에 네모 점 격자 (벤토) 도 쓸 때; 항목이 둘 이하
- Interaction Behavior: 누르면 격자 패널 또는 목록이 열림; 항목을 누르면 해당 서비스 또는 기능으로 이동하고 닫힘; Esc 또는 바깥 누름으로 닫힘
- Required States: 닫힘; 열림 (`aria-expanded`); hover; focus-visible; 눌림; 항목 비활성
- Visual Guidelines: 점을 둥글게 균일한 간격으로 3x3 배치 (원본 이미지 기준); 패널 안 항목은 아이콘 및 글자 이름을 함께 둠; 아이콘 대비 3:1 (WCAG 1.4.11)
- Accessibility: `<button>` 에 `aria-label` (예: 앱 전환, 바로가기); `aria-expanded` 및 패널 형태에 맞춰 `aria-haspopup`; 목표 44x44pt (Apple HIG), 48x48dp (Material Design); 패널 항목은 키보드로 이동 가능
- Responsive Considerations: 좁은 화면은 전체 화면 또는 바텀시트 패널, 넓은 화면은 단추 아래 떠 있는 패널; 데스크톱은 hover 툴팁으로 기능 이름 보조
- Implementation Guidelines: 와플 및 벤토를 모양 별명이 아니라 기능 이름으로 구분해 컴포넌트 이름을 짓고 (예: 앱 전환 단추); 패널 항목은 링크 목록; 패널이 열리면 첫 항목으로 초점 이동
- Common Mistakes: 별명이 섞여 팀 안에서 다른 모양을 가리킴; 아이콘만 두고 이름 없음; 격자 패널에서 키보드 이동 불가; 주요 이동 메뉴를 대신함
- Related Patterns: IC-05, IC-01, NV-01, FB-07
- Reference Image: `assets/10-icon-terminology.png` 와플 카드: 둥근 점 9개 (3x3). 펼친 메뉴 "혜택", "쿠폰함", "찜 목록"

## IC-05 벤토 (Bento)
- ID: IC-05
- Korean Name: 벤토
- English Name: Bento
- Category: Menu Icon Terminology (10)
- Definition: 네모 점 9개를 3x3 격자로 놓은 아이콘
- Purpose: 전체 기능 모음 또는 설정을 여는 단추 (원본 이미지의 사용 예)
- User Problem: 기능이 많아 한 화면 안에서 모두 보여줄 수 없음
- When to Use: 제품의 전체 기능 목록을 한 곳에 모아 둘 때 (원본 이미지: 전체 기능, 설정); 와플과 구분해 쓰는 팀 규칙이 있을 때
- When Not to Use: 같은 제품에서 와플과 병용; 주요 이동 메뉴 대체; 기능이 소수라 직접 노출이 가능할 때
- Interaction Behavior: 누르면 기능 모음 패널이 열림; 항목을 누르면 이동하고 닫힘; Esc 또는 바깥 누름으로 닫힘
- Required States: 닫힘; 열림 (`aria-expanded`); hover; focus-visible; 눌림; 항목 비활성
- Visual Guidelines: 점을 네모로 균일하게 3x3 배치 (원본 이미지 기준); 와플과 모양 차이가 작아 별명보다 기능 이름 병기; 아이콘 대비 3:1 (WCAG 1.4.11)
- Accessibility: `<button>` 에 `aria-label` (예: 전체 기능, 설정 메뉴); `aria-expanded` 및 필요 시 `aria-haspopup`; 목표 44x44pt (Apple HIG), 48x48dp (Material Design); 키보드로 패널 이동
- Responsive Considerations: 좁은 화면은 전체 화면 패널, 넓은 화면은 단추 아래 패널; 데스크톱은 hover 시 기능 이름 툴팁 (초점에도 표시)
- Implementation Guidelines: 컴포넌트 이름을 모양 별명 대신 기능 이름으로 짓고 별명은 주석 또는 문서에 병기; 패널 구조는 와플과 같은 링크 목록; 패널 열림 때 초점 이동
- Common Mistakes: 와플 및 벤토를 혼용해 소통 오류; 이름 없는 아이콘만 둠; 설정 및 전체 기능을 한 메뉴에 섞어 목적이 불분명; 패널의 키보드 이동 불가
- Related Patterns: IC-04, IC-01, NV-03, FB-07
- Reference Image: `assets/10-icon-terminology.png` 벤토 카드: 네모 점 9개 (3x3). 펼친 메뉴 "전체 기능", "설정"

## IC-06 도너 (Döner)
- ID: IC-06
- Korean Name: 도너
- English Name: Döner
- Category: Menu Icon Terminology (10)
- Definition: 아래로 갈수록 짧아지는 가로줄 3개를 쌓은 아이콘
- Purpose: 필터 값을 고르는 메뉴를 여는 단추 (원본 이미지의 사용 예)
- User Problem: 조건이 많은 목록에서 필터를 어디서 바꾸는지 찾기 어려움
- When to Use: 목록에 조건 (편도, 서울, 조식 포함) 을 걸 때; 적용 중인 필터 개수를 단추에 표시할 때
- When Not to Use: 정렬 메뉴 (계단 IC-08 사용 예); 범위 조절 (슬라이더 아이콘 IC-09); 이동 메뉴 (햄버거)
- Interaction Behavior: 누르면 필터 값 목록 또는 패널이 열림; 값을 고르면 목록이 갱신됨; 적용 중 필터는 칩 또는 개수로 표시
- Required States: 기본; 필터 적용 중 (개수); 열림; hover; focus-visible; 눌림; 결과 없음 (ES-03)
- Visual Guidelines: 줄 길이가 아래로 갈수록 짧아지는 모양; 적용 중임을 색만으로 하지 않고 개수 또는 칩으로 함 (WCAG 1.4.1); 아이콘 대비 3:1 (1.4.11)
- Accessibility: `<button>` 에 `aria-label` (예: 필터); `aria-expanded`, 패널 내 선택은 `<fieldset>`/`<legend>` 와 체크박스 또는 라디오; 적용 결과 개수를 `role="status"` 로 알림; 목표 44x44pt (Apple HIG), 48x48dp (Material Design)
- Responsive Considerations: 좁은 화면은 바텀시트 또는 전체 화면 필터 패널, 넓은 화면은 단추 아래 패널 또는 옆 패널; 터치 및 마우스 모두 같은 항목
- Implementation Guidelines: 이 모양이 필터를 뜻하는 것은 표준이 아니므로 기능 이름 `필터` 를 `aria-label` 과 보이는 글자 모두에 둠; 선택 상태는 URL 에 반영해 새로고침 후에도 유지할지 제품에서 정한다
- Common Mistakes: 필터 및 정렬 아이콘이 구분되지 않음; 적용 중인 필터가 보이지 않음; 결과 없음일 때 초기화 수단이 없음; 글자 없는 아이콘만 둠
- Related Patterns: IC-08, IC-09, ES-03, NV-05
- Reference Image: `assets/10-icon-terminology.png` 도너 카드: 아래로 갈수록 짧아지는 가로줄 3개. 펼친 메뉴 "편도", "서울", "조식 포함"

## IC-07 베지 버거 (Veggie burger)
- ID: IC-07
- Korean Name: 베지 버거
- English Name: Veggie burger
- Category: Menu Icon Terminology (10)
- Definition: 같은 길이의 가로줄 2개를 쌓은 아이콘
- Purpose: 계정 및 설정 같은 보조 메뉴를 여는 단추 (원본 이미지의 사용 예)
- User Problem: 이동 메뉴와 분리된 보조 기능 (설정, 로그아웃) 을 둘 자리가 필요함
- When to Use: 메뉴 항목이 적은 보조 메뉴 (원본 이미지: 설정, 로그아웃); 별도 이동 메뉴가 이미 있어 구분이 필요할 때
- When Not to Use: 같은 화면에 줄 3개 햄버거도 있을 때 (줄 수 차이가 작아 혼동); 주요 목적지; 이름이 널리 통하지 않아 팀 밖에 전달해야 할 때
- Interaction Behavior: 누르면 보조 메뉴 목록이 열림; 항목을 고르면 실행 또는 이동하고 닫힘; Esc 또는 바깥 누름으로 닫힘
- Required States: 닫힘; 열림 (`aria-expanded`); hover; focus-visible; 눌림; 항목 비활성
- Visual Guidelines: 줄 2개 길이 및 간격을 균일하게; 줄 3개 아이콘과 나란히 두지 않음; 아이콘 대비 3:1 (WCAG 1.4.11)
- Accessibility: `<button>` 에 `aria-label` (예: 계정 메뉴, 설정 메뉴) 이고 별명은 쓰지 않음; `aria-haspopup` 및 `aria-expanded`; 목표 44x44pt (Apple HIG), 48x48dp (Material Design)
- Responsive Considerations: 데스크톱은 계정 영역에 글자 또는 프로필과 함께 노출하는 방식이 대응; 좁은 화면은 햄버거 메뉴 안에 항목을 통합하는 방식도 있음
- Implementation Guidelines: 이름은 모양 별명 대신 기능 이름으로 문서화; 목록에 로그아웃 같은 위험 행동이 있으면 구분해 배치; 메뉴 열림 후 첫 항목으로 초점 이동
- Common Mistakes: 햄버거와 줄 수 차이만으로 구분해 사용자가 혼동; 이름 없는 아이콘만 둠; 로그아웃을 확인 없이 즉시 실행; 별명으로만 소통
- Related Patterns: IC-01, IC-02, NV-03, FB-04
- Reference Image: `assets/10-icon-terminology.png` 베지 버거 카드: 가로줄 2개. 펼친 메뉴 "설정", "로그아웃"

## IC-08 계단 (Stairs)
- ID: IC-08
- Korean Name: 계단
- English Name: Stairs
- Category: Menu Icon Terminology (10)
- Definition: 어긋나게 놓인 가로줄 3개를 쌓은 아이콘
- Purpose: 정렬 기준을 고르는 메뉴를 여는 단추 (원본 이미지의 사용 예)
- User Problem: 목록 순서를 바꾸는 방법을 찾기 어렵고 현재 정렬을 알기 어려움
- When to Use: 목록 정렬 기준이 둘 이상일 때 (원본 이미지: 최신순, 낮은 가격순, 인기순); 현재 정렬을 보여줄 때
- When Not to Use: 필터 값 선택 (도너 IC-06 사용 예); 연속 범위 조절 (슬라이더 아이콘 IC-09); 정렬 기준이 하나뿐
- Interaction Behavior: 누르면 정렬 기준 목록이 열림; 하나를 고르면 목록이 다시 정렬되고 닫힘; 현재 기준이 선택 표시됨 (원본 이미지: 최신순)
- Required States: 닫힘; 열림; 현재 기준 선택됨; hover; focus-visible; 정렬 중; 결과 없음
- Visual Guidelines: 현재 기준을 체크 표시 및 굵은 글씨로 구분하고 색만으로 하지 않음 (WCAG 1.4.1); 항목 글자 대비 4.5:1 (1.4.3)
- Accessibility: `<button>` 에 `aria-label` (예: 정렬); `aria-haspopup` 및 `aria-expanded`; 목록은 `role="menuitemradio"` 및 `aria-checked` 또는 네이티브 `<select>`, 라디오; 정렬 변경 결과를 `role="status"` 로 알림; 목표 44x44pt (Apple HIG), 48x48dp (Material Design)
- Responsive Considerations: 좁은 화면은 바텀시트 (FB-05), 넓은 화면은 단추 아래 목록 또는 `<select>`; 단추 옆에 현재 기준 글자를 노출하면 아이콘 의존이 줄어듦
- Implementation Guidelines: 한 번에 하나만 선택되므로 라디오 의미를 쓰는 구조; 선택 값을 URL 에 반영할지 제품에서 정한다; 정렬 뒤 목록 맨 위로 이동하고 초점을 목록 시작에 둠
- Common Mistakes: 현재 정렬 기준이 보이지 않음; 아이콘만 두고 이름 없음; 정렬 후 스크롤이 중간에 남음; 필터 아이콘과 구분되지 않음
- Related Patterns: IC-06, FM-02, FM-06, FB-05
- Reference Image: `assets/10-icon-terminology.png` 계단 카드: 어긋나게 놓인 가로줄 3개. 펼친 메뉴 "최신순"(선택), "낮은 가격순", "인기순"

## IC-09 슬라이더 아이콘 (Sliders)
- ID: IC-09
- Korean Name: 슬라이더 아이콘
- English Name: Sliders
- Category: Menu Icon Terminology (10)
- Definition: 조절 손잡이가 달린 가로줄 2개를 쌓은 아이콘
- Purpose: 값의 범위를 조절하는 메뉴를 여는 단추 (원본 이미지의 사용 예)
- User Problem: 가격, 평점처럼 연속된 범위로 조건을 걸고 싶은데 값 목록으로는 맞지 않음
- When to Use: 범위 조건이 있는 목록 (원본 이미지: 가격 범위, 평점 범위); 조절 결과 개수를 바로 보여줄 때
- When Not to Use: 정해진 값 선택 (도너 IC-06 사용 예); 정렬 (계단 IC-08); 값이 두세 개뿐인 경우 (세그먼트 또는 칩)
- Interaction Behavior: 누르면 범위 조절 패널이 열림; 손잡이를 움직여 값을 바꿈; 적용 후 목록이 갱신됨; 초기화 수단 제공
- Required States: 닫힘; 열림; 값 조절 중; 적용됨; 초기화; 결과 없음 (ES-03); hover; focus-visible
- Visual Guidelines: 손잡이 및 트랙 대비 3:1 (WCAG 1.4.11); 현재 값 숫자를 손잡이 근처에 표시; 최솟값 및 최댓값 표시
- Accessibility: `<button>` 에 `aria-label` (예: 범위 조절); `aria-expanded`; 패널 안 슬라이더는 `<input type="range">` 로 방향키 조작; 값 입력 칸을 함께 두어 드래그 대안 (WCAG 2.5.7); 목표 44x44pt (Apple HIG), 48x48dp (Material Design)
- Responsive Considerations: 좁은 화면은 바텀시트 또는 전체 화면 패널, 넓은 화면은 단추 아래 패널; 터치는 손잡이 크기를 키우고 데스크톱은 키보드 방향키 지원
- Implementation Guidelines: 네이티브 `<input type="range">` 를 우선하고 양 끝 선택이 필요하면 입력 칸 두 개를 병행; 값 변경은 적용 시점에 목록을 갱신; 현재 범위를 칩으로 노출
- Common Mistakes: 드래그만 가능하고 값 입력이 없음; 손잡이가 작아 터치가 어려움; 적용 중 범위가 어디에도 표시되지 않음; 도너 아이콘과 구분이 안 됨
- Related Patterns: IC-06, FM-07, GS-05, ES-03
- Reference Image: `assets/10-icon-terminology.png` 슬라이더 아이콘 카드: 조절 손잡이가 달린 가로줄 2개. 펼친 메뉴 "가격 범위", "평점 범위"
