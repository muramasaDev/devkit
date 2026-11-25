# 통제 상세

> OWASP Cheat Sheet Series (https://cheatsheetseries.owasp.org, CC BY-SA 4.0) 를 요약, 재구성, 한국어로 번역한 문서. 이 파일은 CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/) 으로 배포된다. 변경: 요약, 재구성, 번역, 다른 출처와 결합. OWASP 가 보증하지 않는다.

통제는 SEC-01 ~ SEC-24 순서다. 확인 표시는 세 가지다. `[원문]` 원문 페이지를 직접 읽은 것. `[요약 확인]` 웹 페이지 읽기 도구가 돌려준 요약으로 확인한 것 (원문과 한 글자까지 같다고 보장하지 않음). `[일반]` 확인하지 못했고 널리 알려진 내용이라 도입 전 확인이 필요한 것. 실행해 보지 못한 명령은 `[미실행]` 을 함께 적는다. 통제별 확인 수준은 문서 끝의 표에 모았다. 날짜는 확인일이다.

## SEC-01 SQL 인젝션
- 모든 쿼리는 매개변수화 (prepared statement). 문자열 이어 붙이기로 값을 넣지 않는다
- 입력 검증 (타입, 길이, 형식) 은 서버에서 한다. 검증만으로는 방어가 되지 않으며 매개변수화와 함께 쓴다
- 표 이름, 열 이름, 정렬 방향처럼 바인딩할 수 없는 부분은 허용 목록으로 고른다. OWASP 원칙: 매개변수 표시는 값을 나타내며 표 이름, 열 이름, `ASC`, `DESC` 같은 키워드를 나타내지 않는다 `[요약 확인, 2026-11-25]`
- 증거: 쿼리 바인딩 사용 여부를 소스에서 확인, SQL 인젝션 시험
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html

### 스택별 안전 및 위험 코드 쌍 `[요약 확인, 2026-11-25]`
| 스택 | 안전 | 위험 | 근거 |
|---|---|---|---|
| JDBC | `conn.prepareStatement("SELECT balance FROM acct WHERE name = ?")` 후 `ps.setString(1, name)` | `"... WHERE name = '" + name + "'"` 로 이어 붙임 | OWASP SQL Injection Prevention |
| JPQL, HQL | `createQuery("from Inventory where productID=:pid")` 후 `setParameter("pid", v)` | `createQuery("from Inventory where productID='" + v + "'")` | OWASP SQL Injection Prevention |
| MyBatis | `WHERE name = #{name}` `[일반]` (`#{}` 는 PreparedStatement 매개변수로 처리됨) | `WHERE name = '${name}'`, `ORDER BY ${col}` | MyBatis 문서: `${}` 는 값을 변환 없이 넣으며 사용자 입력을 그대로 넘기는 것은 안전하지 않다 |
| node-postgres | `client.query('SELECT * FROM users WHERE id = $1', [id])` | `` client.query(`SELECT * FROM users WHERE id = ${id}`) `` | node-postgres 문서: 문자열 결합은 SQL 인젝션으로 이어진다 |
| Python DB-API | `cur.execute("SELECT * FROM stocks WHERE symbol = ?", (symbol,))` (sqlite3 의 qmark 방식. 드라이버마다 자리표시자 형식이 다름) | `cur.execute("... WHERE symbol = '%s'" % symbol)` | Python sqlite3 문서 |
| Prisma | `` prisma.$queryRaw`SELECT * FROM "User" WHERE name = ${name}` `` (태그 템플릿) | `prisma.$queryRawUnsafe("... WHERE name = " + name)`, `$executeRawUnsafe` | Prisma 문서: `Unsafe` 메서드는 SQL 인젝션 위험이 크다 |
| Sequelize | `sequelize.query('... WHERE status = :status', { replacements: { status } })` 또는 `bind` | `sequelize.query("... WHERE status = '" + status + "'")`. `Sequelize.literal(사용자 입력)` 도 같다 `[일반]` | Sequelize 문서 (replacements 와 bind). 문서 페이지에 `literal` 설명은 없었음 |
| Django | ORM 쿼리셋. `Person.objects.raw("... WHERE last_name = %s", [lname])` | `raw()` 에 문자열 포맷, 자리표시자에 따옴표 (`'%s'`), `extra()` 및 `RawSQL` 에 사용자 입력 | Django 보안 문서 및 raw SQL 문서 |

- 합격 기준: 사용자 입력이 SQL 문자열 안으로 들어가는 경로가 없다. 예외는 허용 목록으로 고른 식별자와 정렬 방향뿐이다
- 검색 (POSIX 셸 기준, PowerShell 은 따옴표를 바꾼다) `[미실행]`
  - `rg -n '\$\{' -g '*Mapper.xml'`
  - `rg -n 'queryRawUnsafe|executeRawUnsafe|Sequelize\.literal'`
  - 결과 한 건마다 허용 근거 (값의 출처가 고정 상수 또는 허용 목록인지) 를 보고서에 기록한다. 근거를 적지 못하는 건은 FAIL

## SEC-02 무차별 대입
- 로그인 5회 실패부터 통제 (사용자 정책). 방식: 점진적 지연, 임시 차단, 추가 인증
- 계정 기준과 IP 또는 네트워크 기준 속도 제한을 같이 둔다
- '영구적으로 5번만 허용' 으로 구현하지 않는다. 남이 계정을 잠가 버리는 공격이 되므로 복구 절차를 둔다
- 로그와 경보를 남긴다
- 증거: 5회와 6회 실패 시험, 여러 IP 시도, 잠금 악용 및 복구 시험

### 기본값 예시 (사용자 정책값)
아래 수치는 이 스킬의 예시이며 KISA 가이드, OWASP, ASVS 어느 문서에도 없는 값이다. 프로젝트가 정해 `security-architecture.md` 5절에 적는다. KISA 2-16 은 시도 횟수 수치를 정하지 않았고 (`kisa-map.md` 3절), 5회는 사용자 정책이다.
| 항목 | 예시 | 비고 |
|---|---|---|
| 계정당 관찰 창 | 15분 안에 5회 실패 | 실패 횟수는 계정에 연결해 센다 (OWASP: 카운터는 IP 가 아니라 계정에 연결) `[요약 확인]` |
| 5회 초과 후 | 지수 지연. 5번째 실패 뒤 30초, 이후 실패마다 2배, 상한 15분 | OWASP 가 지수 잠금을 방식의 하나로 든다. 시작 값, 상한은 사용자 정책값 |
| IP 당 한도 | 분당 20회 시도 (성공 및 실패 합산) | IP 한도는 계정 카운터와 별개로 둔다 |
| 전체 실패율 경보 | 로그인 실패율이 평소의 몇 배를 넘으면 경보. 배수는 운영 데이터로 정함 | 분산 공격은 계정별 및 IP별 한도에 걸리지 않아 전체 지표로 본다 |
| 잠금 악용 대비 | 지연 중에도 비밀번호 재설정 경로는 열어 둔다 | OWASP 가 잠금을 이용한 서비스 거부를 경고하며 재설정으로 로그인하게 하는 방법을 든다 `[요약 확인]` |

### 패스워드 스프레이 및 분산 IP 크리덴셜 스터핑
- 패스워드 스프레이는 약한 비밀번호 하나를 많은 계정에 시도하고, 크리덴셜 스터핑은 다른 사이트에서 유출된 계정 정보 쌍을 시도한다. 계정별 카운터는 두 공격 모두 쉽게 피한다 `[일반]`
- 유출 및 흔한 비밀번호 대조: ASVS 6.2.4 (상위 3000개 이상 비밀번호 대조), 6.2.12 (유출 비밀번호 집합 대조) `[요약 확인]`. 상세는 SEC-06 비밀번호 정책
- 다중요소 인증: OWASP Authentication Cheat Sheet 는 비밀번호 관련 공격 대부분에 대한 최선의 방어로 든다. ASVS 6.3.3 (L2) 도 같다 `[요약 확인]`
- 문서화: ASVS 6.1.1 은 속도 제한, 자동화 방지, 적응형 대응을 어떻게 쓰는지 문서에 정의하고 악의적 계정 잠금을 막으라고 요구한다. 6.3.1 은 크리덴셜 스터핑 및 무차별 대입을 막는 통제를 구현하라고 요구한다 `[요약 확인]`. 정의는 `security-architecture.md` 5절에 적는다
- CAPTCHA 는 방어 심화 수단이며 예방 통제가 아니다. 실패 몇 회 뒤에만 요구하는 방식을 OWASP 가 든다 `[요약 확인]`
- 로그인, 복구, 가입 응답은 계정 존재, 잠금 여부와 상관없이 같은 일반 메시지, 같은 상태 코드, 비슷한 응답 시간으로 한다 `[요약 확인]`
- KISA 2-16 (p275): 인증시도 횟수를 제한하고 실패가 한도를 넘으면 계정 잠금 또는 추가 인증을 거치게 한다. 한국사회복지협의회 사례는 2천만 회 이상의 접속 시도를 탐지하지 못했다 (`incidents.md`)
- 시험: 계정 하나에 6회 실패, IP 하나에서 서로 다른 계정 30개에 같은 비밀번호 1회씩, 여러 IP 에서 계정 하나에 시도. 세 경우 모두 통제 또는 경보가 걸려야 한다 `[미실행]`
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html , https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/en/0x15-V6-Authentication.md

## SEC-03 비밀번호 해시 [원문]
알고리즘 우선순위 (원문 기준): Argon2id, scrypt (Argon2id 불가 시), bcrypt (구형 시스템 한정), PBKDF2 (FIPS-140 요구 시).

| 알고리즘 | 최소 설정 |
|---|---|
| Argon2id | m=19456 (19 MiB), t=2, p=1. 같은 방어 수준의 대안: m=47104 t=1 / m=12288 t=3 / m=9216 t=4 / m=7168 t=5 (모두 p=1) |
| scrypt | N=2^17, r=8, p=1. 대안: N=2^16 p=2 / N=2^15 p=3 / N=2^14 p=5 / N=2^13 p=10 (모두 r=8) |
| bcrypt | 작업 계수 10 이상. 입력 최대 72 바이트 (구현에 따라 더 작을 수 있음), 그 이상은 입력 길이를 제한 |
| PBKDF2 | HMAC-SHA256 600,000회 이상, HMAC-SHA512 220,000회 이상. SHA-1 1,400,000회는 구형 한정, 새 시스템에 고르지 않음 |

- salt: 비밀번호마다 고유한 무작위 값. 대부분의 라이브러리가 자동 생성 및 관리하므로 직접 만들지 않는다
- pepper: 데이터베이스 밖에 보관하는 공통 비밀값. 추가 방어일 뿐이며 바꾸면 비밀번호 재설정이 필요하다
- bcrypt 에서 입력을 미리 해시하는 방식은 널 바이트와 password shucking 문제가 있어 원문이 위험하다고 설명한다
- 금지: 평문, 복호화 가능한 암호화, 단순 SHA-256 또는 MD5
- 증거: 저장된 값 형식, 알고리즘 설정값, 비교 함수 (상수 시간 비교 제공 API)
- KISA 2-14 (p266): 비밀번호를 솔트 없이 해시하면 미리 계산한 해시값으로 찾을 수 있다. 가이드 예제는 솔트를 붙인 SHA-256 이다. OWASP 기준은 위 표를 따르고, 차이는 `kisa-map.md` 3절
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html (페이지에 날짜 표기 없음, 2026-11-25 수치 일치 확인)

## SEC-04 파일 업로드
[원문]
- 확장자는 허용 목록으로 검사한다 (디코딩 후). 차단 목록만으로는 약하다
- Content-Type 헤더는 위조할 수 있다. 파일 시그니처와 함께 확인하고 어느 하나만 믿지 않는다
- 파일명은 무작위 UUID 등으로 다시 만든다. 사용자 이름이 필요하면 길이와 문자 집합을 제한하고 선행 점과 연속 점을 거부한다
- 크기 제한. 압축을 풀 때는 푼 뒤 크기에도 제한을 건다
- 저장: 다른 호스트가 가장 좋고, 아니면 웹 루트 밖. 웹 루트 안은 마지막 수단. 업로드 디렉터리는 디렉터리별 설정 덮어쓰기를 끈다
- 인증된 사용자만 업로드, 파일시스템 최소 권한, 실행 전 검사
- 가능하면 백신 또는 샌드박스 검사, PDF 및 Office 는 콘텐츠 무해화 (CDR)
- 이미지는 디코딩 후 허용 형식으로 다시 인코딩하고 메타데이터를 제거한다. 다시 인코딩해도 악성 내용 제거가 보장되지는 않는다. 이미지 처리 라이브러리는 최신으로 유지하고 형식, 자원, 격리를 제한한다
- 이중 확장자 (`.jpg.php`), 널 바이트 (`.php%00.jpg`), 대소문자 (`.pHp`), 대체 확장자 (`.phtml`, `.php5`), NTFS 스트림 (콜론) 우회를 시험한다
- ZIP: 원문이 압축 폭탄을 가용성 위협으로 들고 ZIP 업로드를 권장하지 않는다고 적었다
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

[일반] 이 문서에 없음, 도입 전 확인
- SVG 는 스크립트를 담을 수 있으므로 업로드 허용 목록에서 빼거나 정제한 뒤 `Content-Disposition: attachment` 로 내려 준다. 업로드한 HTML 및 SVG 를 앱과 같은 출처에서 열면 XSS 가 된다. SEC-08 참조
- 압축 해제 시 항목 경로가 대상 폴더를 벗어나는지 (zip slip) 확인한다. 비교 방법은 SEC-22 경로 조작

증거: 우회 확장자, 이중 확장자, 초과 크기, 악성 파일 시험 결과

## SEC-05 의존성 취약점
- 진단과 변경을 구분한다. 진단 명령은 읽기 전용이다
- 영향도와 실제 사용 여부를 평가한 뒤 검토된 버전으로 올리고, 빌드와 시험과 재감사를 한다
- `npm audit fix --force` 는 주 버전을 올릴 수 있으므로 무심코 쓰지 않는다
- 폐쇄망은 외부 권고 정보에 접근할 수 없다. 내부에서 승인한 취약점 DB 또는 SBOM 점검 방식을 준비한다
- 서버 소프트웨어와 운영체제의 보안 업데이트도 대상이다 (사례). Equifax 는 공개된 Struts 취약점 패치 미적용, SK텔레콤, 롯데카드, 순천향대는 패치 미적용이 개인정보위 자료에 적혔다
- 도구별 명령과 실패 조건은 SEC-18 표

```bash
npm audit                  # 알려진 취약점 보고, 보통 네트워크 필요
npm audit --json           # 자동 처리용 출력
npm audit fix --dry-run    # 가능한 변경 사전 확인
```
npm 문서: https://docs.npmjs.com/cli/commands/npm-audit/

[일반] npm 이 아닌 프로젝트의 감사 도구 (이 문서에서 공식 문서를 확인하지 않음, 도입 전 확인): Go `govulncheck`, Rust `cargo audit`, .NET `dotnet list package --vulnerable`, 언어 공통 `osv-scanner`. Python `pip-audit` 과 Maven `dependency-check-maven` 은 SEC-18 에서 확인했다.

## SEC-06 인증 및 MFA [요약 확인, 2026-11-25]
- 중요 계정은 다중요소 인증을 쓴다. ASVS 6.3.3 (L2): 다중요소 인증 또는 단일요소 인증 수단의 조합으로 접근한다. 6.3.6 (L3): 이메일을 단일 또는 다중요소 인증 수단으로 쓰지 않는다
- 비밀번호 재설정은 켜져 있는 다중요소 인증을 우회하지 않는다 (ASVS 6.4.3, L2)
- 관리자 영역은 역할 기반 접근, 추가 인증, 접속 제한, 인터넷 비노출을 둔다 (KISA 부록 관리자 페이지 예시 p368 및 사례. SEC-07 참조)
- 증거: 중요 계정의 MFA 적용 확인, 재설정 경로로 MFA 를 건너뛰는 시도

### 비밀번호 정책 (KISA 2-9 와 ASVS 5.0 V6)
KISA 2-9 (p252) 는 숫자, 영문자, 특수문자 혼합과 자릿수 등 강한 조건을 검증하고 주기적 변경을 유도한다. ASVS 5.0 V6 은 조합 규칙과 주기 변경 강제를 금지하므로 두 기준은 조합 규칙에서 정면으로 충돌하고, 주기 변경에서는 KISA 가 '유도', ASVS 가 '강제 금지' 라 부딪힌다.
| 항목 | KISA 2-9 (가이드 요지) | ASVS 5.0 (원문 번호) |
|---|---|---|
| 최소 길이 | 자릿수 조건 검증 (수치는 이 문서에서 확인 못 함) | 6.2.1 (L1): 8자 이상, 15자 이상을 강하게 권장 |
| 최대 길이 | 이 문서에서 확인한 가이드 요지에 없음 | 6.2.9 (L2): 64자 이상 비밀번호를 허용 |
| 조합 규칙 | 숫자, 영문자, 특수문자 혼합 검증 | 6.2.5 (L1): 어떤 조합도 허용하고 대소문자, 숫자, 특수문자의 최소 개수 요구가 없어야 함 |
| 주기 변경 | 주기적 변경 유도 | 6.2.10 (L2): 주기적 자격증명 변경을 요구하지 않아야 함 |
| 흔한 비밀번호 | 이 문서에서 확인한 가이드 요지에 없음 | 6.2.4 (L1): 상위 3000개 이상 비밀번호 대조 |
| 유출 비밀번호 | 이 문서에서 확인한 가이드 요지에 없음 | 6.2.12 (L2): 유출 비밀번호 집합 대조 |
| 문맥 단어 | 이 문서에서 확인한 가이드 요지에 없음 | 6.2.11 (L2): 문서화한 문맥 단어 목록으로 추측하기 쉬운 비밀번호를 막음 |
OWASP Authentication Cheat Sheet 도 같은 방향이다: MFA 가 없으면 15자 미만, 있으면 8자 미만을 약하다고 보고, 최대는 64자 이상, 조합 규칙 없음, 임의 주기 변경 요구 금지, 흔한 및 유출 비밀번호 차단 `[요약 확인]`. bcrypt 의 72바이트 제한 (SEC-03) 과 64자 허용을 같이 만족시키려면 입력 길이 처리를 설계에 적는다.

결정 규칙 (사용자 정책)
1. 발주 요건 또는 점검 기준이 KISA 이면 KISA 2-9 를 따른다
2. 그렇지 않으면 ASVS 5.0 V6 을 따른다
3. 어느 쪽을 골랐는지, KISA 와 ASVS 중 따르지 않은 항목은 보고서에 선택 및 예외로 기록한다. 예: KISA 점검을 받으면서 ASVS 6.2.5 (조합 규칙 금지) 를 따르지 않음 + 사유

### 인증번호 (OTP) 및 재설정
ASVS 5.0 V6 에 수치가 있다. 프로젝트가 고른 값은 `templates/security-architecture.md` 5절에 적는다.
| 항목 | 수치 | 번호 |
|---|---|---|
| 대역 외 요청 (SMS, 이메일 등으로 보낸 코드) 유효 시간 | 최대 10분 | 6.5.5 (L2) |
| TOTP 최대 유효 시간 | 30초 | 6.5.5 (L2) |
| 코드 최소 엔트로피 | 20비트 (무작위 영숫자 4자 또는 무작위 숫자 6자면 충분하다고 문서가 설명) | 6.5.4 (L2) |
| 1회 사용 | 조회용 비밀, 대역 외 코드, TOTP 는 한 번만 성공적으로 사용 가능 | 6.5.1 (L2) |
| 난수 | CSPRNG 로 생성 | 6.5.3 (L2) |
| 무차별 대입 방어 | 코드 기반 대역 외 수단에 속도 제한. 64비트 이상 엔트로피 코드를 검토하라고 문서가 제안 | 6.6.3 (L2) |
- OWASP MFA: 6자리는 약 100만 가지, 사용성이 허용하면 8자리 이상. OWASP Forgot Password: 재설정 PIN 은 6 ~ 12자리, 보조 채널 `[요약 확인]`
- 암호학적 난수로 만들고 1회용으로 한다. 검증에 성공하면 무효화하고, 재전송하면 새 값을 만들어 이전 값을 덮어쓴다
- 시도 횟수 상한의 수치는 ASVS 에 없다. 프로젝트가 정해 5절에 적는다 (SEC-02 기본값 예시 참조)
- 값은 로그에 남기지 않고 장기 평문 저장을 하지 않는다. 키 공간이 작아서 해시를 해도 무차별 대입은 빠르다
- 재설정 요청은 계정 존재 여부와 상관없이 같은 메시지와 일관된 응답 시간을 쓴다. 계정별 속도 제한 또는 CAPTCHA 를 둔다. 재설정 공격을 이유로 계정을 잠그지 않는다
- SMS 와 음성 코드는 NIST SP 800-63B 의 restricted 인증수단이라 개인정보 또는 금융 위험이 있는 앱의 보호에 쓰지 않는다. SMS 가 유일한 수단이면 계정별 속도 제한을 두고 문자 비용 고갈 공격에 대비한다
- TOTP: OWASP MFA 문서는 시간 단계 기본 30초 (RFC 6238), 현재와 직전 단계 하나까지 허용, 받아들인 코드 재사용 거부, 시드 암호화 저장 및 등록 후 클라이언트에 돌려주지 않기를 든다. 직전 단계까지 허용하면 코드 유효 시간이 30초를 넘으므로 ASVS 6.5.5 와 맞는지 보고서에 기록한다
- 증거: 틀린 코드 연속 제출, 만료 후 제출, 사용한 코드 재제출, 재전송 후 이전 코드 제출
- 출처: https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/en/0x15-V6-Authentication.md , https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html , https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html , https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html

## SEC-07 권한 관리 [요약 확인, 2026-11-25]
- 기본 거부. 명시적으로 허용하지 않으면 거부한다. 프레임워크 기본값에 기대지 않고 명시 설정한다
- 모든 요청에서 검사한다. 일부 경로에만 걸지 않고 전역으로 적용한다. 정적 파일과 클라우드 저장소도 정책에 포함한다
- 검사는 서버, 게이트웨이, 서버리스 함수에서 한다. 클라이언트 측 검사에 의존하지 않는다 (화면에서 메뉴를 숨겨도 주소를 직접 치면 열린다)
- 최소 권한. 사용자 유형, 자원, 작업을 설계 때 정리하고 권한이 불어나는지 주기적으로 점검한다
- 객체 접근 (IDOR): 접근 시도마다 그 객체에 대한 권한을 확인한다. 조회 범위를 현재 사용자로 한정한다 (`Project.find(params[:id])` 대신 `@current_user.projects.find(params[:id])`, Spring 은 `findByIdAndOwnerId(id, currentUser().getId())`)
- 존재 여부 자체가 민감하면 없음과 권한 없음을 같은 응답 (404) 으로 처리한다
- 난수 ID 와 UUID 는 심층 방어이며 접근 통제를 대체하지 않는다. 식별자 암호화는 안전하게 하기 어려워 피한다
- 입구 계층 한 곳의 검사만 믿지 않는다. 입구 계층은 기본 거부로 두되 데이터 접근 함수와 각 서버 동작의 첫 줄에서 다시 인가한다 (`architecture.md` 원칙 2)
- 시험: 사용자 A 로 로그인한 채 B 의 객체에 읽기, 생성, 수정, 삭제, 내보내기, 관리 작업을 시도한다
- KISA 구현 1-15 p200, 2-1 p212, 2-2 p215, 설계 2.4 p101: 쿠키, 환경변수, 파라미터 (히든필드 포함) 로 보안 결정을 하지 않고 상태와 세션 정보는 서버에 저장하며 보안 확인도 서버에서 한다. 클라이언트 검사를 우회해도 서버에 접근하지 못하게 설계한다. 중요한 정보 페이지는 재인증을 적용한다. 모든 실행경로에 접근제어를 검사한다
- 관리자 영역 (KISA 부록 관리자 페이지 예시 p368 및 사례): 관리자 전용 페이지는 역할과 접근권한 기반으로만 접근, URL 을 추측하기 어렵게, 원격 연결은 암호화 채널. 사례에서 개인정보위가 지적한 것: 관리자 페이지가 외부 접속 가능 (비와이엔블랙야크), 추가 인증수단과 접속 IP 제한 없음 (네오팜)
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html , https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html

## SEC-08 XSS [요약 확인, 2026-11-25]
- 프레임워크 기본 출력 인코딩을 쓰고, 화면에 들어가는 비신뢰 데이터는 모든 위치에서 인코딩한다. 입력 검증은 출력 인코딩을 대체하지 않는다
- HTML 본문은 엔티티 인코딩한다. JS 로 표시할 때는 `textContent` 에 대입한다
- 속성 값은 항상 따옴표로 감싼다. 이벤트 핸들러 속성에 비신뢰 값을 넣지 않고 `addEventListener()` 를 쓴다
- `script`, `style` 안, HTML 주석, `eval()`, `setTimeout()` 에 비신뢰 데이터를 넣지 않는다
- URL 은 `href` 와 `src` 에 http 와 https 만 허용한다 (`javascript:` 금지)
- 사용자가 HTML 을 써야 하면 유지보수되는 sanitizer (DOMPurify 등) 를 쓴다
- CSP 는 방어 심화이며 주 방어가 아니다. WAF 나 필터로 인코딩을 대체하지 않는다
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html

### 인코딩 우회 API
프레임워크 기본 인코딩을 끄는 API 는 한 곳이라도 쓰면 그 위치는 보호받지 못한다.
| 스택 | 우회 API | 근거 |
|---|---|---|
| React | `dangerouslySetInnerHTML` | React 문서: 신뢰하는 소스가 아니면 XSS 가 된다. 신뢰하고 정제한 데이터에만 쓴다 `[요약 확인]` |
| Vue | `v-html`, `innerHTML` 바인딩, 사용자 입력을 컴포넌트 템플릿으로 사용 | Vue 문서: 안전하다고 아는 HTML 에만 쓴다 `[요약 확인]` |
| Angular | `DomSanitizer.bypassSecurityTrustHtml` 등 `bypassSecurityTrust*` | Angular 문서: 악의적일 수 있는 값을 신뢰하면 취약점이 생긴다 `[요약 확인]` |
| Jinja2 | `\|safe` 필터, `markupsafe.Markup` | Jinja 문서: 자동 이스케이프가 켜져 있어도 이 표시를 붙이면 이스케이프되지 않는다 `[요약 확인]`. 자동 이스케이프 기본값은 환경 설정에 따름 |
| Thymeleaf | `th:utext` (기본은 이스케이프되는 `th:text`) | Thymeleaf 문서 `[요약 확인]` |
| EJS | `<%- ... %>` (이스케이프 없는 출력. `<%= ... %>` 는 이스케이프) | 이 문서에서 EJS 문서로 확인하지 못함 `[일반]` |
| 브라우저 DOM | `innerHTML =`, `outerHTML =`, `insertAdjacentHTML`, `document.write` | `[일반]` |
- 검색 `[미실행]`: `rg -n 'dangerouslySetInnerHTML|v-html|bypassSecurityTrust|th:utext|<%-|innerHTML\s*=|\|safe|Markup\('`
- 결과 한 건마다 값의 출처와 sanitizer 적용 여부 (사용 라이브러리, 허용 태그 설정) 를 기록한다. sanitizer 없이 사용자 입력이 들어가면 FAIL

### 업로드한 HTML 및 SVG
- 사용자가 올린 HTML 또는 SVG 를 앱과 같은 출처 (같은 도메인) 에서 `text/html`, `image/svg+xml` 로 열면 그 안의 스크립트가 앱의 세션과 같은 권한으로 실행된다 `[일반]`
- 대응: 업로드 파일은 앱과 다른 호스트에서 내려 주거나 (SEC-04 원문: 다른 호스트가 가장 좋다), `Content-Disposition: attachment` 와 `X-Content-Type-Options: nosniff` 로 내려 준다. SVG 는 허용 목록에서 빼거나 정제한다 (SEC-04, SEC-14 헤더 표)
- 시험: 스크립트를 담은 `.svg`, `.html` 을 올리고 파일 주소를 직접 열어 실행되는지 본다

## SEC-09 CSRF [요약 확인, 2026-11-25]
쿠키로 인증하는 상태 변경 요청에 적용한다. 헤더로 토큰을 보내는 API 는 쿠키가 자동 전송되지 않으므로 해당이 줄어든다 `[일반]`.
- 순서: 프레임워크 내장 보호를 확인해 쓰고, 없으면 상태 변경 요청에 CSRF 토큰을 붙이고, 방어 심화를 하나 이상 더한다 (OWASP)
- 동기화 토큰: 서버가 세션별로 만든 예측할 수 없는 비밀 값. 숨은 폼 필드 또는 사용자 지정 헤더로 보내고 쿠키, URL, 로그에 싣지 않는다. 없거나 세션 값과 다르면 거부한다. 상태를 가진 서버에 쓴다
- 상태가 없는 서버는 서명한 double submit 쿠키를 쓰되 세션 정보에 묶는다. 단순 double submit 은 쿠키 주입 공격에 취약해 OWASP 가 권하지 않는다. 값 검증은 쿠키가 아니라 헤더 또는 폼 값으로 한다
- `Sec-Fetch-Site` 검사: OWASP 가 CSRF 보호의 1차 신호로 든다. 값은 `same-origin`, `same-site`, `cross-site`, `none`. `same-origin` 허용, `same-site` 는 형제 하위 도메인을 신뢰할 때만 허용, `cross-site` 의 안전하지 않은 메서드는 거부. 이 헤더를 보내지 않는 클라이언트를 위한 대체 검사가 필수다
- `Origin` 검사: 있으면 대상 출처와 전체가 일치하는지 본다 (`example.org.attacker.com` 은 실패해야 함). 없으면 `Referer` 의 호스트를 본다. 헤더가 없는 것과 `Origin: null` 은 같은 출처라는 증거가 아니다
- 사용자 지정 헤더 (`X-CSRF-Token` 등): AJAX 및 API 에 쓴다. CORS 사전 요청 (preflight) 에 의존한다

```js
// Sec-Fetch-Site 검사 (OWASP 정책을 Express 로 옮긴 예. 동작은 [미실행])
const SAFE = new Set(['GET', 'HEAD', 'OPTIONS']);
const TRUST_SAME_SITE = false; // 형제 하위 도메인을 신뢰할 때만 true
app.use((req, res, next) => {
  const site = req.get('Sec-Fetch-Site');
  if (site === 'cross-site' && !SAFE.has(req.method)) return res.sendStatus(403);
  if (site === 'same-site' && !TRUST_SAME_SITE && !SAFE.has(req.method)) return res.sendStatus(403);
  if (!site && !SAFE.has(req.method) && req.get('Origin') !== BASE_ORIGIN) return res.sendStatus(403); // 대체 검사
  next();
});
```
- SameSite 쿠키가 막지 못하는 경우: `SameSite=Lax` 는 안전하지 않은 메서드의 교차 사이트 요청만 막는다
  - GET 요청으로 상태가 바뀌는 기능이 하나라도 있으면 `Lax` 는 그것을 막지 못한다. 상태 변경은 GET 으로 만들지 않는다
  - same-site 는 등록 가능한 도메인 기준이다. `app.example.com` 이 설정한 쿠키는 `anything.example.com` 에서 온 요청에도 같은 사이트로 취급된다. 형제 하위 도메인에 신뢰할 수 없는 콘텐츠가 있으면 `SameSite` 만으로 막지 못한다
  - OWASP 는 SameSite 를 방어 심화로 두고 대부분의 배포에서 토큰 또는 double submit 과 함께 쓰라고 한다
- 시험: 다른 출처의 폼과 `fetch` 로 상태 변경 요청 보내기, 토큰 없는 요청, 다른 세션의 토큰, `Origin: null`, GET 으로 상태가 바뀌는 경로 찾기
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html

## SEC-10 세션과 쿠키 [요약 확인, 2026-11-25]
| 항목 | 기준 | 근거 |
|---|---|---|
| 세션 ID 엔트로피 | OWASP: 최소 64비트, 직접 만드는 ID 는 128비트 이상, 저장 토큰은 128비트 이상 160비트 이상 권장. ASVS 7.2.3 (L1): CSPRNG 로 128비트 이상. 따를 값: 128비트 이상 | OWASP Session Management, ASVS 7.2.3 |
| 유휴 만료 | OWASP: 고가치 앱 2 ~ 5분, 저위험 앱 15 ~ 30분. ASVS 7.3.1 (L2) 는 유휴 만료 후 재인증을 요구하고 시간 수치는 정하지 않는다 | 서버에서 강제 |
| 절대 만료 | OWASP: 하루 근무하는 사무 사용자 4 ~ 8시간. ASVS 7.3.2 (L2) 는 절대 최대 수명 후 재인증을 요구하고 수치는 정하지 않는다 | 서버에서 강제 |
| 재발급 | 로그인, 비밀번호 변경, 권한 변경, 관리자 역할 전환 뒤 세션 ID 를 새로 발급. ASVS 7.2.4 (L1): 재인증 포함 인증 때 새 토큰을 만들고 이전 토큰을 종료 | OWASP, ASVS |
| 고위험 재인증 | 비밀번호 및 이메일 변경, 낯선 기기 또는 IP, 계정 복구 뒤 재인증 | OWASP |
| 로그아웃 | 서버에서 세션 무효화 (클라이언트 쿠키 삭제만으로는 부족). 같은 세션에 묶인 회전 전 ID 도 폐기. ASVS 7.4.1 (L1) | OWASP, ASVS |
- 만료 수치는 위험도에 따라 정하고 `security-architecture.md` 5절 또는 설계 문서에 적는다. 위 범위는 OWASP 가 제시한 값이며 프로젝트 값이 아니다
- 쿠키 속성 (OWASP)
  - `Secure`, `HttpOnly` 필수
  - `SameSite=Strict` 권장, 또는 `Lax` 를 명시. 브라우저 기본값에 기대지 않는다. `Secure` 없이 `None` 금지. CSRF 토큰을 대체하지 않는다
  - `Domain` 은 설정하지 않는다 (설정하면 하위 도메인에 노출). `Path` 는 가능한 한 좁게
  - `Expires` 또는 `Max-Age` 가 있으면 디스크에 남는 영속 쿠키가 된다. 인증을 유지할 필요가 없으면 쓰지 않는다
  - 쿠키 이름은 `PHPSESSID`, `JSESSIONID` 같은 프레임워크 기본값을 피한다
  - `__Host-` 접두: `Secure` 필수, `Domain` 속성 없음, `Path=/`. 세션 ID 에 권장. `__Secure-` 는 하위 도메인 공유가 필요할 때만

```http
Set-Cookie: __Host-sid=<값>; Secure; HttpOnly; SameSite=Lax; Path=/
```
(OWASP 문서의 예는 `SameSite=Strict`. `Lax` 는 외부 링크로 들어온 첫 이동에도 쿠키를 보내는 선택이며 SEC-09 의 한계가 따른다)
- 로그인 시 재발급 (스택별)
  - Node (express-session): `req.session.regenerate(cb)` 를 부르면 새 SID 와 새 `Session` 이 생긴다. 사용자 정보는 콜백 안에서 넣는다 `[요약 확인]`
  ```js
  req.session.regenerate((err) => {
    if (err) return next(err);
    req.session.userId = user.id;
    res.redirect('/');
  });
  ```
  - Django: `login()` 은 사용자 ID 를 세션에 저장한다. 익명 세션에서 로그인할 때 `cycle_key()` 로 키를 바꾼다는 설명은 공식 페이지가 아니라 Django 소스 기준이므로 사용 버전에서 확인한다 `[일반]`
  - Spring Security: 로그인 때 새 세션을 만들거나 세션 ID 를 바꾸는 세션 고정 방어가 자동이다. 전략은 `changeSessionId` (Servlet 3.1 이상 기본), `newSession`, `migrateSession`. `none` 으로 끄면 취약하다 `[요약 확인]`
- 세션 고정 확인: 로그인 전후 쿠키 값이 달라야 한다
- JWT 를 세션으로 쓸 때 `[일반]`: 액세스 토큰 만료를 짧게, refresh 토큰은 사용할 때마다 새 값으로 바꾸고 이전 값을 폐기 (회전), 로그아웃 및 탈취 대응용 폐기 목록을 서버에 둔다. 만료 수치는 사용자 정책값이다. 서명 알고리즘과 `iss`, `aud`, `exp` 검증은 SEC-13. ASVS V9 (자체 포함 토큰) 의 항목 번호는 이 문서에서 확인하지 않았다
- KISA 구현 2-12 p260, 설계 4.1 p131: 영속적 쿠키에 세션 ID 와 권한 등급 같은 중요정보를 넣지 않고 쿠키 만료시간은 세션 지속시간을 고려해 최소로 한다. 설계: 로그아웃 인터페이스, 세션 ID 비노출, 중복 로그인 불허 시 세션 종료 정책. 사례: 최대접속시간 제한 및 자동 로그아웃을 법원이 통상 요구되는 보호조치로 본 판결 (네이트 및 인터파크)
- 시험: 로그아웃 후 이전 토큰으로 요청, 로그인 전후 세션 ID 비교, 유휴 및 절대 만료 후 요청, 쿠키 속성 확인
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html , https://github.com/OWASP/ASVS/blob/v5.0.0/5.0/en/0x16-V7-Session-Management.md , https://expressjs.com/en/resources/middleware/session.html , https://docs.spring.io/spring-security/reference/servlet/authentication/session-management.html

## SEC-11 전송 보안
상세 없음: SKILL.md 표 참조. HSTS 헤더 값은 SEC-14 의 헤더 표.

## SEC-12 비밀정보 [요약 확인, 2026-11-25]
- 코드와 로그에서 노출된 비밀은 폐기, 회전, 삭제한다. IDE 또는 pre-commit 훅 단계에서 비밀 탐지를 돌린다
- 정기 회전, 가능하면 자동화. 쓰지 않는 비밀은 폐기한다. 앱 재시작은 탈취된 자격증명을 폐기하지 않는다
- 비밀마다 읽기와 쓰기 권한을 제한하고 애플리케이션과 환경별로 보관소를 분리한다
- Docker 이미지에 `ENV` 나 `ARG` 로 비밀을 넣지 않는다. 배포 시점에 주입하거나 파일로 마운트한다
- 환경변수는 모든 프로세스가 읽을 수 있어서 다른 방법이 불가능할 때가 아니면 권하지 않는다고 원문이 적었다
- 비밀을 로그에 평문으로 남기지 않는다. 암호화 키를 암호화 대상 데이터 옆에 두지 않는다
- 비밀번호, 토큰, API 키를 URL 에 넣지 않는다 (서버 로그에 남음). 본문이나 헤더에 둔다 (REST Security 원문)
- DB 자격증명은 소스에 넣지 않고 웹 루트 밖 설정 파일에 둔다 (Database Security 원문)
- [일반] 원문에 직접 없음, 도입 전 확인: `.env` 를 `.gitignore` 에 둔다. 브라우저로 내려가는 번들, 소스맵, 공개 환경변수 접두어 (`NEXT_PUBLIC_`, `VITE_` 등) 에 비밀을 넣지 않는다. 외부 API 키는 서버에서만 쓰고 클라이언트는 서버를 거쳐 호출한다
- KISA 2-6, 2-13: 소스에 하드코드된 비밀번호와 키 금지, 주석에 ID 와 비밀번호 금지. 사례: 퇴사한 개발자가 재직 중 관리하던 서명키를 계속 쓸 수 있었다 (쿠팡). 키와 계정은 사람이 떠나거나 역할이 바뀔 때 갱신한다
- 시험: `git ls-files` 와 `git log -p` 에서 `.env` 및 키 문자열 검색, 빌드 결과물과 네트워크 탭에서 키 검색
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html , https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html

## SEC-13 API 입력 처리 [요약 확인, 2026-11-25]
### 요청 처리
- 입력은 길이, 범위, 형식, 타입을 검증한다. 요청 크기 제한을 두고 초과하면 `413`, 너무 빠르면 `429` 를 반환한다
- 오류는 일반 메시지로 응답하고 스택 등 기술 정보를 클라이언트에 주지 않는다
- JWT: `alg: none` 을 받지 않고 검증 알고리즘을 JWT 헤더에서 고르지 않는다. `iss`, `aud`, `exp` 를 검증한다
- CORS 및 관리 엔드포인트 노출은 SEC-14
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html

### SSRF (KISA 1-12, p191)
서버가 사용자 입력으로 받은 주소로 요청을 보내는 기능 (URL 미리보기, 웹훅, 파일 가져오기) 에 적용한다.
- 대상이 미리 정해져 있으면 허용 목록 (스킴, 호스트, 포트) 으로 제한한다. 대상이 임의여야 하면 차단 목록을 쓰는데 우회하기 쉬우므로 마지막 수단이다 (OWASP)
- 도메인 허용 목록만으로는 DNS 리바인딩을 막지 못한다. 호스트를 DNS 로 해석한 뒤 결과 IP 를 허용 대역과 비교하고, 비교한 그 IP 로 연결한다. 원래 호스트명은 Host 헤더, SNI, 인증서 검증에 유지한다. 재시도와 대체 연결에도 같은 정책을 적용한다
- 리다이렉트는 따라가지 않는다 (HTTP 클라이언트의 자동 추종을 끈다). 따라가야 하면 매번 다시 검사한다
- 비교 전에 IPv4 로 매핑된 IPv6 주소는 원래 IPv4 형태로 바꿔서 검사한다
- 차단 대역 (OWASP 가 최소로 든 목록)
  | 구분 | 대역 |
  |---|---|
  | 루프백, 0 번 대역 | `127.0.0.0/8`, `0.0.0.0/8`, `::1/128` |
  | 사설 (RFC1918) | `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` |
  | 링크 로컬 | `169.254.0.0/16`, `fe80::/10` |
  | IPv6 고유 로컬 | `fc00::/7` |
  | 클라우드 메타데이터 | `169.254.169.254`, AWS 의 `fd00:ec2::254`, GCP 의 `metadata.google.internal` |
  | 멀티캐스트 | `224.0.0.0/4`, `ff00::/8` |
  | IPv4 매핑 및 NAT64 | `::ffff:0:0/96`, `64:ff9b::/96`, `64:ff9b:1::/48` |
- AWS: IMDSv2 는 SSRF 의 일부 사례를 줄이는 방어 심화 수단이며 IMDSv1 을 끄라고 OWASP 가 권한다. 기존 인스턴스에서 IMDSv2 를 필수로 하는 명령은 AWS 문서 기준 `aws ec2 modify-instance-metadata-options --instance-id <ID> --http-tokens required --http-endpoint enabled` (실행 전에 `MetadataNoToken` 지표로 IMDSv1 사용이 없는지 확인). 인스턴스 속성 이름은 `HttpTokens=required` 이다. 실행은 `[미실행]`

```python
# DNS 해석 후 IP 검사 (동작은 [일반], 대역 목록은 위 OWASP 표)
import ipaddress, socket
from urllib.parse import urlsplit

ALLOWED_HOSTS = {"api.partner.example"}

def checked_ips(url):
    p = urlsplit(url)
    if p.scheme != "https" or p.hostname not in ALLOWED_HOSTS:
        raise ValueError("대상 불허")
    ips = {ipaddress.ip_address(a[4][0]) for a in
           socket.getaddrinfo(p.hostname, p.port or 443, type=socket.SOCK_STREAM)}
    for ip in ips:
        ip = getattr(ip, "ipv4_mapped", None) or ip
        if ip.version == 6 and ip in ipaddress.ip_network("64:ff9b::/96"):
            ip = ipaddress.IPv4Address(int(ip) & 0xFFFFFFFF)
        if not ip.is_global or ip.is_multicast:
            raise ValueError("비공개 대역")
    return ips   # 호출한 쪽이 이 IP 로 연결하고 리다이렉트는 따라가지 않는다
```
- 시험: `http://127.0.0.1`, `http://169.254.169.254/`, 허용 호스트가 내부 IP 로 해석되도록 만든 도메인, 내부 주소로 302 를 돌려주는 외부 서버를 대상으로 넣어 본다
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html , https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-existing-instances.html

### 신뢰할 수 없는 데이터의 역직렬화 (KISA 5-5, p311)
- 데이터 스트림이 역직렬화할 객체 유형을 정하게 하지 않는다. 언어 고유의 직렬화 형식은 피하고 JSON 같은 표준 형식을 쓴다. 서명한 데이터는 서명을 검증한 뒤에만 역직렬화한다 (OWASP Deserialization)
- 필터링은 신뢰할 수 없는 데이터의 역직렬화를 안전하게 만들지 않는다고 OWASP 가 적었다. 구조적으로 피하는 것이 우선이다
| 스택 | 규칙 | 근거 |
|---|---|---|
| Java | 직렬화 필터로 허용 클래스 목록과 `!*` (나머지 거부) 를 건다. 예: `-Djdk.serialFilter="com.example.dto.*;java.base/*;!*"` 또는 `ObjectInputFilter.Config.createFilter(...)` 후 `setSerialFilter`. 필터가 결정하지 않은 클래스를 거부하도록 설정할 수 있다 (`rejectUndecidedClass`) | Oracle `ObjectInputFilter` API 문서의 예 (`example.*;java.base/*;!*`) `[요약 확인]`. 패턴 문법의 세부, `maxdepth` 같은 자원 제한은 확인하지 못함 `[미실행]` |
| Python | 신뢰할 수 없는 데이터에 `pickle.load`, `pickle.loads` 금지. YAML 은 `yaml.safe_load()` 만 쓰고 `yaml.load()`, `yaml.unsafe_load()`, `Loader=yaml.Loader` 금지 | OWASP Deserialization `[요약 확인]` |
| Jackson (Java) | OWASP: jackson-databind 는 다형성을 쓰지 않으면 안전하게 쓸 수 있다. 기본 타입 지정 (default typing, `enableDefaultTyping`, `activateDefaultTyping`) 과 입력에 따른 `@JsonTypeInfo` 를 쓰지 않는다 | 다형성 부분은 OWASP `[요약 확인]`, 기본 타입 지정 메서드 이름은 `[일반]` |
- 검색 `[미실행]`: `rg -n 'ObjectInputStream|readObject\(|pickle\.loads?\(|Unpickler|yaml\.(unsafe_)?load(_all)?\(|jsonpickle\.decode|enableDefaultTyping|activateDefaultTyping|@JsonTypeInfo'`. 결과마다 입력이 신뢰 경계 안인지 기록
- 시험: 신뢰할 수 없는 경로가 받는 직렬화 객체에 허용 목록에 없는 클래스를 넣어 거부되는지 본다
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html , https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/ObjectInputFilter.html

## SEC-14 보안 설정 [요약 확인, 2026-11-25]
### 보안 헤더
| 헤더 | 값 | 비고 |
|---|---|---|
| `Content-Security-Policy` | 최소 `frame-ancestors 'none'; object-src 'none'` | 값은 OWASP CSP 문서의 예 (`frame-ancestors 'none'`, 엄격 정책의 `object-src 'none'`). `frame-ancestors` 는 `<meta>` 에서 무시되고 `default-src` 로 대체되지 않으므로 응답 헤더로 보낸다. 스크립트 통제를 포함한 본 정책은 앱에 맞춰 따로 만든다 |
| `Strict-Transport-Security` | 최소 `max-age=31536000` | OWASP HTTP Headers 의 권장 값은 `max-age=63072000; includeSubDomains; preload`. 31536000 (1년) 은 이 스킬의 최소 예시 `[일반]`. `preload` 는 등록 요건을 확인한 뒤 쓴다. 긴 max-age 는 인증서 문제 때 사용자를 막을 수 있다 |
| `X-Content-Type-Options` | `nosniff` | `Content-Type` 도 정확히 지정한다 |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | 기본값에 기대지 않고 명시 |
| `X-Frame-Options` | `DENY` | CSP `frame-ancestors` 를 우선 쓰고 구형 브라우저용으로 병행 |
| `Permissions-Policy` | 예: `geolocation=(), camera=(), microphone=()` | 쓰지 않는 기능을 끈다 |
| `Cache-Control` | 민감한 응답은 `no-store` | 공유 캐시 저장 방지 |
- 검사 `[미실행]`: `curl -sI "$BASE"` 로 응답 헤더에 위 값이 있는지 본다. 로그인 후 화면과 API 응답도 따로 확인한다

### CORS
- 교차 도메인 호출이 없으면 끄고, 허용 출처를 구체적으로 한다. `*` 를 쓰지 않는다
- `Origin` 요청 헤더 값을 그대로 `Access-Control-Allow-Origin` 에 돌려주는 반사와 `Access-Control-Allow-Credentials: true` 의 조합을 금지한다. 인증 정보를 허용하려면 정확히 일치하는 신뢰 출처 허용 목록에서 고른 값만 쓴다 (OWASP)
- `null` 출처를 허용하지 않는다 (OWASP: Never allow the `null` origin)
- 허용 출처가 요청의 `Origin` 에 따라 달라지면 `Vary: Origin` 을 보낸다
- 시험: `curl -sI -H 'Origin: https://evil.example' "$BASE/api/me"`, `-H 'Origin: null'` 로 보내 `Access-Control-Allow-Origin` 에 그 값이 돌아오지 않는지 확인 `[미실행]`

### 스택 설정 점검
| 스택 | 점검 | 근거 |
|---|---|---|
| Spring Boot | `management.endpoints.web.exposure.include` 를 필요한 엔드포인트로만 한정한다. 기본은 `health` 만 노출. `*` 로 전체를 열지 않는다. 노출하는 엔드포인트는 방화벽 또는 Spring Security 로 보호 | Spring Boot Actuator 문서 |
| Django | 운영에서 `DEBUG = False`. 켜 두면 소스 발췌, 지역 변수, 설정이 유출된다. 배포 전 `manage.py check --deploy` 를 운영 설정으로 실행 | Django 배포 점검표 |
| Node (Express) | `NODE_ENV=production`. Express 가 덜 상세한 오류 메시지를 만든다. 서버에는 셸이 아니라 init 시스템에서 설정 | Express 문서 |
- 디버그 코드, 테스트 계정은 배포 전에 제거한다. 오류 시 내부 정보를 노출하지 않는다 (KISA 4-1 ~ 4-3, 6-2, p287 ~ p321): 오류 메시지에는 사용자에게 필요한 최소 정보만 담고 예외는 내부에서 처리해 미리 정한 메시지를 준다. 빈 `catch` 로 오류를 넘기지 않고 (가이드 예제에 빈 catch 로 인증을 통과시키는 사례), 광범위한 예외 대신 구체적 예외를 처리한다. 인증과 권한 검사 중 오류가 나면 거부한다 (이 문장은 `[일반]`). 배포 전에 디버그 코드와 콘솔 및 콜스택 출력을 제거한다
- 관리 엔드포인트는 인터넷에 노출하지 않는다 (REST Security)
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html , https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html , https://docs.spring.io/spring-boot/reference/actuator/endpoints.html , https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/ , https://expressjs.com/en/advanced/best-practice-performance.html

## SEC-15 로그
상세 없음: SKILL.md 표 참조.
- 사례: 이상행위 로그를 점검하고 탐지한다 (SK텔레콤, 쿠팡). 로그에 주민등록번호 같은 개인정보를 평문으로 남기지 않는다 (롯데카드)

## SEC-16 공급망과 빌드
사례는 `incidents.md` 4절 (tj-actions/changed-files, Shai-Hulud, Codecov). 아래는 그 유형을 막는 설정이다.
| 항목 | 규칙 | 근거 |
|---|---|---|
| 액션 고정 | 서드파티 액션은 전체 커밋 SHA 로 고정한다: `uses: owner/action@<40자 SHA>`. SHA 가 포크가 아니라 그 액션의 저장소 것인지 확인 | GitHub Actions 보안 강화 문서 `[요약 확인]` |
| 토큰 권한 | 워크플로 최상단에 `permissions:` 를 두고 `contents: read` 로 시작하며 필요한 작업에서만 올린다. `permissions` 에 하나라도 지정하면 지정하지 않은 권한은 `none` 이다 | GitHub 문서 `[요약 확인]`. 기본 토큰 권한을 저장소 읽기로 제한하라는 권고도 같은 문서 |
| npm 설치 | CI 는 `npm ci --ignore-scripts`. lockfile 과 다르면 설치가 중단된다. 설치 스크립트가 필요한 패키지만 별도로 실행 (예: `npm rebuild <패키지>` `[일반]`). `--ignore-scripts` 는 설치 때 스크립트를 미룰 뿐이며 `npm run`, `npm start`, `npm test` 는 스크립트를 실행한다 | OWASP NPM Security `[요약 확인]` |
| Python 설치 | `pip install --require-hashes -r requirements.txt`. 요구사항을 `==` 로 고정하고 `--hash=sha256:...` 를 붙인다. 하나라도 `--hash` 가 있으면 전체에 해시 확인이 켜진다 | pip 문서 `[요약 확인]` |
| SBOM | npm: `npm sbom --sbom-format cyclonedx` (`spdx` 도 가능). 출력을 파일로 저장해 릴리스 산출물로 보관 | npm 문서 `[요약 확인]`. 다른 스택의 SBOM 도구는 확인하지 못함 `[미실행]` |
| 무결성 | lockfile 을 저장소에 두고 내려받은 패키지의 해시를 검증한다 | OWASP CI/CD Security `[요약 확인]` |
- 검사 `[미실행]`
  - `rg -n 'uses: [^@]+@(v[0-9]|main|master)' .github/workflows` 결과 0건
  - 더 넓게: `rg -n 'uses: [^@]+@' .github/workflows | rg -v '@[0-9a-f]{40}'` 결과 0건 (로컬 액션과 `docker://` 는 `@` 가 없어 걸리지 않음)
  - `rg -n '^permissions:' .github/workflows` 로 모든 워크플로 파일에 최상단 `permissions` 가 있는지 확인
- 원격에서 내려받은 코드나 실행파일은 무결성 검사 없이 실행하지 않고 최소 권한으로 실행한다 (KISA 2-15, p270)

## SEC-17 배포와 인프라 중 DB 접근 [요약 확인, 2026-11-25]
- DB 는 애플리케이션 서버와 격리된 내부 네트워크에 둔다. 포트는 특정 호스트에만 연다. TCP 접근을 끄거나 최소한 localhost 에만 바인딩한다
- 원문: 클라이언트 (thick client) 에서 백엔드 DB 로 직접 연결을 만들지 않는다. 신뢰할 수 없는 클라이언트는 접근 통제를 강제하는 API 를 거친다
- 계정은 앱 또는 서비스마다 하나. root, sa, SYS 를 쓰지 않는다. 대부분의 앱은 SELECT, UPDATE, DELETE 만 필요하고 계정이 DB 를 소유하지 않는다. 개발, 검수, 운영은 DB 와 계정을 분리한다
- 암호화된 연결만 허용하고 (TLS 1.2 이상) 클라이언트가 서버 인증서를 검증한다
- [일반] BaaS 처럼 클라이언트가 DB 에 직접 쿼리하는 구조는 행 단위 접근 규칙이 서버 역할을 한다. 규칙이 없는 표는 모두 열린 것과 같으므로 해당 서비스의 공식 문서로 확인한다
- KISA 2-3 (p219): 설정파일, 실행파일, 라이브러리는 관리자만 읽고 쓰게 한다. 사례: BaaS 의 행 수준 규칙 누락 (Lovable, Moltbook, UpGuard), 인터넷망에서 관리망 서버 접근 무제한 (SK텔레콤), 개발과 운영 미분리 (쿠팡). 앞의 `[일반]` BaaS 항목은 이 사례들로 필요성이 확인된 것이며, 설정 방법은 해당 서비스 공식 문서로 확인한다
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html

## SEC-18 시험과 대응 [요약 확인, 2026-11-25]
자동 점검은 스택별 최소 세트를 CI 에 넣고, 실패 조건을 넘으면 빌드를 실패시킨다. 도구가 통과해도 `attack-tests.md` 의 시험을 대신하지 않는다.
| 구분 | 도구 | 명령 | 실패 조건 | 확인 |
|---|---|---|---|---|
| SAST | Semgrep | `semgrep scan --config p/owasp-top-ten --error` | 발견 항목이 있으면 종료 코드 1 (`--error` 가 없으면 발견이 있어도 실패 코드를 돌려주지 않음) | `--config`, `--error` 는 Semgrep CLI 문서 `[요약 확인]`. 레지스트리 이름 `p/owasp-top-ten` 은 문서 페이지에서 확인하지 못함 `[미실행]` (같은 문서가 `p/default` 를 예로 듦) |
| SCA (Node) | npm audit | `npm audit --audit-level=high` | 지정한 수준 (`low`, `moderate`, `high`, `critical`) 이상의 취약점이 있으면 0 이 아닌 종료 코드 | npm 문서 `[요약 확인]` |
| SCA (Python) | pip-audit | `pip-audit -r requirements.txt` | 알려진 취약점이 있으면 종료 코드 1. 종료 코드는 숨길 수 없음 | PyPI 문서 `[요약 확인]` |
| SCA (Maven) | OWASP Dependency-Check | `mvn org.owasp:dependency-check-maven:check -DfailBuildOnCVSS=7` | CVSS 7 이상이 발견되면 빌드 실패. 파라미터 기본값은 11 이라 기본은 실패하지 않음 | 파라미터 설명은 Dependency-Check 문서 `[요약 확인]`. 위 `-D` 명령줄 형식은 `[미실행]` |
| DAST | OWASP ZAP baseline | `docker run -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py -t https://<대상>` | 종료 코드 0 성공, 1 FAIL 규칙 있음, 2 경고만 있음, 3 도구 오류. 1 을 실패로 하고 2 는 팀이 정함 | ZAP 문서 `[요약 확인]`. 실제 공격은 하지 않는 수동 점검이라 공격 시나리오 시험을 대신하지 않음 |
- 실패 수준 (예: high 이상, CVSS 7 이상) 은 사용자 정책값이다. 예외로 넘기는 항목은 보고서에 근거와 기한을 적는다
- 폐쇄망에서는 규칙 및 취약점 DB 를 내부로 들여와야 한다 (SEC-05). 도구별 오프라인 방법은 확인하지 못함 `[미실행]`
- 위협 모델링, 사고 대응, 회귀 시험: 상세 없음. `attack-tests.md` 의 행을 기능이 생길 때마다 더한다
- 출처: https://docs.semgrep.dev/cli-reference , https://docs.npmjs.com/cli/v10/commands/npm-audit , https://pypi.org/project/pip-audit/ , https://dependency-check.github.io/DependencyCheck/dependency-check-maven/configuration.html , https://www.zaproxy.org/docs/docker/baseline-scan/

## SEC-19 비즈니스 로직과 결제 [요약 확인, 2026-11-25]
가격, 수량, 쿠폰, 결제 성공은 클라이언트가 보낸 값을 믿지 않는다. 원문 문장: 클라이언트 상태는 입력이지 진실이 아니다.
- 결제 요청은 상품 ID 와 수량만 받는다. 가격, 합계, 배송비, 할인 필드는 받지 않고 서버가 DB 값으로 계산한다
- 값은 형식뿐 아니라 업무 의미를 검증한다. 수량은 1 이상이고 재고 이하, 날짜 순서 등. 숨김 필드와 파생 필드도 신뢰하지 않는다
- 다단계 흐름은 서버에 상태를 저장하고 전이마다 현재 상태를 검증한다. 숨은 폼 필드나 클라이언트가 읽는 쿠키로 단계를 추적하지 않는다
- 1회성 혜택 (가입 보너스, 쿠폰, 추천 보상) 은 영속 저장소에 사용 완료로 표시하고 `(user_id, bonus_type)` 유니크 제약으로 DB 가 중복을 거부하게 한다
- 확인 후 실행하는 작업은 원자적으로 한다: `SERIALIZABLE` 트랜잭션, `SELECT ... FOR UPDATE`, `UPDATE ... WHERE balance >= amount` 후 영향 행 수 확인
- 외부 작업 재시도에는 멱등성 키를 쓴다. 키는 인증된 호출자 및 작업에 한정하고 원래 매개변수에 묶어, 다른 매개변수로 재사용하면 거부한다
- 혜택을 주는 기능은 작업별, 계정별, 출처별 상한과 속도 제한을 둔다. 지급마다 사용자, 대상 사용자, IP, 시각을 기록한다
- 사용자 입력을 기다리는 흐름 (이메일 인증, KYC) 은 기한을 두고, 넘기면 부분 상태를 무효화해 처음부터 다시 한다
- 결제: 주문 생성 전에 신뢰하는 데이터로 합계를 다시 계산하고, 이행 전에 게이트웨이 API 로 결제 상태를 확인해 금액, 통화, 주문 ID 를 대조한다
- 결제: 콜백은 HMAC 서명 또는 비밀 토큰으로 진위를 검증한다. 서버 간 콜백만 신뢰하고 사용자 리다이렉트 매개변수는 신뢰하지 않는다
- 결제: 이행은 멱등으로 한다. 콜백이 여러 번 와도 주문당 한 번만 처리하고 중복 이벤트를 영속 기록한다
- 결제: 늦게 온 이벤트는 만료됐다고 버리지 말고 서명을 검증한 뒤 현재 결제 상태와 대조한다
- 결제: 로그에 콜백 식별자, 검증 결과, 주문 연결 정보를 남기고 원본 헤더와 본문, 자격증명, 불필요한 개인정보 및 결제정보는 남기지 않는다. 카드 검증 코드와 PIN 은 승인 후 보관하지 않는다
- 증거: 가격 및 수량 변조 요청, 음수 및 0 및 재고 초과 수량, 같은 쿠폰 동시 100건, 위조 콜백, 금액이 다른 콜백, 같은 콜백 2회
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html , https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Payment_Gateway_Integration_Cheat_Sheet.html

## SEC-20 입력 필드 허용 목록 (Mass Assignment) [요약 확인, 2026-11-25]
가입, 프로필 수정처럼 요청 본문을 객체에 그대로 넣는 곳에서 `role`, `isAdmin` 같은 필드가 끼어들 수 있다.
### 쓰기 쪽
- 입력을 도메인 객체에 바로 바인딩하지 않는다. 수정 가능한 필드만 가진 DTO 를 쓴다 (예: `isAdmin` 이 없는 가입 DTO)
- 바인딩할 필드는 허용 목록으로 지정한다. Spring `binder.setAllowedFields(...)`, Node.js 는 `_.pick(req.body, safeFields)`, Laravel 은 `$fillable`
- 차단 목록만으로는 부족하다. 새로 생기거나 놓친 민감 필드가 계속 바인딩된다 (CWE-915 도 허용 목록을 권고)
- DTO 와 허용 목록은 쓰기 가능한 속성만 제한한다. 객체와 작업에 대한 권한 검사 (SEC-07) 를 대체하지 않는다
- 증거: 가입 및 수정 요청에 `role=admin`, `isAdmin=true` 등을 추가해 보내고 저장된 값 확인
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html

### 읽기 쪽 (응답 허용 목록, OWASP API Security Top 10 2023 API3 BOPLA) `[요약 확인]`
응답에 내부 필드 (`passwordHash`, `isAdmin`, 다른 사용자의 이메일 등) 가 실리지 않게 한다.
- 노출하는 객체 속성마다 사용자가 접근해도 되는지 확인한다. `to_json()`, `to_string()` 같은 범용 직렬화 메서드를 피하고 반환할 속성을 골라서 담는다. 응답 구조는 엔드포인트 요구에 맞는 최소로 한다. 추가 방어로 스키마 기반 응답 검증을 둔다 (API3 의 예방 항목)
| 스택 | 응답 허용 목록 방법 | 근거 |
|---|---|---|
| 공통 | 응답 전용 DTO 를 만들고 엔티티 및 모델 객체를 그대로 반환하지 않는다 | API3 |
| Next.js (Drizzle 예) | 조회에서 `columns: { id: true, name: true, email: true }` 로 필요한 열만 명시하고, DTO 함수에서 필드별 노출 여부를 판단한다 | Next.js 인증 가이드 `[요약 확인]` |
| Prisma | `select: { id: true, name: true }` 로 응답 필드를 명시한다 | `[일반]` |
| Jackson (Java) | 응답 DTO 에 필드를 두지 않거나, 엔티티에 `@JsonIgnore` 또는 `@JsonView` 를 붙인다 | `[일반]` |
| Django REST framework | `fields = ['id', 'account_name', 'created']` 처럼 명시한다. `fields = '__all__'` 은 모델에 필드가 추가될 때 의도하지 않게 노출되므로 쓰지 않는다 | DRF 문서가 명시 지정을 강하게 권장 `[요약 확인]` |
- 합격 기준: 각 응답 JSON 의 키 목록이 허용 목록과 일치한다
- 시험 `[미실행]`: 응답 키를 뽑아 허용 목록 파일과 비교한다. 목록에 없는 키가 있으면 FAIL
  ```bash
  curl -s -b "$COOKIE" "$BASE/api/users/me" | jq -r 'keys[]' | sort | diff - allowed/users-me.txt
  ```
- 출처: https://api-security.owasp.org/editions/2023/en/0xa3-broken-object-property-level-authorization , https://www.django-rest-framework.org/api-guide/serializers/

## SEC-21 AI 기능 (LLM 프롬프트 인젝션) [요약 확인, 2026-11-25]
AI 가 사용자 입력, 문서, 웹 내용을 읽는 기능에 적용한다.
- 신뢰하는 지시와 신뢰할 수 없는 데이터를 분리한다. 라벨이나 프롬프트 문구를 강제 경계로 믿지 않는다
- 사용자 입력, 외부 문서, 인코딩된 데이터는 모두 비신뢰 입력으로 선별한다. 단어 하나가 아니라 구문으로 매칭하고 (단어 단위는 오탐), 매칭 전에 입력 길이를 제한한다
- 모델 출력은 모든 후속 사용처에서 비신뢰로 취급한다. 목적지에 맞게 안전한 HTML 렌더링 또는 매개변수화 쿼리를 쓴다. 시스템 프롬프트 유출과 API 키 노출 같은 주입 성공 징후를 감시한다
- 권한은 모델 밖의 실행 코드에서 강제한다. 도구 호출과 매개변수를 사용자 권한과 세션 문맥으로 검증한다
- 최소 권한: 읽기 전용 DB 계정, 제한된 API 범위, 도구마다 필요한 데이터와 동작만 준다
- 결과가 큰 동작은 실행 전에 사람 승인을 받고, 실행 쪽이 그 정확한 동작의 승인을 확인한다. 요청 수는 사용자 또는 IP 별로 제한한다
- 증거: '이전 지시를 무시해' 류 입력, 외부 문서에 숨긴 지시, 다른 사용자 데이터 요청, 시스템 프롬프트 출력 요청에 대한 결과
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html

## SEC-22 인젝션과 입력 해석 (SQL 제외) [KISA 가이드 2021.12.29 확인, 2026-11-25]
외부 입력이 코드, 명령, 경로, 주소, 쿼리, 헤더의 일부로 해석되는 곳마다 적용한다. SQL 은 SEC-01.
- 코드 삽입 (1-2, p143): 입력값에 든 코드가 동적으로 실행되는 약점. 동적 코드를 실행하는 함수를 쓰지 않는다. 필요하면 외부 입력에 허용 목록 방식을 적용한다
- 운영체제 명령어 삽입 (1-5, p157): 웹 인터페이스로 서버 내부에 시스템 명령어를 전달하지 않게 구성한다. 외부 값을 검증 없이 명령어로 쓰지 않고, 명령 생성에 필요한 값을 미리 정해 두어 외부 입력은 선택만 하게 한다
- 신뢰되지 않는 URL 로 자동접속 (1-7, p166): 사용자 입력을 외부 사이트 주소로 써서 연결하면 피싱에 노출된다. 연결 대상 URL 과 도메인을 허용 목록으로 관리하고 입력값이 목록에 있는지 확인한 뒤 연결한다. 비교 코드는 아래 열린 리다이렉트
- XML 외부개체 (1-8, p170): 외부에서 받은 XML 문서의 DTD 를 완전히 비활성화한다. 불가능하면 파서별 방식으로 외부 엔티티와 외부 문서 유형 선언을 비활성화한다. 로컬 정적 DTD 를 쓴다
- XML 삽입 (1-9, p174): XQuery 또는 XPath 쿼리에 쓰는 입력의 특수문자와 예약어를 걸러내고, 파라미터화된 쿼리를 지원하는 방식을 쓴다
- LDAP 삽입 (1-10, p183): DN 과 필터에 쓰는 입력의 특수문자를 제거하거나 일반 문자로 처리한다
- HTTP 응답분할 (1-13, p193): 요청 파라미터를 응답 헤더 (`Set-Cookie` 등) 에 넣을 때 CR, LF 개행문자를 제거한다
- [일반] 가이드 예제는 Java, C# 이다. JavaScript 및 Python 에서는 문자열을 쉘로 넘기는 `exec` 대신 인자 배열로 실행하는 API (`execFile`, `subprocess.run([...])`), `eval` 과 `Function` 문자열 실행 금지로 옮긴다. 도입 전 해당 언어 문서 확인
- 증거: `../` 와 인코딩된 `..%2f` 로 경로 이탈 시도, 외부 도메인으로 `?next=` 리다이렉트, 개행문자를 넣은 헤더 값, 명령 구분자를 넣은 입력
- 출처: KISA 소프트웨어 개발보안 가이드 2021.12.29 제4장 제1절 (대응표 `kisa-map.md`)

### 경로 조작 (KISA 1-3, p146)
KISA 의 대책은 파일명 입력에서 경로순회 문자 (`/`, `\`, `..`) 를 제거하는 것이다. 제거만으로는 부족하다. `"../"` 를 한 번 지우는 방식에서는 `....//` 의 가운데 `../` 가 지워진 뒤 `../` 가 다시 남는다. 제거 대신 최종 경로가 허용 루트 아래인지 비교한다.
```js
// Node: 루트 뒤에 구분자를 붙여 비교한다
const ROOT = path.resolve('/srv/app/files');
const p = path.resolve(ROOT, name);
if (!p.startsWith(ROOT + path.sep)) throw new Error('forbidden');
// 심볼릭 링크: p 가 이미 있으면 fs.realpath(p) 를 realpath(ROOT) 와 같은 방식으로 다시 비교 [일반]
```
```python
# Python 3.9+: resolve() 는 심볼릭 링크와 .. 를 해석한다
ROOT_RESOLVED = Path(ROOT).resolve()
p = Path(ROOT, name).resolve()
if not p.is_relative_to(ROOT_RESOLVED):
    raise PermissionError
```
```java
// Java: normalize() 는 문자열 처리만 하므로 실제 파일 경로는 toRealPath() 로 다시 확인한다
Path root = Path.of("/srv/app/files").toRealPath();
Path p = root.resolve(name).normalize();
if (!p.startsWith(root)) throw new SecurityException();
Path real = p.toRealPath();                 // 파일이 있어야 하며 심볼릭 링크를 해석함
if (!real.startsWith(root)) throw new SecurityException();
```
- 함정 1, 문자열 접두 비교: 루트가 `/srv/app` 일 때 `"/srv/app-evil/x".startsWith("/srv/app")` 는 참이다. Node 는 루트 뒤에 `path.sep` 을 붙여 비교하고, Java `Path.startsWith(Path)` 는 이름 요소 단위로 비교하므로 `/srv/app-evil` 을 통과시키지 않는다. Java 에서 `p.toString().startsWith(rootString)` 으로 바꾸면 이 보호가 사라진다
- 함정 2, 심볼릭 링크: `path.resolve`, `normalize()` 는 파일시스템을 보지 않아 루트 안의 링크가 밖을 가리켜도 통과한다 (Java 문서: `normalize()` 는 파일시스템에 접근하지 않으며 앞 이름이 심볼릭 링크이면 다른 파일을 가리킬 수 있다). Python `resolve()` 와 Java `toRealPath()` 는 링크를 해석한다. 업로드 디렉터리에 사용자가 링크를 만들 수 없게 한다 (SEC-04)
- 함정 3, 절대 경로 입력: `path.resolve(ROOT, '/etc/passwd')` 는 `/etc/passwd` 가 된다 (Node 문서: 오른쪽부터 처리해 절대 경로가 되면 멈춤). 위 비교가 이것을 거른다
- 근거: Node `path.resolve`, Python `pathlib`, Java `Path` 문서 `[요약 확인]`. `path.isAbsolute()` 는 경로 순회 방어로 안전하지 않다고 Node 문서가 적었다. 코드 실행은 `[미실행]`
- 시험: `....//`, `..%2f`, `%2e%2e/`, `/etc/passwd`, 루트와 이름이 같은 접두의 다른 폴더, 루트 안에서 밖을 가리키는 링크

### 열린 리다이렉트 (KISA 1-7, p166)
'상대 경로면 허용' 은 `//evil.example` (프로토콜 상대 URL), `/\evil.example` 이 `/` 로 시작해 통과한다. 브라우저는 이를 외부 주소로 해석한다 `[일반]`. 문자열 모양이 아니라 파싱한 결과의 출처를 비교한다. OWASP 는 접두 및 접미 문자열 비교를 쓰지 말고, 유지보수되는 URL 파서로 구성 요소를 비교하며, 사용자 정보가 든 주소를 거부하고, 검사한 URL 을 그대로 쓰라고 한다 `[요약 확인]`.
```js
const BASE = 'https://app.example.com';
const BASE_ORIGIN = new URL(BASE).origin;

function safeNext(next) {
  try {
    const u = new URL(next, BASE);
    if (u.origin !== BASE_ORIGIN || u.username || u.password) return '/';
    return u.pathname + u.search + u.hash;   // 검사한 값으로 이동
  } catch { return '/'; }
}
```
- `new URL('//evil.example', BASE)` 와 `new URL('/\\evil.example', BASE)` 의 출처가 `evil.example` 로 나와 `/` 로 대체된다 (WHATWG URL 동작 `[일반]`, 실행은 `[미실행]`)
- 외부 목적지가 필요하면 허용 목록에 스킴, 호스트, 포트를 정해 두고 비교한다. 가능하면 짧은 토큰을 서버에서 목적지로 매핑한다 (OWASP)
- 시험: `?next=//evil.example`, `?next=/\evil.example`, `?next=https://evil.example`, `?next=https://app.example.com@evil.example`, `?next=javascript:alert(1)`

## SEC-23 암호와 데이터 보호 [KISA 가이드 2021.12.29 확인, 2026-11-25]
- 자체 알고리즘을 만들지 않고 검증된 표준 알고리즘을 쓴다. base64 같은 단순 인코딩은 암호화가 아니다 (2-4, p223)
- 가이드가 취약하다고 든 것: RC2, RC4, RC5, RC6, MD4, MD5, SHA1, DES. 안전성 수준은 최소 112비트. 가이드 참고표: ARIA (128, 192, 256), SEED (128), AES, SHA-224 이상 (224, 256, 384, 512), HMAC, 공개키 RSAES 2048 및 3072
- 키 길이 (2-7, p245): RSA 는 2,048비트 이상, 대칭 암호는 128비트 이상
- 난수 (2-8, p248): 세션 ID, 암호화 키처럼 보안 결정에 쓰는 값은 예측할 수 없는 난수를 쓴다. 가이드는 Java 의 `SecureRandom` 을 쓰고 `Random()` 과 `Math.random()` 을 쓰지 말라고 한다 [일반] JavaScript 는 `crypto.randomBytes` 또는 `crypto.getRandomValues`, Python 은 `secrets` 모듈
- 개인정보, 금융정보, 비밀번호는 전송과 저장 시 암호화한다. 필요 시 HTTPS 를 쓰고, 중요정보 접근 시 권한을 확인한다 (2-5, p227)
- 하드코드된 키와 비밀번호를 쓰지 않는다. 암호화 키를 소스에 상수로 넣지 않는다 (2-6, p237) 상세는 SEC-12
- 인증서 검증 (2-11, p257): 인증서의 Common Name 과 실제 호스트가 일치하는지, 신뢰된 발급기관의 서명인지, 유효기간과 해지 여부, 안전한 암호화 알고리즘 사용 여부를 확인한다. [일반] 시험 중 `rejectUnauthorized: false`, `verify=False` 같은 검증 끄기 설정이 코드에 남아 있는지 찾는다
- 전자서명 (2-10, p255): 서명이 포함된 파일은 항상 서명을 확인하고, 신뢰할 수 없는 곳에서 만든 파일은 쓰지 않는다
- 사례: 유심 인증키 평문 저장 (SK텔레콤), 주민등록번호와 비밀번호 암호화 미이행 및 결제 로그 평문 기록 (롯데카드), 모든 장비가 같은 인증서를 쓰고 유효기간 10년 (KT). 상세 `incidents.md`
- 법령상 암호화 대상 (주민등록번호 등) 은 해당 법령과 고시로 확인한다. 이 문서에서 조항을 확인하지 않았다
- 국산 암호 및 검증필 암호모듈 요구 여부는 발주 요건 또는 고시로 확인한다 (가이드는 업무 내용 및 개인정보에 검증필 암호모듈 사용을 제시)
- 증거: 알고리즘과 키 길이 설정값, 평문 저장 여부 (DB 와 로그 파일), 인증서 검증 설정, 난수 함수 종류

### 운용 모드 `[요약 확인, 2026-11-25]`
알고리즘 이름과 키 길이만으로는 안전하지 않다. 'AES 128비트 이상' 은 ECB, 고정 IV, nonce 를 재사용한 GCM 도 통과시킨다.
- 인증 암호화 (AEAD) 를 첫 선택으로 한다. OWASP: 가장 흔한 인증 모드는 GCM 과 CCM 이며 첫 선호로 쓴다. AES-GCM 은 같은 키로 nonce 를 다시 쓰면 그 키로 만든 모든 메시지의 안전이 깨진다 (`cryptography` 문서 경고). nonce 는 키당 유일해야 하며 길이는 96비트 (12바이트) 를 NIST 가 권고한다
- ChaCha20-Poly1305 도 AEAD 이며 nonce 12바이트를 키당 재사용하지 않는다 (`cryptography` 문서). OWASP Cryptographic Storage 문서에는 이 알고리즘이 없다
- ECB 금지: OWASP 는 매우 특수한 경우가 아니면 쓰지 말라고 한다. 이 스킬은 예외 없이 금지한다 (사용자 정책)
- CBC, CTR 은 변조를 막지 못한다. 별도 인증이 필요하며 암호화 후 MAC (encrypt-then-MAC) 으로 HMAC 을 결합한다
- 라이브러리의 고수준 API 가 IV 및 nonce 를 자동 처리하면 그것을 쓴다. 직접 만들면 CSPRNG 로 메시지마다 새로 만든다
- 같은 키로 암호화할 수 있는 메시지 수의 상한은 NIST SP 800-38D 로 확인한다 `[미실행]`
| 스택 | 안전 | 위험 |
|---|---|---|
| Java | `Cipher.getInstance("AES/GCM/NoPadding")`, `GCMParameterSpec(128, iv)`, 메시지마다 `SecureRandom` 으로 만든 12바이트 `iv` `[일반]` (변환 이름은 `[요약 확인]`) | `Cipher.getInstance("AES")`. 모드와 패딩을 생략하면 공급자 기본값이 쓰이고 SunJCE 는 ECB 와 PKCS5Padding 을 기본으로 쓴다고 Oracle 문서가 적었다. 문서는 모드와 패딩을 모두 지정하라고 권한다 |
| Node.js | `crypto.createCipheriv('aes-256-gcm', key, iv)` 후 `cipher.getAuthTag()` 를 암호문과 함께 저장하고, 복호화 때 `decipher.setAuthTag(tag)` 후 `final()` (변조되면 예외) | `crypto.createCipher(...)` (IV 없이 비밀번호에서 키를 만드는 구형 API. 최신 Node 에서 제거됨 `[일반]`), `aes-256-ecb` |
| Python | `AESGCM.generate_key(bit_length=256)` 로 키 생성, `AESGCM(key).encrypt(nonce, data, aad)` 에서 `nonce = os.urandom(12)` 를 메시지마다 새로 `[요약 확인]` | `AES.new(key, AES.MODE_ECB)`, 고정 `nonce`, 같은 키와 nonce 쌍 재사용 |
- 합격 기준: 소스에 ECB 와 모드 생략이 없고, IV 및 nonce 가 메시지마다 새로 만들어진다
- 검색 `[미실행]`: `rg -n 'AES/ECB|getInstance\("AES"\)|MODE_ECB|modes\.ECB|-ecb[\x27"]|createCipher\(' ` 결과 0건. 결과가 있으면 위치마다 사유를 기록하고 AEAD 로 바꾼다
- 시험: 같은 평문을 두 번 암호화해 암호문이 달라지는지, 암호문 한 바이트를 바꾸면 복호화가 실패하는지 확인
- 출처: https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html , https://cryptography.io/en/latest/hazmat/primitives/aead/ , https://docs.oracle.com/en/java/javase/21/docs/api/java.base/javax/crypto/Cipher.html , https://docs.oracle.com/en/java/javase/21/security/oracle-providers.html

## SEC-24 언어 한정 코드 안전성 (해당 언어일 때만) [KISA 가이드 2021.12.29 확인, 2026-11-25]
항목마다 언어에 따라 판정 방식이 다르다. 번호는 `kisa-map.md` 에 맞췄다.

### 언어 한정 (쓰지 않는 언어면 `NOT_APPLICABLE` 과 이유를 적는다)
| KISA | 항목 | 해당 언어 | 내용 |
|---|---|---|---|
| 1-16 (p205) | 메모리 버퍼 오버플로우 | C, C++ | 메모리 접근을 허용 범위 안으로 제한. 금지 함수는 안전 함수로 |
| 1-17 (p208) | 포맷 스트링 삽입 | C, C++ | 외부 입력을 포맷 문자열로 쓰지 않음 |
| 5-3 (p306) | 해제된 자원 사용 | C, C++ | 해제한 메모리를 다시 쓰지 않음 |
| 5-4 (p309) | 초기화되지 않은 변수 사용 | C, C++ | 변수를 선언과 함께 초기화 |
| 6-3 (p324) | Public 메소드부터 반환된 Private 배열 | Java 등 클래스 기반 | private 배열을 public 메소드로 그대로 반환하지 않고 복사본을 씀 |
| 6-4 (p328) | Private 배열에 Public 데이터 할당 | Java 등 클래스 기반 | 인자를 그대로 저장하지 않고 복사본을 씀 |
- 금지 함수는 대체 안전 함수로 (7-2, p336, `gets` 대신 `fgets`, `strcpy` 대신 `strcpy_s`). 가이드의 금지 함수 목록은 C 중심이다. 다른 언어는 SEC-05 에서 본다

### 언어 무관 (모든 프로젝트에서 판정)
`NOT_APPLICABLE` 로 넘기지 않고 PASS 또는 FAIL 로 판정한다.
- 정수형 오버플로우 (1-14, p196): 언어와 플랫폼별 정수 범위를 확인하고, 외부 입력이 반복문, 메모리 할당, 복사에 쓰이면 값이 적정 범위인지 확인한다. 수량과 금액은 SEC-19. `kisa-map.md` 는 이 항목에 '언어' 를 적었다. 고정 폭 정수를 쓰는 언어에 모두 해당하므로 여기서는 항상 판정으로 둔다
- 종료되지 않는 반복문 또는 재귀 (3-2, p285): 재귀에 호출 횟수 제한 또는 종료 조건을 둔다. 자원 고갈을 일으킨다
- 부적절한 자원 해제 (5-2, p301): 열린 파일, 소켓, DB 연결은 오류 경로에서도 반드시 해제한다
- 잘못된 세션에 의한 정보노출 (6-1, p316): 싱글톤 및 서블릿 멤버 변수에 요청별 사용자 데이터를 저장하면 다중 스레드에서 세션끼리 데이터가 섞인다. 지역변수를 쓴다. [일반] Node 에서는 모듈 전역 변수에 요청별 데이터를 저장하는 경우에 같은 위험이 있다
- 경쟁조건 (3-1, p279): 공유자원은 동기화 구문으로 한 번에 하나만 접근하게 한다. 임계 코드 주변만 동기화한다. 같은 쿠폰이나 재고에 대한 동시 요청은 SEC-19
- 널 역참조 (5-1, p296): 널이 될 수 있는 값은 참조 전에 검사한다. 요청 파라미터도 널 검사 후 쓴다. `kisa-map.md` 는 '언어' 로 적었고 널 또는 None 값이 있는 언어에는 모두 해당한다 `[일반]`
- DNS lookup 에 의존한 보안결정 (7-1, p332): 보안결정에 도메인명 DNS lookup 을 쓰지 않고 IP 주소를 직접 비교한다. SSRF 의 DNS 해석 후 IP 검사 (SEC-13) 와 방향이 다르므로 같이 읽는다
- 증거: 해당 언어 정적 분석 결과, 오류 경로 시험, 동시 요청 시험

## 확인 수준 (통제별)
| 통제 | 확인 수준 | 비고 |
|---|---|---|
| SEC-01 | 기존 부분 `[원문]` (2026-11-23, 이번에 재확인하지 않음). 스택 코드 쌍 `[요약 확인]` | MyBatis `#{}`, `Sequelize.literal` 은 `[일반]`. 검색 명령 `[미실행]` |
| SEC-02 | 정책값 `[일반]` (사용자 정책). 스프레이 및 스터핑 대책 `[요약 확인]` | ASVS 6.1.1, 6.2.4, 6.2.12, 6.3.1, 6.3.3 및 OWASP Authentication |
| SEC-03 | `[원문]` (표기 유지) | 이번에 재확인하지 않음 |
| SEC-04 | `[원문]` (표기 유지) | SVG 및 zip slip 은 `[일반]` |
| SEC-05 | 기존 부분 `[원문]` (표기 유지). 사례 보강 | 비 npm 감사 도구는 `[일반]` |
| SEC-06 | `[요약 확인]` | 비밀번호 정책 및 OTP 는 ASVS 6.x, OWASP Forgot Password, MFA |
| SEC-07 | `[요약 확인]` | KISA 보강은 가이드 확인 |
| SEC-08 | `[요약 확인]` | EJS 와 DOM API 는 `[일반]`. 업로드 HTML 및 SVG 위험은 `[일반]` |
| SEC-09 | `[요약 확인]` | OWASP CSRF. 코드는 `[미실행]` |
| SEC-10 | `[요약 확인]` | JWT 항목과 Django `cycle_key()` 는 `[일반]` |
| SEC-11 | 상세 없음 | SKILL.md 표 참조 |
| SEC-12 | `[요약 확인]` | `.env`, 공개 환경변수 항목은 `[일반]` |
| SEC-13 | `[요약 확인]` | Jackson 기본 타입 지정은 `[일반]`, Java 필터 세부는 `[미실행]` |
| SEC-14 | `[요약 확인]` | HSTS 31536000 은 `[일반]`. 검사 명령은 `[미실행]` |
| SEC-15 | 상세 없음 | 사례 한 줄만 있음 |
| SEC-16 | `[요약 확인]` | `npm rebuild` 및 SBOM 외 스택은 `[일반]` 또는 `[미실행]` |
| SEC-17 | `[요약 확인]` | BaaS 항목은 `[일반]` |
| SEC-18 | `[요약 확인]` | `p/owasp-top-ten` 이름과 Maven `-D` 형식은 `[미실행]` |
| SEC-19 | `[요약 확인]` | |
| SEC-20 | `[요약 확인]` | Prisma `select`, Jackson 어노테이션은 `[일반]` |
| SEC-21 | `[요약 확인]` | |
| SEC-22 | KISA 가이드 확인. 코드는 `[요약 확인]` 문서 근거 + `[일반]` | KISA 가이드 PDF 를 읽은 경로가 기록되지 않아 요약 확인 수준으로 본다 |
| SEC-23 | KISA 가이드 확인. 운용 모드는 `[요약 확인]` | Node `createCipher` 제거 여부는 `[일반]` |
| SEC-24 | KISA 가이드 확인 | 코드 예제 본문은 일부 항목만 읽음 |
- `[요약 확인]` 은 원문과 한 글자까지 같다고 보장하지 않으므로, 수치와 코드 예시를 규정이나 계약에 인용할 때는 위 출처 URL 에서 다시 확인한다
- SEC-22 ~ SEC-24 와 KISA 보강은 행정안전부 및 한국인터넷진흥원의 소프트웨어 개발보안 가이드 PDF (2021.12.29, 381쪽) 에서 항목별 개요와 보안대책 절을 읽고 정리했다. 코드 예제 본문은 일부 항목만 읽었다. 문장을 그대로 옮기지 않고 요지를 적었으므로 인용할 때는 표시한 쪽에서 원문을 확인한다. 사고 사례는 `incidents.md` 에 출처와 근거 등급을 적었다

## 기준 문서 대응표
KISA 가이드 항목과 통제의 대응은 `kisa-map.md`. 아래는 OWASP ASVS 5.0 장 및 OWASP API Security Top 10 2023 항목과 통제의 대응이다. 장과 항목의 이름은 ASVS 저장소 파일 목록과 API Security 사이트에서 확인했고 `[요약 확인]`, 통제와 연결한 것은 이 스킬의 판단이다 `[일반]`. CWE 번호는 `kisa-map.md` 에 KISA 항목별로 있다. OWASP Top 10:2025 대응표는 만들지 않았다.

### ASVS 5.0.0 (2025-05-30 게시)
| ASVS 장 | 통제 | 이 문서에서 원문 확인한 항목 번호 |
|---|---|---|
| V1 Encoding and Sanitization | SEC-01, SEC-08, SEC-22 | 없음 |
| V2 Validation and Business Logic | SEC-19, SEC-13 | 없음 |
| V3 Web Frontend Security | SEC-08, SEC-09, SEC-14 | 없음 |
| V4 API and Web Service | SEC-13, SEC-20 | 없음 |
| V5 File Handling | SEC-04 | 없음 |
| V6 Authentication | SEC-02, SEC-03, SEC-06 | 6.1.1, 6.2.1, 6.2.4, 6.2.5, 6.2.9, 6.2.10, 6.2.11, 6.2.12, 6.3.1, 6.3.3, 6.3.6, 6.4.3, 6.5.1, 6.5.3, 6.5.4, 6.5.5, 6.6.3 |
| V7 Session Management | SEC-10 | 7.2.3, 7.2.4, 7.3.1, 7.3.2, 7.4.1 |
| V8 Authorization | SEC-07, SEC-20 | 없음 |
| V9 Self-contained Tokens | SEC-10, SEC-13 (JWT) | 없음 |
| V10 OAuth and OIDC | 대응 통제 없음 | 없음 |
| V11 Cryptography | SEC-23 | 없음 |
| V12 Secure Communication | SEC-11, SEC-14 (HSTS) | 없음 |
| V13 Configuration | SEC-12, SEC-14, SEC-17 | 없음 |
| V14 Data Protection | SEC-23, SEC-15 | 없음 |
| V15 Secure Coding and Architecture | SEC-05, SEC-16, SEC-24 | 없음 |
| V16 Security Logging and Error Handling | SEC-15, SEC-14 (오류 응답) | 없음 |
| V17 WebRTC | 대응 통제 없음 | 없음 |

### OWASP API Security Top 10 2023
| 항목 | 통제 |
|---|---|
| API1 Broken Object Level Authorization | SEC-07 |
| API2 Broken Authentication | SEC-02, SEC-03, SEC-06, SEC-10 |
| API3 Broken Object Property Level Authorization | SEC-20 |
| API4 Unrestricted Resource Consumption | SEC-13 (요청 크기 및 속도 제한), SEC-02 |
| API5 Broken Function Level Authorization | SEC-07 |
| API6 Unrestricted Access to Sensitive Business Flows | SEC-19 |
| API7 Server Side Request Forgery | SEC-13 |
| API8 Security Misconfiguration | SEC-14, SEC-17 |
| API9 Improper Inventory Management | 대응 통제 없음 (미대응) |
| API10 Unsafe Consumption of APIs | SEC-19 (외부 콜백 검증) 일부. 그 외는 미대응 |
- 항목 설명의 세부는 API3 만 읽었다. 나머지 항목은 이름만 확인했다

## 기준 문서 (2026-11-23 확인)
- OWASP ASVS 5.0.0 (2025-05-30 게시), OWASP Top 10:2025
