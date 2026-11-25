# Loading & Progress (로딩)

- 범위: 데이터를 기다리거나 작업이 진행되는 동안 상태를 보여주는 표시 패턴 9종
- 색인: `pattern-catalog.md`
- 값 정본: `defaults.md` (본문의 DF-nn 은 그 표의 항목 번호)

## 대기 시간 구간표 (정본)
- 대기가 시작된 뒤 걸린 시간에 따라 아래 표시를 쓴다. `glossary.md`, `terms-extended.md`, `interaction-rules.md` 는 이 표를 참조한다. 값은 `defaults.md` DF-21 및 DF-22

| 걸린 시간 | 표시 | 근거 |
|---|---|---|
| 0.1초 이내 | 결과를 바로 표시. 눌림 상태도 이 안에 그림 | NN/g 응답 시간 한계 0.1초 확인 |
| 0.1초에서 1초 | 로딩 표시를 하지 않음 (표시 안 함) | 1초 미만은 결과 표시 외 특별한 피드백이 필요 없음: NN/g 확인 |
| 1초 이상 | 지연 후 스피너 (LD-01) 또는 스켈레톤 (LD-02, 모양이 정해진 화면). 한 번 표시했으면 0.5초 이상 유지해 번쩍임을 막음 | 1초 이상은 작업 중임을 보여야 함: NN/g 확인. 최소 유지 0.5초는 일반 권고, 출처 미확인 |
| 2초 이상 | 무엇을 하는 중인지 설명하는 문구를 덧붙임 (문구 추가) | 2초에서 10초에는 퍼센트가 과할 수 있다는 NN/g 설명 확인. 문구 기준 2초는 일반 권고, 출처 미확인 |
| 10초 이상 | 취소 수단을 제공 (취소 제공). 진행을 측정할 수 있을 때만 퍼센트 또는 진행 막대 (LD-03, LD-04). 측정할 수 없으면 퍼센트 대신 불확정 표시와 지금까지 한 양을 보임 | 10초 이상은 끝날 시점 표시와 중단 수단 필요, 총량을 모르면 지금까지 한 양을 보임: NN/g 확인 |

- `측정 가능할 때만 퍼센트`: 시간 경과나 임의 값으로 퍼센트를 만들지 않는다. NN/g 의 퍼센트 권고는 총량을 아는 작업에 해당한다

## 유사 패턴 구분

| 헷갈리는 쌍 | 고르는 기준 |
|---|---|
| 스피너(LD-01) 대 스켈레톤(LD-02) | 최종 화면의 모양을 미리 알 수 있고 콘텐츠 영역이 크면 스켈레톤, 모양을 알 수 없거나 짧은 작은 영역 대기면 스피너 |
| 진행 막대(LD-03) 대 스피너(LD-01) | 진행률을 실제로 측정할 수 있으면 진행 막대, 측정할 수 없으면 스피너; 측정되지 않은 값을 퍼센트로 꾸며 보이지 않는다 |
| 진행 막대(LD-03) 대 단계 표시(LD-05) | 전송량 또는 처리량처럼 연속으로 늘어나는 값이면 진행 막대, 사용자가 거치는 정해진 화면 수 안의 위치면 단계 표시 |
| 낙관적 업데이트(LD-08) 대 버튼 로딩(LD-06) | 실패 확률이 낮고 되돌릴 수 있는 가벼운 동작이면 낙관적 업데이트, 서버 결과를 확인한 뒤 다음으로 가야 하거나 되돌릴 수 없으면 버튼 로딩 |
| 상단 로딩 바(LD-09) 대 스피너(LD-01) | 화면 전체가 바뀌는 이동의 진행이면 화면 맨 위 상단 로딩 바, 화면 일부 영역의 대기면 그 영역 안 스피너 |

## LD-01 스피너 (Spinner)
- ID: LD-01
- Korean Name: 스피너
- English Name: Spinner
- Category: Loading & Progress
- Definition: 회전하는 원으로 길이를 알 수 없는 대기 중임을 알리는 불확정 로딩 표시
- Purpose: 시스템이 동작 중이며 멈춘 것이 아님을 알림
- User Problem: 아무 변화가 없으면 앱이 멈춘 줄 알고 다시 누르거나 이탈함
- When to Use: 소요 시간 및 진행률을 알 수 없는 짧은 대기; 레이아웃을 미리 알 수 없는 영역; 작은 영역의 데이터 갱신
- When Not to Use: 진행률을 측정할 수 있으면 LD-03 또는 LD-04; 큰 콘텐츠 자리의 대기는 LD-02; 단추 안 대기는 LD-06; 화면 전환은 LD-09
- Interaction Behavior: 대기가 시작되면 나타나고 끝나면 즉시 사라짐; 사용자 조작을 막는 범위는 해당 영역으로 한정; 2초 이상이면 문구를 덧붙이고 10초 이상이면 취소 수단을 제공함 (대기 시간 구간표)
- Required States: 대기 중; 완료(스피너 제거 및 결과 표시); 실패(스피너 제거 및 ES-08 또는 FB-06 안내); 오래 걸릴 때의 추가 문구
- Visual Guidelines: 회전 원 및 문구 "불러오는 중"; 원 대비 3:1(WCAG 1.4.11); 영역 크기에 맞춰 크기 선택; 한 화면에 여러 개를 흩뿌리지 않음
- Accessibility: 로딩 영역에 `aria-busy="true"`, 문구를 `role="status"`로 알림(WCAG 4.1.3); 회전 애니메이션은 `prefers-reduced-motion`에서 줄이거나 정지; 문구 없이 아이콘만 두지 않음
- Responsive Considerations: 모든 화면 크기에서 같은 표시; 좁은 화면에서는 영역 가운데 정렬; 가로 스크롤 영역에서는 해당 영역 안에 위치
- Implementation Guidelines: 스피너를 표시하는 영역을 정해 `aria-busy`를 끝날 때 해제; 아주 짧은 대기에는 표시하지 않아 번쩍임 방지(지연 기준은 1초, 한 번 표시하면 최소 0.5초 유지, DF-21, DF-22); 취소 가능한 작업이면 취소 수단 제공
- Common Mistakes: 진행률을 알 수 있는데도 스피너만 둠; 오류가 나도 계속 돌아감; 문구 없이 전체 화면을 덮음
- Related Patterns: LD-02, LD-03, LD-06
- Reference Image: 장면: 회전 원 및 문구 "불러오는 중"

## LD-02 스켈레톤 (Skeleton)
- ID: LD-02
- Korean Name: 스켈레톤
- English Name: Skeleton
- Category: Loading & Progress
- Definition: 불러올 콘텐츠의 모양을 회색 자리 표시로 먼저 그려 두는 로딩 표시
- Purpose: 최종 레이아웃을 미리 보여 대기 체감을 줄이고 화면이 튀지 않게 함
- User Problem: 빈 화면 뒤에 콘텐츠가 갑자기 나타나 레이아웃이 밀리고 어색함
- When to Use: 목록, 카드, 상세처럼 모양이 예측되는 콘텐츠의 첫 로딩; 크기가 큰 영역
- When Not to Use: 모양을 알 수 없으면 LD-01; 진행률이 있으면 LD-03; 단추 하나의 대기는 LD-06; 이미 보이는 내용 갱신은 기존 내용 유지
- Interaction Behavior: 데이터가 오면 자리 표시가 실제 콘텐츠로 교체됨; 사용자가 조작할 수 없는 영역임을 시각적으로 구분; 실패하면 ES-08 로 교체
- Required States: 로딩 중; 로딩 완료(콘텐츠 교체); 실패; 데이터 없음(ES-01 등으로 교체); 일부만 먼저 도착한 상태
- Visual Guidelines: 썸네일 자리 및 글줄 자리의 회색 자리 표시 2행; 실제 콘텐츠와 같은 크기 및 줄 수; 번쩍이는 효과를 쓰면 느리고 약하게 하며 `prefers-reduced-motion`에서 정지
- Accessibility: 자리 표시 블록은 스크린리더에서 숨기고(`aria-hidden`) 영역에 `aria-busy="true"` 및 로딩 안내 문구 하나를 `role="status"`로 제공; `prefers-reduced-motion`에서는 번쩍이는 효과를 끔
- Responsive Considerations: 화면 폭에 따라 실제 콘텐츠의 열 수와 같은 개수의 자리 표시를 배치; 좁은 화면에서 한 열
- Implementation Guidelines: 콘텐츠 컴포넌트와 같은 레이아웃 크기를 공유해 교체 시 이동이 없게 함; 영역 단위로 로딩 상태를 관리; 아주 짧은 로딩에서는 지연 후 표시 (기준 1초, DF-21)
- Common Mistakes: 실제 모양과 다른 자리 표시로 교체 시 화면이 튐; 로딩이 끝나도 남음; 모든 영역에 무조건 사용
- Related Patterns: LD-01, LD-07, ES-01
- Reference Image: 장면: 썸네일 자리 및 글줄 자리의 회색 자리 표시 2행

## LD-03 진행 막대 (Progress bar)
- ID: LD-03
- Korean Name: 진행 막대
- English Name: Progress bar
- Category: Loading & Progress
- Definition: 가로 막대가 차오르는 정도로 작업의 실제 진행률을 보여주는 표시
- Purpose: 업로드 또는 다운로드 같은 긴 작업이 어디까지 왔는지 알림
- User Problem: 오래 걸리는 작업이 진행 중인지, 얼마나 남았는지 알 수 없음
- When to Use: 전송량, 처리 개수 등으로 진행률을 실제로 측정할 수 있는 작업; 비교적 긴 작업; 남은 시간을 근거 있게 추정할 수 있을 때만 표시
- When Not to Use: 진행률을 측정할 수 없으면 LD-01 또는 LD-02, 가짜 퍼센트 금지(진행률은 시간 경과나 임의 값으로 꾸며 만들지 않는다); 정해진 화면 수의 위치는 LD-05
- Interaction Behavior: 측정값이 갱신될 때마다 막대 및 퍼센트가 늘어남; 완료 시 완료 표시로 바뀜; 취소 가능한 작업이면 취소 수단 제공; 값이 줄어들지 않게 처리
- Required States: 대기(0%); 진행 중(실제 값); 완료; 실패(재시도 수단); 취소됨; 측정 불가로 바뀐 경우 LD-01 로 전환
- Visual Guidelines: "사진 올리는 중" 제목, 막대 68%, "약 10초 남았어요"; 막대 및 배경 구분 3:1(WCAG 1.4.11); 퍼센트 숫자를 병기; 남은 시간 문구는 추정이 가능할 때만
- Accessibility: `<progress>` 또는 `role="progressbar"`와 `aria-valuenow`, 최솟값 및 최댓값 제공(WCAG 4.1.2); 레이블로 무엇이 진행되는지 명시; 큰 진행 변화는 `role="status"`로 요약 알림(WCAG 4.1.3)
- Responsive Considerations: 좁은 화면에서 막대 폭 100%, 문구는 막대 위 또는 아래로 이동; 숫자 문구가 줄바꿈되지 않게 고정 폭 확보
- Implementation Guidelines: `<progress value max>`를 우선 사용; 값은 전송 이벤트 등 실측 소스에서 계산; 측정을 못 하면 `value`를 생략해 불확정 상태로 두거나 LD-01 사용; 느린 구간 때문에 값을 임의로 올리지 않음
- Common Mistakes: 시간에 따라 꾸민 가짜 퍼센트; 99%에서 오래 멈춤을 방치하고 안내가 없음; 남은 시간을 근거 없이 표시
- Related Patterns: LD-01, LD-04, LD-05
- Reference Image: 장면: "사진 올리는 중", 막대 68%, "약 10초 남았어요"

## LD-04 원형 진행 (Progress ring)
- ID: LD-04
- Korean Name: 원형 진행
- English Name: Progress ring
- Category: Loading & Progress
- Definition: 원형 호가 차오르는 정도로 목표 대비 진행 정도를 보여주는 표시
- Purpose: 목표 달성도 또는 작업 진행을 공간을 적게 쓰고 한눈에 보여줌
- User Problem: 목표를 얼마나 채웠는지 숫자만으로는 직관적으로 파악하기 어려움
- When to Use: 달성률처럼 측정된 값을 보여줄 때(목표 대비 현황); 가로 막대를 두기 좁은 영역; 중앙에 숫자를 함께 둘 때
- When Not to Use: 진행률을 측정할 수 없으면 LD-01, 가짜 퍼센트 금지; 긴 작업의 상세 경과는 LD-03; 연속 단계의 위치는 LD-05
- Interaction Behavior: 값이 바뀌면 호가 부드럽게 갱신됨; 누르면 상세 정보를 보여주는 구성도 가능; 완료 시 완료 표시로 전환
- Required States: 0%; 진행 중(실제 값); 목표 달성(100%); 측정 불가(원형 진행 대신 LD-01); 초과 달성 표기 규칙
- Visual Guidelines: 원형 72% 및 문구 "이번 달 저축 목표 5회 중 4회"(장면. 원본 이미지의 두 수치는 서로 맞지 않으며, 구현에서는 퍼센트 및 분수를 같은 값에서 계산); 호 및 배경 구분 3:1(WCAG 1.4.11); 중앙 숫자 4.5:1(WCAG 1.4.3); 분수 또는 퍼센트를 글자로 병기
- Accessibility: `role="progressbar"` 및 `aria-valuenow`, 최솟값, 최댓값; 시각 호만으로 정보를 전하지 않고 "5회 중 4회" 문구 제공(WCAG 1.4.1); 갱신 알림은 필요한 경우만 `role="status"`
- Responsive Considerations: 크기를 영역에 맞추되 중앙 숫자가 읽히는 최소 크기 유지; 좁은 화면에서 문구는 원 아래로 배치
- Implementation Guidelines: SVG 원의 `stroke-dasharray` 등으로 값 계산; 값 소스는 실측 데이터만 사용; 값 범위를 0~100% 내로 제한하고 초과 표기는 따로 정의; `prefers-reduced-motion`에서 애니메이션 생략
- Common Mistakes: 로딩 대기에 임의 값으로 호를 채움; 호만 있고 숫자가 없음; 값이 100%를 넘는 경우를 정의하지 않음
- Related Patterns: LD-03, LD-05, ES-09
- Reference Image: 장면: 원형 72%, "이번 달 저축 목표 5회 중 4회"

## LD-05 단계 표시 (Step indicator)
- ID: LD-05
- Korean Name: 단계 표시
- English Name: Step indicator
- Category: Loading & Progress
- Definition: 여러 단계로 나뉜 흐름에서 전체 단계 수 및 현재 위치를 보여주는 표시; 수량 입력인 스테퍼 FM-08 과 다름
- Purpose: 끝까지 몇 단계가 남았는지 알려 흐름을 이어가게 함
- User Problem: 다단계 입력 도중 지금 어디이고 몇 단계가 남았는지 알 수 없음
- When to Use: 예약, 가입, 결제처럼 단계가 정해진 흐름; 단계 이름이 있고 순서가 있음
- When Not to Use: 연속 진행률이 있는 작업은 LD-03; 단계가 정해지지 않은 흐름; 수량 증감 입력은 FM-08; 화면 이동 구조는 NV 계열
- Interaction Behavior: 다음 단계로 가면 현재 위치가 갱신됨; 지난 단계는 돌아가기가 가능하면 눌러서 이동; 아직 안 간 단계는 비활성
- Required States: 완료 단계; 현재 단계; 남은 단계; 오류가 있는 단계; 이동 불가 단계
- Visual Guidelines: "날짜 고르기 2 / 3" 및 단계 이름 "여행지", "날짜", "확인"; 현재 단계는 색 외 굵기 또는 모양으로 구분(WCAG 1.4.1); 단계 이름은 글자 4.5:1(WCAG 1.4.3)
- Accessibility: 현재 위치를 "2 / 3" 문구로 제공하고 색만으로 구분하지 않음(WCAG 1.4.1); 순서 있는 목록(`<ol>`)으로 구성; 단계가 바뀌면 `role="status"`로 알림(WCAG 4.1.3); 이동 가능한 단계는 키보드로 접근(WCAG 2.1.1)
- Responsive Considerations: 좁은 화면에서 단계 이름을 생략하고 "2 / 3"만 표시하거나 현재 단계 이름만 표시; 가로 스크롤을 만들지 않음
- Implementation Guidelines: 현재 단계 값을 상태 하나로 관리하고 표시 및 화면에서 같이 사용; 단계 수가 바뀌는 흐름에서는 전체 수가 달라질 수 있음을 반영; 뒤로 갈 때 입력값을 보존
- Common Mistakes: 단계 수가 중간에 바뀜; 진행 막대처럼 퍼센트로 표시; 라이브러리에 따라 단계 표시를 Stepper 로 부르기도 하므로 수량 입력(FM-08)과 구분되게 문서에 ID 를 같이 적음
- Related Patterns: LD-03, FM-08, MO-07
- Reference Image: 장면: "날짜 고르기 2 / 3", 단계 이름 "여행지", "날짜", "확인"

## LD-06 버튼 로딩 (Button loading)
- ID: LD-06
- Korean Name: 버튼 로딩
- English Name: Button loading
- Category: Loading & Progress
- Definition: 눌린 단추 안에 대기 표시를 넣고 중복 입력을 막는 로딩 표시
- Purpose: 누른 동작이 처리 중임을 그 자리에서 알리고 중복 제출을 막음
- User Problem: 누른 뒤 반응이 없어 여러 번 누르면 중복 처리가 생김
- When to Use: 저장, 제출, 결제처럼 서버 결과를 확인해야 하는 동작; 단추 하나가 동작을 트리거하는 경우
- When Not to Use: 되돌릴 수 있는 가벼운 동작은 LD-08; 영역 전체의 데이터 로딩은 LD-01 또는 LD-02; 긴 작업의 진행률은 LD-03
- Interaction Behavior: 누르면 단추가 흐려지고 안에 회전 원 및 진행 문구가 나옴; 처리 중에는 다시 눌려도 반응하지 않음; 끝나면 원래 단추로 돌아가거나 성공 표시
- Required States: 기본; 로딩 중(비활성 처리); 성공; 실패(오류 안내 및 재시도); 초점 유지
- Visual Guidelines: 흐려진 단추 안 회전 원 및 "저장 중"; 단추 크기가 바뀌지 않게 유지; 로딩 문구 4.5:1(WCAG 1.4.3)
- Accessibility: 처리 중에는 `aria-disabled="true"`로 표시하고 단추 이름을 "저장 중"으로 바꿈; 초점이 단추에서 사라지지 않게 유지(WCAG 2.4.3); 완료 및 실패는 `role="status"` 또는 `role="alert"`로 알림
- Responsive Considerations: 모든 크기에서 단추 폭을 고정해 문구 변경 시 흔들림 방지; 터치 목표 44x44pt(Apple HIG) 또는 48x48dp(Material Design)
- Implementation Guidelines: `disabled` 대신 `aria-disabled`로 두면 초점을 유지할 수 있음; 서버 처리 중 중복 요청을 상태 값으로 차단; 시간이 길면 취소 수단이나 LD-03 을 고려
- Common Mistakes: 처리 중에도 계속 눌려 중복 제출; 회전 표시만 있고 문구가 없음; 실패 후 단추가 비활성으로 남음
- Related Patterns: LD-01, LD-08, FB-01
- Reference Image: 장면: 흐려진 단추 안 회전 원 및 "저장 중"

## LD-07 이미지 블러 로딩 (Progressive image)
- ID: LD-07
- Korean Name: 이미지 블러 로딩
- English Name: Progressive image
- Category: Loading & Progress
- Definition: 흐린 저해상도 이미지를 먼저 보이고 원본이 도착하면 선명하게 바꾸는 이미지 로딩 방식
- Purpose: 이미지가 올 때까지 빈칸 대신 대략의 모습을 보여 레이아웃 이동을 막음
- User Problem: 이미지가 늦게 나타나 영역이 비어 있거나 레이아웃이 밀림
- When to Use: 큰 이미지, 썸네일 목록, 갤러리처럼 이미지가 콘텐츠의 중심일 때; 네트워크가 느린 환경
- When Not to Use: 작은 아이콘 및 단색 요소; 이미지가 없는 영역의 대기는 LD-02; 저해상도 이미지를 따로 준비할 수 없을 때
- Interaction Behavior: 저해상도 이미지가 먼저 나타나고 원본이 도착하면 부드럽게 교체됨; 사용자는 기다리지 않고 다른 콘텐츠를 읽을 수 있음; 로드 실패 시 자리 표시 이미지로 대체
- Required States: 자리 표시(색 또는 흐린 이미지); 원본 로딩 중; 로드 완료; 로드 실패
- Visual Guidelines: 파란 그라디언트 이미지 안 노란 원 및 흰 막대(장면, 선명한 상태); 영역 크기가 처음부터 고정; 교체 전환은 짧고 부드럽게 (짧음 단 100ms, DF-23); `prefers-reduced-motion`에서 전환 생략
- Accessibility: 이미지에 `alt` 필수, 장식이면 빈 `alt`; 로딩 중 자리 표시는 스크린리더가 중복 읽지 않게 함; 이미지 실패 시 대체 텍스트가 남아야 함
- Responsive Considerations: 화면 크기에 맞는 해상도 선택(`srcset` 등)으로 불필요한 데이터 절감; 영역 비율을 유지해 크기 변화에도 이동 없음
- Implementation Guidelines: `width`와 `height` 또는 CSS `aspect-ratio`로 영역을 예약; 화면 밖 이미지는 `loading="lazy"`를 우선 사용; 흐린 이미지는 작은 크기 파일을 인라인 또는 별도 요청으로 제공
- Common Mistakes: 영역 크기를 예약하지 않아 레이아웃이 밀림; 저해상도 이미지가 원본과 너무 달라 교체 시 놀람; `alt` 누락
- Related Patterns: LD-02, LD-01, MO-06
- Reference Image: 장면: 파란 그라디언트 이미지 안 노란 원 및 흰 막대 (선명한 상태의 장면)

## LD-08 낙관적 업데이트 (Optimistic update)
- ID: LD-08
- Korean Name: 낙관적 업데이트
- English Name: Optimistic update
- Category: Loading & Progress
- Definition: 서버 응답을 기다리지 않고 성공한 것으로 가정해 화면을 먼저 바꾸고, 실패하면 되돌리는 방식
- Purpose: 서버 지연 없이 누르는 순간 반응하는 화면을 제공함
- User Problem: 좋아요처럼 가벼운 동작이 매번 서버를 기다리면 느리고 답답함
- When to Use: 실패 확률이 낮고 되돌릴 수 있는 가벼운 동작(좋아요, 찜, 읽음 처리); 결과를 예측할 수 있을 때
- When Not to Use: 결제, 영구 삭제처럼 되돌릴 수 없는 동작은 LD-06 으로 결과 확인; 서버 값이 결과를 정하는 경우; 실패 확률이 높은 동작
- Interaction Behavior: 누르는 순간 화면(하트, 숫자)이 바로 바뀜; 서버 응답이 성공이면 그대로 확정; 실패하면 원래 상태로 되돌리고 사용자에게 알림; 응답 전 연속으로 누른 경우도 순서대로 처리
- Required States: 낙관 반영 직후; 서버 확정; 실패 시 되돌림; 실패 알림(되돌렸음을 알림 및 재시도); 응답 대기 중 연속 입력 처리
- Visual Guidelines: 하트 및 숫자 13이 바로 바뀜, 문구 "누르는 순간 바로 바뀌어요"; 반영 전후가 색 외 모양으로도 구분(WCAG 1.4.1); 되돌림 시 전환이 눈에 띄게 하되 과하지 않게
- Accessibility: 상태 변화를 `role="status"`로 알림(WCAG 4.1.3); 실패 되돌림 및 알림은 `role="alert"` 또는 FB-01 로 전달; 토글이면 `aria-pressed` 또는 `aria-checked`로 현재 값 노출(WCAG 4.1.2)
- Responsive Considerations: 모든 크기에서 같은 동작; 느린 네트워크에서 되돌림이 늦게 발생할 수 있으므로 화면 이동 후에도 실패 알림이 도달해야 함
- Implementation Guidelines: 낙관 반영 전 이전 값을 보관해 실패 시 복원; 요청마다 순서를 관리해 늦게 온 응답이 최신 상태를 덮어쓰지 않게 함; 같은 대상의 중복 요청은 마지막 입력만 서버에 반영하거나 대기열로 처리
- Common Mistakes: 실패했는데 화면이 그대로 남아 서버와 어긋남; 되돌림을 알리지 않아 사용자가 원인을 모름; 되돌릴 수 없는 동작에 사용
- Related Patterns: LD-06, FB-01, FB-02
- Reference Image: 장면: "여행 후기 모음" 아래 하트 및 숫자 13, 문구 "누르는 순간 바로 바뀌어요"

## LD-09 상단 로딩 바 (Top loading bar)
- ID: LD-09
- Korean Name: 상단 로딩 바
- English Name: Top loading bar
- Category: Loading & Progress
- Definition: 화면 맨 위에 붙은 가는 띠가 진행하며 화면 전환 또는 불러오기 중임을 알리는 표시
- Purpose: 화면 이동 중임을 조작을 막지 않고 알림
- User Problem: 화면 이동을 눌렀는데 반응이 없어 멈춘 줄 알고 다시 누름
- When to Use: 페이지 또는 화면 단위 이동 및 큰 데이터 요청의 진행; 이전 화면 내용을 유지한 채 표시할 때
- When Not to Use: 화면 일부 영역 대기는 LD-01 또는 LD-02; 파일 전송처럼 상세 진행이 필요하면 LD-03; 버튼 하나의 처리는 LD-06
- Interaction Behavior: 이동이 시작되면 위에서 띠가 진행하고 완료되면 끝까지 차오른 뒤 사라짐; 사용자는 그동안 화면을 계속 조작할 수 있음; 실패하면 띠가 사라지고 오류 안내
- Required States: 대기 시작; 진행 중(불확정 또는 실측); 완료; 실패; 취소(다른 이동으로 대체)
- Visual Guidelines: "상품 상세" 화면 맨 위 가는 띠가 진행; 띠 및 배경 구분 3:1(WCAG 1.4.11); 헤더 위나 바로 아래에 고정되어 다른 요소를 가리지 않음
- Accessibility: 띠 자체는 보조 표시이므로 화면에 `aria-busy="true"` 및 `role="status"` 문구를 함께 제공(WCAG 4.1.3); 진행률을 모르면 `role="progressbar"`에서 `aria-valuenow`를 생략; 움직임은 `prefers-reduced-motion`에서 줄임
- Responsive Considerations: 모든 화면 폭에서 가로 전체를 덮음; 모바일 상태 표시줄 및 고정 헤더와 겹치지 않게 위치 조정
- Implementation Guidelines: `position: fixed` 또는 `sticky`로 맨 위에 두고 이동 시작 및 종료 이벤트에 연결; 진행률을 모르면 가짜 비율 대신 불확정 애니메이션 사용; 이동이 짧으면 표시 지연 후 노출 (기준 1초, DF-21)
- Common Mistakes: 가짜 비율로 80%까지 올린 뒤 멈춤; 완료되었는데 사라지지 않음; 오류가 나도 띠만 사라지고 안내가 없음
- Related Patterns: LD-01, LD-03, NV-08
- Reference Image: 장면: "상품 상세" 화면 맨 위 가는 띠가 진행
