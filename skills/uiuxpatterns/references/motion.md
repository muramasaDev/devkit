# Motion & Animation (움직임)

- 범위: 움직임 9종. MO-01 ~ 04 속도 곡선, MO-05 ~ 07 등장 방식, MO-08 ~ 09 화면 전환
- 색인: `pattern-catalog.md`
- 값 정본: `defaults.md` (본문의 DF-nn 은 그 표의 항목 번호)

## 공통 원칙
- 움직임은 상태 변화를 이해시키는 용도이고 장식으로 쓰지 않는다
- 움직임은 실제 UI 상태와 동기화한다 (끝난 뒤의 상태가 화면의 진실이고, 움직임 중에도 입력 및 초점이 상태를 따른다)
- `prefers-reduced-motion` 에서는 움직임을 줄이거나 끈다 (이동은 페이드 또는 즉시 교체로 바꿈). 켜짐일 때 이동, 확대, 회전, 계속 도는 애니메이션은 끄고 투명도 및 색 변화는 유지하며 전역 `animation-duration: 0.01ms` 는 쓰지 않는다 (DF-20, `interaction-rules.md` 7절과 같다)
- 애니메이션은 transform 및 opacity 위주로 하고 너비, 높이, 위치 같은 레이아웃 속성은 피한다
- 시간 값 및 곡선 값은 토큰 한 곳에서 정한다. 기본값은 `defaults.md` 를 따른다: 짧음 100ms, 보통 300ms, 김 500ms (DF-13), 곡선 (DF-14). 토큰 값은 Material Web 토큰 파일에서 확인했고 용도별 단 배정은 일반 권고이다. 원본 이미지에는 ms 및 베지어 값이 없다

## 유사 패턴 구분
| 헷갈리는 쌍 | 고르는 기준 |
|---|---|
| 이즈 인 (MO-01) 대 이즈 아웃 (MO-02) | 이즈 인은 천천히 출발해 빠르게 끝나므로 화면에서 나갈 때, 이즈 아웃은 빠르게 시작해 살살 멈추므로 화면에 들어올 때 |
| 이즈 아웃 (MO-02) 대 스프링 (MO-03) | 이즈 아웃은 정해진 시간의 곡선, 스프링은 물리 모델이라 제스처를 놓은 뒤 속도를 이어받고 도중에 목표가 바뀌어도 끊기지 않음 |
| 스프링 (MO-03) 대 바운스 (MO-04) | 스프링은 물리 모델로 감쇠 값에 따라 목표를 살짝 넘었다가 안착, 바운스는 목표에 닿은 뒤 되튀는 모습을 눈에 띄게 보이는 연출. 바운스는 완료 같은 드문 순간에만 |
| 슬라이드 (MO-07) 대 페이드 (MO-06) | 방향이 있는 이동 (다음 단계, 이전 단계) 은 슬라이드, 위치 이동 없이 나타나거나 값이 바뀔 때는 페이드 |
| 확대 전환 (MO-08) 대 공유 요소 전환 (MO-09) | 확대 전환은 작은 카드가 화면 영역으로 커지며 출처 위치를 보임, 공유 요소 전환은 같은 요소 (이미지, 제목) 하나가 두 화면 사이에서 이어져 이동 |
| 순차 등장 (MO-05) 대 일괄 등장 | 항목이 적고 처음 보일 때만 순차. 항목이 많거나 반복해서 보이면 일괄 등장 (총 지연이 누적됨) |

## MO-01 이즈 인 (Ease-in)
- ID: MO-01
- Korean Name: 이즈 인
- English Name: Ease-in
- Category: Motion & Animation (07)
- Definition: 느리게 시작해 갈수록 빨라지는 속도 곡선
- Purpose: 화면 밖으로 나가는 요소의 퇴장을 자연스럽게 표현
- User Problem: 요소가 갑자기 사라지면 어디로 갔는지 알 수 없음
- When to Use: 닫히는 시트, 사라지는 알림, 화면을 떠나는 요소; 끝에서 화면 밖으로 완전히 나가는 이동
- When Not to Use: 화면에 들어오는 요소 (반응이 늦게 시작해 느리게 느껴짐); 사용자 입력에 즉시 반응해야 하는 피드백; 화면 안 목표 위치에 멈추는 이동
- Interaction Behavior: 시작은 느리고 끝으로 갈수록 빨라짐; 끝에서 요소가 화면 밖으로 나가거나 사라짐; 중간에 취소되면 현재 위치에서 이어서 반응
- Required States: 시작 전; 진행 중; 종료 (요소 숨김 또는 제거); 중단; reduced-motion
- Visual Guidelines: 끝이 가장 빠르므로 화면 밖으로 완전히 나가는 이동에만 씀; 시간은 같은 요소의 들어올 때보다 한 단 짧게 둠 (DF-15)
- Accessibility: reduced-motion 에서 즉시 숨김 또는 페이드; 나간 요소는 `inert` 또는 `hidden` 으로 초점 및 읽기 대상에서 제외; 닫힘 뒤 초점 복귀
- Responsive Considerations: 데스크톱 및 터치에서 같은 곡선; 이동 거리가 화면 크기에 따라 달라지므로 시간은 DF-13 의 3단 중에서 거리에 맞춰 한 단 올리거나 내림
- Implementation Guidelines: CSS `transition-timing-function` 에 곡선 토큰 하나를 지정하고 이름은 용도 (퇴장) 로 붙임; transform 및 opacity 만 변경; 끝나면 상태 값 (열림, 닫힘) 을 갱신
- Common Mistakes: 모든 전환에 같은 곡선 하나; 입장에 이즈 인을 써서 반응이 굼뜸; 퇴장 후 요소가 남아 초점을 받음; 곡선 값을 컴포넌트마다 따로 적음
- Related Patterns: MO-02, MO-07, FB-01, FB-05
- Reference Image: 장면: 이즈 인 카드: 사각형 및 문구 "천천히 출발해서 빠르게 나가요"

## MO-02 이즈 아웃 (Ease-out)
- ID: MO-02
- Korean Name: 이즈 아웃
- English Name: Ease-out
- Category: Motion & Animation (07)
- Definition: 빠르게 시작해 갈수록 느려지며 멈추는 속도 곡선
- Purpose: 화면에 들어오는 요소 및 입력에 대한 반응을 즉각적이면서 부드럽게 표현
- User Problem: 입력 뒤 반응이 늦거나 갑자기 멈추면 시스템이 굼뜨거나 거칠게 느껴짐
- When to Use: 들어오는 요소 (시트, 메뉴, 대화 상자); 눌림 및 펼침 같은 입력 반응; 화면 안 목표 위치에 멈추는 이동
- When Not to Use: 화면 밖으로 나가는 퇴장 (MO-01); 제스처를 놓은 뒤 속도를 이어받아야 하는 이동 (MO-03)
- Interaction Behavior: 시작이 바로 빠르게 일어나 반응이 즉각적이고, 목표 가까이에서 속도가 줄어 멈춤; 중간에 방향이 바뀌면 현재 값에서 새 목표로 이어서 이동
- Required States: 시작 전; 진행 중; 도착 (최종 상태 확정); 중단; reduced-motion
- Visual Guidelines: 도착 지점이 분명하게 보이도록 멈추는 구간을 유지; 입장 시간을 퇴장보다 길게 둠 (DF-15)
- Accessibility: reduced-motion 에서 즉시 도착 또는 페이드; 대화 상자는 도착 전에도 초점이 들어가고 상태 (`aria-modal`) 가 맞아야 함; 진행 중 입력을 막는지 여부를 명확히
- Responsive Considerations: 터치 및 데스크톱에서 같은 곡선; hover 반응은 짧음 단 100ms (DF-13)
- Implementation Guidelines: 입장용 곡선 토큰을 하나 정해 재사용 (기본 `cubic-bezier(0, 0, 0, 1)`, DF-14); transform 및 opacity 만 변경; 도착 즉시 입력을 받을 수 있게 상태를 먼저 갱신
- Common Mistakes: 기본값 곡선을 그대로 사용해 의도 없는 조합; 입장 중 입력을 받지 않음; 퇴장에도 같은 곡선을 씀; 도착 후 위치가 어긋남
- Related Patterns: MO-01, MO-03, MO-06, FB-04
- Reference Image: 장면: 이즈 아웃 카드: 사각형 및 문구 "빠르게 들어와서 살살 멈춰요"

## MO-03 스프링 (Spring)
- ID: MO-03
- Korean Name: 스프링
- English Name: Spring
- Category: Motion & Animation (07)
- Definition: 물리 모델의 용수철처럼 목표 위치에 안착하는 움직임
- Purpose: 손의 움직임을 이어받아 자연스럽게 마무리하고 중단에도 끊기지 않게 함
- User Problem: 고정 시간 곡선은 제스처를 놓은 뒤의 속도와 어긋나 부자연스럽고, 도중에 멈추면 끊겨 보임
- When to Use: 아래에서 올라오는 시트; 드래그를 놓은 뒤 제자리로 안착; 도중에 방향이 바뀔 수 있는 이동
- When Not to Use: 수치 읽기가 중요한 값 변화; 출렁임이 의미 없는 정적 전환; 움직임을 최소화해야 하는 환경
- Interaction Behavior: 놓은 순간의 속도에서 이어서 목표로 이동; 도중에 목표가 바뀌면 현재 위치 및 속도에서 새 목표로 이어서 이동; 강성 및 감쇠 값은 모션 라이브러리 기본값을 그대로 씀 (DF-17)
- Required States: 대기; 이동 중; 안착 (최종 상태); 중단 및 재개; reduced-motion
- Visual Guidelines: 출렁임은 크게 두지 않고 안착이 분명하게 보임; 같은 역할의 요소는 같은 설정을 씀
- Accessibility: reduced-motion 에서 출렁임 없이 도착 위치로 이동 또는 짧은 페이드; 움직임 중에도 최종 상태가 보조기기에 반영됨; 안착 전에도 입력을 받고 현재 위치 및 속도에서 이어감 (DF-17)
- Responsive Considerations: 터치 제스처에 잘 맞고, 데스크톱 마우스 드래그에도 같은 방식 적용; 마우스 hover 에는 쓰지 않음
- Implementation Guidelines: 최종 상태는 곡선과 무관하게 같은 값으로 끝나게 함; CSS 로 근사하거나 스크립트로 계산하되 속도를 이어받는 경우 스크립트가 필요; 상태 값은 안착 전 먼저 갱신
- Common Mistakes: 출렁임이 과해 읽기를 방해; 움직임이 끝난 뒤에야 입력을 받음; 설정 값이 컴포넌트마다 다름; reduced-motion 처리 누락
- Related Patterns: MO-02, MO-04, GS-05, FB-05
- Reference Image: 장면: 스프링 카드: 아래에서 올라오는 시트

## MO-04 바운스 (Bounce)
- ID: MO-04
- Korean Name: 바운스
- English Name: Bounce
- Category: Motion & Animation (07)
- Definition: 목표 지점에서 눈에 띄게 튕기며 멈추는 움직임
- Purpose: 결제 완료 같은 드문 완료 순간을 강조
- User Problem: 중요한 완료가 조용히 지나가면 성공했는지 확신하기 어려움
- When to Use: 사용 범위가 좁음. 한 번 보이는 완료 순간 (결제 완료, 목표 달성); 화면에 하나뿐인 강조
- When Not to Use: 일상 요소 (단추, 목록, 메뉴); 반복되는 알림; 오류 및 경고; 한 화면에 여러 개; 자주 도달하는 상태
- Interaction Behavior: 한 번 튕기고 멈춤; 반복하지 않음; 완료 문구는 움직임 없이도 읽힘
- Required States: 대기; 재생 중; 완료 후 정지; reduced-motion (정지 상태의 최종 모양)
- Visual Guidelines: 크기 및 횟수를 작게 유지; 완료 문구 (원본 이미지: "결제 완료!") 와 함께 쓰며 움직임이 의미를 대신하지 않음
- Accessibility: 완료를 `role="status"` 로 글자 알림; reduced-motion 에서 정지한 체크 표시; 5초 넘게 자동 반복하지 않고 한 번 재생 후 멈춤 (WCAG 2.2.2)
- Responsive Considerations: 데스크톱 및 터치에서 같은 동작; 화면이 좁을 때 튕김 범위가 화면 밖으로 넘지 않게 함
- Implementation Guidelines: 일회성 효과로 만들고 트리거를 완료 이벤트 한 곳에 연결; 크기 변화는 transform; 사용처를 완료 순간으로 제한하고 일상 컴포넌트에는 붙이지 않음
- Common Mistakes: 일상 UI 전반에 바운스를 사용해 산만; 반복 재생; 움직임만으로 완료를 전달; 오류 화면에 사용
- Related Patterns: MO-03, FB-01, ES-06, LD-03
- Reference Image: 장면: 바운스 카드: 초록 점 및 문구 "결제 완료!"

## MO-05 순차 등장 (Stagger)
- ID: MO-05
- Korean Name: 순차 등장
- English Name: Stagger
- Category: Motion & Animation (07)
- Definition: 여러 요소가 시작 시점을 조금씩 어긋나게 차례로 나타나는 움직임
- Purpose: 묶음 안 항목의 순서 및 개수를 눈으로 따라가게 함
- User Problem: 여러 항목이 한꺼번에 나타나면 어디부터 볼지 알 수 없음
- When to Use: 처음 불러온 소수의 목록 및 카드; 단계별로 읽는 안내; 결과 화면의 첫 진입
- When Not to Use: 항목이 많은 목록 (총 시간이 길어짐); 재방문 및 반복 노출; 사용자가 빨리 찾아야 하는 목록; 스크롤할 때마다 나타나는 항목
- Interaction Behavior: 읽는 순서대로 항목 시작 시점이 어긋남; 항목당 50ms 시차, 전체 상한 500ms (DF-16); 도중에 이동하면 남은 항목을 즉시 표시
- Required States: 대기 (자리만 있음); 순차 진행; 모두 표시; 중단 (즉시 모두 표시); reduced-motion
- Visual Guidelines: 개별 효과는 페이드 또는 짧은 이동 한 가지로 통일; 자리 표시 (스켈레톤, LD-02) 와 최종 배치가 어긋나지 않음
- Accessibility: DOM 순서 및 초점 순서 유지 (WCAG 2.4.3); 아직 나타나지 않은 항목이 초점을 받지 않음; reduced-motion 에서는 한꺼번에 표시
- Responsive Considerations: 열이 여러 개인 화면은 행 단위로 묶어 순서를 정함; 항목이 한 화면에 더 많이 보이면 총 시간이 길어지므로 상한을 둠
- Implementation Guidelines: 항목 순번을 CSS 변수로 넘겨 지연을 계산하고 간격은 토큰 한 곳에서 정함 (기본 50ms, DF-16); 데이터 로딩이 끝난 뒤에만 시작; 지연 중 레이아웃이 움직이지 않게 자리 확보
- Common Mistakes: 항목 수가 늘어도 간격을 그대로 두어 총 시간이 길어짐; 재방문 때마다 반복; 지연 중 클릭이 안 됨; reduced-motion 누락
- Related Patterns: MO-06, LD-02, FB-09, NV-08
- Reference Image: 장면: 순차 등장 카드: 목록 "오사카", "후쿠오카", "삿포로"

## MO-06 페이드 (Fade)
- ID: MO-06
- Korean Name: 페이드
- English Name: Fade
- Category: Motion & Animation (07)
- Definition: 투명도를 바꿔 요소가 서서히 나타나거나 사라지는 움직임
- Purpose: 위치 이동 없이 요소를 나타내거나 값을 바꿈
- User Problem: 값이나 내용이 갑자기 바뀌면 바뀐 줄 모르고 지나치거나 화면이 깜빡임
- When to Use: 위치가 고정된 내용의 등장 및 퇴장; 숫자 및 문구 교체 (원본 이미지: 저축률); 슬라이드가 과한 곳의 대체 (reduced-motion)
- When Not to Use: 방향이 있는 이동 (MO-07); 큰 면적의 장면 전환에서 맥락 단서가 필요할 때
- Interaction Behavior: 투명도가 0 에서 1 로 또는 반대로 변함; 값 교체 시 이전 값이 사라진 뒤 새 값이 나타남; 시간은 보통 단 300ms (DF-13)
- Required States: 숨김; 나타나는 중; 표시; 사라지는 중; 중단 시 현재 투명도에서 이어감
- Visual Guidelines: 전환이 끝난 상태에서 글자 대비 4.5:1 (WCAG 1.4.3); 겹친 두 값이 동시에 읽히는 구간을 짧게 둠
- Accessibility: 투명해진 요소도 접근성 트리에 남으므로 숨길 때 `hidden` 또는 `inert` 도 적용; 값 변경은 `role="status"` 로 알림; 깜빡임 구간을 두지 않음
- Responsive Considerations: 데스크톱 및 터치에서 같은 동작; 가장 가벼운 전환이라 성능이 낮은 기기의 대체 전환으로 씀
- Implementation Guidelines: opacity 만 변경; 퇴장 뒤 `visibility` 또는 `hidden` 으로 정리해 클릭을 막음; 값 교체 때 레이아웃 크기가 변하지 않도록 자리 확보
- Common Mistakes: 투명해졌지만 클릭 및 초점을 계속 받음; 레이아웃 속성과 함께 애니메이션; 교체 중 두 값이 겹쳐 읽히지 않음; 알림 없는 값 변경
- Related Patterns: MO-02, MO-07, LD-07, FB-01
- Reference Image: 장면: 페이드 카드: 문구 "이번 달 저축률 24%"

## MO-07 슬라이드 (Slide)
- ID: MO-07
- Korean Name: 슬라이드
- English Name: Slide
- Category: Motion & Animation (07)
- Definition: 요소 또는 화면이 옆이나 아래에서 밀려 들어오고 나가는 움직임
- Purpose: 앞으로 가기 및 뒤로 가기의 방향을 화면 이동으로 알려줌
- User Problem: 화면이 갑자기 바뀌면 단계 흐름 및 현재 위치를 놓침
- When to Use: 단계 진행 (원본 이미지: 2단계에서 다음 화면); 계층 이동; 시트 및 패널의 입장
- When Not to Use: 같은 계층의 탭 내용 교체 (페이드가 나음); 면적이 매우 큰 이동 (움직임에 민감한 사용자 부담); 빈번한 반복 전환
- Interaction Behavior: 앞으로는 새 화면이 들어오는 방향, 뒤로는 반대 방향으로 이동; 두 화면이 함께 움직이거나 한 화면이 위로 겹침; 시간은 보통 단 300ms (DF-13, DF-18)
- Required States: 이전 화면; 이동 중; 새 화면; 취소 (제스처로 시작한 경우 복귀); reduced-motion
- Visual Guidelines: 방향 규칙을 제품 전체에서 하나로 통일; 이동 거리는 전체 폭 대신 30px 로 짧게 하고 페이드를 병행 (DF-18)
- Accessibility: 이동 뒤 초점을 새 화면 제목 또는 첫 요소로 옮김 (WCAG 2.4.3); reduced-motion 에서 페이드 또는 즉시 교체; 큰 면적의 움직임은 움직임에 민감한 사용자에게 불편을 줄 수 있어 줄임
- Responsive Considerations: 좁은 화면은 전체 화면 이동, 넓은 화면은 패널이 옆에서 나타나는 이동으로 범위를 줄임; 데스크톱 키보드 이동에서도 같은 효과
- Implementation Guidelines: `transform: translate` 로 이동하고 left, margin 같은 레이아웃 속성은 피함; 나간 화면은 `inert` 처리; 뒤로 가기는 역방향 재생
- Common Mistakes: 앞으로 및 뒤로 가는 방향이 일정하지 않음; 이동 후 초점이 이전 화면에 남음; 큰 화면에서 전체 폭을 이동시켜 어지러움; 레이아웃 속성 애니메이션
- Related Patterns: MO-01, MO-02, MO-06, LD-05, NV-09
- Reference Image: 장면: 슬라이드 카드: "2단계 날짜 고르기" 화면 및 옆에서 들어오는 다음 화면

## MO-08 확대 전환 (Zoom transition)
- ID: MO-08
- Korean Name: 확대 전환
- English Name: Zoom transition
- Category: Motion & Animation (07)
- Definition: 작은 요소 자리에서 영역이 커지며 새 화면으로 바뀌는 전환
- Purpose: 상세 화면이 어디에서 왔는지 보여 공간적 맥락을 유지
- User Problem: 카드를 눌러 상세로 가면 어느 항목의 상세인지 놓치고 돌아올 때도 위치를 잃음
- When to Use: 카드 및 썸네일에서 상세 화면 열기; 목록으로 돌아올 때 같은 자리로 축소
- When Not to Use: 출발 요소가 화면 밖이거나 없는 경우; 목록이 바뀌어 돌아올 자리가 없는 경우; 빈번한 반복 전환
- Interaction Behavior: 눌린 요소의 위치 및 크기에서 시작해 화면 영역으로 확대; 닫으면 같은 자리로 축소; 시간은 김 단 500ms (DF-13)
- Required States: 목록; 확대 중; 상세; 축소 중; 출발 요소 없음 (페이드로 대체); reduced-motion
- Visual Guidelines: 확대되는 영역의 모서리 및 색이 출발 요소와 이어짐; 내용이 늘어나 보이지 않도록 영역 및 내용을 따로 처리
- Accessibility: reduced-motion 에서 페이드 또는 즉시 교체; 전환 뒤 초점을 상세 화면 제목으로 옮기고 닫을 때 출발 요소로 복귀; 목록 위치 유지
- Responsive Considerations: 화면 크기에 맞춰 확대 대상 영역이 달라짐; 데스크톱 넓은 화면은 전체 확대 대신 패널 확대로 범위를 줄임 (DF-19)
- Implementation Guidelines: View Transitions API 사용 시 지원 범위가 브라우저마다 다르므로 미지원 시 페이드로 대체; 확대는 transform 로 처리하고 레이아웃 속성 애니메이션 회피
- Common Mistakes: 출발 요소가 사라진 상태에서 확대; 닫을 때 다른 자리로 돌아감; 내용이 찌그러져 보임; 지원하지 않는 브라우저의 대체 없음
- Related Patterns: MO-09, MO-06, GS-07, GS-06
- Reference Image: 장면: 확대 전환 카드: 작은 카드 자리에서 커지는 파란 영역

## MO-09 공유 요소 전환 (Shared element transition)
- ID: MO-09
- Korean Name: 공유 요소 전환
- English Name: Shared element transition
- Category: Motion & Animation (07)
- Definition: 두 화면에 모두 있는 같은 요소가 이어져 움직이며 화면이 바뀌는 전환
- Purpose: 같은 대상을 두 화면에서 이어 보여 연속성을 줌
- User Problem: 목록의 이미지가 상세의 이미지와 같은 것인지 알아보기 어려움
- When to Use: 목록 썸네일에서 상세 대표 이미지로; 제목 및 대표 요소 한두 개; 두 화면에 같은 요소가 있을 때
- When Not to Use: 두 화면에 같은 요소가 없을 때; 이어질 요소가 여러 개라 산만할 때; 지원 환경이 없고 대체 전환도 없을 때
- Interaction Behavior: 요소가 위치 및 크기를 바꾸며 이어지고 나머지 내용은 페이드 또는 슬라이드로 바뀜; 시간은 김 단 500ms (DF-13)
- Required States: 출발 화면; 이어지는 중; 도착 화면; 중단 및 취소; 이어질 요소 없음 (페이드로 대체); reduced-motion
- Visual Guidelines: 이어지는 요소를 한두 개로 제한; 원본 이미지는 왼쪽 위의 파란 사각형이 이어지는 동작 중간 장면
- Accessibility: reduced-motion 에서 이어짐 없이 페이드 또는 즉시 교체; 도착 화면에서 초점을 제목으로 옮김; 이어지는 요소가 읽기 순서를 바꾸지 않음
- Responsive Considerations: 화면 크기에 따라 도착 위치가 달라지므로 도착 위치를 계산하고 데스크톱에서도 같은 방식 적용; 좁은 화면에서는 이어짐 요소 수를 줄임
- Implementation Guidelines: View Transitions API 와 `view-transition-name` 을 쓰며 지원 범위가 브라우저마다 다름; 같은 시점에 같은 이름이 둘 이상이면 전환이 적용되지 않으므로 항목별로 고유한 이름을 부여; 미지원 시 페이드로 대체
- Common Mistakes: 이름 중복으로 전환이 실패; 이어지는 요소가 너무 많아 산만; 미지원 브라우저 대체 없음; 도착 후 초점 위치가 어긋남
- Related Patterns: MO-08, MO-06, MO-07, NV-09
- Reference Image: 장면: 공유 요소 전환 카드: 화면 왼쪽 위의 파란 사각형 요소 (동작 중간 장면)
