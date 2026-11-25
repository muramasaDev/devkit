---
name: kickoff
description: 새 프로젝트 시작, 프로젝트 세팅, 킥오프, 초기 설정, 개발 시작 전 준비, 기존 저장소 준비 요청에 사용. CLAUDE.md, .gitignore, git init, 보안 문서, 적용할 스킬을 정한다. 프로젝트 초기 세팅은 kickoff, 개별 코드의 보안 검토는 securecoding.
---

# Kickoff (프로젝트 시작 세팅)

프로젝트를 시작하는 첫 단계에서 작업 규칙과 보안과 화면 기준을 한 번에 정한다. 이미 있는 파일은 덮어쓰지 않는다. 이 스킬은 `securecoding`, `uiuxpatterns` 와 같은 폴더(`skills/`)에 있어야 하며, 보안 문서 템플릿은 `securecoding` 것을 쓴다.

## 조건 정의 (조건은 여기서만 정의하고 아래 단계와 템플릿이 이 이름으로 참조한다)
- **화면 있음**: 2번의 종류가 '웹 또는 앱 화면'
- **보안 대상**: 다음 중 하나 이상
  - 기능: 로그인, 파일 업로드, DB 사용, 관리자 화면, 결제 또는 쿠폰, 인증번호, AI 기능
  - 종류가 '서버 또는 API'
  - 다루는 데이터가 '개인정보 또는 기밀 있음'
  - 매니페스트(`package.json`, `pyproject.toml`, `pom.xml` 등)에 외부 의존성 항목이 있음
- **보안 문서 생성됨**: 보안 대상이고 3번에서 `docs/security/` 문서를 실제로 만들었거나 이미 있음

## 순서
1. **현재 상태 확인**: git 저장소인지, `CLAUDE.md`, `.gitignore`, `.gitattributes`, `docs/` 가 이미 있는지, 매니페스트가 있는지 확인한다. 있는 파일은 건드리지 않고 차이만 제안한다
2. **프로젝트 성격 질문** (`AskUserQuestion` 도구로 객관식. 한 번 호출에 4문항까지이므로 두 번에 나눈다. 이미 답이 보이는 항목은 묻지 않고 빈 자리는 다음 항목으로 채운다)
   - 1차 (4문항)
     - 종류: 웹 또는 앱 화면 / 서버 또는 API / 데이터 처리 스크립트 / 라이브러리 또는 CLI
     - 다루는 데이터: 개인정보 또는 기밀 있음 / 없음
     - 배포: 인터넷 / 폐쇄망 / 아직 미정
     - 기능 A (복수 선택): 로그인 / 파일 업로드 / DB 사용 / 관리자 화면
   - 2차
     - 기능 B (복수 선택, 3개): 결제 또는 쿠폰 / 인증번호 / AI 기능
     - 스택 (복수 선택, 매니페스트로 알 수 없을 때만): Node / Python / Java / .NET. 그 밖(Go 등)은 기타 입력으로 받는다
   - 기능 A 와 B 모두 선택이 없으면 기능은 '없음'
3. **파일 만들기** (없는 것만. 아래 순서를 지킨다)
   1. 저장소가 아니면 `git init` 만 한다. 원격 저장소 연결과 push 는 사용자가 요청할 때만 한다
   2. `.gitignore`: `templates/gitignore` 의 `# [기본]` 블록과, 스택 답(또는 매니페스트)에 해당하는 스택 블록(`# [Node]`, `# [Python]`, `# [Java]`, `# [.NET]`, `# [Go]`)만 복사한다. 이미 있으면 빠진 줄만 제안한다
   3. `.gitattributes`: `templates/gitattributes` 를 복사한다. `*.sh` 가 없고 리눅스 또는 컨테이너 실행 계획도 없으면 `*.sh` 줄과 앞 주석을 지운다
   4. 보안 문서: **보안 대상**이면 kickoff 폴더 기준 상대 경로 `../securecoding/templates/security-report.md` 와 `../securecoding/templates/security-architecture.md` 가 있는지 확인한다
      - 있으면 각각 `docs/security/security-report.md`, `docs/security/security-architecture.md` 로 복사한다. `security-architecture.md` 는 2번 답으로 알 수 있는 칸(역할, 결제 여부, AI 여부)만 채우고 나머지는 `미정`. 기능 코드보다 먼저 사용자와 이 문서를 채우도록 안내한다
      - 없으면 마무리 보고에 '`securecoding` 미설치' 로 적고 이 단계를 건너뛴다 (**보안 문서 생성됨** 이 아님)
   5. `CLAUDE.md`: `templates/CLAUDE.md.tmpl` 로 만든다 (아래 '`CLAUDE.md` 채우는 법'). `.gitignore` 와 보안 문서 결과가 필요하므로 마지막에 만든다
4. **적용할 스킬 안내**
   - **화면 있음**이면 `uiuxpatterns` (설계 전에 모드 A, 구현 후에 모드 C)
   - **보안 대상**이면 `securecoding` (설계 단계는 첫 기능 코드 전, 공격 시나리오 시험은 기능 구현 후). 미설치면 안내하지 않고 3번 4항대로 보고
5. **선택 도구 제안** (`references/tools.md`). 프로젝트 성격에 맞는 것만 이름과 용도 한 줄로 알려 주고, 사용자가 승인한 것만 공식 설치 명령을 실행한다. 승인 없이 설치하지 않는다
   - 비밀 탐지 훅(gitleaks): 첫 커밋 전에 제안한다. 승인하면 `references/tools.md` 의 절차를 따른다
6. **생성 결과 확인** (보고 전에 실제로 실행한다)
   - `CLAUDE.md` 가 가리키는 경로(`docs/...` 등)가 모두 실제로 있는지 확인한다. 없는 경로가 있으면 그 줄을 지우거나 고친다
   - `CLAUDE.md` 에 `{` 로 시작하는 자리표시가 남아 있지 않은지 확인한다
   - `.gitignore` 에 `.env` 가 걸리는지 `git check-ignore .env` 로 확인한다. 걸리지 않으면 `.gitignore` 에 `.env` 줄 추가를 제안한다
7. **마무리 보고**: 만든 파일, 건너뛴 파일과 이유(예: '`securecoding` 미설치'), 6번 확인 결과, 다음 할 일 한 줄

## `CLAUDE.md` 채우는 법
- `{프로젝트 이름}`: 저장소 폴더 이름
- 종류, 다루는 데이터, 주요 기능, 배포: 2번 답 그대로. 기능은 고른 항목을 쉼표로 이어 쓰고 없으면 '없음'. 답이 없으면 `미정`
- 조건 줄: 줄 앞에 `{화면 있음일 때만}`, `{보안 대상일 때만}`, `{보안 문서 생성됨일 때만}`, `{.env 무시 확인됨일 때만}` 이 붙어 있다. 조건이 맞으면 접두 표시만 지우고 줄을 남기고, 맞지 않으면 줄 전체를 지운다
  - `.env 무시 확인됨`: 3번 2항 뒤 `git check-ignore .env` 가 성공(종료 코드 0)했을 때만
- `{명령}` (시험, 빌드): 매니페스트에서 찾는다. 코드는 읽지 않고, 찾지 못하면 `미정`
  - `package.json`: `scripts` 의 `test`, `build` 항목. 락 파일에 맞는 실행기(`npm run`, `pnpm`, `yarn`)로 적는다
  - `pyproject.toml`, `requirements.txt`: `pytest` 설정 또는 `tests/` 가 있으면 시험 `pytest`. 빌드는 `pyproject.toml` 의 build 설정이 있을 때만 `python -m build`
  - `Makefile`: `test`, `build` 대상이 있으면 `make test`, `make build`
  - `pom.xml`: `mvn test`, `mvn package`. `build.gradle`: `gradle test`, `gradle build`
  - `*.sln` 또는 `*.csproj`: `dotnet test`, `dotnet build`. `go.mod`: `go test ./...`, `go build ./...`. `Cargo.toml`: `cargo test`, `cargo build`
- 메모 칸: 비워 둔다 (템플릿의 안내 주석만 남긴다)
- 기존 저장소에 `CLAUDE.md` 가 이미 있으면(내장 `/init` 결과 포함) 그것을 기준으로 쓰고 덮어쓰지 않는다. 템플릿의 작업 규칙 중 빠진 줄만 제안한다. `CLAUDE.md` 가 없는 기존 저장소는 코드 구조와 명령 정리를 `/init` 에 맡길지 사용자에게 먼저 묻는다. kickoff 는 작업 규칙, `.gitignore`, `.gitattributes`, 보안 문서만 다룬다

## 지키는 것
- 질문은 객관식, 한 번 호출에 4문항 이하
- 설치형 도구는 에이전트 설정을 바꿀 수 있으므로 설치 전에 어떤 설정이 바뀌는지 알려 준다
- 값을 추측해서 채우지 않는다. 모르면 `미정` 으로 둔다
