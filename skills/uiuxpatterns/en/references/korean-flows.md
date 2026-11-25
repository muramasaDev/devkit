# Korean Flows (core flows of Korean domestic services)

Korean original: ../../references/korean-flows.md. Korean terms are given in parentheses after the English explanation. In the error message examples, the Korean text is kept as is, with the English meaning in (meaning: ...). Evidence labels: `verified` = original source read (MDN, W3C WCAG 2.2, local run, 2026-11-25), `general advice` = general recommendation with no original source read, `unverified` = could not be confirmed. Other references are Korean for now and are linked by their Korean original path.

- Role: screen states, error message examples and accessibility requirements for 6 flows that recur in Korean domestic services
- Evidence labels: `verified` original source read (MDN, W3C WCAG 2.2, local run. 2026-11-25), `general advice` general recommendation with no original source read, `unverified` could not be confirmed
- Error message examples may be adapted to the tone of the service. `{ }` inside the text is filled with a value from the server
- Pattern IDs are in `../../references/pattern-catalog.md` (Korean for now), time values are in `defaults.md`

## 1. Mobile phone identity verification (휴대폰 본인확인)
- Input fields: phone number `type="tel"`, `autocomplete="tel"` (verified: MDN says `tel` is the full number including the country code). Verification code `autocomplete="one-time-code"` (verified: one-time code received by SMS, email or an authenticator app), `inputmode="numeric"` (verified: only brings up a digit 0~9 keyboard and does no input validation)
- For carrier selection (통신사), use the list provided by the identity verification provider (general advice). If a number already entered in the same process is needed again, fill it automatically or let the user pick it (verified: WCAG 3.3.7, re-entry for security purposes is an exception)
- Compute the remaining time from the expiry time given by the server (alternative UX of DP-03 in `../../references/dark-patterns.md`, Korean for now). If there is a time limit, provide a warning before expiry and a means to extend (verified: WCAG 2.2.1, warning of 20 seconds or more and extension with a simple action, 10 times or more). Do not read it aloud every second, announce only at the start, at 1-minute intervals, and just before expiry (general advice)
- For resend, show the count and wait time as server policy values and do not invent numbers on screen (general advice)

| Screen state | Error message example | Accessibility requirement |
|---|---|---|
| Number entry, sending, sent, verifying, done | 번호 형식이 맞지 않아요. 숫자만 입력해 주세요 (meaning: The number format is wrong. Enter digits only) | Field `<label>`, link the error with `aria-describedby` (3.3.1) |
| Mismatch | 인증번호가 일치하지 않아요. 다시 확인해 주세요 (meaning: The verification code does not match. Check again) | Keep the entered value, focus on the error field |
| Time expired | 인증 시간이 지났어요. 인증번호를 다시 받아 주세요 (meaning: The verification time has passed. Request the code again) | Announce the expiry once with `role="status"` (4.1.3) |
| Resend limit | 요청 횟수를 넘었어요. {n}분 뒤에 다시 시도해 주세요 (meaning: The request count was exceeded. Try again in {n} minutes) | One line giving the reason on the disabled button (section 1 of `../../references/interaction-rules.md`) |

## 2. Payment (결제)
- If the payment window (결제창, PG) is a new window or popup, open it within the user's click handling. Opening it after an asynchronous task following the click may get it blocked by the browser (general advice, per-browser policy unverified). Provide guidance for when it is blocked
- Preventing duplicate payment: change the button to processing immediately on click (LD-06 in `../../references/loading.md`), and the server also rejects repeated requests for the same order (general advice)
- Back and refresh during payment: confirm and show the result from the order state on the server, not from screen state, and make sure a refresh does not become a second payment (general advice)
- Show the total and fees from the start in the summary just before payment (DP-07)

| Screen state | Error message example | Accessibility requirement |
|---|---|---|
| Before payment, payment window open, checking result | 결제창이 열리지 않았어요. 팝업 차단을 풀고 다시 눌러 주세요 (meaning: The payment window did not open. Turn off the popup blocker and press again) | `aria-disabled` on the processing button, `role="status"` for state changes |
| Checking | 결제 결과를 확인하고 있어요. 이 화면을 닫지 말아 주세요 (meaning: Checking the payment result. Do not close this screen) | State in text whether it is safe to close |
| Success | (no error) show order number and amount (주문번호) | Move focus to the result heading (general advice) |
| Failure, cancel | 결제가 완료되지 않았어요. 결제 수단을 확인하고 다시 시도해 주세요 (meaning: The payment was not completed. Check the payment method and try again) | Show failure and cancel distinctly, do not distinguish by color alone (1.4.1) |

## 3. Currency format (금액 표기)
- `new Intl.NumberFormat('ko-KR', { style: 'currency', currency: 'KRW' }).format(19000)` gives `₩19,000` (verified: run on Node v24.22.1). `currencyDisplay: 'name'` gives `19,000 대한민국 원`. To write it with `원` (won), apply `toLocaleString('ko-KR')` to the number and append `원`
- `19000.6` is rounded to `₩19,001` (verified: same run). Show the integer won value given by the server as it is, and do not compute or round amounts on screen (general advice)
- Input field uses `inputmode="numeric"`, commas are for display only and the submitted value is digits only (general advice). Column alignment uses `tabular-nums` (`../../references/design-system.md`, Korean for now)
- How screen readers read `₩` is unverified. Where reading aloud matters, write it with the `원` character (general advice)

| Screen state | Error message example | Accessibility requirement |
|---|---|---|
| No value, 0 won, large value | 금액을 숫자로 입력해 주세요 (meaning: Enter the amount as a number) | Announce amount changes with `role="status"` (DP-05) |

## 4. Address input (주소 입력)
- Field separation: postal code (우편번호), road-name address (도로명 주소) or lot-number address (지번 주소) (filled by search), detailed address (상세 주소). `autocomplete` is `postal-code`, `address-line1`, `address-line2` (verified: MDN value descriptions). Use `street-address` only when the whole address is taken in one field
- If an address search service (widget or API) is used, check the widget's accessibility per provider (unverified). When selection is finished, move focus to the detailed address field (general advice)
- The number of postal code digits and the road-name and lot-number notation follow the response values of the address provider service (the digit rule is unverified)

| Screen state | Error message example | Accessibility requirement |
|---|---|---|
| Empty, searching, no results, selected | 주소를 검색해 선택해 주세요 (meaning: Search for an address and select it) | Announce the number of search results with `role="status"` |
| Detailed address missing | 상세 주소를 입력해 주세요 (meaning: Enter the detailed address) | Focus on the error field, keep the value |

## 5. Hangul input (한글 입력)
- The canonical rules for Enter and Escape during composition, search debounce, and character counting are section 2 of `../../references/interaction-rules.md`, the input table of `../../references/modern-web.md`, and DF-27 of `defaults.md` (the first two are Korean for now). Do not decide them again here
- Check for this flow: in every submit field that takes Hangul, press Enter while the last character is still being composed and confirm with a real input method editor that the submit happens only once (general advice)

| Screen state | Error message example | Accessibility requirement |
|---|---|---|
| Composing, committed | 글자 수를 넘었어요. {max}자까지 입력할 수 있어요 (meaning: The character limit was exceeded. You can enter up to {max} characters) | Update the character count after composition is committed, prevent a burst of screen reader announcements |

## 6. Personal information consent screen (개인정보 동의 화면)
- Divide required and optional into sections and leave optional items unchecked by default. `전체 동의` (agree to all) turns on the sub-items only when the user presses it (DP-02 in `../../references/dark-patterns.md`, Korean for now). The service must be usable without agreeing to optional items. For the legal provisions, see the section `법규 대응 (대한민국)` (legal compliance, Republic of Korea) of the same file
- Open the full terms by link, and if it opens in a new window, say so in the link text (general advice)

| Screen state | Error message example | Accessibility requirement |
|---|---|---|
| All unchecked, partly selected, all selected | 필수 항목에 동의해야 가입할 수 있어요 (meaning: You can sign up only if you agree to the required items) | `<fieldset>` and `<legend>`, a `<label>` for each item (3.3.2). If `전체 동의` is a native checkbox, set `indeterminate = true` by script when partly selected. Only a hand-made checkbox uses `aria-checked="mixed"` (verified: ARIA in HTML prohibits using `aria-checked` on `input type=checkbox`) |

## What this file does not cover
- Specifications for identity verification and payment gateway (PG) integration, per-provider screens and error codes
- Simple authentication (간편인증), joint certificate (공동인증서), and financial security program installation flows
- Collection and storage of resident registration numbers (주민등록번호), consent of a legal guardian for children under 14
- Content of legally required notice text, input screens per payment method, foreign currencies, app store payments
- Internals of address search widgets, postal code rules
- Differences in reading by version of domestic assistive technology (such as Sense Reader)
