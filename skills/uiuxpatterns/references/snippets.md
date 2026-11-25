# Snippets (최소 마크업 예)

- 역할: 패턴 9개의 `좋은 예` 및 `나쁜 예`. 프레임워크가 갈리는 곳(라이브 영역, `<dialog>`, 조건부 렌더링)은 HTML, React, Vue 3 를 병기
- 쓰는 법: `^## FB-02 ` 같은 제목을 Grep 해 해당 블록만 읽는다. 규칙의 근거는 `interaction-rules.md` 및 각 카테고리 파일
- 시간 값(`*_MS`)은 `defaults.md` 의 값을 쓴다
- `[미실행]` 표시가 없는 `좋은 예` (HTML) 는 Chrome 에서 실행해 동작을 확인했다. 표시가 있는 것은 실행하지 않았다 (React 및 Vue 는 프로젝트 환경에서 확인한다)
- `showToast` 는 FB-01 의 함수이고 다른 예가 불러 쓴다

## FB-01 토스트 (Toast)
- 라이브 영역을 처음부터 마운트해 두고 문구만 바꾼다. 오류는 자동으로 닫지 않는다. 일시정지 조건은 `defaults.md` DF-04 (예는 생략)

### 좋은 예 (HTML)
```html
<div id="toast" role="status" aria-live="polite"></div>
<style>#toast:empty{opacity:0;pointer-events:none}</style>
<script>
const TOAST_MS = 5000; // defaults.md 참조
let timer;
function showToast(msg, isError = false) {
  const el = document.getElementById('toast');
  clearTimeout(timer);
  el.textContent = msg;
  if (!isError) timer = setTimeout(() => { el.textContent = ''; }, TOAST_MS);
}
</script>
```

### 좋은 예 (React) [미실행]
```jsx
function useToast() {
  const [msg, setMsg] = useState('');
  const timer = useRef();
  useEffect(() => () => clearTimeout(timer.current), []);
  const show = (m, isError = false) => {
    clearTimeout(timer.current);
    setMsg(m);
    if (!isError) timer.current = setTimeout(() => setMsg(''), TOAST_MS);
  };
  return [msg, show];
}
// 항상 렌더 <div role="status" aria-live="polite" className="toast">{msg}</div>
```

### 좋은 예 (Vue 3) [미실행]
```vue
<script setup>
import { ref, onUnmounted } from 'vue'
const msg = ref('')
let timer
function show(m, isError = false) {
  clearTimeout(timer)
  msg.value = m
  if (!isError) timer = setTimeout(() => { msg.value = '' }, TOAST_MS)
}
onUnmounted(() => clearTimeout(timer))
</script>
<template><div role="status" aria-live="polite" class="toast">{{ msg }}</div></template>
```

### 나쁜 예 [미실행]
```jsx
{open && <div role="status">저장했어요</div>}
```
- 반례: 영역이 문구와 함께 새로 생겨 낭독되지 않을 수 있다. Vue 의 `v-if` 도 같다

## FB-02 스낵바 (Snackbar)
- 삭제를 미뤄 두고 시간이 지나면 확정한다. 되돌리기를 누르면 타이머를 지운다

### 좋은 예 (HTML)
```html
<div class="snackbar">
  <span id="snack-msg" role="status"></span>
  <button type="button" id="undo" hidden>되돌리기</button>
</div>
<script>
const SNACKBAR_MS = 10000; // defaults.md 참조
let pending;
function removeItem(commit, restore) {
  const msg = document.getElementById('snack-msg'), undo = document.getElementById('undo');
  msg.textContent = '일정을 삭제했어요';
  undo.hidden = false;
  pending = setTimeout(() => { undo.hidden = true; msg.textContent = ''; commit(); }, SNACKBAR_MS);
  undo.onclick = () => {
    clearTimeout(pending);
    undo.hidden = true;
    msg.textContent = '되돌렸어요';
    restore();
  };
}
</script>
```

### 나쁜 예 [미실행]
```js
list.removeChild(item); showToast('일정을 삭제했어요');
```
- 반례: 이미 지워져 되돌리는 길이 없다. 토스트는 행동 단추가 없는 패턴이다

## FB-04 모달 (Modal dialog)
- `showModal()` 은 배경 차단, 초점 가두기, Esc 닫기, 초점 복귀를 제공한다. `show()` 및 `open` 속성은 비모달

### 좋은 예 (HTML)
```html
<button type="button" id="open-pay">결제</button>
<dialog id="pay" aria-labelledby="pay-title">
  <h2 id="pay-title">결제할까요?</h2>
  <p>결제 후엔 취소 수수료가 있어요</p>
  <form method="dialog">
    <button value="cancel">취소</button>
    <button value="ok">결제</button>
  </form>
</dialog>
<script>
const pay = document.getElementById('pay');
document.getElementById('open-pay').onclick = () => pay.showModal();
pay.addEventListener('close', () => { if (pay.returnValue === 'ok') submitPayment(); });
</script>
```

### 좋은 예 (React) [미실행]
```jsx
function PayDialog({ open, onClose, onOk }) {
  const ref = useRef(null);
  useEffect(() => {
    const d = ref.current;
    if (open && !d.open) d.showModal();
    if (!open && d.open) d.close();
  }, [open]);
  return (
    <dialog ref={ref} aria-labelledby="pay-title" onClose={onClose}>
      <h2 id="pay-title">결제할까요?</h2>
      <button type="button" onClick={onClose}>취소</button>
      <button type="button" onClick={() => { onOk(); onClose(); }}>결제</button>
    </dialog>
  );
}
```

### 좋은 예 (Vue 3) [미실행]
```vue
<script setup>
import { ref, watch } from 'vue'
const props = defineProps({ open: Boolean })
const emit = defineEmits(['close', 'ok'])
const dlg = ref(null)
watch(() => props.open, (v) => {
  if (v && !dlg.value.open) dlg.value.showModal()
  if (!v && dlg.value.open) dlg.value.close()
})
</script>
<template>
  <dialog ref="dlg" aria-labelledby="pay-title" @close="emit('close')">
    <h2 id="pay-title">결제할까요?</h2>
    <button type="button" @click="emit('close')">취소</button>
    <button type="button" @click="emit('ok'); emit('close')">결제</button>
  </dialog>
</template>
```

### 나쁜 예 [미실행]
```jsx
{open && <div className="modal"><dialog open>결제할까요?</dialog></div>}
```
- 반례: `open` 속성은 비모달이라 배경이 조작되고 Esc 로 닫히지 않으며 초점을 가두지 않는다

## FB-07 툴팁 (Tooltip)
- 가리키기, 초점, 눌러 열기를 지원하고 Esc 로 닫는다. 말풍선 위로 옮겨도 유지

### 좋은 예 (HTML)
```html
<span class="tip-wrap" id="rate-wrap">
  이번 달 저축률
  <button type="button" aria-label="저축률 기준 설명" aria-describedby="rate-tip">i</button>
  <span role="tooltip" id="rate-tip">최근 3개월 지출 기준이에요</span>
</span>
<style>
.tip-wrap{position:relative}
[role=tooltip]{position:absolute;visibility:hidden}
.tip-wrap[data-open] [role=tooltip],
.tip-wrap:focus-within [role=tooltip]{visibility:visible}
@media (hover:hover){.tip-wrap:hover [role=tooltip]{visibility:visible}}
</style>
<script>
const wrap = document.getElementById('rate-wrap'), tip = document.getElementById('rate-tip');
wrap.querySelector('button').onclick = () => wrap.toggleAttribute('data-open');
wrap.onkeydown = (e) => { if (e.key === 'Escape') { wrap.removeAttribute('data-open'); tip.style.visibility = 'hidden'; } };
wrap.onmouseleave = wrap.onfocusout = () => { tip.style.visibility = ''; };
</script>
```

### 나쁜 예 [미실행]
```html
<span class="icon-i" onmouseover="showTip()">i</span>
```
- 반례: 초점을 받지 못해 키보드 사용자가 볼 수 없고 대상과 연결되지 않아 스크린 리더도 읽지 못한다

## FM-01 텍스트 필드 상태 (Text field states)
- 보이는 `<label>`, 벗어날 때 검증, 오류일 때만 오류 문구를 `aria-describedby` 에 연결. 한글 조합 중 Enter 는 제출 안 함

### 좋은 예 (HTML)
```html
<label for="email">이메일</label>
<input id="email" type="email" autocomplete="email"
       aria-describedby="email-hint" aria-invalid="false">
<p id="email-hint">회사 메일</p>
<p id="email-err" hidden>이메일 형식을 확인해 주세요</p>
<script>
const f = document.getElementById('email'), err = document.getElementById('email-err');
f.addEventListener('blur', () => {
  const bad = f.value !== '' && !f.validity.valid;
  f.setAttribute('aria-invalid', String(bad));
  f.setAttribute('aria-describedby', bad ? 'email-hint email-err' : 'email-hint');
  err.hidden = !bad;
});
f.addEventListener('keydown', (e) => {
  if (e.key !== 'Enter' || e.isComposing || e.keyCode === 229) return;
  submit();
});
</script>
```
- React: `onKeyDown={(e) => { if (e.key === 'Enter' && !(e.nativeEvent.isComposing || e.keyCode === 229)) submit(); }}` [미실행]
- Vue 3: `@keydown.enter="(e) => { if (!(e.isComposing || e.keyCode === 229)) submit() }"` [미실행]

### 나쁜 예 [미실행]
```html
<input placeholder="이메일" onkeydown="if (event.key === 'Enter') submit()">
```
- 반례: 레이블이 없어 입력하면 안내가 사라진다. 한글 조합 중 Enter 에 제출돼 마지막 글자가 한 번 더 들어간다

## FM-04 스위치 (Switch)
- 눌러서 즉시 적용한다. 반영에 실패하면 원래 상태로 돌리고 알린다. `switch` 속성 병기는 `defaults.md` DF-28

### 좋은 예 (HTML)
```html
<label><input type="checkbox" switch role="switch" id="push"> 알림 받기</label>
<script>
const push = document.getElementById('push');
push.addEventListener('change', async () => {
  const on = push.checked;
  try { await saveSetting({ push: on }); }
  catch { push.checked = !on; showToast('저장하지 못했어요', true); }
});
</script>
```

### 나쁜 예 [미실행]
```html
<div class="switch on" onclick="this.classList.toggle('on')"></div>
```
- 반례: 역할, 상태, 레이블이 없고 키보드로 조작할 수 없다. 실패해도 켜진 채 남는다

## NV-02 상단 탭 (Top tabs)
- 현재 탭만 Tab 순서에 두고 나머지는 방향키로 이동

### 좋은 예 (HTML)
```html
<div role="tablist" aria-label="예약">
  <button role="tab" id="t1" aria-selected="true" aria-controls="p1">전체</button>
  <button role="tab" id="t2" aria-selected="false" aria-controls="p2" tabindex="-1">예약 중</button>
  <button role="tab" id="t3" aria-selected="false" aria-controls="p3" tabindex="-1">예약 완료</button>
</div>
<div role="tabpanel" id="p1" aria-labelledby="t1" tabindex="0">전체</div>
<div role="tabpanel" id="p2" aria-labelledby="t2" tabindex="0" hidden>예약 중</div>
<div role="tabpanel" id="p3" aria-labelledby="t3" tabindex="0" hidden>예약 완료</div>
<script>
const tabs = [...document.querySelectorAll('[role=tab]')];
function select(t) {
  tabs.forEach((x) => {
    const on = x === t;
    x.setAttribute('aria-selected', String(on));
    x.tabIndex = on ? 0 : -1;
    document.getElementById(x.getAttribute('aria-controls')).hidden = !on;
  });
  t.focus();
}
tabs.forEach((t, i) => {
  t.onclick = () => select(t);
  t.onkeydown = (e) => {
    const d = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
    if (d) select(tabs[(i + d + tabs.length) % tabs.length]);
  };
});
</script>
```

### 나쁜 예 [미실행]
```html
<div class="tab active" onclick="go('reserved')">예약 중</div>
```
- 반례: 역할과 선택 상태가 없고 키보드로 닿지 않는다. 페이지 이동이면 `<a href>` 여야 한다

## LD-06 버튼 로딩 (Button loading)
- `aria-disabled` 로 초점을 유지하고 이름을 `저장 중` 으로 바꾸며 중복 실행을 막는다. 끝나면 반드시 되돌린다

### 좋은 예 (HTML)
```html
<button type="button" id="save" aria-disabled="false">저장</button>
<script>
const save = document.getElementById('save');
save.addEventListener('click', async () => {
  if (save.getAttribute('aria-disabled') === 'true') return;
  save.setAttribute('aria-disabled', 'true');
  save.textContent = '저장 중';
  try { await saveForm(); showToast('저장했어요'); }
  catch { showToast('저장하지 못했어요', true); }
  finally { save.setAttribute('aria-disabled', 'false'); save.textContent = '저장'; }
});
</script>
```

### 좋은 예 (React) [미실행]
```jsx
const [busy, setBusy] = useState(false);
const onSave = async () => {
  if (busy) return;
  setBusy(true);
  try { await saveForm(); } finally { setBusy(false); }
};
// <button type="button" aria-disabled={busy} onClick={onSave}>{busy ? '저장 중' : '저장'}</button>
```

### 좋은 예 (Vue 3) [미실행]
```vue
<script setup>
import { ref } from 'vue'
const busy = ref(false)
async function onSave() {
  if (busy.value) return
  busy.value = true
  try { await saveForm() } finally { busy.value = false }
}
</script>
<template><button type="button" :aria-disabled="busy" @click="onSave">{{ busy ? '저장 중' : '저장' }}</button></template>
```

### 나쁜 예 [미실행]
```js
btn.disabled = true; await saveForm();
```
- 반례: `disabled` 는 초점을 잃게 하고 실패하면 비활성으로 남아 다시 시도할 수 없다

## AI-02 스트리밍 답변 (Streaming response)
- 생성 중 `aria-busy`, 완료 및 중단은 처음부터 마운트한 상태 영역으로 알린다. 위로 스크롤하면 따라가기 중지. 정지는 요청을 취소

### 좋은 예 (HTML)
```html
<div id="log" aria-busy="false"><div id="answer"></div></div>
<p id="stream-status" role="status"></p>
<button type="button" id="stop">정지</button>
<script>
const log = document.getElementById('log'), answer = document.getElementById('answer');
const status = document.getElementById('stream-status');
let ctrl;
async function ask(q) {
  ctrl = new AbortController();
  answer.textContent = '';
  status.textContent = '';
  log.setAttribute('aria-busy', 'true');
  try {
    const res = await fetch('/api/chat', { method: 'POST', body: JSON.stringify({ q }), signal: ctrl.signal });
    const reader = res.body.pipeThrough(new TextDecoderStream()).getReader();
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      const follow = log.scrollHeight - log.scrollTop - log.clientHeight < 40;
      answer.textContent += value;
      if (follow) log.scrollTop = log.scrollHeight;
    }
    status.textContent = '답변이 완성됐어요';
  } catch (e) {
    status.textContent = e.name === 'AbortError' ? '답변을 멈췄어요' : '답변이 중간에 끊겼어요';
  } finally { log.setAttribute('aria-busy', 'false'); }
}
document.getElementById('stop').onclick = () => ctrl && ctrl.abort();
</script>
```

- React 렌더 [미실행]: `<div aria-busy={busy}>{text}</div><p role="status">{status}</p>` 정지는 `onClick={() => ctrl.current?.abort()}`
- Vue 3 렌더 [미실행]: `<div :aria-busy="busy">{{ text }}</div><p role="status">{{ status }}</p>` 정지는 `@click="ctrl?.abort()"`

### 나쁜 예 [미실행]
```jsx
{done && <p role="status">답변이 완성됐어요</p>}
```
- 반례: 영역이 완료 때 새로 생겨 낭독되지 않을 수 있다. 중단 및 오류 안내도 없다
