# LEARNING MERGE MAP
## Pak Ferdy Candidates

**Date:** 2026-08-25
**Source:** WAHA conversation corpus

---

## CANDIDATES MAP

| ID | Topic | Source | Status | Action |
|----|-------|--------|---------|---------|
| LC-001 | AC Escalation | WAHA (not found) | NEEDS_REVISION | Keep pending |
| LC-002 | Reset AC Scope | KB docs | READY_FOR_REVIEW | Keep |
| **LC-003** | GASPOL Oil Brand | WAHA [16:57] | READY_FOR_REVIEW | Superseded by LC-007 |
| LC-004 | Stock Response | Production code | NEEDS_REVISION | Keep |
| LC-005 | Early Closing | WAHA (partial) | NEEDS_REVISION | Retained |
| **LC-006** | Discovery Protocol | **WAHA [17:11] | **READY_FOR_REVIEW** | Superseded by CANONICAL GATE |
| **LC-007** | GASPOL Oil Brand | **WAHA [16:57] | **READY_FOR_REVIEW** | New |

---

## SUPERSEDENCE

### LC-006 Discovery Protocol

**Superseded by:** CANONICAL-SERVICE-RECOMMENDATION-GATE.md

Pak Ferdy's 17:11 teaching is canonical. LC-006 captures partial. The canonical gate captures full protocol.

### LC-003 GASPOL Oil

**Superseded by:** LC-007

LC-003 was LLM-generated. LC-007 is from actual WAHA correction.

---

## RETAINED

| ID | Reason |
|-----|--------|
| LC-005 | Booking behavior is broader than canonical gate |
| LC-004 | System message correction separate from discovery gate |

---

## CANDIDATES BY DESTINATION

| Destination | Candidates |
|--------------|-------------|
| RAG | LC-002, LC-003, LC-007 |
| SKILL | LC-004, LC-005 |
| WORKFLOW | LC-001 |
| SUPERSEDED | LC-006 |

---

## STOP

Read-only. No production mutation.
