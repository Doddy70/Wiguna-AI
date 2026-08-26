# WIGUNA Learning Candidates

Learning candidates yang di-extract dari conversation Pak Ferdy.

---

## Candidate Format

```yaml
id: LC-XXX
source_conversation: "Date/Session reference"
original_statement: >
  "Original quote from Pak Ferdy..."
classification: KNOWLEDGE | DECISION_KNOWLEDGE | RESPONSE_POLICY |
                ESCALATION_RULE | BUSINESS_RECOMMENDATION | SKILL |
                TOOL_REQUIREMENT | EXAMPLE_ONLY | TEMPORARY_GUIDANCE
topic: "Short Topic Name"
trigger: "Customer query pattern or condition"
context: "Background context"
condition: "Precondition"
principle: >
  Normalized teaching/rule
recommended_action: >
  What agent should do
exceptions:
  - "Exception 1"
  - "Exception 2"
scope: "Vehicle type, service, or general"
confidence: 0.0-1.0
status: CANDIDATE | NEEDS_REVISION | READY_FOR_REVIEW | APPROVED | REJECTED | MERGED | DEPLOYED
destination: RAG | SKILL | WORKFLOW | TOOL | NONE
created: "YYYY-MM-DD"
```

---

## Classification → Destination Mapping

| Classification | Destination | Processing |
|----------------|-------------|------------|
| KNOWLEDGE | RAG | Create QA pairs |
| DECISION_KNOWLEDGE | RAG | Create decision rule |
| RESPONSE_POLICY | SKILL | Create behavior skill |
| ESCALATION_RULE | WORKFLOW | Create escalation workflow |
| BUSINESS_RECOMMENDATION | RAG | Add to service collection |
| SKILL | SKILL | Create skill definition |
| TOOL_REQUIREMENT | TOOL | Create tool specification |
| EXAMPLE_ONLY | NONE | Do not promote |
| TEMPORARY_GUIDANCE | NONE | Session context only |

---

## Extracted Candidates

### LC-001: AC Major Service Escalation

```yaml
id: LC-001
source_conversation: "2026-08-25 WhatsApp Session"
original_statement: >
  "Kalau AC bocor atau freon berkurang terus setelah diisi
  atau tetap bermasalah setelah penggantian part, itu jatuhnya
  servis besar AC dan harus diarahkan ke tim teknikal atau
  handoff ke human supaya tidak salah diagnosis."
classification: ESCALATION_RULE
topic: "AC Major Service Escalation"
trigger: >
  Customer reports: AC bocor, freon cepat habis,
  AC tidak dingin setelah isi freon,
  AC bermasalah setelah part replacement
context: >
  AC issues that persist after initial treatment
  indicate more serious problem requiring technical assessment
condition: >
  AC problem persists AFTER freon fill
  OR
  AC problem persists AFTER part replacement
principle: >
  When AC issues persist after standard treatment,
  escalate to technical team to avoid misdiagnosis.
recommended_action: >
  Handoff to technical team or human agent.
  Explain: "Ini perlu pemeriksaan lebih lanjut oleh tim teknikal
  untuk diagnosis yang tepat."
exceptions:
  - "First-time AC service request (not yet treated)"
  - "Minor cooling issues (recommend reset AC first)"
scope: >
  All vehicles with persistent AC issues
  after standard treatment
confidence: 0.95
status: NEEDS_REVISION
destination: WORKFLOW
created: "2026-08-25"
```

**Review Status:** NEEDS_REVISION (2026-08-25)
- Source conversation PARTIAL - listed in architecture doc, no transcript found
- Handoff capability NOT verified
- Scope may be too broad
- Required: Find conversation or REJECT

**Review Notes:**
- [ ] Source conversation verified
- [ ] Handoff mechanism exists
- [ ] Scope appropriate
- **Recommendation:** NEEDS_REVISION → Find conversation OR REJECT

---

### LC-002: Reset AC Service Scope

```yaml
id: LC-002
source_conversation: "2026-08-25 WhatsApp Session"
original_statement: >
  "Reset AC mencakup flushing system, vacuum + leak test,
  pembersihan blower AC, pembersihan evaporator menggunakan
  endoscope tanpa bongkar dashboard, pengecekan filter AC,
  pembersihan condenser AC, penggantian oli compressor,
  penggantian freon AC, ozone sterilization."
classification: KNOWLEDGE
topic: "Reset AC Service Scope"
trigger: >
  Customer asks: "Reset AC apa saja?"
  "Reset AC termasuk apa?"
context: >
  Reset AC is comprehensive service, not just "reset"
condition: >
  Customer inquiring about AC reset service
principle: >
  Reset AC includes:
  1. Flushing system
  2. Vacuum + leak test
  3. Blower AC cleaning
  4. Evaporator cleaning (endoscope, no dashboard disassembly)
  5. Filter AC check
  6. Condenser AC cleaning
  7. Compressor oil replacement
  8. Freon AC replacement
  9. Ozone sterilization
recommended_action: >
  Provide comprehensive scope when explaining Reset AC.
  Emphasize it's not just "reset" but full treatment.
exceptions: []
scope: >
  Reset AC service (non-EV vehicles)
confidence: 0.95
status: READY_FOR_REVIEW
destination: RAG
created: "2026-08-25"
```

**Review Status:** READY_FOR_REVIEW (2026-08-25)
- Source verified: KB docs + PAK-FERDY-LEARNING.md
- Knowledge factual and complete
- No capability risk
- Ready for Pak Ferdy approval

**Review Notes:**
- [x] Detailed service scope definition ✅
- [x] Can be converted to QA pairs ✅
- [x] Useful for customer education ✅
- **Recommendation:** READY_FOR_REVIEW → Present to Pak Ferdy for approval

---

### LC-003: GASPOL Oil Brand Correction

```yaml
id: LC-003
source_conversation: >
  WAHA API [16:57:56] - 2026-08-25
original_statement: >
  "Saya ingin mengajari bahwa paket gaspol tdk menggunakan oli Eneos.
  Paket Gaspol menggunakan oli Shield atau Aspira.
  Jika ada customer yg ingin menggunakan oli Eneos,
  bisa di tawarkan paket oli eneos."
classification: KNOWLEDGE
topic: "GASPOL Oil Brand Correction"
trigger: >
  Agent mentions GASPOL uses ENEOS oil
  Customer asks "GASPOL pakai ENEOS?"
context: >
  Agent initially said GASPOL uses ENEOS oil.
  Pak Ferdy corrected this.
  Agent acknowledged correction.
condition: >
  Customer asks about oil brand in GASPOL package
  OR
  Agent mentions ENEOS in GASPOL context
principle: >
  GASPOL package uses SHIELD or ASPIRA oil, NOT ENEOS.
  If customer specifically wants ENEOS, offer ENEOS package separately.
  Do NOT claim GASPOL contains ENEOS.
recommended_action: >
  If customer asks "GASPOL pakai ENEOS?":
  - CORRECT: "Paket GASPOL menggunakan oli Shield/Aspira."
  - WRONG: "GASPOL pakai ENEOS."
  
  If customer wants ENEOS:
  - Offer ENEOS package separately.
exceptions:
  - None — this is factual correction.
scope: >
  GASPOL package
  ENEOS package queries
confidence: 0.95
status: READY_FOR_REVIEW
destination: RAG
created: "2026-08-25"
updated: "2026-08-25"
```

**Source Evidence:** WAHA API [16:57:56] - ACTUAL PAK FERDY CORRECTION

**Verification:**
- [x] Actual conversation found ✅
- [x] Pak Ferdy's exact words preserved ✅
- [x] Agent acknowledged ✅

**Review Notes:**
- [x] Source conversation VERIFIED via WAHA API
- [x] Pak Ferdy corrected Agent's wrong statement
- [x] Agent acknowledged correctly
- **Recommendation:** READY_FOR_REVIEW → Present to Pak Ferdy for approval

---

### LC-003 (OLD - Fortuner Oil - SUPERSEDED)

> **NOTE:** Previous LC-003 "Fortuner Oil Selection" is SUPERSEDED by new extraction.
> The WAHA conversation shows GASPOL oil brand correction, not Fortuner recommendation.
> Old candidate REJECTED. New candidate READY_FOR_REVIEW.

---

### LC-004: Stock Query Response Policy

```yaml
id: LC-004
source_conversation: "2026-08-25 WhatsApp Session"
original_statement: >
  "Jangan langsung bilang stok tidak ada kalau datanya
  tidak ditemukan."
classification: RESPONSE_POLICY
topic: "Stock Query Response"
trigger: >
  Customer asks about stock/availability
  and data is not found in Knowledge Base
context: >
  Knowledge Base contains price list, not inventory.
  Absence of data does not mean absence of stock.
condition: >
  Customer asks: "Ada?", "Stok?", "Tersedia?"
  AND
  Knowledge Base has no data
principle: >
  Absence of Knowledge Base evidence must NOT be
  interpreted as product unavailability.
  Always acknowledge limitation.
recommended_action: >
  DO NOT say: "Stok tidak ada", "Tidak tersedia",
  "Barang tidak ada"
  INSTEAD say: "Mohon maaf, untuk informasi ini Minna cek dulu"
  OR
  "Data belum tersedia, Minna bantu konfirmasi ke gudang"
exceptions: []
scope: >
  All stock/availability queries
confidence: 0.95
status: NEEDS_REVISION
destination: SKILL
created: "2026-08-25"
```

**Review Status:** NEEDS_REVISION (2026-08-25)
- Source verified: Production code in PAK-FERDY-CHANNEL-IMPLEMENTATION.md ✅
- Principle correct ✅
- BUT: "Cek gudang" implies live inventory capability ❌
- Required: Revise recommended_action to clarify as behavioral guidance

**Review Notes:**
- [x] Source verified ✅
- [x] Principle correct ✅
- [ ] recommended_action revision needed ❌
- **Recommendation:** NEEDS_REVISION → Revise to clarify "cek gudang" as human follow-up, not live tool

---

### LC-005: Early Closing Prevention

```yaml
id: LC-005
source_conversation: "[PENDING - SOURCE EVIDENCE REQUIRED]"
original_statement: >
  "[PENDING - Pak Ferdy's actual feedback about early closing]
  User stated: Agent terlalu cepat menawarkan booking.
  Customer belum menyatakan keluhan dan solusi sudah cocok.
  Screenshot evidence requested."
classification: RESPONSE_POLICY
topic: "Early Closing Prevention"
trigger: >
  Agent menawarkan solusi/booking sebelum customer memahami dan setuju
context: >
  Customer memberikan koreksi, bertanya, atau meminta penjelasan tambahan
  setelah Agent menawarkan solusi
condition: >
  Customer masih:
  - mengoreksi informasi
  - bertanya tentang detail
  - menyatakan solusi belum lengkap
  - meminta penjelasan tambahan
  - belum yakin
principle: >
  Agent JANGAN menawarkan booking/closing terlalu cepat.
  Pastikan customer memahami dan setuju dengan solusi.
  Jika customer masih bertanya/koreksi, kembali ke clarification.
recommended_action: >
  IF customer masih memberikan koreksi ATAU bertanya:
  - JANGAN closing/booking
  - KEMBALI ke clarification
  - Jawab pertanyaan
  - Konfirmasi pemahaman customer
  
  IF customer menyatakan setuju/mengerti:
  - BARU tawarkan booking/closing
  
  Example CORRECT:
  Customer: "Reset AC itu termasuk apa saja?"
  Agent: [jelaskan cakupan lengkap]
  Customer: "Oh gitu, sudah paham"
  Agent: "Mau booking kapan?"
  
  Example WRONG:
  Customer: "Reset AC itu termasuk apa saja?"
  Agent: [jelaskan singkat] "Mau booking?"
  Customer: [belum selesai memahami]
exceptions:
  - Safety-critical issues (segera ke bengkel)
  - Customer explicitly asks to book
  - Customer sudah menyatakan paham dan setuju
scope: >
  Semua layanan
confidence: 0.80
status: NEEDS_REVISION
destination: SKILL
created: "2026-08-25"
```

**Review Status:** NEEDS_REVISION (2026-08-25)
- Source conversation NOT found in codebase ❌
- Screenshot NOT found in codebase ❌
- Principle sounds reasonable but cannot verify without source

**Review Notes:**
- [ ] Source conversation provided ❌
- [ ] Screenshot provided ❌
- [ ] Scope verified (Pak Ferdy-specific or general?) ❌
- **Recommendation:** NEEDS_REVISION → Provide source evidence before approval

---

## Status Summary

| ID | Topic | Classification | Confidence | Status | Destination |
|----|-------|----------------|------------|--------|-------------|
| LC-001 | AC Major Service Escalation | ESCALATION_RULE | 0.95 | NEEDS_REVISION | WORKFLOW |
| LC-002 | Reset AC Service Scope | KNOWLEDGE | 0.95 | READY_FOR_REVIEW | RAG |
| LC-003 | Fortuner Oil Selection | BUSINESS_RECOMMENDATION | 0.90 | REJECTED | NONE |
| LC-004 | Stock Query Response | RESPONSE_POLICY | 0.95 | NEEDS_REVISION | SKILL |
| LC-005 | Early Closing Prevention | RESPONSE_POLICY | 0.80 | NEEDS_REVISION |
| **LC-006** | **Discovery Before Booking** | **RESPONSE_POLICY** | **0.95** | **READY_FOR_REVIEW** |
| LC-007 | GASPOL Oil Brand | KNOWLEDGE | 0.95 | READY_FOR_REVIEW | SKILL |

---

## Status Legend

| Status | Description | Next Action |
|--------|-------------|-------------|
| CANDIDATE | Initial extraction | Verify source |
| NEEDS_REVISION | Issues found | Revise and re-check |
| READY_FOR_REVIEW | Passed automated checks | Present to Pak Ferdy |
| APPROVED | Pak Ferdy approved | Promote to production |
| REJECTED | Pak Ferdy / Gate rejected | Discard |
| MERGED | Combined with other | Create new candidate |
| DEPLOYED | Promoted to production | Monitor |

---

## Review Process

### For Each Candidate, Verify:

1. **Accuracy** — Does this match Pak Ferdy's intent?
2. **Completeness** — Are all conditions and exceptions captured?
3. **Clarity** — Is the principle clear and actionable?
4. **Scope** — Are boundaries properly defined?
5. **Conflicts** — Does this conflict with existing knowledge?
6. **Priority** — Is this high priority for implementation?

### Review Decision Options

| Decision | Action |
|----------|--------|
| **APPROVED** | Promote to TGO Web |
| **REJECTED** | Discard with reason |
| **MODIFIED** | Update and re-review |
| **MERGED** | Combine with related candidates |

### Review Form

```markdown
## Review: LC-XXX

### Candidate Summary
- **Topic:** [topic]
- **Classification:** [classification]
- **Confidence:** [confidence score]

### Review Questions

1. **Accuracy**
   - [ ] Matches Pak Ferdy's intent
   - [ ] Original statement preserved
   - Notes: _______________

2. **Completeness**
   - [ ] All conditions captured
   - [ ] Exceptions identified
   - [ ] Scope defined
   - Notes: _______________

3. **Conflicts**
   - [ ] No conflict with existing knowledge
   - [ ] Compatible with other candidates
   - Notes: _______________

4. **Priority**
   - [ ] High (implement soon)
   - [ ] Medium (implement later)
   - [ ] Low (optional)

### Decision

- [ ] **APPROVED** — Promote to TGO Web
- [ ] **REJECTED** — Reason: _______________
- [ ] **MODIFIED** — Changes needed: _______________
- [ ] **MERGED** — Merge with: _______________

### Reviewer
Name: _______________
Date: _______________
```

---

## TGO Web Promotion Plan

> **UPDATED:** 2026-08-25 after Task 06 Review

### Priority 1: RESPONSE_POLICY (LC-004) — ON HOLD

**Current State:** NEEDS_REVISION
**Issue:** "Cek gudang" implies live inventory capability
**Action Required:** Revise recommended_action to clarify as behavioral guidance

**Steps:**
1. Revise recommended_action: "follow up via human agent" not "cek gudang"
2. Present to Pak Ferdy for approval
3. Create `wiguna-stock-response-policy` skill after approval

### Priority 2: KNOWLEDGE (LC-002) — READY FOR REVIEW

**Current State:** READY_FOR_REVIEW
**Source:** Verified via KB docs
**Action Required:** Present to Pak Ferdy for approval

**Steps:**
1. Present to Pak Ferdy for approval
2. Create QA pairs from candidate
3. Add to existing RESET AC MOBIL collection
4. Verify retrieval works

### Priority 3: ESCALATION_RULE (LC-001) — ON HOLD

**Current State:** NEEDS_REVISION
**Issue:** Source conversation not found, handoff capability unclear
**Action Required:** Find conversation or REJECT

**Steps:**
1. Search for actual Pak Ferdy conversation about AC escalation
2. If no conversation found → REJECT
3. If conversation found → Verify handoff mechanism
4. After verification → Present to Pak Ferdy

### REJECTED: BUSINESS_RECOMMENDATION (LC-003)

**Current State:** REJECTED
**Reason:** LLM-generated, NOT from Pak Ferdy
**No source evidence:** "10W-30 diesel first" not in KB

**Note:** If Pak Ferdy can provide conversation, re-evaluate.

---

## Next Steps

### Before Human Review

- [ ] Revise LC-004 recommended_action (remove "cek gudang")
- [ ] LC-001: Search for conversation or REJECT
- [ ] LC-003: No action (REJECTED - no source)

### Immediate (Present to Pak Ferdy)

- [ ] LC-002: Present for approval → READY_FOR_REVIEW
- [ ] LC-004: Present after revision → READY_FOR_REVIEW
- [ ] LC-001: Present after verification → READY_FOR_REVIEW

### After Pak Ferdy Approval

- [ ] Implement approved candidates
- [ ] Monitor for conflicts
- [ ] Document in production
- [ ] Monitor effectiveness

### Long-term

- [ ] Set up automated extraction from conversations
- [ ] Build TGO Web integration for candidate review
- [ ] Establish feedback loop for candidate quality

---

## Pipeline Information

**Pipeline Documentation:** [LEARNING-CANDIDATE-PIPELINE.md](../../docs/onboarding/LEARNING-CANDIDATE-PIPELINE.md)

**Pipeline Code:** [pipeline/learning_pipeline.py](../../Wiguna-AI/pipeline/learning_pipeline.py)

**Usage:**
```python
from pipeline.learning_pipeline import LearningPipeline

pipeline = LearningPipeline()
candidates = pipeline.get_candidates(status="CANDIDATE")
for c in candidates:
    print(f"{c.id}: {c.topic} ({c.classification})")
```

---

## References

- [PAK-FERDY-CHANNEL-IMPLEMENTATION.md](../../docs/onboarding/PAK-FERDY-CHANNEL-IMPLEMENTATION.md)
- [RAG-KNOWLEDGE-BASE-IMPLEMENTATION.md](../../docs/onboarding/RAG-KNOWLEDGE-BASE-IMPLEMENTATION.md)
- [PAK-FERDY-LEARNING.md](../../Wiguna-AI/architecture/PAK-FERDY-LEARNING.md)
- [LEARNING-CANDIDATE-PIPELINE.md](../../docs/onboarding/LEARNING-CANDIDATE-PIPELINE.md)

---

## Changelog

| Date | Author | Change |
|------|--------|--------|
| 2026-08-25 | Claude | Enhanced format with full context preservation |
| 2026-08-25 | Claude | Initial extraction (4 candidates) |

---

**END OF DOCUMENT**

---

### LC-006: Discovery Before Booking (NEW)

```yaml
id: LC-006
source_conversation: >
  WAHA [17:11:03] - 2026-08-25
original_statement: >
  "Terima kasih Minna. Tp saya ingin ajarkan anda bahwa kalau ada konsumen
  yg menanyakan servis rutin, anda harus tanya lengkap dulu datanya dan keluhannya.
  
  Type mobil:
  Tahun pembuatan:
  Automatic atau manual:
  Keluhannya:
  
  Setelah itu anda harus cari informasi mengenai cc mobilnya via google atau referensi
  chat sebelumnya. Lalu tentukan oli rekomendasinya dan kapasitasnya sebelum
  menawarkan paket servis yaitu, mulai dr urutan:
  1. Paket siaga
  2. Paket Ajag
  3. Paket Gaspol
  4. Paket Ijig (s/d ban R16)
  Kalau konsumen sudah memilih paket yg tepat, baru di tanyakan untuk data bookingnya."
classification: RESPONSE_POLICY
topic: "Discovery Before Service Offering"
trigger: >
  Customer asks about routine service
  Customer says "mau servis rutin"
  Customer asks about package recommendation
condition: >
  Before offering any service package
  Before recommending any oil/service package
  Before asking for booking data
principle: >
  JANGAN menawarkan paket booking sebelum informasi lengkap.
  
  WAJIB TANYAKAN DULU:
  1. Type mobil
  2. Tahun pembuatan
  3. Automatic atau manual
  4. Keluhan kendaraan
  
  SETELAH informasi lengkap:
  - Cari tahu CC mesin via google/referensi
  - Tentukan oli yang tepat
  - BARU tawarkan paket
  
  URUTAN PAKET YANG BENAR:
  1. Paket Siaga
  2. Paket Ajag
  3. Paket Gaspol
  4. Paket Ijig (s/d ban R16)
  
  Kalau customer sudah memilih paket yang tepat, BARU tanyakan data booking.
recommended_action: >
  PADA SAAT customer menyebut "servis rutin":
  1. JANGAN langsung tawarkan paket.
  2. Tanya informasi kendaraan:
     - Type mobil apa?
     - Tahun berapa?
     - Automatic atau manual?
     - Keluhannya apa?
  3. Cari tahu CC mesin via google/referensi chat.
  4. Tentukan oli yang tepat.
  5. Urutkan paket: Siaga > Ajag > Gaspol > Ijig.
  6. Pilih paket yang sesuai.
  7. Kalau customer sudah paham dan memilih paket, BARU tanyakan data booking.
  
  SALAH:
  Langsung tawarkan paket tanpa tanya kendaraan.
  Langsung tanya booking sebelum customer memilih paket.
  
  BENAR:
  Tanya kendaraan → Cari info → Pilih paket → Tanya booking.
exceptions:
  - Safety-critical issues (langsung arahkan ke bengkel)
  - Customer sudah memberikan semua info di awal
scope: >
  Servis rutin queries
  Paket recommendation
  Semua layanan Bengkel Wiguna
confidence: 0.95
status: READY_FOR_REVIEW
destination: SKILL
created: "2026-08-25"
source_evidence: >
  WAHA [17:11:03]
```

**Source Evidence:** WAHA conversation [17:11:03] - Pak Ferdy's actual teaching

---

### LC-007: GASPOL Oil Brand Correction (NEW)

```yaml
id: LC-007
source_conversation: >
  WAHA [16:57:56] - 2026-08-25
original_statement: >
  "Saya ingin mengajari bahwa paket gaspol tdk menggunakan oli Eneos.
  Paket Gaspol menggunakan oli Shield atau Aspira. Jika ada customer yg ingin
  menggunakan oli Eneos, bisa di tawarkan paket oli Eneos."
classification: KNOWLEDGE
topic: "GASPOL Oil Brand Correction"
trigger: >
  Customer asks about GASPOL package oil type
  Customer asks "pakai Eneos?"
  Agent mentions GASPOL uses ENEOS
condition: >
  GASPOL Hero Package discussion
  Oil brand question
  Service package recommendation context
principle: >
  Paket GASPOL menggunakan oli SHIELD atau ASPIRA, BUKAN ENEOS.
  
  Jika customer menanyakan atau menginginkan ENEOS dalam konteks GASPOL:
  - Benarkan bahwa GASPOL menggunakan Shield/Aspira
  - Jika customer insist ENEOS, tawarkan paket ENEOS terpisah
  - Jangan claim GASPOL mengandung ENEOS
recommended_action: >
  SALAH: "Paket GASPOL pakai ENEOS"
  BENAR: "Paket GASPOL pakai Shield/Aspira"
  
  Jika customer ingin ENEOS dalam GASPOL:
  - Jelaskan GASPOL pakai Shield/Aspira
  - Tawarkan paket ENEOS terpisah jika ada
exceptions: []
scope: >
  GASPOL Hero Package
  Semua conversation tentang GASPOL
  Oil brand questions
confidence: 0.95
status: READY_FOR_REVIEW
destination: RAG
created: "2026-08-25"
source_evidence: >
  WAHA [16:57:56] - Pak Ferdy's correction
```

**Source Evidence:** WAHA conversation [16:57:56] - Pak Ferdy correction

