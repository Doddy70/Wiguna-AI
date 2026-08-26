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

Run these queries to understand the codebase:

```bash
# Core concepts
graphify query "What is WIGUNA AI?"
graphify query "What is the learning pipeline?"

# Architecture
graphify explain "Pak Ferdy Learning System"
graphify explain "LearningPipeline"

# Production setup
graphify path "WIGUNA" "Production"
```

## Step 3: Review Key Files

Read these files to understand the project:

1. `README.md` - Project overview
2. `knowledge/LEARNING-CANDIDATES.md` - Learning system
3. `pipeline/README.md` - Learning pipeline docs
4. `graphify-out/GRAPH_REPORT.md` - Knowledge graph report

## Step 4: Important Context

**Production:** https://dash.bengkelwiguna.com

**Production Freeze Active:**
- NO build, deploy, rsync, docker operations
- NO database migrations
- Focus only on local development

**Graph State:**
- 554 nodes, 39 communities
- Key nodes: CANONICAL LEARNING REVIEW GATE, LearningPipeline, Pak Ferdy Learning System
- Graphify MCP connected and authenticated

## Step 5: Start Working

After completing Steps 1-4, acknowledge what you learned and ask what task to work on.

---

IMPORTANT: After any significant query or task completion, save the knowledge:

```bash
graphify save-result \
  --question "YOUR_QUESTION" \
  --answer "YOUR_ANSWER" \
  --type query \
  --nodes "RELEVANT_NODE" \
  --outcome useful
```

---

# Graphify

- **graphify** (`.claude/skills/graphify/SKILL.md`) - any input to knowledge graph. Trigger: `/graphify`
When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.
