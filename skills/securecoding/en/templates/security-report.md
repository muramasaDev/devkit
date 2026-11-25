# Security Check Report

- Project:
- Check date:
- Test date:
- Owner:
- Commit hash under check:
- Test environment (URL, dev or test environment only):
- Tools and versions (all used for automated checks and tests):
- Scope (which of code review / automated check / abuse scenario test were run):
- Project profile (personal data, authentication method, internet or closed network, external integration):

Status values
- `PASS(test)`: the request was actually sent and the pass criterion was confirmed
- `PASS(inspection: file:line and command output)`: for controls where the inspection itself is the evidence (e.g., SEC-03 hash settings, SEC-16 lockfile). Write the file, line, and command output checked in the evidence column
- `FAIL`: defect confirmed. Fill in severity, retest date, and retest result
- `NOT_APPLICABLE`: not applicable (reason required)
- `NOT_TESTED`: not run

Do not record a test that was not run as PASS. Judging by reading the code that it is correct is not a test.

| ID | Status | Evidence (file, command, result) | Severity (FAIL) | Action and exception approval | Retest date | Retest result |
|---|---|---|---|---|---|---|
| SEC-01 | | | | | | |
| SEC-02 | | | | | | |
| SEC-03 | | | | | | |
| SEC-04 | | | | | | |
| SEC-05 | | | | | | |
| SEC-06 | | | | | | |
| SEC-07 | | | | | | |
| SEC-08 | | | | | | |
| SEC-09 | | | | | | |
| SEC-10 | | | | | | |
| SEC-11 | | | | | | |
| SEC-12 | | | | | | |
| SEC-13 | | | | | | |
| SEC-14 | | | | | | |
| SEC-15 | | | | | | |
| SEC-16 | | | | | | |
| SEC-17 | | | | | | |
| SEC-18 | | | | | | |
| SEC-19 | | | | | | |
| SEC-20 | | | | | | |
| SEC-21 | | | | | | |
| SEC-22 | | | | | | |
| SEC-23 | | | | | | |
| SEC-24 | | | | | | |

## Automated check log (SEC-18, SEC-05, SEC-16)
One line per automated check run. If not run, `NOT_TESTED`.

| Check | Tool name and version | Command | Exit code | Result summary |
|---|---|---|---|---|
| Static analysis (SAST) | | | | |
| Dependency audit (SCA) | | | | |
| Secret detection | | | | |
| Dynamic check (DAST) | | | | |

## Attack scenario tests (based on `../references/attack-tests.md`)
Only requests actually sent count as `PASS(test)`. If the feature does not exist, `NOT_APPLICABLE` with the reason.

| # | Attack | Status | Request sent and result | Severity (FAIL) | Action | Retest date | Retest result |
|---|---|---|---|---|---|---|---|
| 1 | Append /admin to the address | | | | | | |
| 2 | Change the ID in the URL | | | | | | |
| 3 | API key in the browser | | | | | | |
| 4 | Edit price and name directly | | | | | | |
| 5 | Order quantity -1 | | | | | | |
| 6 | Forge payment success | | | | | | |
| 7 | Use a coupon 100 times | | | | | | |
| 8 | Sign up as admin | | | | | | |
| 9 | Brute-force the verification code | | | | | | |
| 10 | Tell the AI to 'ignore instructions' | | | | | | |
| 11 | Script in the nickname | | | | | | |
| 12 | Upload a non-image file | | | | | | |
| 13 | .env exposed on GitHub | | | | | | |
| 14 | Query the DB directly | | | | | | |
| 15 | Path manipulation | | | | | | |
| 16 | Open redirect | | | | | | |
| 17 | Internal information on error screens | | | | | | |
| 18 | Assume admin account takeover | | | | | | |
| 19 | Change without identity verification | | | | | | |
| 20 | Logout and session reuse | | | | | | |
| 21 | SQL injection | | | | | | |
| 22 | CSRF | | | | | | |
| 23 | SSRF | | | | | | |
| 24 | Login brute force and spraying | | | | | | |
| 25 | Session fixation | | | | | | |
| 26 | CORS reflection | | | | | | |
| 27 | OS command injection | | | | | | |
| 28 | XXE and deserialization | | | | | | |
| 29 | Excessive response exposure | | | | | | |
