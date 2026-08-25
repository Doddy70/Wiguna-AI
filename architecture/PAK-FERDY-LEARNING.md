# Pak Ferdy Learning Channel

## Concept

Pak Ferdy adalah **Human Supervisor / Teacher / Evaluator** untuk WIGUNA AI OS.

Channel ini digunakan untuk:
- Human teaching
- AI evaluation
- Owner correction
- Business knowledge capture
- Decision-rule capture
- Skill/behavior learning
- Workflow/escalation learning

---

## Learning Pipeline

```
PAK FERDY CONVERSATION
        ↓
LEARNING EXTRACTION
        ↓
CLASSIFICATION
        ↓
LEARNING CANDIDATE
        ↓
HUMAN REVIEW
        ↓
TGO WEB PROMOTION
```

---

## Classification Types

| Type | Description |
|------|-------------|
| **KNOWLEDGE** | Fakta bisnis, product knowledge |
| **WORKFLOW RULE** | Aturan alur kerja service |
| **ESCALATION RULE** | Kapan harus handover ke tim teknis |
| **RESPONSE POLICY** | Cara AI harus merespons |
| **BUSINESS RECOMMENDATION** | Rekomendasi bisnis spesifik |
| **SKILL** | Kemampuan/tindakan yang harus dilakukan |
| **TOOL REQUIREMENT** | Tool yang dibutuhkan |
| **EXAMPLE ONLY** | Contoh, bukan rule |
| **TEMPORARY GUIDANCE** | Guidance sementara |

---

## Example Extraction

### AC Escalation

**Original:** "Kalau AC bocor atau freon berkurang terus setelah diisi atau tetap bermasalah setelah penggantian part, itu jatuhnya servis besar AC dan harus diarahkan ke tim teknikal atau handoff ke human."

**Classification:** ESCALATION RULE

**Trigger:** AC bocor / freon berkurang / setelah pengisian/part replacement masih bermasalah

**Action:** Handoff ke tim teknis / human

---

### Fortuner Oli

**Original:** "Untuk Toyota Fortuner yang kapasitas olinya di atas 7 liter, rekomendasikan paket oli 10W-30 diesel terlebih dahulu, setelah itu alternatif 15W-40 dengan tambahan 1 liter oli."

**Classification:** BUSINESS RECOMMENDATION

**Scope:** Toyota Fortuner >7L oil capacity

**Rule:** 10W-30 diesel first, 15W-40 + 1L as alternative

---

### Response Behavior

**Original:** "Jangan langsung bilang stok tidak ada kalau datanya tidak ditemukan."

**Classification:** RESPONSE POLICY

**Rule:** Absence of KB evidence must not be interpreted as product unavailability

---

## Important

- Percakapan Pak Ferdy **TIDAK otomatis** menjadi production knowledge
- Tidak ada automatic promotion
- Extraction menghasilkan **LEARNING CANDIDATE** (READ-ONLY)
- Review diperlukan sebelum TGO Web promotion

---

## Status

- ✅ Extraction capability
- ✅ Classification capability
- ❌ NO production mutation
- ❌ NO automatic promotion
