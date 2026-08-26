# PAK FERDY LEARNING REVISIONS
## Required Corrections for Candidates

**Date:** 2026-08-25
**Task:** TASK 06 — Review & Validate Learning Candidates
**Mode:** READ-ONLY / No Production Mutation

---

## REVISION SUMMARY

| ID | Topic | Problem | Priority |
|----|-------|---------|----------|
| LC-001 | AC Major Service Escalation | Source unverified, handoff capability unclear | HIGH |
| LC-003 | Fortuner Oil Selection | LLM-generated, NOT from Pak Ferdy | CRITICAL |
| LC-004 | Stock Query Response | Implies live inventory capability | HIGH |

---

## LC-001: AC Major Service Escalation

### Original

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
status: CANDIDATE
destination: WORKFLOW
```

### Problem

1. **Source conversation NOT verified**
   - No actual WhatsApp transcript found
   - Statement listed in architecture doc as example
   - Cannot confirm if from Pak Ferdy or LLM-generated

2. **Handoff capability NOT confirmed**
   - Candidate promises "Handoff to technical team"
   - No evidence that routing to technical team exists
   - Current system only transfers to human via WhatsApp

3. **Scope may be too broad**
   - "All vehicles" may not match Pak Ferdy's intent
   - May be specific case discussion, not general rule

### Evidence

```
Source searched:
- Wiguna-AI/architecture/PAK-FERDY-LEARNING.md
- docs/onboarding/PAK-FERDY-CHANNEL-IMPLEMENTATION.md
- docs/knowledge/03-tag-standard.md ("servis besar" exists)

NOT FOUND:
- Actual WhatsApp conversation transcript
- Confirmation of handoff mechanism
- Scope verification
```

### Recommended Revision

**Option A: If conversation found**
```yaml
recommended_action: >
  Escalate to human agent for technical assessment.
  Explain that case requires professional diagnosis.
  
  Note: "Technical team handoff" means human agent review,
  NOT automated routing to a separate agent.
```

**Option B: If no conversation found**
```
REJECT this candidate.

Reason: No source conversation evidence.
Cannot verify if teaching is from Pak Ferdy.
```

### Reason

The candidate claims to be from Pak Ferdy, but:
1. No conversation transcript found
2. Cannot verify scope
3. Cannot verify capability

---

## LC-003: Fortuner Oil Selection

### Original

```yaml
id: LC-003
source_conversation: "2026-08-25 WhatsApp Session"
original_statement: >
  "Untuk Toyota Fortuner yang kapasitas olinya di atas 7 liter,
  rekomendasikan paket oli 10W-30 diesel terlebih dahulu,
  setelah itu alternatif 15W-40 dengan tambahan 1 liter oli
  sesuai kebutuhannya."
classification: BUSINESS_RECOMMENDATION
topic: "Fortuner Oil Selection"
trigger: >
  Customer asks about oil for Toyota Fortuner
  or vehicle with >7L oil capacity
condition: >
  Vehicle is Toyota Fortuner
  OR
  Oil capacity > 7 liters
principle: >
  For Fortuner with >7L oil capacity:
  - PRIMARY: 10W-30 Diesel package
  - ALTERNATIVE: 15W-40 with +1L additional oil
recommended_action: >
  Recommend 10W-30 Diesel first.
  Offer 15W-40 + 1L as alternative.
exceptions:
  - "Diesel vehicle → use diesel-specific oil"
  - "Specific manufacturer recommendation takes priority"
scope: >
  Toyota Fortuner
  Vehicles with >7L oil capacity
confidence: 0.90
status: CANDIDATE
destination: RAG
```

### Problem

**CRITICAL: This candidate appears to be LLM-GENERATED, NOT from Pak Ferdy.**

1. **No source conversation found**
   - No WhatsApp transcript about Fortuner oil
   - Statement only in architecture doc (as example)

2. **Specific recommendation NOT in KB**
   - "10W-30 diesel FIRST" does NOT exist in KB
   - KB shows both options but no priority order
   - KB states: "Untuk kendaraan premium...admin akan membantu memberikan penyesuaian harga"

3. **LLM likely generated the priority order**
   - The KB documents show:
     - ENEOS Diesel 10W-30 (8 Liter)
     - ENEOS Diesel 15W-40 (7 Liter)
   - But does NOT say which to recommend FIRST

### Evidence

```
KB documents searched:
- promo perawatan oli.md
- docs/knowledge-base/KB_PAKET_OLI_MESIN_KOMPLIT.md
- docs/architecture/PHASE-1-NATIVE-TGO-KNOWLEDGE-INVENTORY.md

FOUND:
- Fortuner is listed as compatible vehicle ✅
- ENEOS Diesel packages exist ✅
- "Admin akan membantu penyesuaian harga" ✅

NOT FOUND:
- Priority recommendation "10W-30 diesel first" ❌
- Specific "7 liter" threshold ❌
- Alternative "15W-40 + 1L" ❌

CONCLUSION:
The specific recommendation is LLM-GENERATED.
```

### Recommended Revision

**REJECT this candidate.**

```yaml
status: REJECTED
notes: >
  No source conversation found.
  Specific recommendation "10W-30 diesel first" not in KB.
  Appears to be LLM-generated, not from Pak Ferdy.
  
  If Pak Ferdy actually taught this:
  - Provide actual conversation transcript
  - Verify the specific recommendation
  - Then re-create candidate with source evidence
```

### Reason

This candidate violates the source-faithfulness principle:
1. Cannot verify source conversation exists
2. Specific recommendation not in any KB document
3. LLM likely generated the priority order

**Do NOT promote without source verification.**

---

## LC-004: Stock Query Response

### Original

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
status: CANDIDATE
destination: SKILL
```

### Problem

1. **Source is verified** ✅
   - Production code in PAK-FERDY-CHANNEL-IMPLEMENTATION.md
   - System message contains this rule

2. **Principle is correct** ✅
   - Matches production system message

3. **BUT: "Cek gudang" implies live capability** ❌
   - Candidate suggests "konfirmasi ke gudang"
   - No live inventory tool exists
   - Agent cannot actually check warehouse

### Evidence

```
Production source:
docs/onboarding/PAK-FERDY-CHANNEL-IMPLEMENTATION.md
  Rule 4: "Mohon maaf Minna cek dulu ke bagian gudang"

PROBLEM:
- "Cek gudang" implies live inventory check
- No inventory tool in current system
- Agent cannot verify warehouse stock

REFS:
- WORKFLOWS_OTOMOTIF.md mentions "inventory.check_parts()"
- BUT: This is NOT confirmed as active capability
- No evidence of live inventory integration
```

### Recommended Revision

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
  "Barang tidak ada", "Tidak ada stok"
  
  INSTEAD say one of:
  - "Mohon maaf, untuk informasi ini Minna cek dulu ya Pak."
  - "Minna akan bantu konfirmasi untuk ketersediaan produk tersebut."
  
  Note: "Cek/konfirmasi" means follow up via human agent.
  It does NOT mean live inventory tool is available.
  The agent acknowledges limitation and promises human follow-up.
exceptions: []
scope: >
  All stock/availability queries
confidence: 0.95
status: CANDIDATE
destination: SKILL
```

### Reason

The revision:
1. **Removes implication of live capability**
   - "Cek gudang" removed
   - Replaced with "follow up via human agent"

2. **Preserves behavioral guidance**
   - Still teaches correct response
   - Still encourages acknowledgment

3. **Makes system promise explicit**
   - "Follow up" not "live check"
   - Agent acknowledges limitation

---

## ACTION ITEMS

### LC-001
- [ ] Find actual conversation transcript
- [ ] Verify handoff mechanism exists
- [ ] Clarify scope (specific vs general)
- [ ] OR: Reject if no conversation found

### LC-003
- [ ] **CRITICAL: Find conversation OR REJECT**
- [ ] If conversation found, verify exact recommendation
- [ ] If no conversation, mark as REJECTED

### LC-004
- [ ] Revise `recommended_action`
- [ ] Remove "cek gudang" implication
- [ ] Clarify as "human follow-up"
- [ ] Re-present to Pak Ferdy for review

---

## REVISED STATUS

| ID | Original Status | Required Action | After Revision |
|----|-----------------|-----------------|----------------|
| LC-001 | CANDIDATE | Verify source + capability | PENDING |
| LC-002 | CANDIDATE | None (VALID) | READY FOR REVIEW |
| LC-003 | CANDIDATE | **REJECT** | REJECTED |
| LC-004 | CANDIDATE | Revise recommended_action | CANDIDATE |

---

## CHANGELOG

| Date | Author | Change |
|------|--------|--------|
| 2026-08-25 | Claude | Initial revision recommendations |

---

**END OF REVISIONS**
