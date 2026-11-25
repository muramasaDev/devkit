# Empty & System States (빈 화면)

- 범위: 목록이 비었거나 기능이 막힌 상태에서 보여주는 9개 화면 패턴 (첫 사용, 검색 및 필터 결과 없음, 오프라인, 권한 필요, 모두 완료, 삭제 직후, 오류, 잠김)
- 색인: `pattern-catalog.md`
- 값 정본: `defaults.md` (본문의 DF-nn 은 그 표의 항목 번호)
- 공통 원칙 1: 빈 화면에는 이유 한 줄 및 다음 행동 하나를 보여준다
- 공통 원칙 2: 사용자가 할 수 있는 행동이 없으면 단추를 지어내지 않는다

## 유사 패턴 구분
| 헷갈리는 쌍 | 고르는 기준 |
|---|---|
| ES-02 검색 결과 없음 대 ES-03 필터 결과 없음 | 입력한 검색어를 바꿔야 결과가 나올 것 같으면 ES-02 (검색어 유지, 대안 제안); 적용된 필터 칩을 풀어야 하면 ES-03 (필터 초기화) |
| ES-04 오프라인 대 ES-08 오류 화면 | 기기의 네트워크 연결 자체가 끊겼으면 ES-04; 연결은 있는데 서버 요청이나 처리가 실패했으면 ES-08 |
| ES-05 권한 필요 대 ES-09 잠김 | 사용자가 OS 권한을 허용하면 바로 풀리면 ES-05; 구매액 같은 조건을 채워야 열리면 ES-09 |
| ES-01 첫 사용 대 ES-07 삭제 직후 | 사용자가 한 번도 채운 적이 없으면 ES-01 (시작 행동 안내); 사용자가 방금 비운 결과면 ES-07 (결과 확인, 되돌릴 수 있으면 FB-02) |
| ES-06 모두 완료 대 ES-01 첫 사용 | 처리할 일을 끝내서 비었으면 ES-06; 처음부터 항목이 없었으면 ES-01 |

## ES-01 첫 사용 (First use empty state)
- ID: ES-01
- Korean Name: 첫 사용
- English Name: First use empty state
- Category: Empty & System States
- Definition: 사용자가 아직 항목을 만들거나 담은 적이 없어 목록이 비어 있는 화면 (운영자가 채우는 목록이 빈 경우는 시작 행동 없이 이유만 표시)
- Purpose: 이 영역이 무엇을 채우는 곳인지 알리고 첫 행동으로 이끎
- User Problem: 빈 화면만 보면 고장인지 원래 비어 있는지 알 수 없음
- When to Use: 요청이 성공했고 항목이 0 개이며 사용자가 한 번도 채우지 않은 목록; 첫 방문
- When Not to Use: 검색이나 필터 때문에 비었을 때 (ES-02, ES-03); 불러오는 중 (LD-02); 사용자가 방금 비웠을 때 (ES-07); 요청이 실패했을 때 (ES-08)
- Interaction Behavior: 이유 한 줄 및 첫 행동 단추 하나를 보여줌; 단추는 항목을 채울 수 있는 화면으로 이동; 항목이 생기면 목록으로 교체
- Required States: 불러오는 중에는 표시하지 않음; 비어 있음; 항목이 생긴 뒤 목록으로 전환
- Visual Guidelines: 아이콘 하나, 문구, 단추 순서로 가운데 정렬; 아이콘은 장식이고 문구가 내용을 전달
- Accessibility: 장식 아이콘은 `aria-hidden`; 문구는 텍스트로 제공; 단추는 `<button>` 또는 링크이며 글자 대비 4.5:1 (WCAG 2.2 1.4.3)
- Responsive Considerations: 좁은 화면에서도 문구 및 단추가 한 화면에 보이게 세로 배치; 단추 목표 크기 44x44pt (Apple HIG), 48x48dp (Material Design)
- Implementation Guidelines: 데이터 요청 성공 및 항목 수 0 을 모두 확인한 뒤에만 표시; 단추의 이동 대상이 실제로 항목을 채울 수 있는 곳이어야 함; 사용자가 채울 방법이 없는 화면이면 단추를 두지 않음
- Common Mistakes: 불러오기 전에 빈 상태가 잠깐 노출됨; 요청 실패를 빈 상태로 보여줌; 단추의 도착 화면이 또 빈 화면
- Related Patterns: ES-02, ES-07, ES-08, LD-02
- Reference Image: 장면:, 북마크 아이콘, "아직 찜한 상품이 없어요", 단추 "상품 둘러보기"

## ES-02 검색 결과 없음 (No search results)
- ID: ES-02
- Korean Name: 검색 결과 없음
- English Name: No search results
- Category: Empty & System States
- Definition: 입력한 검색어에 맞는 결과가 없는 화면
- Purpose: 검색어를 어떻게 바꾸면 되는지 방향을 줌
- User Problem: 철자 오류나 너무 좁은 검색어일 때 왜 결과가 없는지 알 수 없음
- When to Use: 검색어를 보냈고 서버가 결과 0 개를 정상 응답했을 때
- When Not to Use: 필터가 걸려 있어 0 개일 때 (ES-03); 검색 요청이 실패했을 때 (ES-08); 검색 전 초기 화면 (ES-01)
- Interaction Behavior: 입력한 검색어를 유지해 보여주고 결과 없음 한 줄을 표시; 대안 제안 칩을 누르면 그 검색을 실행
- Required States: 대안 제안 있음; 대안 제안 없음 (칩 없이 검색어 수정 안내만); 제안 검색 중
- Visual Guidelines: 검색 입력 칸은 그대로 두고 아래에 문구 및 칩 배치; 제안 칩은 검색어와 구분되게 표시
- Accessibility: 결과 없음 변화는 `role="status"` 로 알림 (WCAG 2.2 4.1.3); 칩은 `<button>` 이고 보이는 문구가 이름
- Responsive Considerations: 칩은 줄바꿈; 키보드가 열린 상태에서도 문구가 가려지지 않음
- Implementation Guidelines: 제안은 실제로 검색해 결과가 있는 것만 보여줌; 제안이 없으면 칩을 만들지 않음; 검색어 입력 칸의 값을 지우지 않음
- Common Mistakes: 제안 칩을 눌렀더니 다시 결과 0 개; 검색어가 지워져 수정하기 어려움; 오타 추정을 단정 문장으로 씀
- Related Patterns: ES-03, ES-08, LD-02
- Reference Image: 장면:, 검색어 "후쿠오가", "검색 결과가 없어요", "이렇게 찾아볼까요?", 제안 칩 "이코노미"

## ES-03 필터 결과 없음 (No filter results)
- ID: ES-03
- Korean Name: 필터 결과 없음
- English Name: No filter results
- Category: Empty & System States
- Definition: 적용된 필터 조합에 맞는 항목이 없는 화면
- Purpose: 필터를 조정해 결과를 되찾게 함
- User Problem: 어떤 조건 때문에 결과가 없는지 알기 어려움
- When to Use: 필터 칩이 하나 이상 적용된 상태에서 결과가 0 개일 때
- When Not to Use: 필터가 없는데 비어 있을 때 (ES-01, ES-02); 요청 실패 (ES-08)
- Interaction Behavior: 적용된 칩을 그대로 보여주고 칩 개별 해제 가능; "필터 초기화" 단추는 모든 필터를 해제하고 결과를 다시 불러옴
- Required States: 필터 적용 중 결과 0 개; 초기화 후 불러오는 중; 초기화 후 결과 표시
- Visual Guidelines: 적용 칩은 문구 위나 목록 위에 계속 보임; 초기화 단추는 하나만 강조
- Accessibility: 결과 수 변화는 `role="status"`; 칩 해제 단추는 이름에 대상 포함 ("서울 필터 해제"); 초기화 뒤 초점은 필터 영역의 첫 컨트롤로 옮김 (DF-47) (WCAG 2.2 2.4.3)
- Responsive Considerations: 칩이 많으면 줄바꿈 또는 접기; 초기화 단추는 스크롤 없이 닿게 함
- Implementation Guidelines: 초기화는 필터만 해제하고 검색어는 유지; 서버가 알 수 있을 때만 "어느 조건을 풀면 결과가 있는지" 안내; 필터가 하나뿐이면 초기화 및 해제를 중복 노출하지 않음
- Common Mistakes: 초기화가 검색어까지 지움; 적용 칩이 숨겨져 원인을 알 수 없음; 초기화 후에도 같은 화면이 남음
- Related Patterns: ES-02, ES-01, ES-08
- Reference Image: 장면:, 적용 칩 "서울", "편도", "조식 포함", "조건에 맞는 숙소가 없어요", 단추 "필터 초기화"

## ES-04 오프라인 (Offline state)
- ID: ES-04
- Korean Name: 오프라인
- English Name: Offline state
- Category: Empty & System States
- Definition: 기기의 네트워크 연결이 끊겨 새 데이터를 가져오지 못하는 상태
- Purpose: 원인이 사용자 기기의 연결임을 알리고 복구 방법을 줌
- User Problem: 서비스 고장으로 오해하거나 계속 눌러 봄
- When to Use: 기기 또는 브라우저가 연결 없음을 알릴 때; 요청이 연결 단계에서 실패했을 때
- When Not to Use: 연결은 있는데 서버가 오류를 돌려준 경우 (ES-08); 결과가 0 개인 경우 (ES-02, ES-03)
- Interaction Behavior: 안내 문구를 보여주고 연결이 돌아오면 자동으로 다시 불러옴; 이미 받은 데이터가 있으면 유지하고 오프라인임을 띠로 알림
- Required States: 오프라인; 연결 복구 후 다시 불러오는 중; 복구 성공; 복구 후에도 실패 (ES-08)
- Visual Guidelines: 연결 끊김 아이콘 및 문구 한 줄; 받아 둔 데이터와 겹쳐 가리지 않음
- Accessibility: 상태 변화 (끊김, 복구) 는 `role="status"` 로 알림 (WCAG 2.2 4.1.3); 아이콘만으로 전달하지 않고 문구 병행 (1.4.1)
- Responsive Considerations: 화면 상단 띠는 고정 헤더에 가려지지 않게 배치; 좁은 화면에서 문구 줄바꿈
- Implementation Guidelines: 브라우저의 연결 없음 신호는 믿을 수 있어도 연결 있음은 보장하지 않으므로 실제 요청 결과로 최종 판단; "자동으로 다시 불러와요" 라고 쓰면 실제로 자동 재시도를 구현하고, 구현하지 않으면 문구에 쓰지 않음
- Common Mistakes: 문구는 자동 재시도인데 구현이 없음; 받아 둔 화면을 지우고 전체를 오프라인 화면으로 바꿈; 서버 오류를 오프라인으로 안내
- Related Patterns: ES-08, FB-03, LD-01
- Reference Image: 장면:, 끊긴 연결 아이콘, "인터넷 연결이 끊겼어요", "연결되면 자동으로 다시 불러와요"

## ES-05 권한 필요 (Permission request)
- ID: ES-05
- Korean Name: 권한 필요
- English Name: Permission request
- Category: Empty & System States
- Definition: OS 권한 창을 띄우기 전에 이 권한이 왜 필요한지 먼저 알리는 화면
- Purpose: 이유를 알린 뒤 사용자가 스스로 허용할지 정하게 함
- User Problem: 이유 없이 OS 권한 창이 뜨면 맥락을 모른 채 거절하고, 거절하면 다시 켜기 어려움
- When to Use: 사용자가 권한이 필요한 기능을 쓰려는 시점; 권한이 아직 정해지지 않은 상태
- When Not to Use: 권한이 필요 없는 기능; 이미 허용된 상태; 이미 거절한 뒤 같은 요청을 반복하는 경우 (DP-09); 앱을 열자마자 이유 없이 요청하는 경우
- Interaction Behavior: 이유 한 줄 및 단추 하나를 보여주고, 사용자가 단추를 누른 뒤에야 OS 권한 창을 호출; 허용하면 기능을 켜고, 거절하면 기능 없이 계속 쓸 수 있으며 같은 요청을 자동으로 반복하지 않음
- Required States: 요청 전 (이유 안내); 허용됨 (이 화면을 표시하지 않음); 거절됨 (설정에서 켜는 경로 안내); 시스템이 재요청을 막은 상태 (기기 설정 안내)
- Visual Guidelines: 이유 문구는 사용자가 얻는 것을 구체적으로 씀; 단추 하나만 강조; 보조 선택지는 같은 비중의 중립 문구
- Accessibility: 안내 문구 및 단추를 OS 창 호출 전에 읽을 수 있게 제공; 단추는 `<button>` (WCAG 2.2 2.1.1); OS 창이 닫힌 뒤 초점을 원래 단추 위치로 복귀 (2.4.3)
- Responsive Considerations: 모바일 앱 및 웹 모두 권한 창의 모양은 OS 및 브라우저가 정하므로 사전 화면은 짧게 유지
- Implementation Guidelines: OS 권한 창은 사용자 동작 (단추) 의 결과로만 호출; 사전 화면에서 "나중에" 를 고르면 OS 창을 호출하지 않고 요청 기회를 아껴 둠; 플랫폼에 따라 한 번 거절하면 앱이 다시 묻지 못할 수 있으므로 이때는 기기 설정에서 바꾸도록 안내
- Common Mistakes: 이유 없이 첫 실행에서 권한 창 호출; 거절한 뒤 같은 사전 화면을 계속 띄움 (DP-09); 거절 후 기능이 완전히 막힘
- Related Patterns: DP-09, ES-09, FB-04
- Reference Image: 장면:, 종 아이콘, "가격이 내리면 알려드릴게요", 단추 "알림 켜기"

## ES-06 모두 완료 (All done)
- ID: ES-06
- Korean Name: 모두 완료
- English Name: All done
- Category: Empty & System States
- Definition: 처리할 항목을 모두 끝내 목록이 빈 상태
- Purpose: 끝났음을 확인시키고 필요하면 다음 할 일로 연결
- User Problem: 목록이 비면 다 끝낸 것인지 불러오기에 실패한 것인지 알 수 없음
- When to Use: 사용자가 처리해서 대기 항목이 0 개가 된 직후; 오늘 몫을 끝낸 상태
- When Not to Use: 처음부터 항목이 없었을 때 (ES-01); 동기화가 끝나지 않아 아직 모르는 상태; 요청 실패 (ES-08)
- Interaction Behavior: 완료 문구를 보여주고, 이어서 볼 항목이 있으면 링크 하나 제공 (예: 다음 날 항목); 새 항목이 생기면 목록으로 복귀
- Required States: 완료; 새 항목 도착으로 목록 복귀; 다음 항목 링크 없음
- Visual Guidelines: 완료 아이콘은 색에만 의존하지 않고 문구와 함께 표시 (WCAG 2.2 1.4.1); 단추보다 링크로 가볍게
- Accessibility: 완료 전환은 `role="status"` 로 알림 (4.1.3); 장식 아이콘은 `aria-hidden`; 링크 텍스트는 목적지를 말함
- Responsive Considerations: 문구 및 링크가 한 화면에 보이게 세로 배치
- Implementation Guidelines: 서버 기준으로 대기 항목이 0 개임을 확인한 뒤 표시; 이어서 볼 항목이 없으면 링크를 만들지 않음
- Common Mistakes: 동기화 도중 일부만 보고 완료로 표시; 항상 칭찬 문구만 반복해 정보가 없음; 링크 목적지가 또 빈 화면
- Related Patterns: ES-01, ES-07, FB-01
- Reference Image: 장면:, 초록 체크, "오늘 할 일을 다 끝냈어요", 링크 "내일 할 일 보기 ›"

## ES-07 삭제 직후 (After delete)
- ID: ES-07
- Korean Name: 삭제 직후
- English Name: After delete
- Category: Empty & System States
- Definition: 사용자가 방금 항목을 지우거나 비워서 목록이 빈 화면
- Purpose: 방금 한 동작의 결과를 확인시킴
- User Problem: 삭제 뒤 빈 화면이 나오면 오류로 오해하거나 첫 사용 화면처럼 보여 혼란스러움
- When to Use: 사용자의 삭제 또는 비우기가 반영된 직후
- When Not to Use: 사용자가 한 번도 채운 적 없는 목록 (ES-01); 삭제 요청이 실패했을 때 (ES-08)
- Interaction Behavior: 결과 문구만 보여줌; 되돌릴 수 있으면 FB-02 를 병행; 행동 단추는 필요할 때 하나만 두고 없으면 두지 않음
- Required States: 삭제 처리 중; 삭제 완료 (이 화면); 되돌리기로 복구; 삭제 실패
- Visual Guidelines: 결과를 알리는 아이콘 및 문구 한 줄; 첫 사용 화면과 문구가 겹치지 않게 구분
- Accessibility: 삭제 완료는 `role="status"` 로 알림 (WCAG 2.2 4.1.3); 아이콘은 장식이면 `aria-hidden`
- Responsive Considerations: 화면이 비어도 상단 고정 영역 및 뒤로 가기 경로가 유지됨
- Implementation Guidelines: 서버 반영이 끝난 뒤 완료 문구를 표시; 되돌리기를 약속하면 그 기간 동안 실제로 복구 가능해야 함; ES-01 문구를 재사용해 삭제 사실이 사라지게 하지 않음
- Common Mistakes: "아직 없어요" 류 문구로 삭제 사실을 감춤; 삭제가 실패했는데 완료 문구 표시; 되돌리기를 말하고 복구 수단이 없음
- Related Patterns: ES-01, FB-02, ES-08
- Reference Image: 장면:, 휴지통 아이콘, "휴지통을 비웠어요"

## ES-08 오류 화면 (Error state)
- ID: ES-08
- Korean Name: 오류 화면
- English Name: Error state
- Category: Empty & System States
- Definition: 연결은 있으나 서버나 앱의 처리가 실패해 화면을 채우지 못하는 상태
- Purpose: 실패했음을 사실대로 알리고 다시 시도할 길을 줌
- User Problem: 빈 화면이나 멈춘 화면만 보면 무엇을 해야 할지 알 수 없음
- When to Use: 요청이 실패했거나 처리 중 오류가 나서 화면 내용을 만들 수 없을 때
- When Not to Use: 기기 연결이 끊긴 경우 (ES-04); 결과가 0 개인 경우 (ES-02, ES-03); 다시 시도해도 소용없는 권한 부족 같은 경우는 다른 안내
- Interaction Behavior: 실패 문구 한 줄 및 "다시 시도" 단추 하나; 누르면 같은 요청을 다시 실행; 반복 실패 시 다른 경로를 안내
- Required States: 오류; 다시 시도 중 (단추 비활성 및 상태 표시); 반복 실패; 성공으로 전환
- Visual Guidelines: 오류 아이콘 및 문구 한 줄; 색만으로 오류를 전달하지 않고 문구 병행 (WCAG 2.2 1.4.1)
- Accessibility: 화면 전체가 실패한 긴급 오류는 `role="alert"`; 재시도 뒤 상태는 `role="status"`; 다시 시도 단추는 `<button>` (2.1.1)
- Responsive Considerations: 부분 영역만 실패하면 그 영역 안에서 오류를 보여주고 나머지 화면은 유지
- Implementation Guidelines: 다시 시도는 실제 같은 요청을 재실행해야 하며 전체 새로고침으로 대신하지 않음; 원인을 모르면 모른다고 쓰고 원인을 지어내지 않음; 서버가 오류 식별자를 주면 한 줄로 표시하고 복사할 수 있게 하며 연결 끊김에는 표시하지 않음 (DF-43)
- Common Mistakes: 요청 실패를 삼켜서 빈 상태 (ES-01) 로 보임; 재시도 단추가 동작하지 않음; 실패 원인을 추측해 단정함
- Related Patterns: ES-04, ES-01, FB-06
- Reference Image: 장면:, 빨간 느낌표, "잠시 문제가 생겼어요", 단추 "다시 시도"

## ES-09 잠김 (Locked state)
- ID: ES-09
- Korean Name: 잠김
- English Name: Locked state
- Category: Empty & System States
- Definition: 조건을 채워야 열리는 기능이나 영역이 아직 닫혀 있는 상태
- Purpose: 닫혀 있는 이유, 열리는 조건, 현재 위치를 알림
- User Problem: 왜 쓸 수 없는지 모르고 고장으로 오해함
- When to Use: 사용자가 달성하면 열리는 조건이 있을 때 (금액, 횟수, 단계 등)
- When Not to Use: 사용자가 OS 권한을 허용하면 풀리는 경우 (ES-05); 사용자가 풀 방법이 없는 권한 부족 (단추를 만들지 않고 문의 대상만 안내)
- Interaction Behavior: 열리는 조건 한 줄 및 진행 정도 표시; 조건을 채울 수 있는 곳으로 가는 행동 하나; 조건을 채우면 즉시 열림
- Required States: 잠김 (진행 정도 표시); 조건 충족으로 열림; 진행 정도를 알 수 없음 (조건 문구만)
- Visual Guidelines: 자물쇠 아이콘 및 조건 문구; 진행 막대에는 현재 값과 목표가 텍스트로 함께 표시 (예: 1/3)
- Accessibility: 진행은 `role="progressbar"` 및 `aria-valuenow`; 잠금 상태는 아이콘이 아닌 텍스트로도 전달 (WCAG 2.2 1.4.1, 4.1.2); 조건 충족 시 `role="status"` 로 알림
- Responsive Considerations: 진행 막대 및 문구가 좁은 폭에서도 한 묶음으로 보이게 배치
- Implementation Guidelines: 조건과 현재 값은 서버 또는 상태의 실제 값에서 가져옴; 진행 막대 값을 꾸며 넣지 않음; 비활성 단추만 두지 않고 이유를 함께 보여줌
- Common Mistakes: 이유 없이 비활성 단추만 둠; 진행 막대가 실제 값이 아님; 조건을 채워도 화면이 갱신되지 않음
- Related Patterns: ES-05, LD-03, LD-04
- Reference Image: 장면:, 자물쇠 아이콘, "3만 원 이상 담으면 열려요", 진행 막대 및 "1/3"
