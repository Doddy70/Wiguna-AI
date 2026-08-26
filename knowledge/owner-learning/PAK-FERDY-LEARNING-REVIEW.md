# PAK FERDY LEARNING REVIEW
## Source-Faithfulness Check

**Date:** 2026-08-25
**Task:** TASK 06 — Review & Validate Learning Candidates
**Mode:** READ-ONLY / No Production Mutation
**Status:** VALIDATION COMPLETE

---

## EXECUTIVE SUMMARY

4 learning candidates di-review untuk validasi source-faithfulness. Berikut hasil ringkas:

| ID | Topic | Source Found | Supported | Action |
|----|-------|--------------|-----------|--------|
| LC-001 | AC Major Service Escalation | PARTIAL | PARTIAL | NEEDS_REVISION |
| LC-002 | Reset AC Service Scope | YES | YES | VALID_CANDIDATE |
| LC-003 | Fortuner Oil Selection | NO | NO | NEEDS_REVISION |
| LC-004 | Stock Query Response | YES | YES | VALID_CANDIDATE |

---

## VALIDATION MATRIX

| ID | Source Found | Directly Supported | Context Complete | Generalization Risk | Capability Risk | Destination | Status |
|----|--------------|-------------------|-----------------|---------------------|-----------------|-------------|--------|
| LC-001 | PARTIAL | PARTIAL | PARTIAL | MEDIUM | YES | WORKFLOW | NEEDS_REVISION |
| LC-002 | YES | YES | YES | LOW | NO | RAG | VALID_CANDIDATE |
| LC-003 | NO | NO | NO | HIGH | NO | RAG | NEEDS_REVISION |
| LC-004 | YES | YES | YES | LOW | YES | SKILL | NEEDS_REVISION |

---

## DETAILED REVIEW

### LC-001: AC Major Service Escalation

#### A. SOURCE FOUND?
**PARTIAL**

**Evidence:**
- Original statement quoted in `Wiguna-AI/architecture/PAK-FERDY-LEARNING.md`
- BUT: No actual WhatsApp conversation transcript found
- BUT: "servis besar" term found in `docs/knowledge/03-tag-standard.md`

**Source Documents Found:**
```
 Wiguna-AI/architecture/PAK-FERDY-LEARNING.md
   - Original: "Kalau AC bocor atau freon berkurang terus..."
   - Classification: ESCALATION_RULE
   - Listed as example in architecture doc
```

**Problem:** 
Statement listed as example in architecture doc, but no actual conversation evidence. Cannot verify if this is from real Pak Ferdy conversation or LLM-generated example.

#### B. DIRECTLY SUPPORTED?
**PARTIAL**

The concept of "AC escalation" exists in the system, but the specific statement cannot be verified.

#### C. CONTEXT PRESERVED?
**PARTIAL**

The candidate captures:
- Trigger: AC bocor / freon berkurang
- Condition: After fill / after part replacement
- Action: Handoff to technical team

BUT: Scope may be too broad. Pak Ferdy may have discussed a specific case, not a general rule.

#### D. GENERALIZATION RISK?
**MEDIUM**

The candidate applies to "ALL vehicles with persistent AC issues." This may be:
- Too broad if Pak Ferdy only discussed one specific case
- Correct if this is a general business rule

#### E. SYSTEM CAPABILITY RISK?
**YES**

**CRITICAL ISSUE:**
- The candidate promises "Handoff to technical team"
- BUT: No evidence that live handoff capability exists
- The system may only offer to "transfer to human" via WhatsApp
- Actual technical team routing NOT verified

#### F. DESTINATION CORRECT?
**WORKFLOW** (correct concept)

But workflow implementation requires:
1. Verify handoff capability exists
2. Define what "technical team" means
3. Define routing mechanism

#### RECOMMENDATION
**NEEDS_REVISION**

Problems:
1. Source conversation NOT verified
2. Handoff capability NOT confirmed
3. Scope may be too broad

Required:
- Find actual conversation transcript
- Verify handoff mechanism exists
- Clarify scope (specific case vs general rule)

---

### LC-002: Reset AC Service Scope

#### A. SOURCE FOUND?
**YES**

**Evidence:**
- Listed in `Wiguna-AI/architecture/PAK-FERDY-LEARNING.md` with original statement
- Confirmed in production knowledge base:
  - `docs/knowledge-base/promo-reset-ac-mobil.md`
  - `docs/production/KNOWLEDGE-BASE-RESET-AC.md`

**Source Documents:**
```
 Wiguna-AI/architecture/PAK-FERDY-LEARNING.md
   Original: "Reset AC mencakup flushing system, vacuum + leak test..."
 
 docs/knowledge-base/promo-reset-ac-mobil.md
   Service items match exactly:
   - Flushing AC
   - Vacuum dan Pengecekan Kebocoran
   - Penggantian Oli Kompresor
   - Pengisian Freon
   - Pembersihan Evaporator
   - Pembersihan Blower AC
   - Pembersihan Kondensor
   - Ozonizer Sterilization
```

#### B. DIRECTLY SUPPORTED?
**YES**

The original statement and the KB document match exactly.

#### C. CONTEXT PRESERVED?
**YES**

- Trigger: Customer asks about Reset AC scope
- Context: Comprehensive service, not just "reset"
- Items: All 9 services listed
- Scope: Non-EV vehicles, excludes European cars

#### D. GENERALIZATION RISK?
**LOW**

The knowledge is factual service scope, not a policy or rule. Generalization is appropriate.

#### E. SYSTEM CAPABILITY RISK?
**NO**

This is KNOWLEDGE (factual), not a capability promise. No risk.

#### F. DESTINATION CORRECT?
**RAG** ✅

Correct. This should become QA pairs in the Reset AC KB.

#### RECOMMENDATION
**VALID_CANDIDATE**

This candidate is ready for human review. The source is verified through:
1. Architecture doc with original statement
2. Production KB with matching content

**Ready for:** RAG QA pair creation

---

### LC-003: Fortuner Oil Selection

#### A. SOURCE FOUND?
**NO**

**Problem:** No actual WhatsApp conversation transcript found.

**Evidence Searched:**
- `Wiguna-AI/architecture/PAK-FERDY-LEARNING.md` — Statement listed
- `promo perawatan oli.md` — Fortuner mentioned as compatible vehicle
- `docs/knowledge-base/KB_PAKET_OLI_MESIN_KOMPLIT.md` — Standard packages listed
- `docs/architecture/PHASE-1-NATIVE-TGO-KNOWLEDGE-INVENTORY.md` — Fortuner in vehicle list

**BUT:**
- No conversation transcript showing Pak Ferdy teaching this
- The specific recommendation "10W-30 diesel FIRST" is NOT in KB
- The specific recommendation "15W-40 + 1L as alternative" is NOT in KB

#### B. DIRECTLY SUPPORTED?
**NO**

**Critical Finding:**
The candidate states:
> "rekomendasikan paket oli 10W-30 diesel terlebih dahulu"

This specific recommendation does NOT exist in any KB document. The KB shows:
- ENEOS Diesel 15W-40 (7 Liter)
- ENEOS Diesel 10W-30 (8 Liter)

But does NOT state which to recommend FIRST for Fortuner.

**This appears to be LLM-GENERATED, not from Pak Ferdy.**

#### C. CONTEXT PRESERVED?
**NO**

Without source conversation, cannot verify:
- Trigger conditions
- Scope limitations
- Exceptions

#### D. GENERALIZATION RISK?
**HIGH**

The candidate generalizes:
> "For Fortuner with >7L oil capacity: PRIMARY: 10W-30 Diesel"

This is a specific claim that:
1. May not be from Pak Ferdy
2. May only apply to specific Fortuner models/years
3. May only apply to specific use cases

#### E. SYSTEM CAPABILITY RISK?
**NO**

No capability promise. Just knowledge recommendation.

#### F. DESTINATION CORRECT?
**RAG** (if verified)

But destination cannot be confirmed until source is verified.

#### RECOMMENDATION
**NEEDS_REVISION**

**CRITICAL ISSUE:** This candidate appears to be LLM-generated, not from Pak Ferdy.

**Required Actions:**
1. Find actual conversation transcript with Pak Ferdy
2. If no transcript exists, this candidate must be REJECTED
3. If transcript exists, verify the exact recommendation

**Do NOT promote this candidate until source is verified.**

---

### LC-004: Stock Query Response

#### A. SOURCE FOUND?
**YES**

**STRONG EVIDENCE FOUND:**

Production code in `docs/onboarding/PAK-FERDY-CHANNEL-IMPLEMENTATION.md` contains the exact system message that implements this rule:

```python
def _get_pak_ferdy_system_message(original_system_message):
    pak_ferdy_instructions = """...
    ATURAN PENTING:
    
    2. KNOWLEDGE BASE = PRICE LIST, BUKAN INVENTORY/STOK
       - Knowledge Base adalah DAFTAR HARGA produk
       - Knowledge Base BUKAN sistem inventory/stok
       - "Tidak ditemukan di Knowledge Base" SAMA SEKALI TIDAK berarti "tidak ada stok"
    
    3. JANGAN MENYAMAKAN "TIDAK ADA DI KB" DENGAN "TIDAK ADA STOK"
       Dilarang mengatakan:
       - "Produknya tidak ada"
       - "Barangnya tidak ada"
       - "Tidak tersedia"
       - "Stok habis"
       ...
       Jika ragu: KATAKAN "Mohon maaf Minna cek dulu"
    """
```

**Source Documents:**
```
 docs/onboarding/PAK-FERDY-CHANNEL-IMPLEMENTATION.md
   - Section 6: Special System Message Behavior
   - Contains the exact rules that LC-004 captures
   - Production code evidence

 Wiguna-AI/architecture/PAK-FERDY-LEARNING.md
   - Original: "Jangan langsung bilang stok tidak ada kalau datanya tidak ditemukan."
   - Classification: RESPONSE_POLICY
```

#### B. DIRECTLY SUPPORTED?
**YES**

The candidate's principle matches the production system message exactly:
- "Absence of KB evidence must NOT be interpreted as product unavailability"
- Matches: "TIDAK ADA DI KB ≠ TIDAK ADA STOK"

#### C. CONTEXT PRESERVED?
**YES**

- Trigger: Customer asks about stock/availability
- Condition: KB has no data
- Principle: Do NOT say "stok tidak ada"
- Action: "Mohon maaf Minna cek dulu"

#### D. GENERALIZATION RISK?
**LOW**

The policy is clearly stated and appropriate for all customers.

#### E. SYSTEM CAPABILITY RISK?
**YES** ⚠️

**CRITICAL ISSUE:**

The candidate states:
> "INSTEAD say: ... 'Data belum tersedia, Minna bantu konfirmasi ke gudang'"

**Problem:**
1. "Cek gudang" implies live inventory capability
2. Production does NOT have a live inventory tool
3. The current system cannot actually check warehouse inventory

**From `PAK-FERDY-CHANNEL-IMPLEMENTATION.md`:**
> "Mohon maaf Minna cek dulu ke bagian gudang untuk memastikan..."

This is behavioral guidance (how to respond), NOT a capability promise.

**The candidate must distinguish:**
- ✅ CORRECT: "Acknowledge limitation, offer to check" (behavioral)
- ❌ WRONG: "Can check warehouse inventory" (capability promise)

#### F. DESTINATION CORRECT?
**SKILL** ✅ (correct concept)

But the skill must be written as behavioral guidance, NOT capability promise.

#### RECOMMENDATION
**NEEDS_REVISION**

**Issues:**
1. Source is verified ✅
2. Principle is correct ✅
3. BUT: "Cek gudang" may be interpreted as live capability ❌

**Required Revision:**
Change `recommended_action` from:
> "INSTEAD say: ... 'Data belum tersedia, Minna bantu konfirmasi ke gudang'"

To:
> "Acknowledge limitation and offer to follow up via human agent"

OR clarify that "cek gudang" is behavioral response, not live tool capability.

---

## SUMMARY

### VALID_CANDIDATE
| ID | Topic | Reason |
|----|-------|--------|
| LC-002 | Reset AC Service Scope | Source verified via KB docs, factual knowledge |

### NEEDS_REVISION
| ID | Topic | Reason | Action Required |
|----|-------|--------|-----------------|
| LC-001 | AC Major Service Escalation | Source partial, handoff capability unverified | Find conversation, verify handoff mechanism |
| LC-003 | Fortuner Oil Selection | LLM-generated (not from Pak Ferdy) | Find conversation OR REJECT |
| LC-004 | Stock Query Response | "Cek gudang" implies live capability | Clarify as behavioral guidance only |

### SOURCE_NOT_FOUND
| ID | Topic | Status |
|----|-------|--------|
| LC-003 | Fortuner Oil Selection | No conversation transcript found |

### REJECT
None (all candidates have potential if source is verified)

---

## REQUIRED ACTIONS

### Immediate (Before Human Review)

1. **LC-003 MUST BE ADDRESSED**
   - Find actual Pak Ferdy conversation about Fortuner oil
   - If no conversation exists, this candidate is REJECTED
   - The "10W-30 diesel first" recommendation is NOT in KB

2. **LC-004 REVISION**
   - Remove implication of live inventory capability
   - Rewrite as behavioral guidance only
   - "Follow up via human" not "cek gudang"

3. **LC-001 VERIFICATION**
   - Find actual conversation transcript
   - Verify handoff mechanism exists
   - Clarify scope (specific vs general)

### After Revision

- Present revised candidates to Pak Ferdy for human review
- DO NOT promote until Pak Ferdy approves

---

## ARTIFACTS

### Review Matrix
This document: `knowledge/owner-learning/PAK-FERDY-LEARNING-REVIEW.md`

### Revisions Required
See: `knowledge/owner-learning/PAK-FERDY-LEARNING-REVISIONS.md`

### Pipeline Documentation
See: `docs/onboarding/LEARNING-CANDIDATE-PIPELINE.md`

---

## CHANGELOG

| Date | Author | Change |
|------|--------|--------|
| 2026-08-25 | Claude | Initial source-faithfulness review |

---

**END OF REVIEW**

---

## LC-005: Early Closing Prevention

### A. SOURCE FOUND?
**NOT VERIFIED** ⚠️

**Task Input:**
- User stated: "Pak Ferdy memberikan feedback melalui conversation"
- User stated: "Screenshot menunjukkan Agent melakukan closing"
- User stated: "Customer masih memberikan correction"

**Evidence Searched:**
- ❌ No conversation transcript found
- ❌ No screenshot found in codebase
- ❌ No documented conversation in `WAHA/` or `conversation/` directories
- ❌ No documented feedback in `.remember/` logs

**Source Documents Searched:**
```
- docs/onboarding/PAK-FERDY-CHANNEL-IMPLEMENTATION.md (no evidence)
- Wiguna-AI/architecture/PAK-FERDY-LEARNING.md (no evidence)
- SKILLS/*/SKILL.md (no evidence of this specific feedback)
- .remember/ logs (no evidence)
```

**Problem:**
The user mentioned this is from Pak Ferdy's conversation and provided a screenshot, but:
1. No conversation transcript found in codebase
2. No screenshot found in codebase
3. Cannot verify the exact feedback without source

#### B. DIRECTLY SUPPORTED?
**CANNOT VERIFY** ⚠️

The principle sounds reasonable (don't close too early), but without the actual conversation or screenshot, I cannot verify:
- The exact wording Pak Ferdy used
- The specific context of the correction
- Whether this was one-time feedback or a general policy

#### C. CONTEXT PRESERVED?
**PARTIAL** ⚠️

The task describes:
- Problem: Agent terlalu cepat menawarkan booking
- Root cause: Customer belum menyatakan solusi sudah cocok
- Rule: Jangan closing jika customer masih koreksi/bertanya

**But without source evidence:**
- Cannot verify if this is Pak Ferdy-specific or general CS policy
- Cannot determine scope (all services? specific services?)
- Cannot determine exceptions

#### D. GENERALIZATION RISK?
**UNKNOWN** ⚠️

The task suggests this might be:
- A: khusus Pak Ferdy
- B: customer-service policy umum

**Without source evidence, cannot determine.**

The principle "don't close if customer is still asking questions" could be:
- Universal good CS practice
- Specific to Pak Ferdy's standards
- Context-dependent (some services may warrant faster closing)

#### E. SYSTEM CAPABILITY RISK?
**NO** ✅

This principle does NOT require:
- Workflow new
- Tool baru
- Database change
- Docker change
- Source code change

If implemented, it would be:
- Behavioral guidance in a Skill
- RESPONSE_POLICY type

#### F. DESTINATION CORRECT?
**SKILL** (if verified)

If source is found and principle is confirmed, destination would be:
- RESPONSE_POLICY
- Skill

---

### RECOMMENDATION
**NEEDS_REVISION**

**Issues:**
1. Source conversation NOT found ❌
2. Screenshot NOT found ❌
3. Cannot verify principle without source ❌

**Required Actions:**
1. **PROVIDE SOURCE EVIDENCE** — User must provide:
   - Actual conversation transcript
   - OR screenshot file
   - OR documented feedback

2. **VERIFY SCOPE** — If source provided:
   - Is this Pak Ferdy-specific or general?
   - What services does it apply to?
   - Are there exceptions?

3. **DRAFT PRINCIPLE** — After verification:
   - "Agent jangan closing/booking terlalu cepat"
   - "Sebelum booking, pastikan customer sudah memahami dan同意 solusi"

---

### PRELIMINARY PRINCIPLE (Pending Verification)

If source is provided and verified, the candidate would be:

```yaml
id: LC-005
source_conversation: "[PENDING - SOURCE NEEDED]"
original_statement: "[PENDING - PAK FERDY'S EXACT WORDS]"
classification: RESPONSE_POLICY
topic: "Early Closing Prevention"
trigger: >
  Customer masih bertanya, mengoreksi, atau meminta klarifikasi
context: >
  Agent menawarkan solusi, tapi customer belum menyatakan setuju
condition: >
  Customer memberikan koreksi ATAU bertanya ATAU meminta penjelasan tambahan
principle: >
  JANGAN melakukan booking/closing terlalu cepat.
  Pastikan customer sudah memahami dan同意 solusi yang ditawarkan.
recommended_action: >
  IF customer masih:
  - mengoreksi informasi
  - bertanya tentang detail
  - menyatakan solusi belum lengkap
  - meminta penjelasan tambahan
  THEN:
  - KEMBALI ke clarification
  - Jawab pertanyaan
  - Konfirmasi pemahaman
  - JANGAN closing/booking
exceptions:
  - Safety-critical issues (segera ke bengkel)
  - Customer explicitly asks to book
scope: >
  Semua layanan
confidence: 0.80
status: NEEDS_REVISION
destination: SKILL
```

---

## CHANGELOG

| Date | Author | Change |
|------|--------|--------|
| 2026-08-25 | Claude | Initial source-faithfulness review |
| 2026-08-25 | Claude | Added LC-005 (needs evidence) |
