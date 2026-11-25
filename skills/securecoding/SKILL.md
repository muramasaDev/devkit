---
name: securecoding
description: Use when designing the security structure of a new project, or when writing, reviewing or auditing code that handles login, passwords, sessions, admin pages, object IDs in URLs, prices, quantities, coupons, payments, sign-up fields, OTP codes, file uploads, database access, user input shown on screen, LLM or AI features, API keys, .env files, or third-party dependencies, or when a project needs a security checklist, attack scenario tests or a security report. SQL 인젝션, 무차별 대입, 비밀번호 해시, 파일 업로드 검증, 의존성 취약점, 권한 관리, 관리자 페이지, ID 변조, IDOR, 가격 조작, 수량 음수, 쿠폰 중복, 결제 위조, 가입 시 관리자 권한, 인증번호, 프롬프트 인젝션, XSS, CSRF, 세션, API 키 노출, .env 노출, DB 직접 접근, 클라우드 설정 (Cloudflare, AWS, Oracle Cloud, 공개 버킷, IAM), 경로 조작, 열린 리다이렉트, 명령어 삽입, 암호화 알고리즘, 평문 저장, 시큐어코딩, 소프트웨어 개발보안 (KISA 보안약점), 보안 설계, 보안 점검 요청, 보안 체크리스트, 보안 리포트에 사용.
---

# Secure Coding (보안 설계 및 개발 점검)

시작 단계에서 보안 구조를 정하고, 개발 중 코드를 쓰거나 검수할 때 보안 통제 24개 (SEC-01 ~ SEC-24) 를 적용해 결과를 기록한다. 국내 개발보안 가이드 (KISA) 의 설계 및 구현 항목은 `references/kisa-map.md` 로 통제에 대응시켜 두었다. 이 스킬은 설계 지침과 체크리스트이며 침투시험을 대신하지 않는다.

## 쓰는 순서
1. **설계 (기능을 만들기 전)**: `references/architecture.md` 의 계층 구조와 원칙으로 `docs/security/security-architecture.md` (`templates/security-architecture.md`) 를 채운다. 역할, 경로 구분, 값의 계산 위치, 비밀 보관, 인증번호 수치, AI 도구 권한을 정한다. 모르면 `미정`
2. 프로젝트 성격을 확인한다: 개인정보 또는 기밀 데이터 여부, 인증 방식, 인터넷 또는 폐쇄망, 외부 연동, 결제 및 쿠폰 여부, AI 기능 여부
3. 해당하는 통제를 고른다. 로그인이 있으면 SEC-01 ~ SEC-07 은 필수, 금액 또는 쿠폰이 있으면 SEC-19, 요청 본문을 객체에 넣는 곳은 SEC-20, AI 기능이 있으면 SEC-21, 개인정보 및 비밀번호 및 키를 다루면 SEC-23, 파일 경로 및 명령 실행 및 리다이렉트가 있으면 SEC-22. SEC-24 는 C, C++, Java 등 해당 언어일 때만
4. 구현 후 `코드 검토, 자동 점검, 악용 시나리오 테스트, 수정, 재테스트` 순서로 확인한다. 악용 시나리오는 `references/attack-tests.md` 의 20개 시험표에서 해당 행을 직접 시도한다
5. 국내 점검 또는 납품 기준 (소프트웨어 보안약점 진단) 이 있으면 `references/kisa-map.md` 로 KISA 항목이 어느 통제에서 확인되는지 본다. 사고 사례가 필요하면 `references/incidents.md`
6. 결과를 `templates/security-report.md` 형식으로 남긴다. 항목별 `PASS / FAIL / NOT_APPLICABLE / NOT_TESTED`, 근거, 담당자, 날짜, 예외 승인
7. 실행하지 않은 시험을 PASS 로 적지 않는다. 코드를 읽고 맞다고 판단한 것은 시험이 아니다

## 통제 목록
상세 기준과 수치는 `references/controls.md`.

| ID | 범주 | 핵심 |
|---|---|---|
| SEC-01 | SQL 인젝션 | 서버 입력 검증 + 매개변수화 쿼리. 동적 식별자는 허용 목록 |
| SEC-02 | 무차별 대입 | 로그인 5회 실패부터 통제 (지연, 임시 차단, 추가 인증). 계정과 IP 기준 속도 제한. 영구 잠금은 잠금 악용 위험 |
| SEC-03 | 비밀번호 해시 | Argon2id 우선. 평문, 복호화 가능 형태, 단순 SHA-256 또는 MD5 금지 |
| SEC-04 | 파일 업로드 | 확장자 허용 목록, 시그니처 및 MIME 교차 검증, 크기 제한, 파일명 재생성, 웹 루트 밖 저장 |
| SEC-05 | 의존성 취약점 | 감사 도구로 확인, 영향 평가 후 업데이트, 빌드와 테스트와 재감사. `npm audit fix --force` 를 무심코 쓰지 않음 |
| SEC-06 | 인증 및 MFA | 중요 계정 다중요소, 복구, 재인증, 계정 존재 여부 노출 방지 |
| SEC-07 | 권한 관리 | 모든 API 에 서버 측 인증 및 인가, 최소 권한, 객체 ID 변경 (IDOR/BOLA) 방어 |
| SEC-08 | XSS | 문맥별 출력 인코딩, 안전한 DOM API, 필요 시 CSP |
| SEC-09 | CSRF | 쿠키 인증의 상태 변경 요청에 방어, SameSite 및 Origin 점검 |
| SEC-10 | 세션과 쿠키 | Secure, HttpOnly, SameSite, 만료, 재발급, 로그아웃 무효화 |
| SEC-11 | 전송 보안 | HTTPS/TLS, 민감정보 평문 전송 금지 |
| SEC-12 | 비밀정보 | 키와 비밀번호를 코드 및 Git 에 넣지 않음, 환경별 시크릿 관리 |
| SEC-13 | API 입력 처리 | 요청 크기 및 속도 제한, SSRF, 역직렬화, 오류 응답 |
| SEC-14 | 보안 설정 | 디버그 및 테스트 계정 제거, CORS 출처 제한, 보안 헤더, 오류 시 내부 정보 비노출 |
| SEC-15 | 로그 | 인증 실패와 권한 거부 기록, 토큰과 비밀번호와 개인정보는 기록하지 않음 |
| SEC-16 | 공급망과 빌드 | lockfile, SBOM, 출처 검증, CI/CD 최소 권한 |
| SEC-17 | 배포와 인프라 | 네트워크 분리, 최소 포트, 컨테이너 non-root, 백업 복구 검증 |
| SEC-18 | 시험과 대응 | SAST, SCA, DAST, 위협 모델링, 사고 대응, 회귀 시험 |
| SEC-19 | 비즈니스 로직과 결제 | 가격과 합계와 재고는 서버가 계산, 수량 범위 검증, 쿠폰 중복은 DB 제약, 결제 성공은 서버 간 서명 검증과 금액 대조 |
| SEC-20 | 입력 필드 허용 목록 | 요청 본문을 객체에 바로 넣지 않음, DTO 와 허용 목록, `role` 및 `isAdmin` 주입 방어 |
| SEC-21 | AI 기능 | 지시와 데이터 분리, 모델 출력도 비신뢰, 권한은 모델 밖 코드가 강제, 도구 최소 권한 |
| SEC-22 | 인젝션 (SQL 제외) | 코드 실행, OS 명령, 경로 조작, 열린 리다이렉트, XML 외부개체, LDAP, 응답 헤더 개행. 외부 입력을 해석되는 곳마다 허용 목록 |
| SEC-23 | 암호와 데이터 보호 | 표준 알고리즘과 충분한 키 길이, 보안 결정용 난수, 중요정보 저장 및 전송 암호화, 인증서 검증, 서명 검증 |
| SEC-24 | 언어 한정 코드 안전성 | C 및 C++ 메모리, 정수 범위, 널, 자원 해제, 무한 재귀, 경쟁조건. 해당 언어일 때만, 아니면 `NOT_APPLICABLE` |

SEC-13 의 명령 주입과 경로 조작은 SEC-22 로 옮겼다. SEC-13 은 요청 크기 및 속도 제한, SSRF, 역직렬화, 오류 응답을 맡는다.

## 파일
- `references/controls.md`: 통제 상세와 원문 출처 (`[원문]` OWASP 확인, `[KISA]` 가이드 확인, `[일반]` 미확인)
- `references/architecture.md`: 시작 단계 보안 구조와 원칙
- `references/attack-tests.md`: 공격 시나리오 시험표 20개
- `references/kisa-map.md`: KISA 소프트웨어 개발보안 가이드 (2021.12.29) 설계기준 20개 및 구현약점 49개와 통제 대응표
- `references/incidents.md`: 국내외 사고 사례와 통제 색인 (근거 등급 표시)
- `references/cloud.md`: Cloudflare, AWS, Oracle Cloud 공식 보안 문서의 앱 개발자용 규칙
- `templates/security-architecture.md`, `templates/security-report.md`

## 하지 않는 것
- 사용자 승인 없이 의존성을 일괄 업데이트하지 않는다 (진단과 실제 변경을 구분)
- 점검하지 않은 항목을 안전하다고 쓰지 않는다
- 이 스킬의 범위 밖: 침투시험, 법규 준수 판단, 실제 운영 환경 점검
