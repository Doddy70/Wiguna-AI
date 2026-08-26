# Owner Learning

Dokumentasi untuk review dan validasi learning candidates dari Pak Ferdy.

---

## Directory Structure

```
Wiguna-AI/
└── knowledge/
    └── owner-learning/
        ├── CANONICAL-LEARNING-REVIEW.md          # Review gate mechanism
        ├── PAK-FERDY-LEARNING-REVIEW.md          # Source-faithfulness review
        ├── PAK-FERDY-LEARNING-REVISIONS.md        # Required corrections
        ├── PAK-FERDY-CONVERSATION-EXTRACTION.md  # Conversation corpus search
        ├── PRODUCTION-CONVERSATION-SOURCE.md       # Production message source trace
        └── README.md                              # This file
```

---

## CRITICAL FINDING: Conversation Source Found

**Production messages ARE available via WAHA API.**

| Component | Value |
|-----------|-------|
| Storage Service | WAHA (WhatsApp HTTP API) |
| Message Endpoint | `/api/{session}/chats/{chatId}/messages` |
| Pak Ferdy Chat ID | `10187830259813@lid` |
| Read-Only Access | ✅ Available via WAHA API |

**See:** `PRODUCTION-CONVERSATION-SOURCE.md` for full details.

---

## Current Candidate Status

| ID | Topic | Classification | Source | Status |
|----|-------|----------------|--------|--------|
| LC-001 | AC Major Service Escalation | ESCALATION_RULE | PARTIAL | NEEDS_REVISION |
| LC-002 | Reset AC Service Scope | KNOWLEDGE | VERIFIED (KB) | READY_FOR_REVIEW |
| LC-003 | Fortuner Oil Selection | BUSINESS_RECOMMENDATION | **NONE** | **REJECTED** |
| LC-004 | Stock Query Response | RESPONSE_POLICY | VERIFIED (Production) | NEEDS_REVISION |
| LC-005 | Early Closing Prevention | RESPONSE_POLICY | **NOT FOUND** | NEEDS_REVISION |

---

## Next Steps

### 1. Extract Production Messages

```bash
# Obtain WAHA API key from production
# Extract Pak Ferdy messages
curl -X GET \
  "https://dash.bengkelwiguna.com/waha/api/Minna/chats/10187830259813@lid/messages" \
  -H "X-Api-Key: {WAHA_API_KEY}"
```

### 2. Process Through Learning Pipeline

```
Production WAHA API
    ↓
Extract Pak Ferdy messages
    ↓
LearningPipeline
    ↓
New Learning Candidates
    ↓
Evidence review
    ↓
Production Knowledge
```

### 3. LC-001, LC-003

These candidates can now be verified with actual conversation data.

---

## Documents

| Document | Purpose |
|----------|---------|
| [CANONICAL-LEARNING-REVIEW.md](./CANONICAL-LEARNING-REVIEW.md) | Review gate mechanism |
| [PAK-FERDY-LEARNING-REVIEW.md](./PAK-FERDY-LEARNING-REVIEW.md) | Source-faithfulness review |
| [PAK-FERDY-LEARNING-REVISIONS.md](./PAK-FERDY-LEARNING-REVISIONS.md) | Required corrections |
| [PAK-FERDY-CONVERSATION-EXTRACTION.md](./PAK-FERDY-CONVERSATION-EXTRACTION.md) | Conversation corpus search |
| [PRODUCTION-CONVERSATION-SOURCE.md](./PRODUCTION-CONVERSATION-SOURCE.md) | **Production message source trace** |

---

## Related Documents

- [LEARNING-CANDIDATES.md](../LEARNING-CANDIDATES.md) — Candidate registry
- [PAK-FERDY-LEARNING.md](../../architecture/PAK-FERDY-LEARNING.md) — Architecture concept
- [PAK-FERDY-CHANNEL-IMPLEMENTATION.md](../../../docs/onboarding/PAK-FERDY-CHANNEL-IMPLEMENTATION.md) — Production implementation
- [LEARNING-CANDIDATE-PIPELINE.md](../../../docs/onboarding/LEARNING-CANDIDATE-PIPELINE.md) — Pipeline docs

---

## Rule

```
CONVERSATION SOURCE FOUND
↓
READ-ONLY EXTRACTION
↓
LEARNING PIPELINE
↓
EVIDENCE-BASED CANDIDATES
↓
HUMAN REVIEW
↓
PRODUCTION KNOWLEDGE
```
