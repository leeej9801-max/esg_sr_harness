# Core Principles (절대 설계 기준)

이 문서는 ESG 보고서 자동 생성 시스템의 **최상위 제약 조건**이다.

이 문서의 규칙은 모든 설계, 코드, 데이터 모델, AI 생성 로직보다 우선한다.

---

# 1. Layer 분리 원칙 (절대 불변)

이 시스템은 아래 5개 레이어를 절대 혼합하지 않는다.

- Master = 정의
- Dictionary = 탐지
- Fact = 데이터
- Evidence = 근거
- AI = 생성

## 금지

- Master에 키워드 저장 금지
- Dictionary에 KPI 구조 저장 금지
- KPI를 Evidence처럼 사용 금지
- Evidence 없이 AI 생성 금지

---

# 2. KPI 구조 원칙 (가장 중요)

모든 정량 데이터는 반드시 아래 구조를 따른다.

Issue
→ Metric
→ KPI Fact

## 금지

- KPI를 issue_id에 직접 연결
- Metric 없이 KPI 생성
- KPI를 단일 값으로 취급

## 이유

1 Issue는 여러 Metric을 가진다  
1 Metric은 여러 KPI를 가진다

---

# 3. Evidence 기반 생성 원칙

보고서 문장은 반드시 아래 구조를 따른다.

Issue
→ Sub-topic
→ Evidence + KPI
→ Narrative

## 금지

- Issue만으로 문장 생성
- Evidence 없는 생성
- 근거 없는 수치 생성

---

# 4. Scoring 원칙

점수는 반드시 다음 구조를 따른다.

## 구조

Final Score = Signal + Fact + Judgment

## 분리

- Impact Score
- Financial Score

## 금지

- 단일 점수 모델
- 뉴스 = 점수
- KPI만으로 점수 계산

---

# 5. 데이터 무결성 원칙

- 모든 KPI는 source_document_id를 가진다
- 모든 Evidence는 source_page를 가진다
- 모든 Score는 trace 가능해야 한다

---

# 6. 보안 및 데이터 분리 원칙

- 모든 테이블은 company_id를 가진다
- 회사 간 데이터 접근 절대 금지
- audit_log 필수

---

# 7. 1차 개발 우선순위

다음 4개가 완성되지 않으면 고도화 금지

1. KPI 정확성
2. Evidence 품질
3. Sub-topic 구조
4. Prompt 통제 설계

---

# 8. 고도화 금지 영역 (Phase 1)

다음은 1차 단계에서 구현하지 않는다

- Graph DB
- 멀티 에이전트 병렬 구조
- 자동 의사결정 시스템

---

# 9. 변경 규칙

이 문서의 변경은 반드시 Decision Log로 기록한다.

- D-xxx 생성
- 영향 범위 명시
- 팀 합의 필요