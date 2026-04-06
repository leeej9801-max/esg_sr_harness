# esg-report-platform

ESG 데이터 기반 보고서 자동 생성 플랫폼용 작업환경 스캐폴드입니다.

이 저장소는 단순 코드 저장소가 아니라, 다음을 위한 하네스 저장소입니다.

- 설계 기준 고정
- 작업 요청 / 검토 / 결정 기록
- 역할 프롬프트 기반 작업 흐름
- MCP 연결을 위한 문서/ID/정책 구조 준비
- CI/CD 기본 파이프라인 유지

## 이 버전에서 포함하는 것
- Harness Engineering
- MCP 연결 준비 문서
- CI / CD 기본 워크플로

## 이 버전에서 제외하는 것
- 에러 로그 자동화
- git hook 강제
- PR 본문 에러 강제 검사

## 루트 구조
- docs/: 기준 문서
- templates/: 작업 템플릿
- prompts/: 역할 프롬프트
- tasks/: 작업 요청
- reviews/: 검토 기록
- decisions/: 결정 로그
- automation/: 경량 자동화
- mcp/: MCP 연결 정책
- .github/workflows/: CI/CD
- src/: 향후 실제 코드 위치

## 시작 순서
1. GitHub 저장소 생성
2. 이 구조 업로드
3. docs/00_core_principles.md 팀 합의
4. decisions/D-001 ~ D-005 검토
5. 첫 작업은 tasks/T-001 형식으로 시작
6. MCP는 GitHub read-only → Docs → PostgreSQL read-only 순으로 연결
