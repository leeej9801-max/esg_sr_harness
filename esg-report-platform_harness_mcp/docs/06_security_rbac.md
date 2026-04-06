# Security / RBAC

## 기본 원칙
- 모든 핵심 트랜잭션 테이블에 company_id
- 필요 시 project_id 추가
- Document access는 presigned URL
- audit_log 필수

## Role
- platform_admin
- consultant_admin
- consultant_user
- client_admin
- client_viewer
- auditor_viewer

## 보안 모델
- 데이터 격리 모델
- 접근 모델
- 변경 추적 모델
