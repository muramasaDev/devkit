---
name: kickoff
description: Use when starting a new project, or when preparing an existing repository for AI-assisted development, to set up the project from the first step (CLAUDE.md, .gitignore, git init, security checklist, which skills apply). 새 프로젝트 시작, 프로젝트 세팅, 킥오프, 초기 설정, 처음부터 세팅, 개발 시작 전 준비 요청에 사용.
---

# Kickoff (프로젝트 시작 세팅)

프로젝트를 시작하는 첫 단계에서 작업 규칙과 보안과 화면 기준을 한 번에 정한다. 이미 있는 파일은 덮어쓰지 않는다.

## 순서
1. **현재 상태 확인**: git 저장소인지, `CLAUDE.md`, `.gitignore`, `docs/` 가 이미 있는지 확인한다. 있는 파일은 건드리지 않고 차이만 제안한다
2. **프로젝트 성격 질문** (객관식으로 한 번에 묻는다. 이미 답이 보이는 항목은 묻지 않는다)
   - 종류: 웹 또는 앱 화면 / 서버 또는 API / 데이터 처리 스크립트 / 라이브러리 또는 CLI
   - 다루는 데이터: 개인정보 또는 기밀 있음 / 없음
   - 기능: 로그인, 파일 업로드, DB 사용, 관리자 화면, 결제 또는 쿠폰, 인증번호, AI 기능 중 해당하는 것 (복수, 4개씩 나눠 묻는다)
   - 배포: 인터넷 / 폐쇄망 / 아직 미정
3. **파일 만들기** (없는 것만)
   - `CLAUDE.md`: `templates/CLAUDE.md` 의 빈칸을 2번 답으로 채운다
   - `.gitignore`: `templates/gitignore` 기본형 (이미 있으면 빠진 줄만 제안)
   - `docs/security/security-report.md`: 로그인, 업로드, DB, 개인정보, 관리자 화면, 결제, AI 중 하나라도 해당하면 `securecoding` 스킬의 `templates/security-report.md` 를 복사한다
   - `docs/security/security-architecture.md`: 위와 같은 조건이면 `securecoding` 스킬의 `templates/security-architecture.md` 를 복사하고, 2번 답으로 알 수 있는 칸 (역할, 결제 여부, AI 여부) 만 채운다. 나머지는 `미정`. 기능 코드보다 먼저 사용자와 이 문서를 채우도록 안내한다
   - 저장소가 아니면 `git init` 만 한다. 원격 저장소 연결과 push 는 사용자가 요청할 때만 한다
4. **적용할 스킬 안내**
   - 화면이 있으면 `uiuxpatterns` (설계 전에 모드 A, 구현 후에 모드 C)
   - 로그인, 업로드, DB, API, 의존성, 관리자 화면, 결제, 쿠폰, 인증번호, AI 기능이 있으면 `securecoding` (설계 단계는 첫 기능 코드 전, 공격 시나리오 시험은 기능 구현 후)
5. **선택 도구 제안** (`references/tools.md`). 프로젝트 성격에 맞는 것만 이름과 용도 한 줄로 알려 주고, 사용자가 승인한 것만 공식 설치 명령을 실행한다. 승인 없이 설치하지 않는다
6. **마무리 보고**: 만든 파일, 건너뛴 파일과 이유, 다음 할 일 한 줄

## 지키는 것
- 질문은 객관식, 한 번에 4개 이하
- 설치형 도구는 에이전트 설정을 바꿀 수 있으므로 설치 전에 어떤 설정이 바뀌는지 알려 준다
- 값을 추측해서 채우지 않는다. 모르면 `미정` 으로 둔다
