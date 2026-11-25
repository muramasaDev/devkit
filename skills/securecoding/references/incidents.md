# 사고 사례와 통제 (2026-11-25 조사)

통제가 왜 필요한지를 실제 사고로 확인하기 위한 표다. 출처 본문을 읽은 것만 적었고, 원인은 출처에 적힌 문장의 요지다. 통제 ID 는 원인에 맞춰 이 스킬이 붙인 것이며 출처가 붙인 번호가 아니다.
근거 표기: `A` 기관 자료(개인정보보호위원회, 과학기술정보통신부, 금융위원회, 법원 판결문, NVD, 공급사 보안 공지, CISA, GAO) 본문 확인. `B` 언론 또는 전문 업체 조사 글 확인. 사례에 적힌 수치는 출처가 낸 수치다.
이 표는 침투 경로 전체를 설명하는 것이 아니라 출처가 지적한 결함만 적는다. 출처에 원인이 없으면 적지 않았다.

## 1. 웹 및 API 결함이 직접 원인인 사례
| 연도 | 대상 | 출처에 적힌 원인 | 통제 | 근거 | 출처 |
|---|---|---|---|---|---|
| 2017 | 여기어때 | 마케팅센터 웹페이지의 SQL 인젝션으로 관리자 세션 ID 를 탈취, 세션 변조로 외부에 노출된 관리 페이지에 관리자 권한 접속. 이상 DB 질의 검증과 세션 변조 탐지 없음 | SEC-01, 07, 10 | B | https://byline.network/2017/04/1-691/ |
| 2023 | MOVEit Transfer | 미공개 SQL 인젝션 (CVE-2023-34362), 웹 셸 설치 후 DB 에서 데이터 탈취. 2773개 조직, 9578만명 (Emsisoft 집계) | SEC-01, 05 | A, B | https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-158a |
| 2025 | 비와이엔블랙야크 | 웹사이트 개설 후 SQL 삽입 취약점 점검 및 조치 소홀. 관리자 계정 탈취 후 외부 접속 가능한 관리자 페이지에 로그인. ID 및 비밀번호 외 인증수단 없음. 이용자 342,253명 | SEC-01, 06, 07 | A | https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=11343 |
| 2024 | 한국사회복지협의회 | 비밀번호 변경 기능에서 변경 요청자와 대상자 일치 여부를 확인하지 않음. 2천만 회 이상 접속 시도를 탐지하지 못함. 회원 약 135만명 | SEC-07, 15, 19 | A | https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=10609 |
| 2025 | Next.js 미들웨어 (CVE-2025-29927) | 미들웨어에서 하는 인가 검사를 `x-middleware-subrequest` 헤더로 우회 (CWE-285). 11.1.4 ~ 15.2.3 미만. 악용 피해 수치는 출처에 없음 | SEC-05, 07 | A | https://github.com/vercel/next.js/security/advisories/GHSA-f82v-jwr5-mffw |
| 2024 | 일학, 네오팜 (개인정보위 2024-10-23 의결) | 일학: SQL 삽입, 입력값 검증 절차 부재, 비밀번호 암호화 미조치. 네오팜: 쇼핑몰 관리자 계정 탈취 후 로그인, 추가 인증수단 없음, 접속 IP 미제한, 계정 공유 | SEC-01, 03, 06, 07 | A | https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=10701 |
| 2021 | Log4Shell (CVE-2021-44228) | 로그 메시지의 JNDI lookup 치환이 켜진 상태에서 공격자가 로그 문자열을 제어하면 LDAP 서버의 코드를 실행. 2.0-beta9 ~ 2.15.0 | SEC-05, 13, 16 | A | https://nvd.nist.gov/vuln/detail/CVE-2021-44228 |

## 2. 노출된 DB, 저장소, 키 (BaaS 및 AI 생성 앱 포함)
| 연도 | 대상 | 출처에 적힌 원인 | 통제 | 근거 | 출처 |
|---|---|---|---|---|---|
| 2025 | Lovable 생성 앱 (CVE-2025-48757) | Supabase 행 수준 보안(RLS) 정책 누락 또는 부실. NVD 는 비인증 공격자가 임의 테이블을 읽고 쓸 수 있다고 적음. 공급사는 고객 책임이라고 이의 제기. 조사한 1645개 프로젝트 중 170개 노출 | SEC-07, 12, 17 | A, B | https://nvd.nist.gov/vuln/detail/CVE-2025-48757 |
| 2026 | Moltbook | 프론트엔드 JS 에 Supabase API 키 하드코딩, DB 에 RLS 정책 없음. 키만으로 운영 데이터 전체를 읽고 쓸 수 있음. 에이전트 인증 토큰 약 150만개, 이메일 약 3만 5000개 | SEC-07, 12, 17 | B | https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys |
| 2026 | Supabase 사용 앱 (UpGuard 조사) | RLS 미설정 또는 부실 정책, 클라이언트 코드의 공개 키 오용, API 로 만든 테이블은 RLS 가 기본 비활성. 16,326개 DB 읽기 가능 (악용 사고가 아닌 노출 조사) | SEC-07, 14, 17 | B | https://www.upguard.com/blog/everything-everywhere-systemic-data-exposure-in-supabase-apps |
| 2022 | Toyota T-Connect | 협력사가 소스코드를 공개 GitHub 에 올렸고 코드에 데이터 서버 접근 키가 포함됨. 296,019건 유출 가능, 제3자 접근은 확인되지 않음 | SEC-12, 16 | A | https://global.toyota/jp/newsroom/corporate/38095972.html |
| 2016 | Uber | 비공개 GitHub 계정의 코드에 AWS 키가 있었고, 그 키로 AWS 저장소에 접근. 내려받은 데이터는 비암호화 (제9순회항소법원 판결문) | SEC-12, 17, 23 | A | https://cdn.ca9.uscourts.gov/datastore/opinions/2025/11/12/23-927.pdf |
| 2025 | 쿠팡 | 전직 개발자가 재직 중 관리하던 인증 서명키로 전자 출입증을 위조해 로그인 없이 접속. 관문서버에 위변조 검증 절차 없음, 퇴사 시 서명키 미갱신. 과기정통부는 개발과 운영 미분리, 개발자 노트북에 키 저장을 지적 | SEC-12, 17, 23 | A | https://www.korea.kr/briefing/policyBriefingView.do?newsId=156744092 |

## 3. 암호화, 저장, 로그
| 연도 | 대상 | 출처에 적힌 원인 | 통제 | 근거 | 출처 |
|---|---|---|---|---|---|
| 2025 | SK텔레콤 | 인터넷과 연결된 관리망 서버에 악성코드 설치, 평문으로 저장된 계정정보로 내부 서버 이동, 유심 인증키 26,144,363건 평문 저장. 개인정보위: 인터넷망에서 관리망 서버로 접근을 제한 없이 허용. 보안 업데이트 미적용, 이상행위 로그 미확인 | SEC-05, 15, 17, 23 | A | https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=11453 |
| 2025 | 롯데카드 | 결제 로그에 주민등록번호 등을 별도 검토 없이 평문 기록, 주민등록번호 및 비밀번호 암호화 미이행, 패치 미실시, 백신 미설치 | SEC-05, 15, 23 | A | https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=11878 |
| 2024 | 순천향대, 경성대 | 개인정보처리시스템의 웹로직 취약점 (2017-10 배포 보안패치 미적용) 을 이용한 해킹. 웹방화벽 및 침입방지시스템 미설정, 주민등록번호 암호화 미조치 | SEC-05, 14, 23 | A | https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=10756 |
| 2017 | Equifax | 공개된 Apache Struts 취약점 (CVE-2017-5638) 패치 미적용, 인터넷 노출 분쟁 접수 포털에서 악용. 최소 1억 4550만명 접근 (GAO) | SEC-05, 15 | A | https://www.gao.gov/products/gao-18-559 |
| 2025 | KT 소액결제 | 펨토셀의 생산, 납품, 내부망 접속 인증 전반의 보안 관리 부실. 모든 펨토셀이 같은 인증서를 쓰고 유효기간이 10년 | SEC-23 | A | https://www.korea.kr/briefing/policyBriefingView.do?newsId=156737260 |
| 2016, 2011 | 인터파크, 네이트 및 싸이월드 | 인터파크는 법원이 최대접속시간 제한 및 비밀번호 암호화 조치를 하지 않았다고 판단. 네이트는 대법원이 자동 로그아웃을 통상 요구되는 보호조치라고 보았으나 인과관계는 부정 | SEC-03, 10 | B | https://byline.network/2020/03/19-98/ |

## 4. 공급망과 AI 기능
| 연도 | 대상 | 출처에 적힌 원인 | 통제 | 근거 | 출처 |
|---|---|---|---|---|---|
| 2025 | Shai-Hulud npm 웜 | 개발자 계정 탈취 후 자기 복제로 패키지에 코드를 넣고 변조 버전 게시. GitHub 토큰과 클라우드 키를 탈취해 공개 저장소에 게시. npm 패키지 500개 이상 감염 | SEC-06, 12, 16 | A | https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem |
| 2025 | tj-actions/changed-files (CVE-2025-30066) | 인기 GitHub Action 변조, Actions 로그에 비밀정보 노출 | SEC-12, 16 | A | https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-github-action-cve-2025-30066 |
| 2021 | Codecov | Docker 이미지 생성 과정의 오류로 Bash Uploader 수정용 자격증명이 추출되어 2021-01-31 부터 스크립트 변조. 고객 CI 의 자격증명, 토큰, 키가 외부로 전송됨 | SEC-12, 16 | A | https://about.codecov.io/security-update/ |
| 2025 | Amazon Q Developer 확장 (CVE-2025-8217) | CodeBuild 설정의 GitHub 토큰 권한 범위가 과다해 악성 코드가 저장소에 커밋되고 1.84.0 에 포함 배포. 구문 오류로 실행되지 않음 (미수 사례) | SEC-12, 16, 21 | A | https://aws.amazon.com/security/security-bulletins/AWS-2025-015/ |

## 5. 근거가 약해 원인을 단정하지 않는 사례
원인이 공식 자료에 없거나, 결함이 인정되지 않았거나, 언론 보도 수준인 사례다. 통제의 근거로 인용하지 않는다.
- Capital One 2019: 공지가 설정 취약점이라고만 밝히고 세부 원인을 읽지 못했다
- Optus 2022: 코드 변경으로 API 접근통제가 약해졌다는 것은 규제기관의 소송 주장이며 판결 전이다. 원문을 읽지 못했다
- Parler 2021: 수집한 쪽의 설명과 언론 보도뿐이다
- Replit 에이전트 2025 (운영 DB 삭제): 원인 분석 문서가 없고 언론 보도와 사용자 발언이 근거다. 개발과 운영 DB 분리는 SEC-17 에서 같은 취지로 다룬다
- Samsung 2023 (ChatGPT 입력): 삼성이 유출 내용을 확인하지 않았다
- Tea 앱 2025: 원인은 언론 보도 수준이고 앱 측은 구 저장소 무단 접근이라고만 표현했다
- 예스24 2025, 옥션 2008, 농협 2011: 원인이 공개되지 않았거나 법원이 보호조치 위반을 인정하지 않았다

## 6. 통제별 색인
| 통제 | 사례 |
|---|---|
| SEC-01 SQL 인젝션 | 여기어때, MOVEit, 비와이엔블랙야크, 일학 |
| SEC-03 비밀번호 해시 | 일학 (비밀번호 암호화 미조치), 인터파크 판결 |
| SEC-05 패치와 의존성 | Equifax, SK텔레콤, 롯데카드, 순천향대 및 경성대, Log4Shell, MOVEit, Next.js |
| SEC-06 인증 | 비와이엔블랙야크, 네오팜 (관리자 추가 인증 없음), Shai-Hulud |
| SEC-07 권한 | 여기어때, Next.js, Lovable, Moltbook, UpGuard, 한국사회복지협의회, 비와이엔블랙야크 |
| SEC-10 세션 | 여기어때, 네이트 및 인터파크 (최대접속시간, 자동 로그아웃) |
| SEC-12 비밀정보 | Moltbook, Toyota, Uber, 쿠팡, Shai-Hulud, tj-actions, Codecov |
| SEC-15 로그와 탐지 | SK텔레콤, 롯데카드 (로그에 주민등록번호 평문), 한국사회복지협의회 (2천만 회 시도 미탐지) |
| SEC-16 공급망 | Shai-Hulud, tj-actions, Codecov, Amazon Q, Toyota |
| SEC-17 배포와 DB 접근 | SK텔레콤 (관리망 접근 무제한), Lovable, Moltbook, UpGuard, 쿠팡 (개발과 운영 미분리) |
| SEC-23 암호와 데이터 보호 | SK텔레콤 (평문 저장), 롯데카드, 순천향대, KT (공용 인증서), Uber, 쿠팡 (서명키) |

## 7. 개인정보 안전조치 지적 항목 (국내 기관 자료에 나온 이름)
개인정보보호위원회가 SK텔레콤 처분에서 안전조치 위반으로 적은 항목명: 접근통제, 접근권한 관리, 보안 업데이트, 악성프로그램 대응, 암호화, 로그 점검 및 탐지, 접속기록 보관. 국내 서비스에서 개인정보를 다루면 점검 때 이 항목명으로 대응 여부를 묻는다. 고시 조항 번호는 확인하지 못했다.

## 8. 확인 한계
- 출처끼리 수치가 다른 사례 (인터파크, 쿠팡, 여기어때) 는 이 표에 수치를 적지 않았다. 필요하면 출처에서 확인한다
- 쿠팡과 KT 는 정책브리핑 게재본을 읽었고 첨부 원문은 읽지 못했다
- 2026년 처분 및 소송은 진행 중일 수 있다
