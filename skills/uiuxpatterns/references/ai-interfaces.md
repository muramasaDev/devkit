# AI Interfaces (AI 화면)

- 범위: 대화형 AI 및 에이전트 화면에서 대기, 답변 표시, 근거, 평가, 수정, 첨부, 작업 단계를 다루는 9개 패턴
- 색인: `pattern-catalog.md`
- 값 정본: `defaults.md` (본문의 DF-nn 은 그 표의 항목 번호)

## 유사 패턴 구분
| 헷갈리는 쌍 | 고르는 기준 |
|---|---|
| AI-01 생각 중 표시 대 AI-02 스트리밍 답변 대 AI-09 에이전트 단계 | 첫 출력이 오기 전이면 AI-01 (상태만); 답변 글자가 오는 중이면 AI-02; 서버 또는 도구가 단계 시작 및 종료 이벤트를 실제로 보낼 때만 AI-09 |
| AI-04 다시 생성 대 AI-07 고쳐 묻기 | 질문은 그대로 두고 답변만 새로 받으면 AI-04; 질문 문구나 범위를 바꿔 다시 보내면 AI-07 |
| AI-05 출처 표시 대 AI-06 답변 피드백 | 답변의 근거 자료를 확인시키면 AI-05; 답변에 대한 사용자의 평가를 받으면 AI-06 |
| AI-03 추천 질문 칩 대 AI-07 고쳐 묻기 | 아직 보내지 않은 새 질문의 후보면 AI-03; 이미 보낸 말을 편집하면 AI-07 |
| AI-02 스트리밍 답변 대 LD-03 진행 막대 | 내용이 도착하는 대로 보이면 AI-02; 처리 분량의 실제 비율을 아는 작업이면 LD-03 |

## AI-01 생각 중 표시 (Thinking indicator)
- ID: AI-01
- Korean Name: 생각 중 표시
- English Name: Thinking indicator
- Category: AI Interfaces
- Definition: 사용자 말을 보낸 뒤 첫 출력이 오기 전까지 답변 자리에 보이는 대기 표시 (점 3개 등)
- Purpose: 요청이 접수되어 처리 중이라는 상태만 알림
- User Problem: 보낸 뒤 화면이 변하지 않으면 전송 실패로 오해하고 같은 말을 다시 보냄
- When to Use: 요청을 보낸 직후부터 첫 출력이 도착할 때까지; 첫 출력이 오면 사라져야 하는 구간
- When Not to Use: 답변 글자가 이미 오는 중 (AI-02); 단계 이벤트가 실제로 오는 긴 작업 (AI-09); 진행률이나 남은 시간을 알 수 없는데 숫자로 보여주려는 경우
- Interaction Behavior: 전송 즉시 답변 자리에 표시; 첫 출력 도착 시 같은 자리에서 답변으로 교체; 실패하면 표시를 없애고 오류 안내로 교체
- Required States: 대기 중; 스트리밍으로 교체됨; 실패로 교체됨; 사용자가 취소함
- Visual Guidelines: 답변이 나올 위치에 놓고 사용자 말과 구분; 움직임은 `prefers-reduced-motion` 에서 정적 표시로 대체
- Accessibility: 시각 점은 숨기고 "답변을 준비하는 중" 같은 텍스트를 `role="status"` 로 전달 (WCAG 2.2 4.1.3); `prefers-reduced-motion` 에서는 정적 표시로 대체
- Responsive Considerations: 말풍선 폭을 따라가며 좁은 화면에서도 입력 칸을 가리지 않음; 키보드가 열려도 보이는 위치 유지
- Implementation Guidelines: 이 표시는 상태만 나타냄. 퍼센트, 단계 이름, 남은 시간을 지어내지 않음; 서버의 첫 응답 이벤트로 제거; 응답이 오지 않는 한계 시간은 30초 (DF-25) 이고 넘으면 오류 안내로 전환
- Common Mistakes: 실제로 일어나지 않는 단계 문구를 돌려 보여줌; 첫 출력 뒤에도 남아 있음; 취소 수단이 없음
- Related Patterns: AI-02, AI-09, LD-01, LD-02, ES-08
- Reference Image: 장면:, 사용자 말 "이 가방 어때?" 뒤 답변 자리에 점 3개

## AI-02 스트리밍 답변 (Streaming response)
- ID: AI-02
- Korean Name: 스트리밍 답변
- English Name: Streaming response
- Category: AI Interfaces
- Definition: 답변을 완성 후 한 번에 보여주지 않고 생성되는 대로 이어 붙여 보여주는 방식
- Purpose: 긴 답변도 첫 글자부터 읽기 시작하게 하고 진행 중임을 보여줌
- User Problem: 긴 답변이 끝날 때까지 빈 화면을 기다리거나, 잘못된 방향의 답변을 끝까지 기다려야 함
- When to Use: 답변이 길고 생성에 시간이 걸리는 대화; 서버가 조각 단위로 내려줄 수 있을 때
- When Not to Use: 짧아서 한 번에 오는 답변; 완성 전 값이 틀릴 수 있는 표 및 계산 결과 (완성 후 표시 또는 틀만 먼저 표시)
- Interaction Behavior: 첫 출력 도착 시 AI-01 을 대체; 조각이 이어 붙음; 정지 단추를 누르면 지금까지 나온 부분을 남기고 중단; 사용자가 위로 스크롤하면 자동 따라가기 중지
- Required States: 스트리밍 중; 사용자가 정지함 (부분 답변 유지); 완료; 도중 오류 (받은 부분 유지 및 안내)
- Visual Guidelines: 정지 단추는 입력 영역 또는 답변 근처 한 곳에 둠; 진행 중임을 글자 끝 표시나 정지 단추로 드러냄
- Accessibility: 조각마다 낭독하지 않도록 생성 중에는 영역에 `aria-busy="true"`; 완료 시 `role="status"` 로 "답변이 완성됐어요" 전달; 정지는 `<button>` 으로 키보드 조작 가능 (WCAG 2.2 2.1.1)
- Responsive Considerations: 답변이 늘어나도 입력 칸이 밀려나지 않게 고정; 좁은 화면에서 정지 단추 목표 크기 확보 (24x24 CSS px 이상, WCAG 2.2 2.5.8)
- Implementation Guidelines: 정지는 서버 요청 취소 및 화면 중단을 함께 처리; 서버 취소가 안 되면 중단됐다고만 표시하지 않고 사실대로 알림; 열린 코드 블록 및 목록이 중간에 깨져 보이지 않게 처리
- Common Mistakes: 정지를 눌러도 뒤에서 계속 생성되며 화면만 멈춤; 글자마다 스크린 리더가 낭독; 자동 스크롤이 읽던 위치를 빼앗음
- Related Patterns: AI-01, AI-04, AI-09, LD-03
- Reference Image: 장면:, 사용자 말 "제주 일정 짜줘", 답변이 "1일차 성산일출봉, 우도 2일차 협재 하" 까지 나온 상태, 정지 단추

## AI-03 추천 질문 칩 (Suggested prompts)
- ID: AI-03
- Korean Name: 추천 질문 칩
- English Name: Suggested prompts
- Category: AI Interfaces
- Definition: 입력 전이나 답변 뒤에 눌러서 바로 보낼 수 있는 질문 후보를 칩으로 보여주는 요소
- Purpose: 무엇을 물을지 모르는 사용자에게 시작점을 줌
- User Problem: 빈 입력 칸 앞에서 막막하고 이 서비스가 어떤 요청을 처리하는지 모름
- When to Use: 대화 시작 화면; 답변 뒤 이어서 물을 만한 후속 질문
- When Not to Use: 서비스가 실제로 처리하지 못하는 요청; 대화가 진행 중인데 맥락과 무관한 같은 칩을 계속 반복할 때
- Interaction Behavior: 칩을 누르면 그 문구가 사용자 말이 되어 전송 (기본은 바로 전송, 문구에 사용자가 채울 빈칸이 있으면 입력 칸에 채움, DF-33); 사용 후 칩은 사라지거나 갱신
- Required States: 기본; 포커스; 눌림; 비활성 (답변 생성 중); 숨김
- Visual Guidelines: 칩 줄은 가로로 나열하고 넘치면 줄바꿈; 칩 문구는 그대로 보내질 질문과 같게 씀
- Accessibility: 각 칩은 `<button>` 이고 보이는 문구가 이름; 칩 묶음에 그룹 이름 부여; 목표 크기 24x24 CSS px 이상 (WCAG 2.2 2.5.8), 터치는 44x44pt (Apple HIG), 48x48dp (Material Design) 권장
- Responsive Considerations: 좁은 화면에서는 줄바꿈 우선, 가로 스크롤을 쓰면 키보드로도 칩에 닿게 함
- Implementation Guidelines: 칩 문구는 실제 처리 가능한 요청만 씀; 생성 중 눌러도 이중 전송되지 않게 비활성; 사용자가 입력을 시작하면 칩을 정리
- Common Mistakes: 처리 못 하는 요청을 칩으로 노출; 누르면 입력 칸에만 채워졌는데 전송된 줄로 오해; 모든 화면에 같은 칩을 반복
- Related Patterns: AI-07, AI-02, ES-01
- Reference Image: 장면:, "무엇을 도와드릴까요?" 아래 칩 "이 가방 어때?", "리뷰 요약하기", "일정 짜기"

## AI-04 다시 생성 (Regenerate)
- ID: AI-04
- Korean Name: 다시 생성
- English Name: Regenerate
- Category: AI Interfaces
- Definition: 같은 질문으로 답변을 새로 만들고, 이전 답변은 판 이동으로 남겨 두는 동작
- Purpose: 질문은 그대로 두고 다른 답변을 받음
- User Problem: 답변이 마음에 안 들 때 같은 질문을 다시 쓰기 번거롭고, 이전 답변이 사라질까 걱정함
- When to Use: 질문에는 문제가 없고 답변 내용이나 표현이 불만일 때
- When Not to Use: 질문 문구나 범위를 바꾸고 싶을 때 (AI-07); 같은 입력에 항상 같은 결과가 나오는 기능 (새로 만든 것처럼 보이면 사실과 다름)
- Interaction Behavior: 누르면 마지막 답변 자리에서 AI-01, AI-02 순으로 새 답변 생성; 이전 판은 버리지 않고 `‹ 1/2 ›` 로 열람; 생성 중 정지 가능
- Required States: 기본; 생성 중; 판 이동 (현재 판 번호 및 전체 판 수); 첫 판 및 마지막 판에서 해당 방향 비활성; 생성 실패 (이전 판 유지)
- Visual Guidelines: 답변 아래 행동 줄에 둠; 판 번호는 숫자 텍스트로 표시
- Accessibility: 판 이동 단추 이름은 "이전 답변", "다음 답변"; 판이 바뀌면 `role="status"` 로 현재 판 알림 (WCAG 2.2 4.1.3); 아이콘만 쓰면 `aria-label`
- Responsive Considerations: 좁은 화면에서도 행동 줄이 줄바꿈되어 단추가 잘리지 않음; 터치 목표 크기 확보
- Implementation Guidelines: 판별로 답변을 저장; 재생성이 실패해도 현재 판을 지우지 않음; 다시 생성한 뒤 이어진 대화는 사용자가 보고 있던 판에만 연결하고 다른 판으로 넘기면 그 판의 대화를 보여 줌 (DF-34)
- Common Mistakes: 이전 답변을 덮어써서 되돌릴 수 없음; 실패했는데 빈 판이 남음; 판 번호가 갱신되지 않음
- Related Patterns: AI-07, AI-06, AI-02
- Reference Image: 장면:, 답변 아래 "다시 생성" 및 판 이동 "‹ 1/2 ›"

## AI-05 출처 표시 (Citations)
- ID: AI-05
- Korean Name: 출처 표시
- English Name: Citations
- Category: AI Interfaces
- Definition: 답변이 근거로 쓴 자료를 본문 번호 및 출처 카드로 연결해 보여주는 요소
- Purpose: 사용자가 답변의 근거를 직접 확인하게 함
- User Problem: 답변이 맞는지 확인할 방법이 없어 믿거나 버리는 선택만 남음
- When to Use: 답변이 특정 자료 (상품 상세, 문서, 웹 페이지) 에 근거할 때
- When Not to Use: 근거 자료 없이 생성한 내용; 실제로 근거로 쓰지 않은 자료를 그럴듯하게 붙이는 경우
- Interaction Behavior: 본문 끝 번호를 누르면 해당 출처 카드로 이동하거나 펼침; 출처 카드를 누르면 원문 열기 (새 창이면 미리 알림)
- Required States: 출처 있음; 출처 불러오는 중; 링크 접근 불가; 출처 없음 (표시 영역 자체를 생략)
- Visual Guidelines: 번호는 문장 끝에 작게, 카드는 답변 아래에 제목 및 주소 표기; 번호 및 카드의 순서 일치
- Accessibility: 번호는 링크이고 이름은 "출처 1" 처럼 대상이 드러나게; 문장 안 번호는 WCAG 2.5.8 의 문장 안 링크 예외에 해당하나 누르기 쉽게 눌리는 영역을 넓힘; 카드 제목을 링크 텍스트로 사용
- Responsive Considerations: 카드는 줄바꿈하고 긴 주소는 말줄임하되 전체 주소를 접근 가능한 이름으로 제공
- Implementation Guidelines: 출처 목록은 답변 생성 중 실제로 참조한 자료 기록에서 만듦; 답변이 끝난 뒤 그럴듯한 링크를 사후에 붙이지 않음; 번호 및 문장의 대응을 유지; 출처는 실제 근거로 쓴 것만 표시
- Common Mistakes: 검색 결과 전체를 출처로 나열 (근거로 안 쓴 것 포함); 본문 번호와 카드가 어긋남; 링크 이동으로 현재 대화 및 입력이 사라짐
- Related Patterns: AI-06, AI-02, FB-07
- Reference Image: 장면:, 답변 "이 상품은 2개 사면 무료배송이에요" 끝 번호 1, 출처 카드 "상품 상세 careers.example.com"

## AI-06 답변 피드백 (Response feedback)
- ID: AI-06
- Korean Name: 답변 피드백
- English Name: Response feedback
- Category: AI Interfaces
- Definition: 답변 하나에 대해 좋아요 또는 싫어요로 평가를 남기는 단추 및 응답 문구
- Purpose: 답변 단위 품질 평가를 사용자가 제품에 전달하게 함
- User Problem: 마음에 들거나 안 드는 답변을 알릴 방법이 없음
- When to Use: 답변 단위로 평가를 실제로 수집하고 활용할 때
- When Not to Use: 평가를 저장하거나 활용하는 경로가 없는데 "반영할게요" 라고 쓰는 경우; 답변을 바꾸고 싶은 사용자 (AI-04, AI-07)
- Interaction Behavior: 누르면 선택 상태가 표시되고 응답 문구가 나옴; 다시 누르면 취소; 싫어요 뒤 사유는 선택 사항으로 받고 건너뛸 수 있음 (DF-35)
- Required States: 미선택; 좋아요 선택; 싫어요 선택; 전송 중; 전송 실패
- Visual Guidelines: 답변 아래 행동 줄에 다시 생성과 나란히 둠; 선택 상태는 색만으로 구분하지 않고 채움 및 윤곽 등 모양 차이를 병행 (WCAG 2.2 1.4.1)
- Accessibility: 아이콘 단추는 `aria-label` ("좋아요", "싫어요"); 선택 상태를 텍스트나 이름으로도 전달 (4.1.2); 응답 문구는 `role="status"` (4.1.3)
- Responsive Considerations: 좁은 화면에서 두 단추가 붙어 오탭하지 않게 간격 확보; 터치 목표 44x44pt (Apple HIG), 48x48dp (Material Design)
- Implementation Guidelines: 평가는 답변 ID 에 연결해 저장; 저장이 실제로 성공했을 때만 응답 문구 표시; 실패하면 선택 표시를 되돌리고 안내
- Common Mistakes: 저장 실패인데 "고마워요" 를 표시; 어느 답변의 평가인지 불명확; 아이콘만 있고 이름이 없음
- Related Patterns: AI-04, AI-07, FB-01
- Reference Image: 장면:, 답변 아래 좋아요 및 싫어요, 응답 문구 "고마워요, 반영할게요"

## AI-07 고쳐 묻기 (Edit prompt)
- ID: AI-07
- Korean Name: 고쳐 묻기
- English Name: Edit prompt
- Category: AI Interfaces
- Definition: 이미 보낸 사용자 말을 편집해 다시 보내고 새 답변을 받는 동작
- Purpose: 질문의 오타, 범위, 조건을 바로잡아 다시 묻게 함
- User Problem: 보낸 말을 고치려면 새로 다 써야 하고, 이전 대화가 어떻게 되는지 알 수 없음
- When to Use: 질문 자체를 바꿔야 할 때 (범위 축소, 조건 추가, 오타)
- When Not to Use: 질문은 그대로이고 답변만 다시 받을 때 (AI-04); 이어서 새 질문을 덧붙일 때 (새 말로 보냄)
- Interaction Behavior: 연필 아이콘을 누르면 보낸 말이 편집 칸으로 바뀜; 보내기를 누르면 그 말 이후의 답변이 새 답변으로 이어짐; 취소하면 원문 유지
- Required States: 보기; 편집 중; 보내는 중; 취소; 빈 입력 (보내기 비활성)
- Visual Guidelines: 편집 칸은 원래 말풍선 위치에서 열림; 취소 및 보내기 단추를 편집 칸 근처에 나란히 배치
- Accessibility: 연필 단추 이름 "보낸 말 고치기"; 편집 진입 시 초점을 편집 칸으로 옮기고 취소 후 연필 단추로 복귀 (WCAG 2.2 2.4.3); Esc 로 취소
- Responsive Considerations: 화면 키보드가 열려도 편집 칸 및 단추가 보이게 배치
- Implementation Guidelines: 원문을 보관해 취소 시 복원; 편집 후 보내면 뒤따르던 대화는 대체하지 않고 이전 판으로 보존하며 보내기 전에 알림 (DF-36)
- Common Mistakes: 보내는 순간 뒤 대화가 말없이 사라짐; 취소했는데 편집한 내용이 남음; 연필 아이콘에 이름이 없음
- Related Patterns: AI-04, AI-02, FB-04
- Reference Image: 장면:, 연필 아이콘, 보낸 말 "코디 봐줘", 편집 칸 "이 코디만 봐줘", 단추 "취소" 및 "보내기"

## AI-08 파일 첨부 (File attachment)
- ID: AI-08
- Korean Name: 파일 첨부
- English Name: File attachment
- Category: AI Interfaces
- Definition: 입력 칸에서 파일을 올려 질문에 붙이고, 첨부 카드로 올리는 상태를 보여주는 요소
- Purpose: 말로 설명하기 어려운 자료를 질문과 함께 전달
- User Problem: 파일이 올라갔는지, 올리는 중인지, 실패했는지 알 수 없음
- When to Use: 파일 내용을 바탕으로 답하는 서비스
- When Not to Use: 지원하지 않는 형식이나 크기를 받아 두었다가 나중에 실패시키는 경우; 파일을 쓰지 않는 서비스
- Interaction Behavior: 클립 아이콘으로 파일 선택; 첨부 카드에 올리는 상태 표시; 완료되면 전송 가능; 카드의 제거 단추로 취소
- Required States: 선택됨; 올리는 중; 올리기 완료; 처리 중 (서버가 파일을 읽는 단계가 따로 있을 때만. 진행률을 받지 못하면 퍼센트 없이 상태만); 질문 가능; 실패 (재시도 및 제거); 지원하지 않는 형식; 제거됨
- Visual Guidelines: 첨부 카드는 입력 칸 위에 파일 이름 및 상태 표시; 진행 막대는 실제 진행률 값이 있을 때만 사용
- Accessibility: 클립 단추 이름 "파일 첨부"; 진행은 `role="progressbar"` 및 `aria-valuenow`; 완료 및 실패는 `role="status"`, 긴급 오류는 `role="alert"`; 끌어 놓기만 제공하지 않고 단추 대안 제공 (WCAG 2.2 2.5.7)
- Responsive Considerations: 좁은 화면에서 파일 이름은 말줄임하되 전체 이름을 접근 가능한 이름으로 제공; 여러 파일은 세로로 쌓음
- Implementation Guidelines: 허용 형식 및 크기 한도는 올리기 전에 검사해 즉시 안내 (한도 값은 서버 정책 값을 받아 한 줄로 표시, DF-26); 올리는 중에는 전송을 막거나 완료까지 대기 상태를 알림; 실패한 파일을 첨부된 것으로 두고 보내지 않음; 서버가 파일 처리 결과(성공, 실패)를 알려 주는지 먼저 확인하고, 알려 주면 그 결과를 첨부 카드에 표시; 알려 주지 않으면 `처리 완료` 를 표시하지 않음
- Common Mistakes: 진행 막대가 실제 값이 아님; 실패한 카드가 남아 그대로 전송됨; 형식 오류를 올린 뒤에야 알림
- Related Patterns: LD-03, AI-09, FB-06
- Reference Image: 장면:, 첨부 카드 "카드명세서.pdf" 및 올리는 진행 막대, 입력 칸 클립 아이콘 "메시지 입력"

## AI-09 에이전트 단계 (Agent steps)
- ID: AI-09
- Korean Name: 에이전트 단계
- English Name: Agent steps
- Category: AI Interfaces
- Definition: 에이전트가 수행하는 작업을 단계 목록으로 나누고 단계마다 완료, 진행 중, 대기 상태를 보여주는 요소
- Purpose: 여러 단계로 이뤄진 작업의 현재 위치 및 지금까지 한 일을 알림
- User Problem: 오래 걸리는 작업에서 무슨 일을 하고 있는지, 어디까지 끝났는지 알 수 없음
- When to Use: 서버나 도구가 단계 시작 및 종료 이벤트를 실제로 보낼 때; 단계가 여러 개인 긴 작업
- When Not to Use: 실제 이벤트가 없을 때 (AI-01 로 상태만 표시); 한 번에 끝나는 짧은 응답; 단계 이름을 타이머나 문구 순환으로 꾸며 보여주는 경우
- Interaction Behavior: 이벤트에 따라 대기에서 진행 중, 완료로 바뀜; 실패한 단계는 실패 표시 및 이유 안내; 진행 중 중단 가능; 모두 끝나면 결과 제공
- Required States: 대기; 진행 중; 완료; 실패; 건너뜀 (실제로 건너뛴 경우만); 취소됨
- Visual Guidelines: 단계 상태는 아이콘 모양 및 텍스트로 함께 전달하고 색만으로 구분하지 않음 (WCAG 2.2 1.4.1)
- Accessibility: 단계 목록은 `<ol>` 구조; 각 항목 이름에 "완료", "진행 중", "대기" 텍스트 포함 (4.1.2); 상태 변경 알림은 `role="status"` 로 하되 단계가 바뀔 때만 (4.1.3)
- Responsive Considerations: 단계가 많으면 완료 단계를 접고 현재 단계를 항상 보이게 함
- Implementation Guidelines: 단계 상태는 실제 도구 호출 및 작업 이벤트에서만 만듦; 미리 완료 처리하지 않고, 수행하지 않은 단계를 완료로 표시하지 않음; 전체 단계 수를 모르면 개수를 표시하지 않음; 승인이 필요한 단계는 AI 신뢰성 원칙에 따라 승인 대기로 표시
- Common Mistakes: 타이머로 단계를 자동 진행시킴; 실패를 완료로 표시; 마지막 이벤트가 오지 않아 진행 중에 멈춘 채 방치됨
- Related Patterns: AI-01, AI-02, LD-05, LD-03
- Reference Image: 장면:, 완료 "명세서 읽기", 완료 "지난달과 비교하기", 진행 중 "정리하는 중", 대기 "정리해서 보내기"

## AI 신뢰성 원칙
- 불확실성 표현: 확실하지 않은 내용은 단정 문장으로 쓰지 않고 확인이 필요함을 답변 글로 밝힘; 색이나 아이콘만으로 전달하지 않음
- 근거 및 출처: 출처는 답변에 실제 근거로 쓴 것만 표시하고, 근거 없이 번호나 링크를 붙이지 않음 (AI-05)
- 진행 상태: 실제 처리 상태를 알 수 없으면 진행률이나 처리 단계를 지어내 표시하지 않음; AI-01 은 상태만, AI-09 는 실제 이벤트가 있을 때만
- 오래 걸리는 작업: 진행 중임, 중단 수단, 끝났을 때의 알림 위치를 함께 제공
- 생성 중단 및 재시도: 생성 중에는 정지 수단을 두고, 중단해도 이미 나온 부분은 유지; 재시도는 AI-04, 질문 수정은 AI-07
- 부분 실패 및 복구: 일부 단계만 실패하면 성공한 결과는 유지하고 실패한 단계 및 이유를 표시하며 그 단계만 다시 시도하게 함
- 도구 실행 및 승인: 결제, 삭제, 전송, 외부 공유처럼 되돌리기 어려운 동작은 실행 전에 내용을 보여주고 사용자 승인을 받음 (FB-04); 승인 전에는 실행하지 않고 거절하면 실행하지 않음
- 작업 완료 결과 제공: 수행하지 않은 작업을 완료로 표시하지 않고, 완료 표시에는 실제 수행한 내용 및 결과물 위치를 함께 제시
- 오류 안내: 안 된 내용 및 사용자가 할 수 있는 다음 행동 하나를 씀; 원인을 모르면 모른다고 쓰고, 오류 뒤에도 사용자가 입력한 내용은 유지
