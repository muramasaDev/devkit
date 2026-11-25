# Forms & Inputs (원본 이미지 없음)

원본 이미지 파일 미확보. 본문 설명은 일반 UI 지식이다

- 범위: 값을 입력하거나 선택지에서 고르는 입력 컨트롤 9종
- 참조 이미지: 없음 (원본 이미지 미확보)
- 색인: `pattern-catalog.md`

## 유사 패턴 구분

| 헷갈리는 쌍 | 고르는 기준 |
|---|---|
| 셀렉트(FM-02) 대 라디오 버튼(FM-06) 대 세그먼트 컨트롤(FM-03) | 선택지 수로 고름; 선택지가 적고 한눈에 비교해야 하면 라디오 또는 세그먼트 컨트롤, 선택지가 많아 목록을 접어 두어야 하면 셀렉트; 보기 전환처럼 즉시 화면을 바꾸는 소수 선택이면 세그먼트 컨트롤; 기준 개수는 제품에서 정한다 |
| 스위치(FM-04) 대 체크박스(FM-05) | 누르는 즉시 적용되는 켬 및 끔 설정이면 스위치; 여러 항목을 고른 뒤 제출할 때 적용되거나 동의 및 복수 선택이면 체크박스 |
| 슬라이더(FM-07) 대 스테퍼(FM-08) | 범위 안에서 대략적인 값을 연속으로 고르면 슬라이더; 정확한 정수 하나를 한 칸씩 바꾸면 스테퍼; 슬라이더는 정밀 입력에 부적합, 스테퍼는 큰 폭 이동에 부적합 |
| 체크박스(FM-05) 대 라디오 버튼(FM-06) | 여러 개 동시 선택 가능하면 체크박스, 하나만 선택하면 라디오 버튼 |
| 텍스트 필드(FM-01) 대 날짜 선택기(FM-09) | 형식이 정해진 날짜 값은 날짜 선택기, 자유 문자열은 텍스트 필드; 날짜 선택기도 직접 입력을 허용 |

## FM-01 텍스트 필드 상태 (Text field states)
- ID: FM-01
- Korean Name: 텍스트 필드 상태
- English Name: Text field states
- Category: Forms & Inputs
- Definition: 글자를 입력하는 필드가 가지는 상태(기본, 초점, 입력됨, 오류, 비활성, 읽기 전용)와 각 상태의 표현
- Purpose: 필드가 지금 무엇을 기대하고 어떤 상태인지 일관되게 알림
- User Problem: 어느 필드가 입력 가능한지, 틀렸는지, 수정할 수 없는지 구분하기 어려움
- When to Use: 한 줄 또는 여러 줄 자유 입력(이름, 이메일, 검색어, 메모); 서버로 제출되는 문자열 값
- When Not to Use: 선택지가 정해져 있으면 FM-02, FM-03, FM-06; 날짜는 FM-09; 수량 증감은 FM-08
- Interaction Behavior: 눌러서 초점을 받고 입력함; 입력 중에는 오류를 띄우지 않고 벗어날 때 또는 제출 시 검증; 비활성은 초점 및 입력 불가; 읽기 전용은 초점은 받고 복사 가능하며 수정 불가
- Required States: 기본; 초점; 입력됨; 오류(문구 포함); 비활성; 읽기 전용
- Visual Guidelines: 상태마다 테두리 또는 배경이 구분됨; 초점은 `:focus-visible` 표시(WCAG 2.4.7); 입력 경계 3:1(WCAG 1.4.11); 오류는 색만으로 알리지 않고 문구 병행(WCAG 1.4.1)
- Accessibility: 보이는 `<label>` 필수, 플레이스홀더로 레이블 대체 금지(WCAG 3.3.2); 오류 시 `aria-invalid` 및 `aria-describedby`(WCAG 3.3.1, 3.3.3); 비활성 및 읽기 전용은 의미가 달라 구분하여 구현
- Responsive Considerations: 좁은 화면에서 필드 폭 100% 사용; 터치 목표 44x44pt(Apple HIG) 또는 48x48dp(Material Design); 입력 종류에 맞는 `type` 및 `inputmode`로 알맞은 키보드 노출
- Implementation Guidelines: `<input>` 또는 `<textarea>`와 `<label for>` 사용; `disabled`는 제출에서 제외되고 초점을 못 받고, `readonly`는 제출되고 초점을 받는 차이를 의도에 맞게 선택; 도움말 및 오류 문구를 `aria-describedby`로 연결
- Common Mistakes: 플레이스홀더만 있고 레이블 없음; 비활성 이유를 알려주지 않음; 입력 도중 키 입력마다 오류 표시; 읽기 전용 값을 비활성으로 구현해 복사 불가
- Related Patterns: FB-06, FM-02, FM-09
- Reference Image: 없음 (원본 이미지 미확보)

## FM-02 셀렉트 (Select)
- ID: FM-02
- Korean Name: 셀렉트
- English Name: Select
- Category: Forms & Inputs
- Definition: 접힌 목록에서 선택지 하나를 고르는 입력 컨트롤
- Purpose: 많은 선택지를 좁은 공간에 담아 하나만 고르게 함
- User Problem: 선택지가 많을 때 모두 펼쳐 놓으면 화면을 차지하고 비교하기 어려움
- When to Use: 선택지가 많고 한 번에 하나만 선택; 국가, 지역처럼 목록이 긴 값; 값이 미리 정해져 있음
- When Not to Use: 선택지가 적어 한눈에 보이면 FM-06 또는 FM-03(기준 개수는 제품에서 정한다); 복수 선택은 FM-05 목록; 자유 입력은 FM-01
- Interaction Behavior: 누르면 목록이 열리고 항목을 고르면 닫히고 값이 반영됨; 키보드로 열기, 이동, 선택; 선택하지 않은 초기 상태는 안내 문구로 표시
- Required States: 기본(미선택 안내); 열림; 선택됨; 초점; 오류; 비활성
- Visual Guidelines: 현재 값 및 펼침 표시(화살표)가 보임; 초점 표시(WCAG 2.4.7); 경계 및 화살표 3:1(WCAG 1.4.11); 긴 값은 말줄임 처리 및 전체 값 확인 수단
- Accessibility: 보이는 레이블 필수(WCAG 3.3.2); 기본 `<select>`는 이름, 역할, 값을 제공(WCAG 4.1.2); 사용자 정의 컴포넌트는 `aria-haspopup` 및 `aria-expanded`와 키보드 조작을 직접 구현해야 함
- Responsive Considerations: 모바일에서는 운영체제 기본 선택기를 쓰는 편이 조작이 안정적; 좁은 화면에서 긴 선택지 문구가 잘리지 않게 폭 확인
- Implementation Guidelines: 가능하면 `<select>`와 `<option>` 사용; 목록이 매우 길면 검색 가능한 별도 패턴을 검토; 선택지 그룹이 있으면 `<optgroup>`
- Common Mistakes: 선택지 두세 개에도 셀렉트를 써서 한 번 더 누르게 함; 미선택 상태와 첫 항목이 구분되지 않음; 목록이 화면 밖으로 잘림
- Related Patterns: FM-03, FM-06, FM-01
- Reference Image: 없음 (원본 이미지 미확보)

## FM-03 세그먼트 (Segmented control)
- ID: FM-03
- Korean Name: 세그먼트
- English Name: Segmented control
- Category: Forms & Inputs
- Definition: 나란히 붙은 소수의 선택지 중 하나를 고르는 가로 막대형 컨트롤
- Purpose: 상호 배타적인 소수 선택지를 한 줄에서 바로 비교하고 전환함
- User Problem: 두세 가지 보기 또는 옵션을 전환하는데 라디오는 공간을 많이 차지하고 셀렉트는 단계가 많음
- When to Use: 선택지가 소수이고 항상 하나가 선택된 상태; 같은 화면에서 보기 방식 또는 범위 전환(예: 편도, 왕복)
- When Not to Use: 선택지가 많으면 FM-02; 콘텐츠 영역 전체를 바꾸는 이동은 NV-02; 복수 선택은 FM-05; 선택지 설명이 길면 FM-06
- Interaction Behavior: 항목을 누르면 즉시 선택이 바뀜; 항상 정확히 하나 선택; 키보드 방향키로 이동 및 선택
- Required States: 선택됨; 선택 안 됨; 초점; 비활성; 항상 하나가 선택된 기본값
- Visual Guidelines: 선택 항목은 배경 또는 굵기로 구분하고 색만으로 구분하지 않음(WCAG 1.4.1); 항목 구분선 및 경계 3:1(WCAG 1.4.11); 항목 폭은 문구에 맞추되 균등
- Accessibility: 의미는 라디오 그룹; `<fieldset>`/`<legend>`로 묶고 `<input type="radio">`를 시각적으로 꾸미는 구현 권장; 콘텐츠 패널을 바꾸는 용도면 탭 역할(`tablist`/`tab`/`tabpanel`, `aria-selected`) 사용
- Responsive Considerations: 좁은 화면에서 항목 문구가 줄바꿈되거나 잘리지 않게 항목 수를 제한; 터치 목표 44x44pt(Apple HIG) 또는 48x48dp(Material Design)
- Implementation Guidelines: 라디오 입력 및 레이블을 그대로 쓰고 스타일만 입혀 폼 제출 및 키보드 동작을 확보; 선택 즉시 반영 여부 및 제출 시 반영 여부를 명확히 함
- Common Mistakes: 선택지가 많아 가로로 넘침; 아무것도 선택되지 않은 상태가 가능함; 탭 역할 없이 화면을 바꾸는 용도로 사용
- Related Patterns: FM-02, FM-06, NV-02
- Reference Image: 없음 (원본 이미지 미확보)

## FM-04 스위치 (Switch)
- ID: FM-04
- Korean Name: 스위치
- English Name: Switch
- Category: Forms & Inputs
- Definition: 하나의 설정을 켬 또는 끔으로 바꾸고 즉시 적용하는 토글 컨트롤
- Purpose: 켜짐 및 꺼짐 상태를 보여주고 바로 전환하게 함
- User Problem: 설정의 현재 상태가 불분명하고 적용 여부를 알기 어려움
- When to Use: 눌러서 즉시 효과가 나는 이진 설정(알림 켜기, 다크 모드); 제출 단계가 없는 설정 화면
- When Not to Use: 제출 시 적용되는 입력 및 동의는 FM-05; 선택지가 셋 이상이면 FM-06 또는 FM-03; 한 번만 하는 동작은 `<button>`
- Interaction Behavior: 누르거나 Space로 전환되고 즉시 적용됨; 서버 반영 중에는 상태를 표시하고 실패하면 원래 상태로 되돌려 알림
- Required States: 켬; 끔; 초점; 비활성; 반영 중; 실패(되돌림 및 알림)
- Visual Guidelines: 켬 및 끔을 색만으로 구분하지 않고 위치 또는 문구 병행(WCAG 1.4.1); 트랙 및 손잡이 경계 3:1(WCAG 1.4.11); 레이블은 켬 기준으로 읽히게 작성
- Accessibility: `role="switch"` 및 `aria-checked`; 보이는 레이블과 연결(WCAG 3.3.2, 4.1.2); 키보드 Space 전환(WCAG 2.1.1); 터치 목표 44x44pt(Apple HIG) 또는 48x48dp(Material Design)
- Responsive Considerations: 좁은 화면에서 레이블이 길면 레이블 줄바꿈 후 스위치는 오른쪽 정렬 유지; 모든 크기에서 터치 영역을 레이블 행 전체로 확장 가능
- Implementation Guidelines: `<input type="checkbox" role="switch">` 또는 `<button role="switch" aria-checked>`; 변경 즉시 적용을 전제로 하므로 별도 저장 단추를 두지 않음; 낙관적 반영 시 LD-08 규칙을 따름
- Common Mistakes: 제출해야 적용되는 폼 안에서 스위치를 사용; 켬 및 끔 상태가 문구로 모호함("끄기" 단추처럼 읽힘); 실패해도 켜진 채로 방치
- Related Patterns: FM-05, LD-08, ES-05
- Reference Image: 없음 (원본 이미지 미확보)

## FM-05 체크박스 (Checkbox)
- ID: FM-05
- Korean Name: 체크박스
- English Name: Checkbox
- Category: Forms & Inputs
- Definition: 항목마다 독립적으로 선택 또는 해제하며 보통 제출 시 적용되는 입력 컨트롤
- Purpose: 복수 선택 또는 동의를 받음
- User Problem: 여러 항목 중 원하는 것만 고르거나 약관에 동의하는 방법이 필요함
- When to Use: 복수 선택; 동의 항목; 목록 항목 선택(일괄 처리); 제출 시점에 값이 확정되는 폼
- When Not to Use: 누르는 즉시 적용되는 설정은 FM-04; 하나만 선택하면 FM-06; 동작을 실행하는 용도는 `<button>`
- Interaction Behavior: 누르거나 Space로 선택 및 해제; 전체 선택 체크박스는 일부만 선택된 중간 상태를 가짐; 제출 때까지 적용하지 않음
- Required States: 해제; 선택; 중간(일부만 선택); 초점; 오류(필수 미체크); 비활성
- Visual Guidelines: 선택 표시는 체크 모양으로 색 외 정보 포함(WCAG 1.4.1); 상자 경계 3:1(WCAG 1.4.11); 레이블을 눌러도 토글되게 하여 목표 영역을 넓힘
- Accessibility: `<input type="checkbox">`와 `<label>` 연결; 그룹은 `<fieldset>`/`<legend>`; 중간 상태는 스크립트로 `indeterminate` 값을 설정(HTML 속성 아님), 사용자 정의 체크박스는 `aria-checked="mixed"`(WCAG 4.1.2); 동의가 필수면 오류 식별(WCAG 3.3.1)
- Responsive Considerations: 터치 목표 44x44pt(Apple HIG) 또는 48x48dp(Material Design), 시각적 상자가 작아도 눌리는 영역을 확장(WCAG 2.5.8 최소 24x24 CSS px)
- Implementation Guidelines: 네이티브 체크박스를 쓰고 스타일만 입힘; 동의 항목은 미리 체크하지 않음(DP-02); 전체 선택은 하위 항목 상태에서 계산
- Common Mistakes: 선택 항목을 기본 체크 상태로 둠; 즉시 적용되는 설정에 체크박스를 씀; 레이블이 클릭되지 않음
- Related Patterns: FM-04, FM-06, DP-02
- Reference Image: 없음 (원본 이미지 미확보)

## FM-06 라디오 (Radio button)
- ID: FM-06
- Korean Name: 라디오
- English Name: Radio button
- Category: Forms & Inputs
- Definition: 선택지를 모두 펼쳐 보여주고 그중 하나만 고르게 하는 입력 컨트롤
- Purpose: 상호 배타적인 소수 선택지를 비교하며 선택하게 함
- User Problem: 선택지가 숨어 있으면 비교하기 어렵고 놓치기 쉬움
- When to Use: 하나만 선택하고 선택지가 적을 때; 선택지 설명이 문장으로 길 때; 모든 선택지를 보면서 비교해야 할 때
- When Not to Use: 선택지가 많으면 FM-02; 복수 선택은 FM-05; 즉시 켜고 끄는 설정은 FM-04; 보기 전환이면 FM-03
- Interaction Behavior: 하나를 누르면 같은 그룹의 나머지가 해제됨; 그룹에 초점이 들어오면 방향키로 선택지를 이동하며 선택
- Required States: 선택됨; 선택 안 됨; 초점; 오류(필수 그룹 미선택); 비활성; 기본 선택 여부를 정해 둠
- Visual Guidelines: 원형 표시 안 점으로 선택 표시(색 외 정보); 경계 3:1(WCAG 1.4.11); 선택지 간 간격으로 그룹 구분
- Accessibility: `<fieldset>`/`<legend>`로 그룹에 이름; 같은 `name`의 `<input type="radio">`; 보이는 `<label>`(WCAG 3.3.2); 방향키 이동은 기본 동작 유지(WCAG 2.1.1)
- Responsive Considerations: 선택지를 세로로 쌓아 좁은 화면에서도 읽힘; 터치 목표 44x44pt(Apple HIG) 또는 48x48dp(Material Design)
- Implementation Guidelines: 네이티브 라디오를 사용하고 스타일만 입힘; 필수 선택이면 기본값을 두거나 미선택 오류를 안내; 기본값이 사용자에게 불리한 선택이 되지 않게 함
- Common Mistakes: 선택지가 많은데 라디오를 모두 펼침; 그룹 이름 없이 선택지만 있음; 해제할 수 없다는 점을 간과함(해제가 필요하면 선택 안 함 선택지를 추가)
- Related Patterns: FM-02, FM-03, FM-05
- Reference Image: 없음 (원본 이미지 미확보)

## FM-07 슬라이더 (Slider)
- ID: FM-07
- Korean Name: 슬라이더
- English Name: Slider
- Category: Forms & Inputs
- Definition: 막대 위 손잡이를 움직여 범위 안의 값을 연속적으로 고르는 컨트롤
- Purpose: 대략적인 크기, 범위를 직관적으로 조절하게 함
- User Problem: 가격 범위, 음량처럼 범위 안 값을 숫자 입력 없이 빠르게 고르고 싶음
- When to Use: 최솟값 및 최댓값이 있는 범위; 정확한 값보다 상대적 위치가 중요한 경우; 두 손잡이로 범위 선택
- When Not to Use: 정확한 정수 하나는 FM-08; 자유 입력은 FM-01; 선택지가 몇 개뿐이면 FM-03 또는 FM-06
- Interaction Behavior: 손잡이 드래그, 막대 누르기, 방향키로 값 변경; 변경 중 현재 값을 보여줌; 놓을 때 확정하거나 즉시 반영(제품에서 정함)
- Required States: 기본; 초점; 드래그 중(현재 값 표시); 비활성; 오류(범위 밖); 범위 슬라이더는 두 값 표시
- Visual Guidelines: 손잡이 및 막대 경계 3:1(WCAG 1.4.11); 현재 값을 숫자로 함께 표시하고 위치만으로 전하지 않음; 최솟값 및 최댓값 표기
- Accessibility: `<input type="range">`는 `role="slider"` 및 `aria-valuenow`를 자동 제공(WCAG 4.1.2); 드래그의 단일 포인터 대안으로 막대 누르기 및 값 입력 칸 제공(WCAG 2.5.7); 방향키 조작(WCAG 2.1.1); 손잡이 목표 크기(WCAG 2.5.8)
- Responsive Considerations: 터치에서 손잡이가 손가락에 가리므로 값 표시를 손잡이 위에 둠; 좁은 화면에서 막대 폭 확보; 손잡이 터치 목표 44x44pt(Apple HIG) 또는 48x48dp(Material Design)
- Implementation Guidelines: `<input type="range">`와 `min`, `max`, `step` 사용; 정밀 입력이 필요하면 숫자 입력 필드를 병행; 범위 슬라이더는 두 입력을 쓰고 최솟값이 최댓값을 넘지 않게 제한
- Common Mistakes: 값을 표시하지 않음; 정확한 값이 필요한데 슬라이더만 제공; 드래그 외에는 값을 바꿀 수 없음
- Related Patterns: FM-08, FM-01, IC-09
- Reference Image: 없음 (원본 이미지 미확보)

## FM-08 수량 스테퍼 (Stepper)
- ID: FM-08
- Korean Name: 수량 스테퍼
- English Name: Stepper
- Category: Forms & Inputs
- Definition: 빼기 및 더하기 단추로 수량을 한 칸씩 늘이고 줄이는 숫자 입력 컨트롤; 단계 표시 LD-05 와 다름
- Purpose: 작은 정수 값을 정확히 조절하게 함
- User Problem: 수량을 바꾸려고 키보드로 숫자를 직접 치는 일이 번거롭고 오입력이 생김
- When to Use: 수량, 인원처럼 정수 값을 +/- 로 바꿀 때; 값의 범위가 좁고 한 칸 단위가 의미 있을 때
- When Not to Use: 다단계 흐름의 현재 위치 표시는 LD-05(이름이 비슷해도 입력이 아니라 진행 표시); 큰 범위의 대략 값은 FM-07; 자유 숫자 입력은 FM-01
- Interaction Behavior: 더하기를 누르면 한 칸 증가, 빼기를 누르면 한 칸 감소; 최솟값 및 최댓값에서 해당 단추가 비활성; 누르고 있으면 반복 증감(제품에서 정함); 필요하면 값 필드에 직접 입력 허용
- Required States: 기본; 최솟값(빼기 비활성); 최댓값(더하기 비활성); 초점; 비활성; 오류(직접 입력이 범위 밖)
- Visual Guidelines: 빼기 단추, 숫자, 더하기 단추를 한 줄에 배치; 단추 경계 및 아이콘 3:1(WCAG 1.4.11); 비활성 단추는 시각적으로 구분하되 이유를 알 수 있게 함
- Accessibility: 단추에 `aria-label`("수량 줄이기", "수량 늘리기"); 값 변경을 `role="status"`로 알림(WCAG 4.1.3); 단추 목표 크기 24x24 CSS px 이상(WCAG 2.5.8); 키보드 조작(WCAG 2.1.1)
- Responsive Considerations: 터치 목표 44x44pt(Apple HIG) 또는 48x48dp(Material Design)로 단추 간격 확보; 좁은 화면에서 숫자가 가려지지 않게 폭 유지
- Implementation Guidelines: `<input type="number" min max step>`에 단추를 더하거나 `<button>` 두 개와 값 표시; 증감은 값 범위를 벗어나지 않게 제한; 서버 반영이 필요하면 LD-06 또는 LD-08 규칙 따름
- Common Mistakes: 최솟값에서도 빼기가 눌려 0 이하로 내려감; 단추 영역이 작아 오탭; 라이브러리에 따라 Stepper 가 단계 표시(LD-05)를 뜻하기도 하므로 문서에 ID 를 같이 적음
- Related Patterns: FM-07, FM-01, LD-05
- Reference Image: 없음 (원본 이미지 미확보)

## FM-09 날짜 선택 (Date picker)
- ID: FM-09
- Korean Name: 날짜 선택
- English Name: Date picker
- Category: Forms & Inputs
- Definition: 달력 또는 입력 칸으로 날짜(또는 기간)를 고르는 컨트롤
- Purpose: 올바른 형식의 날짜를 오류 없이 입력하게 함
- User Problem: 날짜를 문자로 직접 치면 형식이 틀리고 요일 및 달력 위치를 가늠하기 어려움
- When to Use: 예약, 일정, 기한 등 오늘과 가까운 날짜 값 (생년월일처럼 먼 과거 날짜는 년, 월, 일 직접 입력이 우선); 시작일 및 종료일 같은 기간 선택; 선택 가능한 날짜가 제한될 때
- When Not to Use: 날짜가 자유 문자열이면 FM-01; 연도만 필요하면 FM-02; 며칠 후 같은 상대 값은 FM-08
- Interaction Behavior: 입력 칸을 누르면 달력이 열려 날짜를 고름; 직접 입력도 허용; 선택 불가 날짜는 비활성; 기간은 시작 및 종료를 차례로 고름
- Required States: 기본; 열림; 선택됨; 오늘 표시; 선택 불가 날짜; 오류(형식 또는 범위); 비활성
- Visual Guidelines: 선택 날짜를 색 외 모양으로도 구분(WCAG 1.4.1); 날짜 글자 4.5:1(WCAG 1.4.3); 날짜 칸 터치 목표 44x44pt(Apple HIG) 또는 48x48dp(Material Design); 허용 형식을 입력 칸 근처에 안내
- Accessibility: 달력만 있고 입력이 없으면 키보드 접근이 어려우므로 직접 입력 병행; 달력 `role="dialog"` 및 초점 이동 및 복귀; 방향키로 날짜 이동(WCAG 2.1.1); 레이블 필수(WCAG 3.3.2); 오류 문구(WCAG 3.3.1)
- Responsive Considerations: 모바일에서는 운영체제 기본 날짜 선택기를 쓰면 조작이 안정적; 좁은 화면에서는 달력을 전체 폭으로 열음
- Implementation Guidelines: 가능하면 `<input type="date">`를 먼저 사용(지원 범위는 브라우저마다 다름), 부족하면 사용자 정의 달력 구현; 값은 전송 시 표준 형식으로 정규화; 선택 가능 범위는 `min`, `max`로 제한
- Common Mistakes: 직접 입력이 막혀 있음; 선택 불가 날짜가 이유 없이 비활성; 지역별 날짜 표기 순서를 안내하지 않음
- Related Patterns: FM-01, FM-02, FB-06
- Reference Image: 없음 (원본 이미지 미확보)
