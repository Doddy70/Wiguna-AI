# WIGUNA Learning Candidates

Learning candidates yang di-extract dari conversation Pak Ferdy.

---

## Candidate Format

```yaml
id: LC-001
source_conversation: "Pak Ferdy Teaching"
original_statement: "..."
normalized_principle: "..."
classification: KNOWLEDGE | WORKFLOW_RULE | ESCALATION_RULE | RESPONSE_POLICY | BUSINESS_RECOMMENDATION | SKILL | TOOL_REQUIREMENT | EXAMPLE_ONLY | TEMPORARY_GUIDANCE
scope: "..."
candidate_artifact: "..."
confidence: HIGH | MEDIUM | LOW
reason: "..."
status: CANDIDATE | APPROVED | REJECTED | MERGED
created: 2026-08-25
```

---

## Extracted Candidates

### LC-001: AC Service Escalation

```yaml
id: LC-001
original_statement: >
  "Kalau AC bocor atau freon berkurang terus setelah diisi
  atau tetap bermasalah setelah penggantian part, itu jatuhnya
  servis besar AC dan harus diarahkan ke tim teknikal atau
  handoff ke human supaya tidak salah diagnosis."
normalized_principle: >
  AC issues that persist after freon fill or part replacement
  must be escalated to technical team to avoid misdiagnosis.
classification: ESCALATION_RULE
scope: AC Service
candidate_artifact: >
  SKILL: AC_DIAGNOSIS_ESCALATION
  TRIGGER: AC bocor | freon berkurang
  CONDITION: after fill | after part replacement | still problematic
  ACTION: Handoff to technical team / human agent
confidence: HIGH
reason: >
  Direct teaching from Pak Ferdy about escalation criteria.
status: CANDIDATE
```

---

### LC-002: Reset AC Scope

```yaml
id: LC-002
original_statement: >
  "Reset AC mencakup flushing system, vacuum + leak test,
  pembersihan blower AC, pembersihan evaporator menggunakan
  endoscope tanpa bongkar dashboard, pengecekan filter AC,
  pembersihan condenser AC, penggantian oli compressor,
  penggantian freon AC, ozone sterilization."
normalized_principle: >
  Reset AC is a comprehensive service package including
  multiple cleaning, testing, and replacement procedures.
classification: KNOWLEDGE
scope: Reset AC Service
candidate_artifact: >
  KNOWLEDGE: RESET_AC_SCOPE
  ITEMS:
    - flushing system
    - vacuum + leak test
    - blower AC cleaning
    - evaporator cleaning (endoscope, no dashboard disassembly)
    - filter AC check
    - condenser AC cleaning
    - compressor oil replacement
    - freon AC replacement
    - ozone sterilization
  PRICE: Rp600.000 (non-EV)
confidence: HIGH
reason: >
  Detailed service scope definition from Pak Ferdy.
status: CANDIDATE
```

---

### LC-003: Fortuner Oil Recommendation

```yaml
id: LC-003
original_statement: >
  "Untuk Toyota Fortuner yang kapasitas olinya di atas 7 liter,
  rekomendasikan paket oli 10W-30 diesel terlebih dahulu,
  setelah itu alternatif 15W-40 dengan tambahan 1 liter oli
  sesuai kebutuhannya."
normalized_principle: >
  For Fortuner with >7L oil capacity, recommend 10W-30 diesel
  first, offer 15W-40 + 1L as alternative.
classification: BUSINESS_RECOMMENDATION
scope: Toyota Fortuner >7L oil capacity
candidate_artifact: >
  RULE: FORTUNER_OIL_SELECTION
  CONDITION: Toyota Fortuner, oil capacity >7L
  PRIMARY: 10W-30 Diesel
  ALTERNATIVE: 15W-40 + additional 1L oil
confidence: HIGH
reason: >
  Specific business recommendation with vehicle scope.
status: CANDIDATE
```

---

### LC-004: Response Policy - Stok

```yaml
id: LC-004
original_statement: >
  "Jangan langsung bilang stok tidak ada kalau datanya
  tidak ditemukan."
normalized_principle: >
  Absence of knowledge base evidence must not be interpreted
  as product unavailability.
classification: RESPONSE_POLICY
scope: Stock/Availability queries
candidate_artifact: >
  POLICY: STOCK_QUERY_RESPONSE
  IF: KB has no data about stock
  THEN: Do not say "stok tidak ada"
  INSTEAD: Acknowledge limitation, offer alternative
confidence: HIGH
reason: >
  Response behavior guidance from Pak Ferdy.
status: CANDIDATE
```

---

## Status Summary

| ID | Classification | Confidence | Status |
|----|----------------|------------|--------|
| LC-001 | ESCALATION_RULE | HIGH | CANDIDATE |
| LC-002 | KNOWLEDGE | HIGH | CANDIDATE |
| LC-003 | BUSINESS_RECOMMENDATION | HIGH | CANDIDATE |
| LC-004 | RESPONSE_POLICY | HIGH | CANDIDATE |

---

## Review Process

1. Candidates di-review oleh owner
2. Approved → promosi ke TGO Web
3. Rejected → discarded
4. Merged → combined dengan candidate lain

---

## Next Steps

- [ ] Review candidates dengan Pak Ferdy
- [ ] Approve/Reject setiap candidate
- [ ] Promote approved candidates ke TGO Web
