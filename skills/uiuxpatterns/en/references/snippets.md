# Snippets (minimal markup examples)

Korean original: ../../references/snippets.md. Pattern IDs are identical. Code blocks are the same as the original: only code comments are translated, and the Korean strings inside code are sample UI text kept as is. Marker meaning: `[not run]` = not executed. Other references are Korean for now and are linked by their Korean original path.

- Role: `Good example` and `Bad example` for 9 patterns. Where frameworks differ (live region, `<dialog>`, conditional rendering), HTML, React and Vue 3 are given together
- How to use: Grep a heading such as `^## FB-02 ` and read only that block. The grounds for the rules are in `../../references/interaction-rules.md` and each category file (Korean for now)
- Use the values in `defaults.md` for time values (`*_MS`)
- A `Good example` (HTML) without the `[not run]` marker was run in Chrome and its behavior was confirmed. Ones with the marker were not run (check React and Vue in the project environment)
- `showToast` is the function of FB-01 and is called by other examples

## FB-01 Toast
- Mount the live region from the start and change only the text. Do not auto-close errors. The pause conditions are in `defaults.md` DF-04 (omitted from the examples)

### Good example (HTML)
```html
<div id="toast" role="status" aria-live="polite"></div>
<style>#toast:empty{opacity:0;pointer-events:none}</style>
<script>
const TOAST_MS = 5000; // see defaults.md
let timer;
function showToast(msg, isError = false) {
  const el = document.getElementById('toast');
  clearTimeout(timer);
  el.textContent = msg;
  if (!isError) timer = setTimeout(() => { el.textContent = ''; }, TOAST_MS);
}
</script>
```

### Good example (React) [not run]
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
// always render <div role="status" aria-live="polite" className="toast">{msg}</div>
```

### Good example (Vue 3) [not run]
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

### Bad example [not run]
```jsx
{open && <div role="status">저장했어요</div>}
```
- Counterexample: the region is newly created together with the text, so it may not be announced. The same applies to `v-if` in Vue

## FB-02 Snackbar
- Defer the deletion and commit it when time passes. If undo is pressed, clear the timer

### Good example (HTML)
```html
<div class="snackbar">
  <span id="snack-msg" role="status"></span>
  <button type="button" id="undo" hidden>되돌리기</button>
</div>
<script>
const SNACKBAR_MS = 10000; // see defaults.md
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

### Bad example [not run]
```js
list.removeChild(item); showToast('일정을 삭제했어요');
```
- Counterexample: it is already deleted and there is no way to undo. A toast is a pattern with no action button

## FB-04 Modal dialog
- `showModal()` provides background blocking, focus trapping, closing with Esc, and focus return. `show()` and the `open` attribute are non-modal

### Good example (HTML)
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

### Good example (React) [not run]
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

### Good example (Vue 3) [not run]
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

### Bad example [not run]
```jsx
{open && <div className="modal"><dialog open>결제할까요?</dialog></div>}
```
- Counterexample: the `open` attribute is non-modal, so the background stays operable, Esc does not close it, and focus is not trapped

## FB-07 Tooltip
- Support hover, focus and press-to-open, and close with Esc. It stays open when the pointer moves onto the bubble

### Good example (HTML)
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

### Bad example [not run]
```html
<span class="icon-i" onmouseover="showTip()">i</span>
```
- Counterexample: it cannot receive focus so keyboard users cannot see it, and it is not linked to its target so screen readers cannot read it either

## FM-01 Text field states
- A visible `<label>`, validate on blur, link the error text to `aria-describedby` only when there is an error. Enter during Hangul composition does not submit

### Good example (HTML)
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
- React: `onKeyDown={(e) => { if (e.key === 'Enter' && !(e.nativeEvent.isComposing || e.keyCode === 229)) submit(); }}` [not run]
- Vue 3: `@keydown.enter="(e) => { if (!(e.isComposing || e.keyCode === 229)) submit() }"` [not run]

### Bad example [not run]
```html
<input placeholder="이메일" onkeydown="if (event.key === 'Enter') submit()">
```
- Counterexample: there is no label, so the guidance disappears once the user types. Enter during Hangul composition submits and the last character is entered once more

## FM-04 Switch
- Apply immediately on press. If applying fails, restore the original state and notify. For using the `switch` attribute together, see `defaults.md` DF-28

### Good example (HTML)
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

### Bad example [not run]
```html
<div class="switch on" onclick="this.classList.toggle('on')"></div>
```
- Counterexample: it has no role, state or label and cannot be operated with the keyboard. Even on failure it stays on

## NV-02 Top tabs
- Only the current tab is in the Tab order, and the rest are reached with the arrow keys

### Good example (HTML)
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

### Bad example [not run]
```html
<div class="tab active" onclick="go('reserved')">예약 중</div>
```
- Counterexample: it has no role or selected state and cannot be reached by keyboard. If it navigates to a page, it must be `<a href>`

## LD-06 Button loading
- Keep focus with `aria-disabled`, change the name to `저장 중` (Saving), and block duplicate runs. Always restore it when finished

### Good example (HTML)
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

### Good example (React) [not run]
```jsx
const [busy, setBusy] = useState(false);
const onSave = async () => {
  if (busy) return;
  setBusy(true);
  try { await saveForm(); } finally { setBusy(false); }
};
// <button type="button" aria-disabled={busy} onClick={onSave}>{busy ? '저장 중' : '저장'}</button>
```

### Good example (Vue 3) [not run]
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

### Bad example [not run]
```js
btn.disabled = true; await saveForm();
```
- Counterexample: `disabled` loses focus, and on failure it stays disabled so retrying is impossible

## AI-02 Streaming response
- `aria-busy` while generating; announce completion and interruption through a status region mounted from the start. Stop following when the user scrolls up. Stop cancels the request

### Good example (HTML)
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

- React render [not run]: `<div aria-busy={busy}>{text}</div><p role="status">{status}</p>` Stop is `onClick={() => ctrl.current?.abort()}`
- Vue 3 render [not run]: `<div :aria-busy="busy">{{ text }}</div><p role="status">{{ status }}</p>` Stop is `@click="ctrl?.abort()"`

### Bad example [not run]
```jsx
{done && <p role="status">답변이 완성됐어요</p>}
```
- Counterexample: the region is newly created at completion, so it may not be announced. There is also no interruption or error guidance
