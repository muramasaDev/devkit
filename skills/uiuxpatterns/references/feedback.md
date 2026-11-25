# Feedback & Notifications (알림과 피드백)

- 범위: 사용자 행동의 결과, 상태 변화, 주의가 필요한 내용을 알리는 메시지 및 안내 패턴 9종
- 참조 이미지: `assets/01-feedback.png`
- 색인: `pattern-catalog.md`

## 유사 패턴 구분

| 헷갈리는 쌍 | 고르는 기준 |
|---|---|
| 토스트(FB-01) 대 스낵바(FB-02) | 사용자가 눌러야 할 행동 단추가 있으면 스낵바(되돌리기 등), 알리기만 하고 행동이 없으면 토스트 |
| 배너(FB-03) 대 토스트(FB-01) | 화면에 머무는 동안 계속 보여야 하고 사용자가 닫기 전까지 남아야 하면 배너, 잠깐 보였다 스스로 사라져도 되면 토스트 |
| 모달(FB-04) 대 바텀시트(FB-05) | 진행 전에 반드시 결정을 받아야 하고 나머지 화면을 막아야 하면 모달, 관련 동작 목록 중 하나를 고르게 하는 가벼운 선택이면 바텀시트 |
| 툴팁(FB-07) 대 코치마크(FB-08) | 항목 하나에 대한 보충 설명을 사용자가 요청할 때(가리키거나 초점) 보이면 툴팁, 처음 쓰는 사용자에게 화면 요소 하나를 강조해 먼저 안내하면 코치마크 |
| 인라인 오류(FB-06) 대 토스트(FB-01) | 오류가 특정 입력 필드에 속하면 그 필드 옆에 인라인 오류, 특정 필드가 없는 일시적 알림이면 토스트 |
| 뱃지(FB-09) 대 배너(FB-03) | 아이콘 옆에 개수 또는 새 항목 유무만 표시하면 뱃지, 문장으로 사정을 설명해야 하면 배너 |

## FB-01 토스트 (Toast)
- ID: FB-01
- Korean Name: 토스트
- English Name: Toast
- Category: Feedback & Notifications
- Definition: 방금 한 동작의 결과를 짧은 문구로 알리고 스스로 사라지는 비차단 메시지; 행동 단추 없음
- Purpose: 흐름을 끊지 않고 동작이 처리됐음을 확인시킴
- User Problem: 저장 또는 복사처럼 화면 변화가 작은 동작 뒤에 성공했는지 알기 어려움
- When to Use: 되돌릴 필요가 없는 가벼운 성공 확인; 사용자가 같은 화면에 계속 머무는 흐름; 놓쳐도 다른 조치가 필요하지 않은 안내
- When Not to Use: 되돌리기 같은 행동이 필요하면 FB-02; 계속 보여야 하는 사정은 FB-03; 필드 입력 오류는 FB-06; 결정을 받아야 하면 FB-04
- Interaction Behavior: 동작 직후 나타나 일정 시간 뒤 스스로 사라짐; 표시 시간은 제품에서 정한다; 한 번에 하나만 보이고 새 메시지는 이전 것을 대체
- Required States: 표시 중; 사라짐; 대체됨; 성공 및 실패 구분(아이콘 및 문구로 구분, 색만으로 구분 금지, WCAG 1.4.1)
- Visual Guidelines: 어두운 알약 모양 안에 짧은 문구 한 줄(이미지 카드 장면); 글자 대비 4.5:1 이상(WCAG 1.4.3); 하단 탭바 및 입력 단추를 가리지 않는 위치
- Accessibility: `role="status"`(aria-live polite)로 읽힘; 사라지기 전에 읽을 시간이 부족할 수 있으므로 시간 조절 고려(WCAG 2.2.1); 중요한 정보는 토스트에만 두지 않음
- Responsive Considerations: 좁은 화면에서 줄바꿈으로 폭 안에 수용; 소프트 키보드 및 하단 탐색에 가리지 않게 위치 조정
- Implementation Guidelines: 알림 영역(live region)을 먼저 화면에 두고 내용만 바꿔야 읽힘; 타이머는 닫힐 때 반드시 정리; 연속 호출은 대체 또는 대기열 중 하나로 일관되게 처리
- Common Mistakes: 행동 단추를 넣고 짧은 시간 안에 누르게 함; 중요한 오류를 토스트로만 알림; 화면 이동 시 사라져 읽지 못함
- Related Patterns: FB-02, FB-03, FB-06
- Reference Image: `assets/01-feedback.png` 카드 장면: "저장하기" 단추 아래 어두운 알약 모양 메시지 "찜 목록에 저장했어요"

## FB-02 스낵바 (Snackbar)
- ID: FB-02
- Korean Name: 스낵바
- English Name: Snackbar
- Category: Feedback & Notifications
- Definition: 동작 결과를 알리면서 짧은 행동 단추(되돌리기 등)를 함께 주는 화면 하단 막대 메시지
- Purpose: 실수로 한 동작을 곧바로 되돌릴 기회를 줌
- User Problem: 삭제 같은 동작이 되돌릴 수 없어 보여 확인 대화 상자가 반복됨
- When to Use: 삭제 또는 이동처럼 되돌릴 수 있는 동작 직후; 행동 하나만 제안할 때
- When Not to Use: 알리기만 하면 FB-01; 되돌릴 수 없는 파괴적 동작은 사전 확인 FB-04; 행동이 둘 이상이면 FB-05
- Interaction Behavior: 동작 직후 하단에 나타나 일정 시간 뒤 사라짐; 표시 시간은 제품에서 정한다; 행동 단추를 누르면 동작을 취소하고 막대가 닫힘
- Required States: 표시 중; 행동 실행됨(되돌림 완료 안내); 시간 초과로 사라짐(삭제 확정); 연속 발생 시 대체
- Visual Guidelines: 어두운 막대, 왼쪽 문구, 오른쪽 행동 단추("되돌리기"); 문구 4.5:1(WCAG 1.4.3); 행동 단추 터치 목표 44x44pt(Apple HIG) 또는 48x48dp(Material Design)
- Accessibility: `role="status"`; 행동 단추는 키보드로 도달해야 함(WCAG 2.1.1); 사라지는 시간이 짧으면 키보드 사용자가 놓침, 시간 조절 필요(WCAG 2.2.1); 단축 수단으로 화면 안 다른 되돌리기 경로도 제공
- Responsive Considerations: 좁은 화면에서는 폭 전체, 넓은 화면에서는 모서리에 붙여 폭 제한; 하단 탐색 위에 배치
- Implementation Guidelines: 되돌리기 전에는 실제 삭제를 미루고 시간이 지나면 확정하는 구조; 사라지는 중에도 행동 단추가 눌릴 수 있게 타이머 정리; 키보드 초점은 호출한 단추 근처에 유지
- Common Mistakes: 행동 단추가 없는데 스낵바로 둠(이 스킬의 구분 규칙: 행동이 없으면 토스트. 디자인 시스템에 따라 스낵바의 행동 단추를 선택 사항으로 두기도 하므로 프로젝트의 이름 규칙을 따름); 되돌릴 시간이 너무 짧음; 되돌리기를 눌러도 실제로 복구되지 않음
- Related Patterns: FB-01, FB-04, FB-05
- Reference Image: `assets/01-feedback.png` 카드 장면: 화면 아래 어두운 막대 "일정을 삭제했어요" 및 행동 "되돌리기"

## FB-03 배너 (Banner)
- ID: FB-03
- Korean Name: 배너
- English Name: Banner
- Category: Feedback & Notifications
- Definition: 화면 위쪽 문서 흐름 안에 표시되어 상태 또는 공지를 알리고 사용자가 닫을 때까지 남는 띠 형태 메시지
- Purpose: 현재 화면 전체에 해당하는 사정을 지속적으로 알림
- User Problem: 마감, 점검, 연결 상태 같은 정보를 놓치면 불이익이 생기는데 일회성 메시지는 금방 사라짐
- When to Use: 화면 전체에 적용되는 상태(마감 임박, 점검 예정, 오프라인); 사용자가 닫거나 해결할 때까지 필요한 안내
- When Not to Use: 동작 결과 확인은 FB-01; 개수만 알리면 FB-09; 결정을 받아야 하면 FB-04; 필드에 속한 오류는 FB-06
- Interaction Behavior: 화면 진입 또는 상태 변화 시 위쪽에 나타남; 닫기(X)로 닫음; 닫아도 되는 정보는 닫으면 같은 화면에서 다시 뜨지 않음; 해결되면 스스로 사라짐
- Required States: 표시 중; 닫힘; 해결되어 제거됨; 심각도 구분(정보, 경고, 오류는 아이콘 및 문구로 구분, WCAG 1.4.1)
- Visual Guidelines: 화면 위 띠, 정보는 파란 계열(이미지 카드 장면); 문구 4.5:1(WCAG 1.4.3); 닫기 단추 터치 목표 44x44pt(Apple HIG) 또는 48x48dp(Material Design)
- Accessibility: 일반 정보는 `role="status"`, 즉시 알려야 하는 오류는 `role="alert"`; 닫기 단추는 `aria-label`로 이름 제공; 닫기 단추 초점이 완전히 가려지지 않음(WCAG 2.4.11)
- Responsive Considerations: 좁은 화면에서 문구가 길면 줄바꿈 또는 말줄임 후 상세 링크; 위쪽 고정 헤더와 겹치지 않게 쌓는 순서 정함
- Implementation Guidelines: 문서 흐름 안에 넣어 아래 콘텐츠를 밀어 내림(고정 위치로 가리지 않음); 닫힘 상태 저장 범위(세션 또는 영구)를 정함; 한 화면에 여러 개를 쌓지 않음
- Common Mistakes: 닫기 단추가 없어 항상 남음; 자동으로 사라지게 해서 놓침; 여러 배너가 쌓여 본문이 밀림
- Related Patterns: FB-01, FB-09, ES-04
- Reference Image: `assets/01-feedback.png` 카드 장면: 화면 위 파란 정보 띠 "쿠폰 마감이 3일 남았어요" 및 닫기(X)

## FB-04 모달 (Modal dialog)
- ID: FB-04
- Korean Name: 모달
- English Name: Modal dialog
- Category: Feedback & Notifications
- Definition: 나머지 화면을 막고 사용자의 결정 또는 확인을 받아야 진행되는 대화 상자
- Purpose: 되돌리기 어렵거나 중요한 결정 앞에서 사용자의 주의를 모음
- User Problem: 비용 발생 또는 삭제 같은 동작이 의도 없이 실행될 수 있음
- When to Use: 결제 또는 영구 삭제처럼 되돌리기 어려운 동작의 확인; 진행 전 필수 정보 한 가지를 받아야 할 때
- When Not to Use: 단순 안내는 FB-01 또는 FB-03; 되돌릴 수 있는 동작은 실행 후 FB-02; 항목 선택 목록은 FB-05; 긴 입력은 별도 화면
- Interaction Behavior: 열리면 뒤 화면이 어두워지고 조작 불가; 초점이 대화 상자 안에 갇힘; Esc 및 닫기 단추로 닫음; 닫으면 연 단추로 초점이 돌아감
- Required States: 열림; 처리 중(확정 단추 중복 누름 방지); 닫힘; 확정 및 취소 단추는 말로 구분(예: "취소" 및 "결제")
- Visual Guidelines: 제목, 보조 문구, 취소 및 확정 단추 두 개(이미지 카드 장면); 파괴적 확정 단추는 색 및 문구로 구분(WCAG 1.4.1); 단추 문구는 동사로 구체적으로
- Accessibility: `role="dialog"` 및 `aria-modal="true"`; 열릴 때 안으로 초점 이동, 닫을 때 호출한 요소로 복귀; 초점 가두기; Esc 닫기; 키보드 함정 아님(WCAG 2.1.2)
- Responsive Considerations: 좁은 화면에서는 폭을 줄여 가운데 유지 또는 아래 시트 형태로 바꾸되 같은 역할 유지; 내용이 길면 대화 상자 안에서만 스크롤
- Implementation Guidelines: `<dialog>`의 `showModal()` 사용 가능(브라우저 지원 확인); 뒤 화면은 `inert` 처리; 열 때 스크롤 잠금; 중첩 모달 금지
- Common Mistakes: 가벼운 안내에도 모달을 씀; 취소 및 확정 위치 및 문구가 모호함; 초점이 안 가둬져 뒤 화면 조작됨; 배경 클릭 닫기를 막지도 허용하지도 않고 방치
- Related Patterns: FB-02, FB-05, DP-09
- Reference Image: `assets/01-feedback.png` 카드 장면: 어두운 배경 위 대화 상자 "결제할까요?", 보조 문구 "결제 후엔 취소 수수료가 있어요", 단추 "취소" 및 "결제"

## FB-05 바텀시트 (Bottom sheet)
- ID: FB-05
- Korean Name: 바텀시트
- English Name: Bottom sheet
- Category: Feedback & Notifications
- Definition: 화면 아래에서 올라와 관련 동작 또는 선택지를 보여주는 패널
- Purpose: 한 손 조작 영역에서 동작 목록을 고르게 함
- User Problem: 항목마다 단추를 모두 두면 화면이 복잡하고, 전체 화면 전환은 과함
- When to Use: 항목에 대한 동작 여러 개(공유, 이름 바꾸기, 삭제); 비교적 짧은 선택 목록; 모바일 화면
- When Not to Use: 반드시 결정을 받아야 하는 확인은 FB-04; 알리기만 하면 FB-01; 긴 입력 및 복잡한 흐름은 별도 화면
- Interaction Behavior: 호출하면 아래에서 올라옴; 항목을 누르면 실행하고 닫힘; 손잡이 드래그, 바깥 누르기, 닫기 단추로 닫음; 드래그에는 단일 포인터 대안 제공(WCAG 2.5.7)
- Required States: 닫힘; 열림; 항목 눌림; 파괴적 항목 구분(빨강은 문구로도 구분, WCAG 1.4.1); 처리 중
- Visual Guidelines: 위쪽에 손잡이, 항목 목록, 삭제 같은 파괴적 항목은 빨강(이미지 카드 장면); 항목 터치 목표 44x44pt(Apple HIG) 또는 48x48dp(Material Design)
- Accessibility: 모달형이면 `role="dialog"` 및 `aria-modal="true"`, 초점 가두기, Esc 닫기, 닫은 뒤 초점 복귀; 손잡이 드래그만으로 닫는 경로 금지, 닫기 단추 제공(WCAG 2.5.7)
- Responsive Considerations: 넓은 화면에서는 작은 팝오버 또는 대화 상자 형태로 대체; 키보드가 올라와도 항목이 가려지지 않게 높이 제한
- Implementation Guidelines: 열려 있는 동안 뒤 화면 `inert`; 높이는 내용에 맞추되 화면 높이의 상한을 둠; 닫힘 애니메이션에서 `prefers-reduced-motion` 존중
- Common Mistakes: 제스처로만 닫을 수 있음; 목록이 길어 시트가 거의 전체 화면을 덮음; 파괴적 항목을 첫 위치에 둠
- Related Patterns: FB-04, IC-02, GS-02
- Reference Image: `assets/01-feedback.png` 카드 장면: 아래에서 올라온 시트, 손잡이, 항목 "공유하기", "이름 바꾸기", "삭제하기"(빨강)

## FB-06 인라인 오류 (Inline error)
- ID: FB-06
- Korean Name: 인라인 오류
- English Name: Inline error
- Category: Feedback & Notifications
- Definition: 오류가 난 입력 필드 바로 옆 또는 아래에 오류 원인과 해결 방법을 보이는 문구
- Purpose: 어느 필드가 왜 틀렸는지 그 자리에서 알림
- User Problem: 화면 위나 토스트의 일반 오류는 어느 필드인지 알려주지 못함
- When to Use: 입력 형식 오류, 필수 누락 등 특정 필드에 속한 오류; 제출 후 또는 필드를 벗어날 때
- When Not to Use: 특정 필드가 없는 일시 알림은 FB-01; 화면 전체 상태는 FB-03; 서버 장애 화면은 ES-08
- Interaction Behavior: 오류가 확인되는 시점에 필드 아래에 문구가 나타남; 고쳐서 유효해지면 사라짐; 제출 후 첫 오류 필드로 초점 이동 가능
- Required States: 오류 없음; 오류(빨간 테두리 및 문구); 수정 중; 해결됨; 여러 오류일 때 모두 표시
- Visual Guidelines: 빨간 테두리 및 필드 아래 문구(이미지 카드 장면); 빨강만으로 알리지 않고 아이콘 또는 문구 병행(WCAG 1.4.1); 문구 4.5:1(WCAG 1.4.3), 테두리 3:1(WCAG 1.4.11)
- Accessibility: 필드에 `aria-invalid="true"` 및 오류 문구를 `aria-describedby`로 연결; 오류 식별(WCAG 3.3.1) 및 수정 제안(WCAG 3.3.3); 즉시 알릴 오류는 `role="alert"`; 레이블 유지(WCAG 3.3.2)
- Responsive Considerations: 좁은 화면에서 문구가 필드 폭 안에서 줄바꿈; 오류 문구 때문에 아래 단추가 밀려도 겹치지 않음
- Implementation Guidelines: 입력 도중 타이핑마다 오류를 띄우지 않고 필드를 벗어날 때 또는 제출 때 검증; 오류 문구에 원인 및 해결법 포함; 법적 및 금융 거래는 제출 전 확인 단계(WCAG 3.3.4)
- Common Mistakes: "오류가 발생했습니다"처럼 원인이 없는 문구; 필드 위 토스트로만 알림; 오류 상태가 색만으로 구분됨
- Related Patterns: FB-01, FM-01, ES-08
- Reference Image: `assets/01-feedback.png` 카드 장면: 이메일 필드(값 "woody@mail") 빨간 테두리, 아래 문구 "이메일 형식을 확인해 주세요"

## FB-07 툴팁 (Tooltip)
- ID: FB-07
- Korean Name: 툴팁
- English Name: Tooltip
- Category: Feedback & Notifications
- Definition: 요소에 가리키거나 초점이 갈 때 나타나는 짧은 보충 설명 말풍선
- Purpose: 아이콘 또는 용어의 의미를 필요한 사람에게만 보충
- User Problem: 용어 뜻이나 아이콘 의미를 모르는데 화면에 설명을 늘 두면 복잡해짐
- When to Use: 용어 또는 아이콘 하나에 대한 한두 문장 보충; 없어도 핵심 작업이 가능한 부가 정보
- When Not to Use: 처음 쓰는 사용자 안내는 FB-08; 필수 정보 및 오류는 화면에 직접 표시; 터치 전용 화면의 유일한 설명 수단으로 사용 금지; 긴 설명은 별도 안내
- Interaction Behavior: 가리키거나 초점이 오면 나타남; 가리킨 채로 말풍선 위로 이동해도 유지됨; 벗어나면 닫힘; Esc로 닫음
- Required States: 숨김; 표시(hover 또는 focus); 닫힘; 터치 환경 대안(누르면 열림)
- Visual Guidelines: 정보 아이콘 위의 작은 말풍선(이미지 카드 장면); 문구 4.5:1(WCAG 1.4.3); 대상 요소를 가리지 않는 위치; 화면 가장자리에서 잘리지 않게 자동 반전
- Accessibility: `role="tooltip"` 및 `aria-describedby`로 대상과 연결; hover 또는 focus로 뜬 내용은 닫을 수 있고 가리킬 수 있고 유지돼야 함(WCAG 1.4.13); 키보드 초점으로도 열림(WCAG 2.1.1)
- Responsive Considerations: 터치 화면은 hover가 없으므로 정보 아이콘을 누르면 열리는 방식 제공; 대상 목표 크기 24x24 CSS px 이상(WCAG 2.5.8)
- Implementation Guidelines: 대상은 초점을 받을 수 있는 `<button>` 등으로 하고 `aria-label` 제공; 위치는 뷰포트 기준으로 계산해 잘림 방지; 말풍선 안에 링크 및 단추를 넣지 않음
- Common Mistakes: hover에서만 열려 키보드 사용자가 못 봄; 마우스를 말풍선으로 옮기면 사라짐; 필수 설명을 툴팁에 숨김
- Related Patterns: FB-08, IC-04, FM-01
- Reference Image: `assets/01-feedback.png` 카드 장면: "이번 달 저축률" 옆 정보 아이콘 위 말풍선 "최근 3개월 지출 기준이에요"

## FB-08 코치마크 (Coach mark)
- ID: FB-08
- Korean Name: 코치마크
- English Name: Coach mark
- Category: Feedback & Notifications
- Definition: 어두운 덮개 위에 화면 요소 하나를 강조하고 사용법을 안내하는 첫 사용 안내
- Purpose: 새 기능 또는 핵심 단추의 위치 및 역할을 처음 한 번 알림
- User Problem: 처음 쓰는 사용자가 핵심 단추를 발견하지 못함
- When to Use: 처음 방문 시 핵심 동작 한두 개를 알려야 할 때; 새로 추가된 기능 안내
- When Not to Use: 항상 필요한 설명은 화면에 직접 표시; 요소 하나에 대한 부가 설명은 FB-07; 반복 노출되는 권유는 DP-09 로 변질되므로 금지
- Interaction Behavior: 처음 진입 시 덮개 및 강조가 나타남; "알겠어요" 또는 닫기로 종료; 다시 보지 않게 기록; 건너뛰기 가능
- Required States: 미표시; 표시 중; 확인 후 종료; 이미 본 상태(재노출 안 함); 여러 단계면 현재 위치 표시
- Visual Guidelines: 어두운 덮개, 강조된 요소 하나(+ 단추), 안내 문구 및 확인 단추(이미지 카드 장면); 안내 문구 4.5:1(WCAG 1.4.3); 강조 요소를 가리지 않음
- Accessibility: 덮개 중에는 `role="dialog"` 및 `aria-modal="true"`, 초점 가두기, Esc 닫기; 안내를 건너뛸 수 있어야 하며 키보드로 확인 단추에 도달(WCAG 2.1.1); 닫은 뒤 초점 복귀
- Responsive Considerations: 화면 크기에 따라 강조 요소 위치가 바뀌므로 위치를 요소에서 계산; 요소가 화면 밖이면 스크롤하거나 안내 생략
- Implementation Guidelines: 이미 본 여부를 저장(사용자 단위가 이상적)하고 로드 시 확인; 대상 요소가 없으면 코치마크를 띄우지 않음; 덮개 뒤 화면은 `inert`
- Common Mistakes: 매번 다시 나옴; 한 번에 여러 개를 연속 노출; 건너뛰기가 없어 사용자를 가둠
- Related Patterns: FB-07, FB-04, ES-01
- Reference Image: `assets/01-feedback.png` 카드 장면: 어두운 덮개 위에 + 단추만 강조, 문구 "여기서 계좌를 연결해요", 단추 "알겠어요"

## FB-09 뱃지 (Badge)
- ID: FB-09
- Korean Name: 뱃지
- English Name: Badge
- Category: Feedback & Notifications
- Definition: 아이콘 모서리에 숫자 또는 점으로 새 항목 유무 및 개수를 표시하는 작은 표식
- Purpose: 확인하지 않은 새 항목이 있음을 한눈에 알림
- User Problem: 알림이나 메시지가 쌓였는지 열어 보지 않으면 알 수 없음
- When to Use: 읽지 않은 알림, 메시지 등 개수가 의미 있을 때(숫자); 새 항목 유무만 알리면 될 때(점)
- When Not to Use: 사정을 문장으로 설명해야 하면 FB-03; 동작 결과 확인은 FB-01; 계속 변하는 수치 전체를 표시하는 용도 금지
- Interaction Behavior: 새 항목이 생기면 나타나고 개수가 갱신됨; 해당 목록을 열어 확인하면 사라지거나 줄어듦; 뱃지 자체는 동작을 갖지 않고 부모 아이콘 단추가 동작
- Required States: 없음; 점; 숫자; 큰 숫자 처리(상한 표기 방식은 제품에서 정한다); 확인 후 해제
- Visual Guidelines: 종 아이콘에 숫자 3, 말풍선 아이콘에 빨간 점(이미지 카드 장면); 숫자 4.5:1(WCAG 1.4.3), 뱃지 및 배경의 구분 3:1(WCAG 1.4.11); 색만으로 의미를 전하지 않음(WCAG 1.4.1)
- Accessibility: 뱃지 값을 부모 단추의 이름에 포함(예: "알림, 새 알림 3개"); 값이 바뀌면 `role="status"`로 알림; 점만 있는 뱃지도 텍스트 대안 제공(WCAG 4.1.2)
- Responsive Considerations: 아이콘 크기에 비례하되 숫자가 읽히는 최소 크기 유지; 자릿수가 늘어도 아이콘을 가리지 않음
- Implementation Guidelines: 시각 뱃지는 `aria-hidden`으로 두고 이름에 텍스트로 반영; 개수 갱신은 실시간이 아니어도 되는지 정함; 부모 단추 터치 목표 44x44pt(Apple HIG) 또는 48x48dp(Material Design)
- Common Mistakes: 뱃지만 있고 스크린리더에는 값이 없음; 확인해도 해제되지 않음; 모든 아이콘에 뱃지를 달아 변별력이 없어짐
- Related Patterns: FB-03, NV-01, IC-01
- Reference Image: `assets/01-feedback.png` 카드 장면: 종 아이콘에 숫자 3, 말풍선 아이콘에 빨간 점, 문구 "새 알림이 3개 왔어요"
