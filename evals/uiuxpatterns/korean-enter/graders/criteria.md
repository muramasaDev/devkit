---
type: llm
weight: 1
---

Pass only if all hold:
- IME 조합 중 Enter 이벤트가 전송을 일으키는 것이 원인이라고 설명한다
- e.nativeEvent.isComposing 과 keyCode 229 를 함께 검사하는 코드를 보인다
- 조합 확정 후 처리(compositionend)나 글자 수 계산 시점을 언급한다
