# TEMPORARY DEVELOPMENT MODE — STAGING FIRST
## WIGUNA-AI | PRODUCTION PROTECTED

> **PRIMARY DEVELOPMENT ENVIRONMENT = LOCALHOST STAGING**
> Production remains as live system but NOT the main development environment.

---

# ENVIRONMENT POLICY

## 1. LOCALHOST STAGING = PRIMARY

All development work MUST be done in staging:
- architecture changes
- Agent behavior & instructions
- Skill development
- RAG / Workflow experiments
- Learning pipeline
- Pak Ferdy learning system
- Regression & integration testing

Staging MAY: build, rebuild, restart, modify source/database/skills/agents/workflows/RAG.

## 2. PRODUCTION = PROTECTED

Production MAY:
- read/inspect/monitor
- verify existing behavior
- minimal safe recovery
- explicitly authorized fixes

Production MUST NOT:
- experimentation
- architecture redesign
- trial-and-error
- broad Docker operations
- database experiments

## 3. NO PRODUCTION DEVELOPMENT

Unless explicitly authorized by user, do NOT:
- docker build/rebuild/restart production
- source sync / rsync production
- database mutation for experiments
- nginx / aaPanel changes

---

# CURRENT PRIORITIES

| Priority | Focus |
|---|---|
| **P1** | STAGING BASELINE — ensure localhost staging starts, healthy, reproducible |
| **P2** | GitHub baseline (`https://github.com/Doddy70/Wiguna-AI`) as source of truth |
| **P3** | PERSISTENT LEARNING — Pak Ferdy teaching → extraction → canonical → runtime retrieval |
| **P4** | RAG/KB REGRESSION — Paket Oli, GASPOL, Siaga, AJAG, IJIG, pricing |
| **P5** | AGENT BEHAVIOR — Discovery First, no GASPOL default, correct RAG usage |
| **P6** | PRODUCTION PROMOTION — only with exact change-set + rollback + explicit auth |

---

# DEVELOPMENT METHOD

Use:
```
READ → IDENTIFY → MINIMUM CHANGE → IMPLEMENT → TEST → STOP
```

Do NOT use:
```
AUDIT → FORENSIC → TASK CHAIN → DOCUMENT → IMPLEMENT
```

---

# STOP CONDITIONS

Task is complete when staging behavior PASSES. Then STOP.

Production promotion requires:
1. Staging behavior PASS
2. Regression PASS
3. Exact change-set known
4. Rollback path available
5. User explicitly authorizes

---

# DOCUMENTATION RULE

Create docs ONLY if:
- permanent architecture changes
- governance changes
- onboarding source of truth needs update
- rollback needed
- business rule canonical needs preservation

Do NOT create:
- forensic reports
- task reports
- audit reports

as default output.

---

# SOURCE OF TRUTH (Priority Order)

1. Current code
2. Graphify current graph
3. Current staging state
4. Verified production state
5. Permanent architecture/governance docs
6. Historical documentation

Historical task reports are NOT source of truth if they contradict current implementation.

---

# GIT / GITHUB

GitHub is the development baseline. Keep:
- clean working tree
- secrets excluded
- customer conversation raw data excluded
- runtime cache excluded
- production credentials excluded

---

# PRODUCTION INCIDENT HANDLING

If you find: broken Docker, stale config, WAHA problem, production drift

Determine first:
- **A** — blocks active task? → minimal safe recovery only
- **B** — customer-facing operational failure? → minimal safe recovery only
- **C** — unrelated to task? → document and move on, do NOT fix

---

# STOP CONDITION

Task done when:
- [ ] staging environment identified
- [ ] staging verified healthy
- [ ] production remains untouched
- [ ] Git baseline confirmed
- [ ] Graphify confirmed usable

**STOP. Production protected. Staging is PRIMARY.**

---

# GRAPHIFY GOVERNANCE

## Purpose

Graphify represents **permanent architecture**, not session artifacts:

- ✅ **Extract:** code relationships, component connections, design patterns, knowledge concepts, API contracts
- ❌ **Don't extract:** debug logs, task histories, audit trails, temporary fixes, experiment noise

## Update Triggers

| Trigger | Update? |
|---|---|
| New file / new relationship | ✅ Yes |
| Architecture refactor | ✅ Yes |
| New knowledge concept | ✅ Yes |
| Debug session | ❌ No |
| Task finished | ❌ No |
| Temporary workaround | ❌ No |

## Memory vs Graph

- `graph.json` = permanent architecture (rebuild on structural changes)
- `memory/` = agent session Q&A (persist per session)
- `LESSONS.md` = aggregated agent memory (not code memory)

---

# Agent Onboarding

On new agent session, follow these steps in order:

## Step 1: Read Previous Session Knowledge

```bash
cd /Users/doddykapisha/Desktop/wgo/Wiguna-AI

# 1. Read lessons from previous sessions
graphify reflect
cat graphify-out/reflections/LESSONS.md 2>/dev/null || echo "No lessons yet"

# 2. Check current graph state
graphify god-nodes --top 10

# 3. Check recent changes
git log --oneline -10
git status
```

## Step 2: Understand Project Structure

```bash
# Core concepts
graphify query "What is WIGUNA AI?"
graphify query "What is the learning pipeline?"

# Architecture
graphify explain "Pak Ferdy Learning System"
graphify explain "LearningPipeline"
```

## Step 3: Review Key Files

1. `README.md` - Project overview
2. `knowledge/LEARNING-CANDIDATES.md` - Learning system
3. `pipeline/README.md` - Learning pipeline docs

## Step 4: Start Working

After completing Steps 1-3, acknowledge what you learned and ask what task to work on.

---

# Graphify

- **graphify** (`.claude/skills/graphify/SKILL.md`) - any input to knowledge graph. Trigger: `/graphify`
When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.
