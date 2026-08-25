# Graph Report - Wiguna-AI  (2026-08-25)

## Corpus Check
- Corpus is ~989 words - fits in a single context window. You may not need a graph.

## Summary
- 55 nodes · 60 edges · 13 communities (6 shown, 7 thin omitted)
- Extraction: 0% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Classification Types
- Production & Governance
- Service Knowledge
- Orchestration Model
- TGO Core Components
- WIGUNA OS Features
- AC Service Flow
- Agent Binding
- Graphify Intelligence
- Knowledge Binding
- Oil Service Flow
- Routing
- Skill Behavior

## God Nodes (most connected - your core abstractions)
1. `Pak Ferdy Learning System` - 10 edges
2. `TGO Upstream` - 9 edges
3. `WIGUNA-AI` - 7 edges
4. `TGO` - 7 edges
5. `WIGUNA Customization` - 7 edges
6. `TGO Web` - 4 edges
7. `Workflow` - 4 edges
8. `Skill` - 4 edges
9. `WIGUNA OS` - 3 edges
10. `Pak Ferdy` - 3 edges

## Surprising Connections (you probably didn't know these)
- `WIGUNA-AI` ----> `TGO`  [high]
  CLAUDE.md → README.md
- `WIGUNA-AI` ----> `WIGUNA OS`  [high]
  CLAUDE.md → README.md
- `TGO` ----> `TGO Upstream`  [high]
  README.md → TGO-VS-WIGUNA.md
- `WIGUNA Customization` ----> `Pak Ferdy Learning System`  [high]
  TGO-VS-WIGUNA.md → architecture/PAK-FERDY-LEARNING.md
- `TGO` ----> `Agent`  [high]
  README.md → architecture/WIGUNA-ORCHESTRATION.md

## Communities (13 total, 7 thin omitted)

### Community 0 - "Classification Types"
Cohesion: 0.22
Nodes (9): Absence of Evidence Rule, AC Escalation Rule, ESCALATION RULE Classification Type, KNOWLEDGE Classification Type, RESPONSE POLICY Classification Type, SKILL Classification Type, TOOL REQUIREMENT Classification Type, WORKFLOW RULE Classification Type (+1 more)

### Community 1 - "Production & Governance"
Cohesion: 0.28
Nodes (9): Code Policy, Docker Policy, Learning Candidate, Learning Pipeline, Orchestration Policy, Production, Production Freeze, TGO Web (+1 more)

### Community 2 - "Service Knowledge"
Cohesion: 0.25
Nodes (8): AC_DIAGNOSIS_SKILL, AC_SERVICE_CATALOG, BUSINESS RECOMMENDATION Classification Type, Fortuner Oil Rule, OIL_CATALOG, OIL_RECOMMENDATION_SKILL, PAK FERDY RECOMMENDATION, SERVICE_AGENT

### Community 3 - "Orchestration Model"
Cohesion: 0.43
Nodes (8): Agent, Customer Input, Knowledge / RAG, Response, Skill, TGO, Tool, Workflow

### Community 4 - "TGO Core Components"
Cohesion: 0.29
Nodes (7): Agent Framework, Knowledge Base / RAG, Core Orchestration Engine, Skill Framework, TGO Upstream, Tool System, Workflow Engine

### Community 5 - "WIGUNA OS Features"
Cohesion: 0.29
Nodes (7): Business Logic, Escalation Rules, Pak Ferdy, Response Policies, Service Catalog, WIGUNA Customization, WIGUNA OS

## Knowledge Gaps
- **26 isolated node(s):** `Docker Policy`, `Core Orchestration Engine`, `Agent Framework`, `Skill Framework`, `Knowledge Base / RAG` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `TGO Upstream` connect `TGO Core Components` to `Production & Governance`, `Orchestration Model`, `WIGUNA OS Features`?**
  _High betweenness centrality (0.317) - this node is a cross-community bridge._
- **Why does `Pak Ferdy Learning System` connect `Classification Types` to `Production & Governance`, `Service Knowledge`, `WIGUNA OS Features`?**
  _High betweenness centrality (0.313) - this node is a cross-community bridge._
- **Why does `WIGUNA Customization` connect `WIGUNA OS Features` to `Classification Types`, `TGO Core Components`?**
  _High betweenness centrality (0.290) - this node is a cross-community bridge._
- **What connects `Docker Policy`, `Core Orchestration Engine`, `Agent Framework` to the rest of the system?**
  _26 weakly-connected nodes found - possible documentation gaps or missing edges._