# Agent UI (에이전트 화면과 이벤트별 표시)

- 역할: AI 에이전트가 이벤트 스트림으로 보내는 상태를 화면에서 어떻게 보여 줄지 정하는 기준. AI-01 ~ AI-09 (`ai-interfaces.md`) 의 바탕이 되는 상태 목록
- 쓰는 때: 에이전트 진행, 도구 호출, 사람 승인, 공유 상태가 있는 화면을 설계하거나 검수할 때
- 근거: AG-UI 프로토콜 (ag-ui-protocol/ag-ui) 문서의 요약본을 2026-11-25 에 읽음. 원문과 한 글자까지 같지 않다. 스펙 1.0 기준이며 문서끼리 다른 곳은 아래에 적었다
- 이벤트 이름 표기: 스트림에서 오는 값은 `type` 필드의 전송 값(`RUN_STARTED` 형식)이다. 괄호 안은 JS SDK 의 이벤트 타입 이름이다. 전송 값은 JS SDK 문서(docs.ag-ui.com `sdk/js/core/events`)의 `EventType` 열거형에서 읽었다 (확인, 2026-11-25). 이벤트 개념 문서(docs.ag-ui.com `concepts/events`)는 이벤트를 `RunStarted` 같은 제목으로 부르고 전송 값은 `REASONING_*` 와 `THINKING_*` 표에서만 적는다. 열거형에 없는 값은 `전송 값 미확인` 이다

## 1. 전제
- 에이전트가 사용자에게 보이는 모든 것은 하나의 이벤트 스트림으로 온다. 화면은 이벤트 종류별로 상태를 가진다
- 필수 계열은 실행 (시작, 종료, 오류) 뿐이고 나머지는 선택이다. 화면은 모르는 이벤트와 모르는 `activityType` 값을 받아도 깨지지 않아야 한다
- 이 프로토콜 자체는 생성형 UI 규격이 아니다. 에이전트가 화면 구성을 제안하는 경우 앱이 검증한 뒤 마운트한다

## 2. 이벤트 계열별 화면 처리
| 계열 | 이벤트 | 화면에서 할 일 | 하지 않는 것 |
|---|---|---|---|
| 실행 | `RUN_STARTED` (`RunStartedEvent`), `RUN_FINISHED` (`RunFinishedEvent`), `RUN_ERROR` (`RunErrorEvent`) | 시작 시 진행 표시와 로딩 상태를 초기화. 종료 결과는 `success`, `interrupt`, `cancelled`. 오류는 메시지를 보여 준다 | 취소를 오류로 표시하지 않는다. 실패를 성공으로 표시하지 않는다 |
| 단계 | `STEP_STARTED` (`StepStartedEvent`), `STEP_FINISHED` (`StepFinishedEvent`) | 단계 표시와 완료 표시를 갱신 | 단계 이름을 지어내지 않는다 |
| 텍스트 | `TEXT_MESSAGE_START` (`TextMessageStartEvent`), `TEXT_MESSAGE_CONTENT` (`TextMessageContentEvent`), `TEXT_MESSAGE_END` (`TextMessageEndEvent`) | 시작에 새 말풍선과 로딩 표시, 조각이 올 때마다 이어 붙임 (모아서 그려도 토큰별로 그려도 된다), 종료에 마무리 렌더링과 로딩 표시 제거 | 종료 전에 완료 표시를 하지 않는다 |
| 도구 호출 | `TOOL_CALL_START` (`ToolCallStartEvent`), `TOOL_CALL_ARGS` (`ToolCallArgsEvent`), `TOOL_CALL_END` (`ToolCallEndEvent`), `TOOL_CALL_RESULT` (`ToolCallResultEvent`) | 도구 이름 카드로 작업 중임을 알림. 인자는 점진적으로 보여 줄 수 있다. 결과는 글, 이미지, 오디오, 영상, 문서 부분으로 표시 | `TOOL_CALL_END` 전에 실행하지 않는다 |
| 상태 | `STATE_SNAPSHOT` (`StateSnapshotEvent`), `STATE_DELTA` (`StateDeltaEvent`), `MESSAGES_SNAPSHOT` (`MessagesSnapshotEvent`) | 스냅샷은 병합 없이 통째로 교체. 변경분은 JSON Patch 로 적용하고, 어긋나면 새 스냅샷을 요청. 대화 전체 스냅샷으로 맥락을 갱신 | 활동과 추론 메시지는 클라이언트 전용이라 스냅샷으로 지우지 않는다 |
| 활동 | `ACTIVITY_SNAPSHOT` (`ActivitySnapshotEvent`), `ACTIVITY_DELTA` (`ActivityDeltaEvent`) | 대화 밖에 구조화된 진행 위젯 (계획, 검색 등) 을 그리고 제자리에서 갱신 | 처음 보는 `activityType` 을 오류로 처리하지 않는다 |
| 추론 | `REASONING_START` (`ReasoningStartEvent`), `REASONING_MESSAGE_START`, `REASONING_MESSAGE_CONTENT`, `REASONING_MESSAGE_END`, `REASONING_END` (SDK 이름은 같은 규칙으로 `ReasoningMessageStartEvent` 식) | 기본은 접어 두고 생각 중 스타일로 표시. 숨겨도 된다 | `REASONING_ENCRYPTED_VALUE` (`ReasoningEncryptedValueEvent`) 는 해석하지 않고 해당 메시지에 저장했다가 그대로 되돌려 보낸다 |
| 하위 에이전트 | `SUBAGENT_STARTED` (`SubagentStartedEvent`), `SUBAGENT_FINISHED` (`SubagentFinishedEvent`), `SUBAGENT_ERROR` (`SubagentErrorEvent`) | 실행 중임을 표시. 하위 에이전트의 실패는 부모가 계속할 수 있다 | 진행 상태를 추측으로 채우지 않는다 |
| 원본과 사용자 정의 | `RAW` (`RawEvent`), `CUSTOM` (`CustomEvent`) | 모르는 이름은 무시 | 마크업으로 렌더링하지 않는다 |

- 시작, 내용, 종료를 합친 축약형이 있다: `REASONING_MESSAGE_CHUNK` (`ReasoningMessageChunkEvent`). 텍스트와 도구 호출의 축약형은 개념 문서가 `TextMessageChunk`, `ToolCallChunk` 로 소개하고 JS SDK 문서는 `TEXT_MESSAGE_CHUNK`, `TOOL_CALL_CHUNK` 형식으로 적었으나, 이 두 값은 JS SDK 문서의 `EventType` 열거형 표에만 빠져 있다. `TEXT_MESSAGE_CHUNK` (`TextMessageChunkEvent`), `TOOL_CALL_CHUNK` (`ToolCallChunkEvent`), `REASONING_MESSAGE_CHUNK` 는 TS SDK 소스(`sdks/typescript/packages/core/src/generated/types.ts`) 및 `docs/spec/1.0/schema.json` 에 있다 (확인)
- 이전 판의 `THINKING_START`, `THINKING_END`, `THINKING_TEXT_MESSAGE_START`, `THINKING_TEXT_MESSAGE_CONTENT`, `THINKING_TEXT_MESSAGE_END` 5종은 개념 문서의 Deprecated 표에서 `REASONING_*` 로 대체된다. 문서는 1.0.0 에서 제거 예정이라고 적었고 JS SDK 열거형에는 이 값이 없다. 새로 만들 때는 `REASONING_*` 만 쓰고, 옛 서버가 `THINKING_*` 를 보내면 같은 자리의 추론 표시로 매핑한다 (일반)

## 3. 사람 승인 화면 (인터럽트)
에이전트가 `RUN_FINISHED` 의 결과를 `interrupt` 로 보내면 실행이 멈추고 사람의 응답을 기다린다.
- 각 항목: 식별자, 이유 (도구 호출, 입력 필요, 확인 등), 기본 대체 화면에 쓸 문구, 연결된 도구 호출, 응답 형식 (폼을 만드는 데 쓴다), 만료 시각
- 응답 형식이 있으면 그 폼을 만든다. 편집된 인자를 받을 수 있는 스키마면 편집 UI 를 제공한다
- 만료 시각이 지나면 응답을 제출하지 못하게 한다
- 이어가려면 모든 인터럽트에 답하거나 포기해야 한다. 그래서 화면은 열린 승인이 몇 건인지 보여 준다
- 문서끼리 다르다: 재개 항목 `status` 의 전송 값은 `resolved`, `cancelled` 이다 (확인: spec 1.0 `schema.json` 및 TS SDK). `answered`, `abandoned` 는 스펙 본문의 설명 문구이며 전송 값이 아니다
- 일시정지, 승인, 편집, 재시도, 상위 보고가 승인 화면에서 필요한 동작이다

## 4. 프런트 도구와 동의
- 에이전트가 제안하고 앱이 실행하는 도구가 있다. 응답 전에는 대기 중인 도구 호출 목록으로 표시한다
- 부작용이 있는 도구 (결제, 삭제, 전송) 는 사용자 동의를 받는다 (문서 표현: SHOULD)
- 승인되지 않은 호출을 승인된 것처럼 표시하지 않는다 (문서 표현: MUST NOT)
- 확인 창에는 무엇을 하려는지와 인자를 보여 준다 (`securecoding` 의 SEC-21 권한은 모델 밖 코드가 강제)

## 5. 기존 패턴과 대응
| 이벤트와 기능 | 기존 패턴 | 빠진 것 |
|---|---|---|
| 실행 시작, 추론 | AI-01 생각 중 표시 | 추론을 접어 두는 기본값 |
| 텍스트 스트리밍 | AI-02 스트리밍 답변 | 취소와 재개 |
| 도구 결과 | AI-05 출처 표시 | 도구 결과의 형식별 표시 |
| 단계, 활동, 하위 에이전트 | AI-09 에이전트 단계 | 활동 위젯, 하위 에이전트 표시 |
| 인터럽트 | 없음 | 사람 승인 화면 (3절) |
| 공유 상태 | 없음 | 에이전트와 사용자가 같은 값을 보는 화면 (스냅샷과 변경분 적용) |
| 도구 출력 스트리밍 | 없음 | 긴 작업 로그를 흘려 보여 주는 영역 |
| 에이전트 조종 | 없음 | 실행 중 입력으로 방향을 바꾸는 입력창 |

## 6. 아직 읽지 못한 것
- 스펙의 실행 입력, 기능 협상, 스트리밍 및 스냅샷 패턴 문서, 개념 페이지 중 상태, 추론, 하위 에이전트, 메시지, SDK 문서, 데모 화면
- 이벤트 표의 `하지 않는 것` 이 비어 있는 곳은 읽은 문서에 지침이 없다는 뜻이며 읽지 않은 페이지에는 있을 수 있다
