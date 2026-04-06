# Data Model

## 핵심 계층
Issue
-> Metric
-> KPI Fact

## 필수 규칙
- KPI Fact는 metric_id로만 연결
- issue direct link 금지
- source_document_id / source_page 필수
- version_no / is_latest 고려

## 주요 테이블
- master
- metric_master
- kpi_fact
- document
- vector_chunk
- scoring_result
- audit_log
