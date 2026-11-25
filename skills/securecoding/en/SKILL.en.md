Korean original: ../SKILL.md. IDs and numbering are identical.
Evidence tags are kept as in the Korean original: `[원문]` source page read, `[요약 확인]` checked via fetched summary, `[KISA]` KISA guide read, `[일반]` common practice not verified, `[미실행]` command not run.

# Secure Coding (security design and development review)

Description (frontmatter of the Korean original): Use when writing or reviewing code where external input is interpreted or authentication state changes (sessions and cookies, redirects, server-side URL fetch, XML and deserialization, CI workflows, Dockerfile, CORS). Secure coding, security check, security report, vulnerability, injection, permission. Initial project setup belongs to the kickoff skill.

Set the security structure at the start. When writing or reviewing code during development, apply the 24 security controls (SEC-01 to SEC-24) and record the results. Design and implementation items of the Korean secure development guide (KISA) are mapped to the controls in `../references/kisa-map.md` (Korean for now). This skill is a design guideline and checklist. It does not replace penetration testing.

## When to use
- Request for security structure design of a new project, security checklist, attack scenario tests, or security report
- Code for login, passwords, verification codes, sessions, cookies, admin pages, permission management
- Screens that put an object ID in the URL (IDOR), input fields for price, quantity, coupon, payment, and sign-up (admin privilege injection)
- Code that shows user input on screen or uses it in a DB, file path, command, redirect, XML, or external URL call (SQL injection, XSS, CSRF, path manipulation, open redirect, command injection, SSRF)
- File upload, dependencies and CI workflows, Dockerfile, CORS and security header settings, cloud settings (Cloudflare, AWS, Oracle Cloud, public buckets, IAM)
- API keys, `.env`, encryption algorithms, plaintext storage, direct DB access code
- LLM or AI features (prompt injection)
- Review against domestic (Korean) software development security (KISA security weaknesses) or delivery criteria

## Order of use
1. **Design (before building features)**: Fill in `docs/security/security-architecture.md` (`templates/security-architecture.md`) using the layer structure and principles in `../references/architecture.md` (Korean for now). Decide roles, path classes, where values are computed, secret storage and keys allowed to be public, default values for verification codes and passwords, and AI tool permissions. Write policy values in this document. If unknown, write `미정` (undecided)
2. Confirm the project profile (use the answers if the `kickoff` skill already asked): personal or confidential data, login, file upload, DB use, admin screen, payment or coupon, verification code, AI feature, deployment (internet or closed network), external integration. Ask with `AskUserQuestion` only about items that cannot be read from the code or the request and that change which controls apply (multiple choice, at most 3 questions per call, with 'Not sure' and 'Proceed with defaults' options): internet exposure, personal data or payment handling, delivery standard (KISA diagnosis or not). Do not ask for a small request such as reviewing one code fragment. If 'Proceed with defaults' is chosen, record the assumptions in the report
3. Pick the required controls from the table below. Add controls not in the table too when the code shows the matching element
4. After implementation, check in the order `code review, automated check, abuse scenario test, fix, retest`. For abuse scenarios, try the matching rows of the 29-test table in `references/attack-tests.md` directly
5. If a domestic review or delivery criterion (software security weakness diagnosis) applies, use `../references/kisa-map.md` (Korean for now) to see which control confirms each KISA item. For incident cases, see `../references/incidents.md` (Korean for now)
6. Record the result in the `templates/security-report.md` format. Per item: `PASS(test) / PASS(inspection) / FAIL / NOT_APPLICABLE / NOT_TESTED`, evidence, owner, date, exception approval. For automated checks (SEC-18), also write tool name and version, command, and exit code
7. Do not record a test that was not run as PASS. Judging by reading the code that it is correct is not a test

## Required controls by condition
Condition names are the same as the question items of the `kickoff` skill (type, data, features, deployment) and the conditions for creating the security design document. For the other conditions in the table below, check in the code.

| Condition | Required IDs |
|---|---|
| All projects | SEC-05, 12, 16, 18, 24 (language-independent items are always judged, `../references/kisa-map.md` (Korean for now) 3-2, 5-2, 1-14, 6-1, etc.) |
| Server or API | SEC-07, 13, 14 |
| Login | SEC-02, 03, 07, 15 |
| Uses sessions or cookies | SEC-10. Add SEC-09 if authenticating by cookie |
| Verification code or password reset | SEC-02, 06 |
| Admin screen | SEC-06, 07 |
| DB use | SEC-01, 17 |
| Shows user input on screen | SEC-08, 14 |
| File upload | SEC-04, 22 |
| Puts request body into an object as is | SEC-20 |
| Server calls an external URL | SEC-13 |
| Uses file paths, OS commands, redirects, XML, LDAP, dynamic code execution | SEC-22 |
| Payment or coupon | SEC-19 |
| AI feature | SEC-21 |
| Handles personal or confidential data, passwords, keys | SEC-23 |
| Deployment: internet or closed network | SEC-11, 17 |
| Uses a language with language-specific items such as C, C++, Java | SEC-24 language-specific items (`../references/kisa-map.md`, Korean for now). If not used, those items are `NOT_APPLICABLE` |

## Control list
Detailed criteria and values are in `../references/controls.md` (Korean for now).

| ID | Category | Key point |
|---|---|---|
| SEC-01 | SQL injection | Server-side input validation + parameterized queries. Allowlist for dynamic identifiers |
| SEC-02 | Brute force | Control based on failed login count (delay, temporary block, additional authentication. 5 is a user policy value; KISA 2-16 does not set a count). Rate limit per account and per IP. Permanent lockout risks lockout abuse |
| SEC-03 | Password hash | Argon2id preferred. No plaintext, reversible form, or plain SHA-256 or MD5 |
| SEC-04 | File upload | Extension allowlist, cross-check of signature and MIME, size limit, regenerate file name, store outside the web root |
| SEC-05 | Dependency vulnerabilities | Check with an audit tool, update after impact assessment, build, test, and re-audit. Do not use `npm audit fix --force` carelessly |
| SEC-06 | Verification code (OTP) and reset | Single use, expiry and attempt limit (ASVS 5.0 V6 values are in `../references/controls.md`), uniform reset response (do not reveal whether the account exists), multi-factor for critical accounts, password policy (KISA if the client's requirement is KISA, otherwise ASVS 5.0) |
| SEC-07 | Permission management | Server-side authentication and authorization on every API, least privilege, defense against object ID tampering (IDOR/BOLA) |
| SEC-08 | XSS | Context-specific output encoding, safe DOM APIs, CSP when needed |
| SEC-09 | CSRF | Defense for state-changing requests under cookie authentication, SameSite and Origin checks |
| SEC-10 | Session and cookie | Secure, HttpOnly, SameSite, expiry, reissue, invalidate on logout |
| SEC-11 | Transport security | HTTPS/TLS, no plaintext transmission of sensitive information |
| SEC-12 | Secrets | Keep keys and passwords out of code and Git, per-environment secret management |
| SEC-13 | API input handling | Request size and rate limits, SSRF, deserialization, error responses. SSRF and deserialization details are in `../references/controls.md` SEC-13 |
| SEC-14 | Security settings | Remove debug and test accounts, restrict CORS origins, security headers, do not expose internal information on errors |
| SEC-15 | Logging | Record authentication failures and permission denials, do not record tokens, passwords, or personal data |
| SEC-16 | Supply chain and build | Lockfile, SBOM, provenance verification, least privilege for CI/CD |
| SEC-17 | Deployment and infrastructure | Network separation, minimum ports, non-root containers, verify backup and recovery |
| SEC-18 | Testing and response | SAST, SCA, DAST, threat modeling, incident response, regression tests. Record tool name and version, command, and exit code of automated checks in the report (details in `../references/controls.md` SEC-18) |
| SEC-19 | Business logic and payment | Server computes price, total, and stock, validate quantity range, DB constraint for coupon duplication, payment success by server-to-server signature verification and amount matching |
| SEC-20 | Input field allowlist | Do not put the request body directly into an object, DTO and allowlist, defense against `role` and `isAdmin` injection |
| SEC-21 | AI feature | Separate instructions from data, treat model output as untrusted, code outside the model enforces permissions, least privilege for tools |
| SEC-22 | Injection (excluding SQL) | Code execution, OS commands, path manipulation, open redirect, XML external entities, LDAP, newline in response headers. Allowlist wherever external input is interpreted |
| SEC-23 | Cryptography and data protection | Standard algorithms and sufficient key length, random numbers for security decisions, encrypt storage and transmission of critical information, certificate verification, signature verification |
| SEC-24 | Language-specific code safety | Language-independent items (integer range, null, resource release, infinite recursion, race condition, data sharing between requests) are always judged. Language-specific items such as C and C++ memory or array exposure in class-based languages apply only to that language, otherwise `NOT_APPLICABLE` |

SEC-13's command injection and path manipulation were moved to SEC-22. SEC-13 covers request size and rate limits, SSRF, deserialization, and error responses.

## Files
- `../references/controls.md` (Korean for now): control details and primary sources (`[원문]` OWASP checked, `[KISA]` guide checked, `[일반]` not verified)
- `../references/architecture.md` (Korean for now): security structure and principles for the starting phase
- `references/attack-tests.md`: attack scenario test table, 29 tests
- `../references/kisa-map.md` (Korean for now): control map for the 설계기준 (design criteria) 20 items and 구현약점 (implementation weaknesses) 49 items of 전자정부 SW 개발·운영자를 위한 소프트웨어 개발보안 가이드 (Software Development Security Guide for e-Government SW Developers and Operators, KISA, 2021.12.29)
- `../references/incidents.md` (Korean for now): domestic and overseas incident cases and control index (evidence grade shown)
- `../references/cloud.md` (Korean for now): rules for app developers from the official security documents of Cloudflare, AWS, and Oracle Cloud
- `templates/security-architecture.md`, `templates/security-report.md`

## What not to do
- Do not bulk-update dependencies without user approval (separate diagnosis from actual change)
- Do not write an unchecked item as safe
- Out of scope for this skill: penetration testing, legal compliance judgment, review of the actual production environment
