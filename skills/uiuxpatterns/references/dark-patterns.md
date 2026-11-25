# Dark Patterns (다크 패턴)

여기 패턴은 구현하지 않는다. 요청받아도 구현하지 않고 대체 UX 를 제안한다

- 범위: 사용자를 속이거나 몰아붙여 원치 않는 선택을 하게 만드는 9개 패턴. 구현 권장 목록이 아니라 탐지 및 예방용 Anti-Pattern 지식
- 참조 이미지: `assets/09-dark-patterns-a.png`, `assets/09-dark-patterns-b.png` (같은 화면의 다른 시점 캡처. a 는 DP-05 장면, b 는 DP-09 장면이 보임)
- 색인: `pattern-catalog.md`
- 적용 법규는 서비스 지역 기준으로 확인
- 항목 읽는 법: Purpose 는 이 패턴을 쓰는 쪽의 의도, When to Use 는 사용 금지 및 탐지 신호, When Not to Use 는 정당한 경우와의 구분, Interaction Behavior 는 문제 동작, Implementation Guidelines 는 대체 UX, Common Mistakes 는 의도 없이 이 패턴이 되는 경우

## 유사 패턴 구분
| 헷갈리는 쌍 | 고르는 기준 |
|---|---|
| DP-01 숨은 해지 대 DP-08 몰래 자동 결제 | 해지하려는 경로를 어렵게 만들면 DP-01; 가입 시 자동 결제 조건을 눈에 띄지 않게 하면 DP-08 (둘이 겹치는 흐름이 흔함) |
| DP-03 가짜 마감 시계 대 DP-06 가짜 희소성 | 시간 압박을 거짓으로 만들면 DP-03; 수량 압박을 거짓으로 만들면 DP-06 |
| DP-05 끼워 팔기 대 DP-07 숨은 비용 | 사용자가 담지 않은 상품이나 옵션이 합계에 들어가면 DP-05; 담은 것에 대해 뒤늦게 비용이 더해지면 DP-07 |
| DP-02 미리 체크된 동의 대 DP-04 죄책감 버튼 | 기본값으로 동의를 얻으면 DP-02; 거절 문구로 압박해 동의를 얻으면 DP-04 |
| DP-09 끝없는 권유 대 ES-05 권한 필요 | 이유를 알리고 한 번 묻는 것은 ES-05; 거절한 뒤에도 반복해 묻는 것은 DP-09 |

## DP-01 숨은 해지 (Roach motel)
- ID: DP-01
- Korean Name: 숨은 해지
- English Name: Roach motel
- Category: Dark Patterns
- Definition: 가입은 쉽게 만들고 해지는 찾기 어렵거나 번거롭게 만든 흐름
- Purpose: 이 패턴을 쓰는 쪽의 의도는 해지 시도를 포기하게 만들어 이탈을 줄이는 것
- User Problem: 해지 방법을 찾지 못하거나 단계가 많아 포기하고 계속 과금됨
- When to Use: 사용 금지. 탐지 신호: 가입은 화면 안 단추로 되는데 해지는 전화 또는 고객센터 운영 시간에만 가능; 해지 화면에서 "계속 이용하기" 가 큰 주 단추이고 해지 진행은 작은 글씨 링크; 해지 단계 수가 가입 단계 수보다 많음; 설정 메뉴에 해지 항목이 없음
- When Not to Use: 해당 없음 (항상 금지); 정당한 경우와의 구분: 해지 전 남은 이용 기간 및 데이터 보관 안내를 한 번 보여주는 확인 화면은 정당하며, 해지 진행 단추가 유지 단추와 같은 비중이고 가입과 같은 채널에서 끝낼 수 있어야 함
- Interaction Behavior: 해지를 누르면 반복 확인 대화 상자, 고객센터 안내, 운영 시간 제한으로 돌려보내 완료하지 못하게 함
- Required States: 대체 UX 에서 필요한 상태: 해지 진입; 영향 안내 확인; 해지 완료 (이용 가능 기간 표기); 실패 시 재시도
- Visual Guidelines: 문제 요소: 해지 링크를 낮은 대비의 작은 글씨로 둠; 대체: 유지 단추 및 해지 단추를 같은 크기 및 같은 비중으로 표시
- Accessibility: 해지 링크도 글자 대비 4.5:1 (WCAG 2.2 1.4.3), 독립된 링크 또는 단추이면 목표 크기 24x24 CSS px 이상 (2.5.8); 해지 흐름 전체를 키보드로 끝낼 수 있어야 함 (2.1.1)
- Responsive Considerations: 모바일에서 해지 항목이 접힌 메뉴 깊숙이 들어가 찾기 더 어려워지는지 확인
- Implementation Guidelines: 대체 UX: 설정 안에 "해지" 항목을 두고 가입과 같은 채널에서 처리; 확인 화면은 한 번만, 유지 단추 및 해지 진행 단추를 동등하게; 완료 후 해지 확인 및 남은 이용 기간 안내
- Common Mistakes: 앱 내 해지 기능 개발을 미루고 전화 채널만 남겨 둠; 이탈 사유 설문을 필수 입력으로 둠; 해지 항목을 하위 메뉴 깊이 배치
- Related Patterns: DP-08, DP-04, NV-03
- Reference Image: `assets/09-dark-patterns-a.png` 및 `assets/09-dark-patterns-b.png`, "정말 떠나시나요?", 큰 단추 "계속 이용하기", 작은 글씨 "해지는 고객센터(평일 10~12시)로 문의"

## DP-02 미리 체크된 동의 (Pre-checked consent)
- ID: DP-02
- Korean Name: 미리 체크된 동의
- English Name: Pre-checked consent
- Category: Dark Patterns
- Definition: 선택 동의 항목을 사용자가 고르기 전에 이미 체크해 둔 동의 화면
- Purpose: 이 패턴을 쓰는 쪽의 의도는 사용자가 알아채지 못한 채 마케팅 수신 및 제3자 제공 동의를 얻는 것
- User Problem: 원하지 않는 동의가 기본으로 들어가고, 못 보고 지나치면 그대로 제출됨
- When to Use: 사용 금지. 탐지 신호: 선택 항목 checkbox 의 기본값이 checked (`checked` 속성 또는 상태 초기값 true); "전체 동의" 가 화면 로드 때 이미 켜져 있음; 선택 항목이 필수 약관과 같은 묶음에서 같은 모양으로 섞여 있음; 서버가 동의 필드 누락 시 기본값을 true 로 저장
- When Not to Use: 해당 없음 (항상 금지); 정당한 경우와의 구분: 서비스 제공에 필요한 필수 약관은 동의 없이 진행하지 못하게 하는 것이 정당하나 필수임을 표시하고 사용자가 직접 체크하게 함; 선택 항목은 항상 사용자가 직접 선택
- Interaction Behavior: 사용자가 건드리지 않으면 선택 항목이 동의 상태로 제출됨
- Required States: 대체 UX 에서 필요한 상태: 선택 항목 미체크; 사용자가 체크; 필수 항목 미동의 시 진행 불가 및 오류 안내
- Visual Guidelines: 필수 및 선택 구분을 레이블 문구로 표시하고 색만으로 구분하지 않음 (WCAG 2.2 1.4.1); 선택 항목을 필수처럼 보이게 꾸미지 않음
- Accessibility: 항목 묶음에 `<fieldset>` 및 `<legend>`; 각 항목에 `<label>`; 필수 미동의 오류는 `aria-invalid` 및 `aria-describedby` 로 연결 (3.3.1, 3.3.2)
- Responsive Considerations: 모바일에서 긴 약관 목록을 접어 둘 때 선택 항목이 접힌 채 동의 상태로 남지 않는지 확인
- Implementation Guidelines: 대체 UX: 선택 항목 기본값 unchecked; 필수 및 선택을 별도 구역으로 나눔; "전체 동의" 는 사용자가 누를 때만 하위 항목을 선택; 서버는 값이 없으면 미동의로 저장
- Common Mistakes: 이전 화면이나 예전 버전에서 기본값을 복사해 옴; 서버 저장 시 기본값이 true; "전체 동의" 상태를 로드 때 계산하면서 켜진 채 시작
- Related Patterns: DP-04, DP-05, FM-05
- Reference Image: `assets/09-dark-patterns-a.png` 및 `assets/09-dark-patterns-b.png`, "[필수] 이용약관 동의" 와 함께 "[선택] 마케팅 수신 동의", "[선택] 제3자 제공 동의" 가 체크된 상태

## DP-03 가짜 마감 시계 (Fake countdown)
- ID: DP-03
- Korean Name: 가짜 마감 시계
- English Name: Fake countdown
- Category: Dark Patterns
- Definition: 실제 마감과 무관하게 줄어드는 시간을 보여주어 서두르게 하는 타이머
- Purpose: 이 패턴을 쓰는 쪽의 의도는 시간 압박으로 비교 및 고민 없이 구매하게 하는 것
- User Problem: 마감이 실제라고 믿고 서둘러 결정하지만 같은 조건이 계속 이어짐
- When to Use: 사용 금지. 탐지 신호: 타이머 시작값이 서버 시각이 아닌 클라이언트 초기화 값 (페이지 로드 때 상수로 설정); 0 이 되면 처음 값으로 다시 시작 (카드: "0이 되면 다시 10:00부터"); 새로고침이나 재방문 때 리셋됨; 서버 응답에 마감 시각 필드가 없음
- When Not to Use: 해당 없음 (항상 금지); 정당한 경우와의 구분: 서버에 저장된 실제 마감 시각 기준 타이머, 마감 뒤 가격이나 혜택이 실제로 바뀌는 행사, 실제 좌석 확보 만료 시간은 정당
- Interaction Behavior: 시간이 줄어드는 표시가 반복되고 끝나도 같은 조건이 유지되거나 다시 시작됨
- Required States: 대체 UX 에서 필요한 상태: 진행 중 (실제 마감까지); 마감됨 (가격이나 혜택 실제 종료); 서버 시각을 못 받음 (타이머 숨김)
- Visual Guidelines: 문제 요소: 붉은색 및 큰 숫자로 긴박감 연출; 대체: 마감 일시를 글로 함께 표기
- Accessibility: 자동으로 움직이는 표시는 멈춤 수단 또는 정적 대체 검토 (WCAG 2.2 2.2.2); 시간 제한이 실제로 있으면 연장 또는 해제 가능성 검토 (2.2.1)
- Responsive Considerations: 기기 시계나 시간대가 달라도 서버 기준 남은 시간이 같게 계산되는지 확인
- Implementation Guidelines: 대체 UX: 서버가 내려준 절대 종료 시각으로 남은 시간 계산; 마감 후 실제로 혜택을 종료하고 표시도 제거; 종료 시각이 없으면 타이머를 만들지 않음
- Common Mistakes: 시연용 고정 시작값이 운영에 남음; 마감 후 서버는 혜택을 계속 주면서 화면 타이머만 리셋; 클라이언트 시계로 계산해 기기마다 다른 값
- Related Patterns: DP-06, DP-09
- Reference Image: `assets/09-dark-patterns-a.png` 및 `assets/09-dark-patterns-b.png`, "특가 종료까지 00:00:03", 설명 "0이 되면 다시 10:00부터"

## DP-04 죄책감 버튼 (Confirmshaming)
- ID: DP-04
- Korean Name: 죄책감 버튼
- English Name: Confirmshaming
- Category: Dark Patterns
- Definition: 거절 선택지 문구를 사용자를 깎아내리거나 손해를 강조하는 말로 써서 수락하게 만드는 방식
- Purpose: 이 패턴을 쓰는 쪽의 의도는 거절을 부끄럽거나 손해로 느끼게 해 수락률을 높이는 것
- User Problem: 거절하려면 스스로를 깎아내리는 문구를 눌러야 하고, 거절 선택지를 찾기도 어려움
- When to Use: 사용 금지. 탐지 신호: 거절 단추 문구가 감정 문구 ("아니요, 할인은 필요 없어요"); 수락은 채워진 강조 단추이고 거절은 작은 글씨나 낮은 대비 링크; 두 선택지의 문구 구조가 비대칭 (수락은 행동 이름, 거절은 자기 비하 문구)
- When Not to Use: 해당 없음 (항상 금지); 정당한 경우와의 구분: "나중에", "닫기", "아니요" 같은 중립 문구는 정당; 되돌리기 어려운 삭제 확인에서 "삭제" 및 "취소" 로 결과를 분명히 쓰는 것도 정당
- Interaction Behavior: 거절 선택지를 눌러야 하는 사용자가 불편한 문구를 읽고 수락으로 기울어짐
- Required States: 대체 UX 에서 필요한 상태: 수락; 거절 (아무 불이익 없이 닫힘); 나중에 다시 보기
- Visual Guidelines: 두 선택지를 같은 크기 및 같은 비중으로 배치; 거절을 회색 작은 글씨로 눌러 두지 않음
- Accessibility: 거절 링크도 글자 대비 4.5:1 (WCAG 2.2 1.4.3), 독립된 링크 또는 단추이면 목표 크기 24x24 CSS px 이상 (2.5.8); 버튼 이름만 읽어도 결과를 알 수 있게
- Responsive Considerations: 좁은 화면에서 거절 선택지가 접히거나 화면 밖으로 밀리지 않는지 확인
- Implementation Guidelines: 대체 UX: 수락은 행동 이름 ("쿠폰 받기"), 거절은 중립 문구 ("닫기" 또는 "나중에") 로 쓰고 두 선택지를 동등하게 배치; 거절 뒤 불이익 없이 화면을 닫음
- Common Mistakes: 마케팅 문구 가이드의 감정 어조를 거절 레이블에 그대로 재사용; 디자인 시스템의 3차 링크 스타일을 거절에 적용해 의도치 않게 눈에 안 띔
- Related Patterns: DP-02, DP-09, FB-04
- Reference Image: `assets/09-dark-patterns-a.png` 및 `assets/09-dark-patterns-b.png`, "할인 쿠폰 받아 가세요", 단추 "쿠폰 받기", 거절 문구 "아니요, 할인은 필요 없어요"

## DP-05 끼워 팔기 (Sneak into basket)
- ID: DP-05
- Korean Name: 끼워 팔기
- English Name: Sneak into basket
- Category: Dark Patterns
- Definition: 사용자가 담지 않은 상품이나 옵션을 장바구니 또는 결제 요약에 자동으로 넣는 방식
- Purpose: 이 패턴을 쓰는 쪽의 의도는 사용자가 알아채지 못한 채 객단가를 높이는 것
- User Problem: 담지 않은 항목의 금액이 합계에 들어 있어도 못 보고 결제함
- When to Use: 사용 금지. 탐지 신호: 사용자가 누르지 않은 항목이 장바구니 또는 결제 요약에 자동 추가; 부가 상품 선택이 기본 선택값; 합계가 사용자가 담은 항목의 합과 다름; 부가 항목 제거 수단이 작거나 없음
- When Not to Use: 해당 없음 (항상 금지); 정당한 경우와의 구분: 사용자가 "추가" 단추를 눌러 넣은 옵션, 상품에 반드시 따라오는 구성품을 담는 시점에 필수임 및 사유를 표시한 경우는 정당
- Interaction Behavior: 사용자가 결제 단계에 들어서면 이미 부가 항목이 들어 있고 지우려면 따로 찾아야 함
- Required States: 대체 UX 에서 필요한 상태: 추천 상품 미선택; 사용자가 추가함; 사용자가 제거함; 합계 갱신
- Visual Guidelines: 장바구니에는 사용자가 담은 항목만 두고 추천은 별도 영역에 표시; 항목마다 이름 및 금액을 같은 서식으로
- Accessibility: 항목 삭제 단추에 항목 이름 포함 (`aria-label`); 합계 변경은 `role="status"` 로 알림 (WCAG 2.2 4.1.3)
- Responsive Considerations: 모바일 결제 요약이 접혀 있을 때 접힌 영역에 추가 항목이 숨지 않는지 확인
- Implementation Guidelines: 대체 UX: 추천은 "추가" 단추로 사용자가 직접 담게 하고 기본 미선택; 결제 요약에 항목별 금액 및 합계를 표시; 제거는 한 번의 동작으로
- Common Mistakes: 이전 주문의 옵션을 기본값으로 복원함; 실험용 기본 추가 설정이 배포 뒤 남음; 결제 직전 단계에서 항목을 덧붙임
- Related Patterns: DP-07, DP-02, DP-06
- Reference Image: `assets/09-dark-patterns-a.png`, 장바구니 "여행 가방 19,000원" 아래에 "+ 파손 보험 9,900원" 이 추가된 장면

## DP-06 가짜 희소성 (Fake scarcity)
- ID: DP-06
- Korean Name: 가짜 희소성
- English Name: Fake scarcity
- Category: Dark Patterns
- Definition: 실제 재고나 수량과 무관한 "남은 수량" 문구를 보여주어 서두르게 하는 방식
- Purpose: 이 패턴을 쓰는 쪽의 의도는 수량 압박으로 구매를 앞당기는 것
- User Problem: 곧 없어진다고 믿고 서둘러 결정하지만 수량이 실제로 줄지 않음
- When to Use: 사용 금지. 탐지 신호: 재고 문구가 하드코딩 ("남은 자리 2석!" 문자열이 소스에 있음); 수량이 새로고침해도 같거나 난수로 만들어짐; 수량을 재고 API 가 아닌 클라이언트 상수나 랜덤 함수에서 가져옴; 재고가 0 이어도 문구가 유지됨
- When Not to Use: 해당 없음 (항상 금지); 정당한 경우와의 구분: 서버의 실제 재고 수량을 표시하는 것, 실제로 한정 수량으로 운영되는 행사는 정당
- Interaction Behavior: 새로고침하거나 오래 머물러도 같은 수량 문구가 유지되어 압박만 남김 (카드: "새로고침해도 계속 2석")
- Required States: 대체 UX 에서 필요한 상태: 재고 충분 (문구 없음); 실제 재고 적음 (서버 값 표시); 품절 (구매 불가 표시)
- Visual Guidelines: 문제 요소: 붉은색, 느낌표로 긴박감 연출; 대체: 수량은 서버 값 및 기준 시각을 중립 서식으로
- Accessibility: 수량 변화는 `role="status"` 로 알리되 계속 바뀌면 과다 알림을 피함 (WCAG 2.2 4.1.3); 색만으로 긴박함을 전달하지 않음 (1.4.1)
- Responsive Considerations: 캐시된 목록 및 상세에서 서로 다른 수량이 보이지 않는지 확인
- Implementation Guidelines: 대체 UX: 서버 재고 값만 표시하고 값이 없으면 문구를 표시하지 않음; 재고 0 이면 품절 상태로 전환; 기준 시각을 알 수 없으면 수량 문구를 쓰지 않음
- Common Mistakes: 개발용 샘플 값이 운영에 남음; 오래된 캐시 값을 최신처럼 표시; 전체 재고와 사용자별 확보 수량을 혼동
- Related Patterns: DP-03, DP-09, DP-07
- Reference Image: `assets/09-dark-patterns-a.png` 및 `assets/09-dark-patterns-b.png`, "제주 한정 특가", "남은 자리 2석!", 설명 "새로고침해도 계속 2석"

## DP-07 숨은 비용 (Hidden costs)
- ID: DP-07
- Korean Name: 숨은 비용
- English Name: Hidden costs
- Category: Dark Patterns
- Definition: 결제 마지막 단계에서야 수수료나 부대 비용을 더해 보여주는 방식
- Purpose: 이 패턴을 쓰는 쪽의 의도는 낮은 가격으로 끌어들인 뒤 이탈하기 어려운 시점에 비용을 올리는 것
- User Problem: 처음 본 가격과 최종 결제 금액이 달라 비교 및 판단이 어긋남
- When to Use: 사용 금지. 탐지 신호: 상품 금액과 결제 금액의 차이를 설명하는 항목이 결제 마지막 단계에서 처음 나옴; 목록 및 상세 가격 표시에 필수 수수료가 빠져 있음; 수수료가 작은 글씨나 낮은 대비; 요약 합계에 없던 항목이 결제 단추 직전에 추가됨
- When Not to Use: 해당 없음 (항상 금지); 정당한 경우와의 구분: 세금 및 배송비를 초반부터 추정치임을 밝히고 표시하는 것, 선택 옵션 비용을 선택 즉시 합계에 반영하는 것, 결제 직전 최종 확인에서 항목별 명세를 다시 보여주는 것은 정당
- Interaction Behavior: 결제 단계가 진행될수록 금액이 늘어나고 처음 가격으로 돌아가기 어려움 (카드: 19,000원에서 23,500원)
- Required States: 대체 UX 에서 필요한 상태: 가격 표시 (필수 비용 포함 또는 근처 표기); 조건부 비용 계산 중; 결제 요약 (항목별 금액 및 합계)
- Visual Guidelines: 필수 비용은 상품 금액과 같은 서식으로 항목별 표시; 합계는 항목 합과 일치
- Accessibility: 결제 요약 표는 항목 이름 및 금액을 읽을 수 있는 구조; 금액 변경은 `role="status"`; 금융 거래는 제출 전 확인 가능해야 함 (WCAG 2.2 3.3.4)
- Responsive Considerations: 모바일에서 결제 요약이 접혀 있어도 최종 금액에 포함된 항목이 보이는지 확인
- Implementation Guidelines: 대체 UX: 가격이 처음 보이는 화면부터 필수 비용을 포함하거나 바로 옆에 표기; 조건에 따라 정해지는 비용은 계산 시점 및 조건을 표기; 결제 요약은 항목별 금액 및 합계
- Common Mistakes: 가격 API 가 수수료 제외 값을 반환해 화면이 그대로 표기함; 수수료가 결제 단계 서버에서만 계산되어 앞 화면에서 보이지 않음
- Related Patterns: DP-05, DP-08, LD-03
- Reference Image: `assets/09-dark-patterns-a.png` 및 `assets/09-dark-patterns-b.png`, "상품 금액 19,000원", "서비스 수수료 +4,500원", "결제 금액 23,500원"

## DP-08 몰래 자동 결제 (Forced continuity)
- ID: DP-08
- Korean Name: 몰래 자동 결제
- English Name: Forced continuity
- Category: Dark Patterns
- Definition: 무료 체험이 끝나면 유료로 자동 전환되는 조건을 눈에 띄지 않게 해 두는 방식
- Purpose: 이 패턴을 쓰는 쪽의 의도는 체험 종료를 잊거나 모르는 사용자에게 과금을 이어가는 것
- User Problem: 체험이 끝나는 날 및 자동 결제 금액을 모른 채 과금됨
- When to Use: 사용 금지. 탐지 신호: 체험 시작 화면에서 자동 결제 조건이 작은 글씨나 접힌 영역에만 있음; 결제 수단 등록을 요구하면서 체험 종료일 및 금액을 표기하지 않음; 체험 종료 전 알림이 없음; 해지 경로가 DP-01 처럼 어려움
- When Not to Use: 해당 없음 (항상 금지); 정당한 경우와의 구분: 체험 후 유료 전환 조건을 시작 단추 근처에 같은 크기 글자로 밝히고 사용자가 동의하며 종료 전 알림을 보내는 구독은 정당
- Interaction Behavior: 사용자가 단추 한 번으로 시작하고 자동 결제 조건은 작은 글씨 한 줄로만 지나감
- Required States: 대체 UX 에서 필요한 상태: 체험 시작 전 조건 확인; 체험 중 (종료일 표시); 종료 전 알림; 유료 전환; 체험 중 해지
- Visual Guidelines: 자동 결제 조건 문구를 시작 단추 바로 근처에 본문과 같은 크기로 배치
- Accessibility: 조건 문구도 글자 대비 4.5:1 (WCAG 2.2 1.4.3); 조건을 접어 두면 펼침 단추에 `aria-expanded`; 금융 거래는 제출 전 확인 가능 (3.3.4)
- Responsive Considerations: 모바일에서 시작 단추 근처 조건 문구가 화면 아래로 밀려 스크롤 전에 안 보이는지 확인
- Implementation Guidelines: 대체 UX: 단추 근처에 "체험 종료일에 월 N원이 결제돼요" 형태로 실제 일자 및 금액 표기; 종료 전 알림 발송; 체험 중에도 바로 해지 가능; 결제 수단 등록이 필요한 이유 설명
- Common Mistakes: 조건을 약관 링크 안에만 둠; 알림 발송 작업이 실패해도 모니터링이 없음; 체험 종료일 계산 오류
- Related Patterns: DP-01, DP-07, DP-02
- Reference Image: `assets/09-dark-patterns-a.png` 및 `assets/09-dark-patterns-b.png`, "7일 무료 체험", 단추 "무료로 시작하기", 작은 글씨 "체험 후 월 9,900원 자동 결제"

## DP-09 끝없는 권유 (Nagging)
- ID: DP-09
- Korean Name: 끝없는 권유
- English Name: Nagging
- Category: Dark Patterns
- Definition: 사용자가 거절한 요청을 계속 다시 띄우는 방식
- Purpose: 이 패턴을 쓰는 쪽의 의도는 반복 노출로 지쳐서 수락하게 만드는 것
- User Problem: 한 번 거절해도 계속 방해받고, 거절이 존중되지 않는다고 느낌
- When to Use: 사용 금지. 탐지 신호: 거절 뒤 재방문이나 앱 재시작 때마다 같은 대화 상자 표시; 거절 기록을 저장하지 않거나 세션 변수에만 저장; "나중에" 만 있고 거절을 기억하는 선택이 없음; 표시 횟수가 늘어남 (카드: "3번째")
- When Not to Use: 해당 없음 (항상 금지); 정당한 경우와의 구분: 사용자가 해당 기능을 직접 쓰려 할 때 한 번 안내하는 것 (ES-05) 은 정당하며, 거절 기록을 저장한 뒤에는 사용자가 그 기능을 다시 시도할 때만 안내
- Interaction Behavior: 사용자가 "나중에" 를 눌러도 다음 방문에서 같은 요청이 다시 뜸
- Required States: 대체 UX 에서 필요한 상태: 요청 전; 거절됨 (기록 저장, 자동 재요청 없음); 허용됨; 설정에서 다시 켜기
- Visual Guidelines: 요청 대화 상자는 거절 선택지를 수락과 동등하게 표시하고 닫기 경로를 분명히 둠
- Accessibility: 대화 상자는 `role="dialog"` 및 `aria-modal="true"`, 초점 가두기, Esc 닫기, 닫은 뒤 초점 복귀; 반복 팝업이 키보드 사용자의 흐름을 끊지 않는지 확인 (WCAG 2.2 2.4.3)
- Responsive Considerations: 모바일에서 전면 팝업이 화면 전체를 가려 본 기능을 막지 않는지 확인
- Implementation Guidelines: 대체 UX: 거절 상태를 기기 또는 계정에 저장; 거절 뒤 같은 요청을 자동으로 반복하지 않음; 사용자가 해당 기능을 직접 쓰려 할 때만 한 번 안내; 설정 화면에 켜는 경로를 둠
- Common Mistakes: 거절 상태를 세션 변수에만 저장해 앱 재시작마다 초기화됨; 로그인 때마다 환영 단계에 요청을 끼워 넣음; 같은 권한 요청을 여러 화면에 중복 배치
- Related Patterns: ES-05, DP-04, FB-04
- Reference Image: `assets/09-dark-patterns-b.png`, "3번째" 표시, 대화 상자 "알림을 켜시겠어요?", 단추 "나중에" 및 "켜기"

## 검수 절차
- 가입: 선택 항목 checkbox 의 초기값이 unchecked 인지, 가입에 필요 없는 정보를 필수로 요구하지 않는지 확인 (DP-02)
- 동의: 필수 및 선택이 문구로 구분되는지, "전체 동의" 가 로드 때 켜져 있지 않은지, 거절 문구가 중립인지 확인 (DP-02, DP-04)
- 결제: 처음 가격 표시부터 최종 결제 금액까지 항목이 일치하는지, 결제 직전에 새 항목이 붙지 않는지 확인 (DP-07)
- 장바구니: 사용자가 담지 않은 항목이 없는지, 재고 문구 및 타이머의 값이 서버 값에서 오는지 소스에서 확인 (DP-05, DP-06, DP-03)
- 해지: 가입 단계 수와 해지 단계 수를 비교하고, 같은 채널에서 끝낼 수 있는지 확인 (DP-01)
- 체험 및 구독: 자동 결제 조건이 시작 단추 근처에 같은 크기로 있고 종료 전 알림이 있는지 확인 (DP-08)
- 알림 권유: 거절한 뒤 재방문 및 앱 재시작에서 같은 요청이 다시 뜨는지 확인 (DP-09)
- 확인 방법: 소스에서 하드코딩 문구와 초기값을 검색하고, 새로고침 및 재방문 동작을 실제 계정으로 처음부터 끝까지 실행해 확인
