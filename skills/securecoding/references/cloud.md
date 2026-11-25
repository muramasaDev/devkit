# 클라우드 플랫폼 보안 가이드 보강 (Cloudflare, AWS, Oracle Cloud)

2026-11-25 에 각 사의 공식 문서를 읽고 앱 개발자에게 해당하는 규칙만 추렸다. 표기: `[CF]` Cloudflare, `[AWS]`, `[OCI]` Oracle Cloud 및 Oracle Database. 요약이며 수치와 설정 이름은 출처 페이지에서 다시 확인한다. 통제 ID 는 이 스킬이 붙인 것이다.
읽지 못한 것: Oracle Java SE 시큐어 코딩 지침 및 Oracle 시큐어 코딩 표준 (접속 403), CF 의 CSP 및 CSRF 및 CORS 전용 안내. 이 범위는 근거 없이 채우지 않았다.

## 비밀과 자격증명 (SEC-12)
- 민감 정보는 설정 `vars` 가 아니라 secrets 에 둔다. 로컬 비밀 파일 (`.dev.vars*`, `.env*`) 은 `.gitignore` 에 넣는다 [CF]
- 서버 워크로드는 장기 키 대신 역할의 임시 자격증명을 쓴다 (IAM 역할, instance principals) [AWS, OCI]
- 자격증명을 소프트웨어, 문서, GitHub 업로드 코드에 하드코딩하지 않는다. 여러 사용자가 자격증명을 공유하지 않는다 [OCI]
- 장기 키는 퇴사 등 필요 시 갱신하고 마지막 사용 정보로 안전하게 삭제한다 [AWS]. 암호와 API 키는 90일 이하 주기로 회전하고 새 키를 확인한 뒤 기존 키를 비활성화한다 [OCI]
- 비밀정보는 관리 서비스에 저장하고 자동 교체를 설정한다. 접근은 최소 권한으로 하고 접근 기록을 감사한다 [AWS]
- Turnstile 같은 서비스의 secret key 는 클라이언트 코드에 노출하지 않는다 [CF]
- 서버리스의 이름과 태그 같은 자유 입력 칸에 고객 이메일 등 민감정보를 넣지 않는다. 청구 및 진단 로그에 쓰일 수 있다 [AWS]

## 권한과 관리자 영역 (SEC-06, 07)
- 필요한 권한만, 특정 자원과 조건으로 부여한다. 미사용 사용자, 역할, 권한은 정기 검토 후 제거한다 [AWS]. 그룹에도 필요한 최소 권한만 준다 [OCI]
- 루트 계정은 루트 전용 작업에만 쓰고 일상 작업용 관리자를 따로 만든다. 루트 액세스 키를 만들지 않는다. MFA 는 피싱 방지 방식 (패스키, 보안 키) 을 권장한다 [AWS]
- 관리자 및 내부 앱은 접근 게이트웨이 (Access) 로 보호하고 기본은 거부다. 정책에 Bypass 를 영구 접근에 쓰지 않는다. 오리진은 전달된 JWT 를 서명과 `iss`, `aud`, `exp` 로 검증하고 공개키는 하드코딩하지 않고 조회한다 [CF]
- 사람의 콘솔 로그인은 ID 공급자 연합과 MFA 를 쓴다 [AWS, OCI]
- 데이터베이스: 기본 계정은 잠그거나 만료시키고 기본 암호를 바꾼다. 권한은 롤에만 부여하고 `ANY` 권한을 최소화하며 일반 앱 계정에서 `RESOURCE`, `CONNECT` 롤을 회수한다 [OCI]

## 공개 노출 (SEC-14, 17)
- 인터넷 공개가 명시적으로 필요하지 않으면 객체 저장소를 공개하지 않는다. S3 Block Public Access, `"Principal": "*"` 정책과 Everyone 대상 ACL 점검 [AWS]. OCI 버킷 기본값은 `NoPublicAccess` 이고 공개 전 용도를 평가한다 [OCI]
- SSH 와 RDP 는 승인된 주소 범위에서만 열고 `0.0.0.0/0` 으로 열지 않는다. DB 같은 민감 호스트는 비공개 서브넷에 둔다 [OCI]
- 오리진이 프록시 요청만 받게 하고 (Authenticated Origin Pulls), 아웃바운드 연결만 쓰는 터널로 인바운드를 모두 막을 수 있다 [CF]
- API 문서 포털에 인증을 요구한다. 인증 없는 공개 API 와 WAF 없는 공개 API 를 우선 조치한다 [AWS]
- 개인 데이터가 든 응답은 `Cache-Control: private` 또는 `no-store` 로 보낸다. `Set-Cookie` 응답은 캐시하지 않는다. 추가 경로로 정적 파일처럼 요청하는 캐시 기만을 오리진이 거부한다. 캐시 키에 없는 헤더 값을 응답에 반사하지 않는다 [CF]
- WAF 규칙은 운영 반영 전에 스테이징에서 시험하고 count 모드로 확인한 뒤 활성화한다 [AWS]

## 속도 제한과 봇 (SEC-02, 06, 19)
- 인증 시도 제한 예 [CF 문서 예시, 플랜별 한도 다름]: `POST /login` 에서 IP 기준 401 또는 403 응답만 집계해 분당 4건 초과 시 챌린지
- OTP 및 검증 엔드포인트 예 [CF 문서 예시]: 정확한 경로에 실패가 401 또는 403 이면 분당 5건 초과 시 10분 차단. 항상 200 을 주는 구조면 전체 집계 분당 10건 초과 시 챌린지
- 속도 제한은 정밀하지 않다 (카운터 갱신 지연, 데이터 센터별 카운터). 앱 자체 제한을 대체하지 않는다 [CF]
- 봇 확인 토큰 (Turnstile) 은 서버에서 반드시 검증한다. 토큰은 위조할 수 있고 300초 만료, 1회용이다. 응답의 action 과 hostname 도 확인한다 [CF]
- 유출된 자격증명 탐지 기능으로 대입 시도를 경고할 수 있다 [CF]
- API 게이트웨이의 스로틀링은 초과 시 `429` 이고 한도는 목표치이며 보장 상한이 아니다 [AWS]

## 전송과 저장 암호화 (SEC-11, 23)
- 오리진 인증서를 검증하는 Full (strict) 모드를 쓴다. Off 와 Flexible 은 구간이 평문이다. HSTS 는 먼저 HTTPS 를 활성화한 뒤 쓴다. 최소 TLS 버전을 올려 TLS 1.0 을 차단한다 [CF]
- 버킷 정책에 `aws:SecureTransport` 조건으로 HTTPS 만 허용한다 [AWS]. 서버리스는 TLS 1.2 필수, 1.3 권장 [AWS]. OCI 는 전송 기본 TLS 1.2 [OCI]
- 저장 데이터는 기본 암호화한다. S3 는 SSE-S3 기본, SSE-C 는 필요하지 않으면 비활성 [AWS]. 객체 스토리지는 AES-256 이고 사용자 지정 키는 Vault 로 관리하며 키 접근은 IAM 으로 엄격히 제한한다 [OCI]
- DB 의 민감 데이터와 백업 매체는 암호화한다 (TDE) [OCI]

## 입력과 API (SEC-13)
- 본문을 전부 읽는 요청은 읽기 전에 최대 크기를 강제한다 [CF]
- OpenAPI 스키마와 요청을 비교하는 검증 (JSON 및 폼 본문만, 응답은 검증하지 않음) 과 JWT 검증을 게이트웨이에서 한다. 스키마 위반 탐지는 자체로 차단하지 않고 규칙으로 차단한다 [CF]
- API 접근 제어 수단 (리소스 정책, IAM, JWT 및 Lambda 권한 부여자, 사용자 풀, 클라이언트 인증서, WAF) 을 목적에 맞게 조합한다 [AWS]

## 코드 작성 (SEC-14, 23, 24)
- 요청별 상태를 모듈 전역 변수에 저장하지 않는다. 인자로 전달한다 [CF] (KISA 6-1 과 같은 취지)
- 보안용 난수는 `crypto.getRandomValues()`, `crypto.randomUUID()` 를 쓰고 `Math.random()` 을 쓰지 않는다 [CF]
- 비밀 비교는 상수 시간 비교 (`timingSafeEqual`) 로 하고 양쪽을 고정 길이로 해시한 뒤 비교한다 [CF]
- 오류 시 오리진으로 열리는 방식 (`passThroughOnException`) 을 피하고 `try...catch` 로 처리한다 [CF]

## 로그와 감사 (SEC-15)
- 운영 전에 로그와 추적을 켜고 구조화된 오류를 기록한다 [CF]
- 감사 로그를 지속 보관하고 (콘솔 기록 90일), 전 리전 trail 을 만들며, 로그 무결성 검증을 켜고, 별도 계정의 전용 버킷에 암호화해 보관한다 [AWS]. OCI Audit 은 모든 API 호출을 기록한다 [OCI]
- 루트 로그인과 사용을 감시한다 [AWS]
- DB 감사는 최소 사용자 접근, 시스템 권한 사용, 스키마 변경을 포함하고 반복 로그인 실패와 비정상 시간 접근을 감시한다 [OCI]

## 설계 원칙 (architecture.md 와 같은 방향)
- 모든 계층에 보안을 적용하고 통제를 버전 관리되는 템플릿으로 코드화한다 [AWS Well-Architected 보안 원칙, 문서가 historical reference 로 표시됨]
- 공동 책임: 선택한 서비스에 따라 고객 책임이 달라진다. 서버를 직접 운영하면 OS 패치와 설치 앱과 방화벽 설정이 고객 책임이다 [AWS]

## 출처 (읽은 페이지)
- Cloudflare 문서 (developers.cloudflare.com): `workers/configuration/secrets`, `workers/best-practices/workers-best-practices`, `waf/managed-rules`, `waf/custom-rules`, `waf/rate-limiting-rules/best-practices`, `waf/detections/leaked-credentials`, `api-shield/security/schema-validation`, `api-shield/security/jwt-validation`, `api-shield/security/mtls`, `ssl/origin-configuration/ssl-modes`, `ssl/origin-configuration/authenticated-origin-pull`, `ssl/edge-certificates/additional-options/http-strict-transport-security`, `ssl/edge-certificates/additional-options/minimum-tls`, `turnstile/get-started/server-side-validation`, `cloudflare-one/policies/access`, `cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app`, `cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json`, `cloudflare-one/networks/connectors/cloudflare-tunnel`, `cache/cache-security/cache-deception-armor`, `cache/cache-security/avoid-web-poisoning`, `cache/concepts/cache-control`
- AWS 문서 (docs.aws.amazon.com): `IAM/latest/UserGuide/best-practices.html`, `IAM/latest/UserGuide/root-user-best-practices.html`, `AmazonS3/latest/userguide/security-best-practices.html`, `secretsmanager/latest/userguide/best-practices.html`, `apigateway/latest/developerguide/security-best-practices.html`, `apigateway/latest/developerguide/api-gateway-request-throttling.html`, `waf/latest/developerguide/waf-rule-statement-type-rate-based.html`, `waf/latest/developerguide/web-acl-testing.html`, `lambda/latest/dg/security-dataprotection.html`, `awscloudtrail/latest/userguide/best-practices-security.html`, `wellarchitected/latest/security-pillar/security.html`, https://aws.amazon.com/compliance/shared-responsibility-model/
- Oracle 문서 (docs.oracle.com): `en-us/iaas/Content/Security/Reference/objectstorage_security.htm`, `iam_security_topic-IAM_Credentials.htm`, `networking_security.htm`, `securityzone_security.htm`, `en-us/iaas/Content/KeyManagement/Concepts/keyoverview.htm`, `en/database/oracle/oracle-database/19/dbseg/` 의 `guidelines-securing-user-accounts-and-privileges.html`, `guidelines-securing-passwords.html`, `guidelines-auditing.html`, `guidelines-securing-data.html`
