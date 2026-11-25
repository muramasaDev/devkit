# 보안 설계 원칙 (시작 단계)

> OWASP Cheat Sheet Series (https://cheatsheetseries.owasp.org, CC BY-SA 4.0) 를 요약, 재구성, 한국어로 번역한 문서. 이 파일은 CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/) 으로 배포된다. 변경: 요약, 재구성, 번역, 다른 출처와 결합. OWASP 가 보증하지 않는다.

기능을 만들기 전에 보안이 걸릴 자리를 먼저 정한다. 아래 원칙은 OWASP Cheat Sheet 원문에 근거가 있는 것에 `[원문]`, KISA 가이드에 근거가 있는 것에 `[KISA]`, 사고 사례가 있는 것에 `[사례]`, 이 스킬이 구조 제안으로 덧붙인 것에 `[일반]` 을 붙였다. 상세 수치와 출처는 `controls.md`, 사고는 `incidents.md`, 가이드 항목은 `kisa-map.md`.

## 1. 구조 (요청 하나가 지나는 길)
```
브라우저, 앱 (비신뢰)
   |
[입구 계층]  인증 -> 인가 (기본 거부) -> 입력 스키마 검증 -> 속도 제한
   |
[서비스 계층]  업무 규칙: 가격 계산, 재고, 쿠폰, 상태 전이 (전부 서버 값 기준)
   |                         \
[데이터 계층]                 [외부 연동]  결제 서명 검증, AI 도구 권한
 소유자 범위 조회, DB 제약,
 데이터 접근 함수 안의 인가 재검사
```
- 계층마다 맡은 검사를 정한다. 입구 계층의 검사는 공통 함수 하나로 두고 라우트마다 다시 쓰지 않는다
- 입구 계층의 인가가 유일한 검사가 되면 안 된다. 입구 계층이 뚫려도 데이터 접근 함수와 각 서버 동작이 스스로 인가를 확인해야 한다 (원칙 2)

## 2. 원칙
| # | 원칙 | 구현 자리 | 통제 |
|---|---|---|---|
| 1 | 클라이언트가 보낸 값은 입력일 뿐 사실이 아니다 `[원문]` | 서비스 계층이 가격, 합계, 재고를 DB 로 계산 | SEC-19 |
| 2 | 모든 요청에서 권한을 검사한다. 기본은 거부. 입구 계층의 검사만 믿지 않는다 `[원문]` | 입구 계층은 기본 거부 (새 라우트는 권한 선언이 없으면 막힘 `[일반]`). 그에 더해 데이터 접근 함수와 각 서버 동작 (Server Action, Route Handler) 의 첫 줄에서 다시 인가한다 `[사례]`. 아래 2.1 | SEC-07 |
| 3 | 객체는 현재 사용자 범위로 조회한다 `[원문]` | 데이터 계층 함수가 소유자를 인자로 받음 | SEC-07 |
| 4 | 쓰기 가능한 필드는 허용 목록으로 정한다 `[원문]` | 요청마다 DTO 또는 스키마 | SEC-20 |
| 5 | 중복 사용과 동시 요청은 DB 가 막는다 `[원문]` | 유니크 제약, 원자적 `UPDATE ... WHERE`, 멱등성 키 | SEC-19 |
| 6 | 외부 결과는 서버 간 검증으로만 믿는다 `[원문]` | 결제 콜백 서명 검증과 금액 대조, 주문당 1회 이행 | SEC-19 |
| 7 | 출력은 문맥에 맞게 인코딩한다 `[원문]` | 템플릿 및 프레임워크 기본 인코딩 사용, 우회 API 금지 | SEC-08 |
| 8 | 비밀은 서버 설정 한 곳에만 둔다 `[원문]` | 설정 모듈이 환경별 보관소에서 읽음. 클라이언트 번들에는 비밀이 없음 `[일반]` | SEC-12 |
| 9 | DB 는 앱 서버만 접근한다 `[원문]` | 내부 네트워크, 서비스 전용 계정, 최소 권한 | SEC-17 |
| 10 | AI 의 권한은 모델 밖 코드가 강제한다 `[원문]` | 도구 호출 앞의 권한 검사, 읽기 전용 계정 | SEC-21 |
| 11 | 인증 실패와 권한 거부를 기록하고 비밀은 기록하지 않는다 `[일반]` | 입구 계층의 공통 로그 | SEC-15 |
| 12 | 관리 기능은 별도 경계로 둔다. 역할 기반 접근, 추가 인증, 접속 제한, 인터넷 비노출 `[KISA, 사례]` | 관리자 경로는 입구 계층의 별도 정책. 사례: 관리자 페이지 외부 노출 (비와이엔블랙야크), 추가 인증과 접속 IP 제한 없음 (네오팜) | SEC-06, 07 |
| 13 | 키와 계정은 사람이 떠나거나 역할이 바뀔 때 갱신한다 `[사례]` | 키 목록과 소유자를 설계 문서에 적음. 사례: 퇴사자의 서명키 (쿠팡) | SEC-12 |
| 14 | 개발과 운영의 데이터와 키를 분리한다 `[사례]` | 환경별 DB 와 계정과 키. 사례: 개발과 운영 미분리 (쿠팡, Replit) | SEC-17 |
| 15 | 보안 결정에 쓰는 값은 서버에 둔다. 쿠키, 숨은 필드, 파라미터로 결정하지 않는다 `[KISA]` | 입구 계층과 서비스 계층 | SEC-07, 19 |
| 16 | 오류가 나면 거부한다 `[일반]` | 입구 계층의 공통 오류 처리. 빈 `catch` 로 통과시키지 않음 `[KISA]` | SEC-14 |

### 2.1 원칙 2 보충: 입구 계층 한 곳에만 인가를 두지 않는다
- 사례: CVE-2025-29927. Next.js 가 재귀를 막으려고 쓰는 내부 헤더 `x-middleware-subrequest` 를 이용해 미들웨어 실행을 건너뛰게 만든 우회다. 수정 버전은 14.2.25, 15.2.3, 13.5.9, 12.3.5 이며 `next start` 와 `output: 'standalone'` 으로 자체 호스팅한 앱이 영향을 받았다. Vercel 의 사후 보고 (https://vercel.com/blog/postmortem-on-next-js-middleware-bypass) 는 Middleware 를 경로 보호의 유일한 방법으로 쓰기를 권하지 않는다고 적었다 `[요약 확인, 2026-11-25]`. 입구 계층 한 곳에 인가를 모은 구조는 그 한 곳이 건너뛰어지면 전부 열린다
- 구조: 입구 계층은 기본 거부로 두고 (빠른 사전 차단), 데이터 접근 함수와 각 서버 동작이 스스로 세션을 확인하고 소유자 조건으로 조회한다. Next.js 인증 가이드 (https://nextjs.org/docs/app/guides/authentication) 문구: 보안 검사의 대부분은 데이터 원본에 최대한 가깝게 한다. 가이드의 Proxy 는 쿠키만 읽는 낙관적 검사용이며 유일한 방어선이 아니다 (위 사례의 Middleware 와 같은 계층의 기능으로 보이나 이름 관계는 확인하지 못함 `[일반]`). Server Action 과 Route Handler 는 공개 API 엔드포인트와 같은 보안 고려로 다룬다. 레이아웃에서 하는 검사는 이동할 때 다시 실행되지 않고 하위 경로 세그먼트와 Server Action 접근을 막지 못한다 `[요약 확인, 2026-11-25]`
- Next.js 예: `server-only` 를 붙인 데이터 접근 함수 안에서 `verifySession()` 을 부른 뒤 소유자 조건으로 조회한다

```ts
// app/lib/dal.ts
import 'server-only'
import { cache } from 'react'
import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'
import { decrypt } from '@/app/lib/session'

export const verifySession = cache(async () => {
  const session = await decrypt((await cookies()).get('session')?.value)
  if (!session?.userId) redirect('/login')
  return { userId: session.userId }
})

// 데이터 접근 함수: 호출하는 쪽이 어디든 여기서 다시 확인한다
export async function getInvoice(id: string) {
  const { userId } = await verifySession()
  return db.invoice.findFirst({ where: { id, ownerId: userId } })  // 소유자 조건
}
```
```ts
// app/lib/actions.ts
'use server'
import { verifySession } from '@/app/lib/dal'

export async function deleteInvoice(id: string) {
  const { userId } = await verifySession()      // 각 서버 동작의 첫 줄
  await db.invoice.deleteMany({ where: { id, ownerId: userId } })
}
```
- `verifySession` 의 `cache` 는 렌더 한 번 안에서만 호출을 합친다. Server Action 과 Route Handler 는 렌더에 속하지 않아 호출마다 실행된다 (Next.js 문서) `[요약 확인]`
- 코드는 Next.js 문서의 Data Access Layer 예시를 줄인 것이며 `decrypt`, `db` 는 프로젝트 것이다. 이 문서에서 실행해 보지 않았다 `[미실행]`
- 다른 프레임워크도 같은 규칙이다: 미들웨어, 필터, 라우터 가드는 첫 관문이고, 서비스 및 저장소 함수가 소유자 조건을 갖는다 (원칙 3). 시험은 입구 계층을 거치지 않고 서버 동작 또는 API 를 직접 부르는 요청으로 한다 `[일반]`

## 3. 프로젝트마다 정하는 것
`templates/security-architecture.md` 를 복사해 아래를 채운다. 모르면 `미정` 으로 두고 추측으로 채우지 않는다.
- 역할 목록과 역할별로 접근하는 자원 (사용자 유형, 자원, 작업)
- 공개 경로와 보호 경로의 구분
- 금액, 재고, 쿠폰이 있으면 값의 계산 위치와 중복 방지 방법
- 비밀 보관 위치와 환경 구분 (개발, 검수, 운영)
- 비밀번호 정책 기준 (발주 요건이 KISA 면 KISA 2-9, 아니면 ASVS 5.0 V6. 선택과 예외는 보고서에 기록. `controls.md` SEC-06)
- 로그인 시도 제한의 관찰 창, 지연, IP 한도 (`controls.md` SEC-02 의 사용자 정책값)
- 인증번호의 길이, 만료 시간, 시도 횟수. 길이와 만료 시간은 ASVS 5.0 6.5.4, 6.5.5 에 수치가 있고 (`controls.md` SEC-06), 시도 횟수 수치는 문서에 없어 프로젝트가 정한다. 고른 값은 `templates/security-architecture.md` 5절에 적는다
- 세션 유휴 및 절대 만료 시간 (`controls.md` SEC-10)
- AI 기능이 있으면 모델이 부를 수 있는 도구와 그 권한

## 4. 시작 단계에서 만들어 두는 것 (나중에 고치기 어려운 것)
- 입구 계층 (인증, 인가, 입력 스키마, 속도 제한) 을 첫 기능보다 먼저 만든다 `[일반]`
- DB 소유자 조회와 제약 (유니크, 외래 키, 음수 방지) 을 표 설계 때 넣는다 `[일반]`
- 설정 모듈과 `.gitignore`, 비밀 탐지 훅을 첫 커밋 전에 둔다 (원문: pre-commit 훅 단계 비밀 탐지)
- 공격 시나리오 시험표 (`attack-tests.md`) 를 기능이 생길 때마다 한 줄씩 더한다 `[일반]`
