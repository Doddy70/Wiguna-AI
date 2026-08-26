# CANONICAL LEARNING REVIEW GATE
## Final Review Mechanism for Pak Ferdy Learning Candidates

**Date:** 2026-08-25
**Task:** TASK 07 — Build Canonical Learning Review Gate
**Mode:** READ-ONLY / No Production Mutation
**Status:** READY FOR USE

---

## PURPOSE

Mechanism ini memastikan hanya learning yang terverifikasi dari Pak Ferdy
yang boleh menjadi production knowledge.

```
CANDIDATE
    ↓
EVIDENCE CHECK
    ↓
SCOPE CHECK
    ↓
CAPABILITY CHECK
    ↓
CONFLICT CHECK
    ↓
HUMAN REVIEW
    ↓
APPROVAL / REJECTION
    ↓
PROMOTION GATE
```

---

## 1. REVIEW CRITERIA

### 1.1 Evidence Requirement

 Setiap candidate wajib memiliki evidence yang dapat ditelusuri.

**Evidence Priority:**

| Priority | Type | Description |
|----------|------|-------------|
| 1 | **Pak Ferdy Conversation** | Actual WhatsApp transcript or export |
| 2 | **Approved Business Knowledge** | KB document, promo material, official doc |
| 3 | **Production Documentation** | System message, code, workflow definition |

**Evidence Check:**

| Evidence Found | Status |
|---------------|--------|
| Pak Ferdy conversation transcript | ✅ EVIDENCE_FOUND |
| KB/production docs match statement | ✅ EVIDENCE_FOUND |
| Only architecture doc (no source) | ⚠️ PARTIAL |
| LLM-generated statement | ❌ NO_EVIDENCE |

### 1.2 Source-Faithfulness Check

Candidate hanya boleh berasal dari:

- ✅ Ajaran/explanation langsung dari Pak Ferdy
- ✅ Business fact yang disetujui Pak Ferdy
- ✅ Knowledge yang ada di official KB

Tidak boleh:

- ❌ LLM inference tanpa source
- ❌ Generalization tanpa konfirmasi
- ❌ "Probably true" tanpa evidence

### 1.3 Completeness Check

Setiap candidate harus memiliki:

| Field | Required | Description |
|-------|----------|-------------|
| `id` | ✅ | Unique identifier (LC-XXX) |
| `original_statement` | ✅ | Exact quote from Pak Ferdy |
| `classification` | ✅ | Type: KNOWLEDGE, POLICY, etc. |
| `topic` | ✅ | Short summary (2-5 words) |
| `trigger` | ✅ | What triggers this learning |
| `context` | ✅ | Background context |
| `condition` | ✅ | Precondition for rule |
| `principle` | ✅ | Core teaching/rule |
| `recommended_action` | ✅ | What agent should do |
| `exceptions` | ⚠️ | When NOT to apply (if any) |
| `scope` | ✅ | Boundaries of applicability |
| `confidence` | ✅ | Score 0.0-1.0 |
| `status` | ✅ | Current state |
| `source_evidence` | ✅ | Reference to source |

---

## 2. SCOPE REQUIREMENT

### 2.1 Scope Definition

Setiap candidate harus menjelaskan:

| Dimension | Question | Example |
|-----------|----------|---------|
| **WHO** | Berlaku untuk siapa? | Toyota Fortuner, all diesel vehicles |
| **WHEN** | Kapan berlaku? | Oil capacity > 7L, after fill fails |
| **WHERE** | Konteks apa? | Stock query, AC service |
| **HOW** | Kondisi apa? | After standard treatment |
| **NOT** | Kapan TIDAK berlaku? | First-time service, minor issues |

### 2.2 Scope Validation

| Scope | Assessment |
|-------|------------|
| Specific (vehicle type, condition) | ✅ ACCEPTABLE |
| General (all vehicles, all cases) | ⚠️ REVIEW |
| Undefined | ❌ REJECT |

### 2.3 Overgeneralization Detection

**Warning Signs:**

```
❌ "Always do X"
   → Pak Ferdy may have said "for this case, do X"

❌ "All vehicles should Y"
   → Pak Ferdy may have said "Fortuner should Y"

❌ "Never say Z"
   → Check if this is context-specific
```

**Safe Generalization:**

```
✅ "For stock queries where KB has no data,
   acknowledge limitation and offer follow-up"
   → Applies to specific context

✅ "For AC issues persisting after treatment,
   escalate to human"
   → Applies to specific condition
```

---

## 3. CAPABILITY REQUIREMENT

### 3.1 Capability vs Policy Distinction

| Type | Definition | Example |
|------|------------|---------|
| **BUSINESS RULE** | How business operates | "Stok tidak ada di KB ≠ stok habis" |
| **SYSTEM CAPABILITY** | What system can do | Live inventory check, booking tool |
| **BEHAVIORAL POLICY** | How agent should act | "Acknowledge limitation, follow up" |

### 3.2 Capability Check

Untuk setiap `recommended_action`, verifikasi:

**Question:** Apakah ini promise tentang apa yang sistem BISA LAKUKAN?

| Action | Capability? | Policy? |
|--------|-------------|---------|
| "Handoff to technical team" | ❌ No system handoff | ✅ Behavioral |
| "Cek gudang untuk stok" | ❌ No live inventory | ✅ Behavioral |
| "Booking slot check" | ❌ No booking tool | ❌ WRONG |
| "Acknowledge limitation" | N/A | ✅ Behavioral |
| "Offer human follow-up" | N/A | ✅ Behavioral |

### 3.3 Capability Mapping

| Candidate Says | System Can Do | Correct Phrasing |
|---------------|---------------|------------------|
| "Cek stok" | ❌ NO | "Minna akan bantu konfirmasi" |
| "Handoff to teknisi" | ❌ NO | "Minna akan eskalasi ke tim" |
| "Booking check" | ❌ NO | "Silakan booking via WhatsApp" |
| "Live inventory" | ❌ NO | "Admin akan bantu cek" |

### 3.4 Action Revision

If candidate promises capability that doesn't exist:

```yaml
recommended_action: |
  Original: "Cek gudang untuk verifikasi stok"
  
  Problem: No live inventory tool
  
  Revised: |
    "Acknowledge limitation.
     Offer to follow up via human agent.
     
     DO NOT claim to have live inventory check."
```

---

## 4. CONFLICT DETECTION

### 4.1 Conflict Types

| Type | Description | Example |
|------|-------------|---------|
| **DIRECT** | Contradicts existing KB | New rule says X, KB says Y |
| **PARTIAL** | Overlaps with existing KB | New scope different from KB |
| **CAPABILITY** | Promises unavailable capability | Says can do X, system can't |
| **PRIORITY** | Conflicts with another candidate | A says do X, B says do Y |

### 4.2 Conflict Check

Before approval, verify:

```
1. Does this contradict existing RAG content?
   → Check KB documents

2. Does this conflict with another candidate?
   → Check all candidates

3. Does this promise unavailable capability?
   → Check system capabilities

4. Does this override production rules?
   → Check PAK-FERDY-CHANNEL-IMPLEMENTATION.md
```

### 4.3 Resolution

| Conflict | Resolution |
|----------|------------|
| Direct contradiction | REJECT candidate |
| Partial overlap | MERGE candidates or narrow scope |
| Capability mismatch | REVISE recommended_action |
| Priority conflict | PAK FERDY DECIDES |

---

## 5. APPROVAL WORKFLOW

### 5.1 State Machine

```
CANDIDATE
    │
    ├──[Evidence Check]──► NEEDS_REVISION (no evidence)
    │
    ├──[Scope Check]──► NEEDS_REVISION (scope unclear)
    │
    ├──[Capability Check]──► NEEDS_REVISION (capability issue)
    │
    ├──[Conflict Check]──► NEEDS_REVISION (conflict found)
    │
    └──[All Checks Pass]──► READY_FOR_REVIEW
                                │
                                ├──[PAK FERDY APPROVES]──► APPROVED
                                │                                     │
                                ├──[PAK FERDY REJECTS]──► REJECTED
                                │
                                └──[NEEDS MODIFICATION]──► NEEDS_REVISION
```

### 5.2 State Definitions

| State | Description | Who Sets |
|-------|-------------|----------|
| **CANDIDATE** | Initial extraction | System/Agent |
| **NEEDS_REVISION** | Missing evidence, scope, or capability | Review Gate |
| **READY_FOR_REVIEW** | Passed all automated checks | Review Gate |
| **APPROVED** | Pak Ferdy approved | Human (Pak Ferdy) |
| **REJECTED** | Pak Ferdy rejected | Human (Pak Ferdy) |
| **MERGED** | Combined with another candidate | Human |
| **DEPLOYED** | Promoted to production | System |

### 5.3 Review Checklist

**For Human Reviewer:**

```
Candidate: [ID] - [Topic]
Classification: [Type]
Confidence: [Score]

▢ Evidence verified
  - Source conversation found
  - Statement matches source
  
▢ Scope verified
  - WHO defined
  - WHEN defined
  - NOT applicable defined
  
▢ Capability verified
  - recommended_action achievable
  - No false capability promise
  
▢ No conflicts
  - Does not contradict existing KB
  - Does not conflict with other candidates
  
▢ Appropriately generalized
  - Not overgeneralized
  - Specific enough to be actionable

Decision:
[ ] APPROVED
[ ] REJECTED
[ ] NEEDS REVISION

Notes: _______________
Reviewer: _______________
Date: _______________
```

---

## 6. PROMOTION GATE

### 6.1 Promotion Requirements

Before any candidate can be promoted:

| Requirement | Status | Verified By |
|------------|--------|-------------|
| APPROVED status | Required | Human (Pak Ferdy) |
| Evidence on file | Required | System |
| Scope documented | Required | System |
| Capability verified | Required | System |
| No conflicts | Required | System |
| Destination confirmed | Required | Human |

### 6.2 Promotion Gate Checklist

```
PROMOTION GATE
│
├──▢ Candidate status = APPROVED
│   └── Verified by: System
│
├──▢ Evidence attached
│   └── File reference: _______________
│
├──▢ Scope documented
│   └── Scope: _______________
│
├──▢ Capability verified
│   └── System can do: _______________
│   └── recommended_action: _______________
│
├──▢ No active conflicts
│   └── Conflicting candidates: _______________
│
├──▢ Destination confirmed
│   └── Target: RAG / Skill / Workflow / Tool
│   └── Target name: _______________
│
└──▢ Human approval
    └── Approver: _______________
    └── Date: _______________

RESULT: [ ] PASS / [ ] FAIL
```

### 6.3 Destination Promotion

| Destination | Promotion Method |
|-------------|------------------|
| **RAG** | Create QA pairs → Import to collection |
| **SKILL** | Create skill → Deploy to registry |
| **WORKFLOW** | Add rule to workflow → Deploy |
| **TOOL** | Create tool spec → Implement (future) |

---

## 7. CURRENT CANDIDATE STATUS

### 7.1 Registry

| ID | Topic | Classification | Confidence | Status | Destination | Evidence |
|----|-------|----------------|------------|--------|-------------|----------|
| LC-001 | AC Major Service Escalation | ESCALATION_RULE | 0.95 | **NEEDS_REVISION** | WORKFLOW | PARTIAL |
| LC-002 | Reset AC Service Scope | KNOWLEDGE | 0.95 | **READY_FOR_REVIEW** | RAG | ✅ VERIFIED |
| LC-003 | Fortuner Oil Selection | BUSINESS_RECOMMENDATION | 0.90 | **REJECTED** | — | ❌ NONE |
| LC-004 | Stock Query Response | RESPONSE_POLICY | 0.95 | **NEEDS_REVISION** | SKILL | ✅ VERIFIED |

### 7.2 Status Reasons

**LC-001 — NEEDS_REVISION:**
- Source conversation not verified
- Handoff capability unclear
- Required: Find conversation OR REJECT

**LC-002 — READY_FOR_REVIEW:**
- Source verified via KB docs
- Knowledge factual, not policy
- Ready for Pak Ferdy approval

**LC-003 — REJECTED:**
- LLM-generated, NOT from Pak Ferdy
- "10W-30 diesel first" not in KB
- No source conversation found

**LC-004 — NEEDS_REVISION:**
- Source verified (production code)
- BUT: "Cek gudang" implies live capability
- Required: Revise recommended_action

---

## 8. CANONICAL RULE

### The One Rule

```
CONVERSATION
    ≠
AUTOMATIC KNOWLEDGE

CONVERSATION
    ↓
EVIDENCE
    ↓
VERIFICATION
    ↓
REVIEW
    ↓
APPROVAL
    ↓
KNOWLEDGE
```

### Forbidden Paths

```
❌ LLM inference → Candidate
❌ "Probably true" → Business rule
❌ "Seems right" → Production knowledge
❌ CANDIDATE → DEPLOYED (without review)
```

### Allowed Paths

```
✅ Conversation → Candidate → Evidence → Review → APPROVED → DEPLOYED

✅ Conversation → Candidate → NO EVIDENCE → REJECTED

✅ Candidate → NEEDS_REVISION → Source found → READY → APPROVED → DEPLOYED
```

---

## 9. IMPLEMENTATION NOTES

### 9.1 For Next Agent

When reviewing new candidates:

1. **Find the source**
   - Actual WhatsApp conversation
   - KB document
   - Production code

2. **Verify the statement**
   - Quote matches source
   - Not LLM-generated

3. **Check the scope**
   - WHO, WHEN, NOT defined
   - Not overgeneralized

4. **Verify capability**
   - recommended_action achievable
   - No false promises

5. **Check conflicts**
   - No KB contradiction
   - No candidate conflict

6. **Human review**
   - Present to Pak Ferdy
   - Get explicit approval

### 9.2 Anti-Patterns

**❌ WRONG:**
```
"This seems like a good rule based on common sense"
→ Create candidate
→ Approve
→ Deploy
```

**✅ CORRECT:**
```
"Pak Ferdy said X in conversation Y"
→ Verify conversation exists
→ Create candidate with evidence
→ Review with Pak Ferdy
→ Approve/Reject
→ Deploy if approved
```

---

## 10. ARTIFACTS

| Artifact | Purpose |
|----------|---------|
| `CANONICAL-LEARNING-REVIEW.md` | This gate document |
| `PAK-FERDY-LEARNING-REVIEW.md` | Source-faithfulness review |
| `PAK-FERDY-LEARNING-REVISIONS.md` | Required corrections |
| `LEARNING-CANDIDATES.md` | Candidate registry |

---

## CHANGELOG

| Date | Author | Change |
|------|--------|--------|
| 2026-08-25 | Claude | Initial canonical review gate |

---

**END OF GATE DOCUMENT**
