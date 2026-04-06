# Architecture

## 서비스 레이어
- Frontend: React
- API: FastAPI
- DB: PostgreSQL
- Vector: pgvector
- Storage: S3
- Worker: Python Worker
- AI: LLM + RAG

## CI / CT / CD
- CI: GitHub Actions + pytest + lint
- CT: Python validation module + PostgreSQL constraints
- CD: GitHub Actions + Docker + EC2

## 운영 원칙
- 배치 처리: PDF parsing, Dictionary scan, embedding
- API 처리: 조회 / 수정 / 승인 / 생성 요청
- 검증은 데이터 흐름마다 수행
