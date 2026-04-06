# MCP 연결 계획

## 목표
읽기 전용 MCP를 먼저 연결한다.

## 연결 대상
1. GitHub MCP
2. Workspace Docs MCP
3. PostgreSQL Read-only MCP

## 현재 전략
- 문서 / 결정 / 작업 / 리뷰는 GitHub와 Docs MCP로 읽기
- 데이터 모델과 스키마는 PostgreSQL read-only MCP로 조회
- write 권한은 열지 않음

## Phase 4 이후
- 검증 에이전트 분리
- 문서화 에이전트 분리
- 병렬 검증 구조 검토
