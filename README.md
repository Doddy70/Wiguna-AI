# WIGUNA-AI

Development repository for WIGUNA OS — an intelligent automotive service assistant powered by AI agents (LLM), RAG, and Tools Orchestrations.

## Purpose

This repository serves as:
- **WIGUNA customization layer** 
- **Agent definitions** for automotive service orchestration
- **Knowledge architecture** for service intelligence
- **Learning pipeline** for continuous AI improvement from real customer interactions
- **Workflow orchestration** documentation
- **Production governance** guidelines
- **Graphify code intelligence** knowledge graphs

## Status

**DEVELOPMENT ONLY** — This is a localhost staging baseline, not a production deployment target.

Production: https://dash.bengkelwiguna.com

**Production systems must not be mutated without explicit authorization.**

## Repository Structure

```
Wiguna-AI/
├── agents/           # Agent definitions and configurations
├── architecture/     # System architecture documentation
├── docs/             # General documentation
├── governance/       # Development and production governance rules
├── graphify/         # Graphify skill for code intelligence
├── graphify-out/     # Generated knowledge graphs (interactive HTML)
├── knowledge/        # Service knowledge and learning corpus
│   ├── LEARNING-CANDIDATES.md    # Canonical learning candidates
│   └── owner-learning/           # Owner-driven learning system
│       ├── CANONICAL-LEARNING-REVIEW.md
│       ├── CANONICAL-SERVICE-RECOMMENDATION-GATE.md
│       ├── PAK-FERDY-LEARNING-REVIEW.md
│       └── source/pak-ferdy/     # Service corpus (JSON excluded — sensitive)
├── pipeline/         # Learning pipeline code
│   ├── learning_pipeline.py
│   └── README.md
├── skills/           # WIGUNA-specific skills
├── tools/            # Development tools
└── workflows/        # Workflow definitions
```

## Knowledge Graph

Interactive knowledge graph available at: [`graphify-out/graph.html`](./graphify-out/graph.html)

**Stats:** 55 nodes · 60 edges · 13 communities

**God Nodes (most connected):**
- Pak Ferdy Learning System (10 edges)
- TGO Upstream (9 edges)
- WIGUNA-AI (7 edges)
- TGO (7 edges)
- WIGUNA Customization (7 edges)

**Top Communities:**
- Classification Types
- Production & Governance
- Service Knowledge
- Orchestration Model
- TGO Core Components
- WIGUNA OS Features

See [`graphify-out/GRAPH_REPORT.md`](./graphify-out/GRAPH_REPORT.md) for full analysis.

## Learning System

WIGUNA-AI includes an owner-driven learning system that extracts insights from real customer conversations to continuously improve AI responses.

### Learning Pipeline

The `pipeline/` directory contains:
- `learning_pipeline.py` — Core learning extraction pipeline
- Automated extraction from WAHA conversation corpus
- Canonical learning candidate management
- Service recommendation gate validation

### Learning Candidates

Canonical learning candidates are documented in [`knowledge/LEARNING-CANDIDATES.md`](./knowledge/LEARNING-CANDIDATES.md), including:
- Pak Ferdy Learning Review — corrections and improvements from service owner
- Canonical Service Recommendation Gate — standards for service offers
- Corpus Index — tracking of conversation sources

**Note:** Raw conversation corpus (`knowledge/owner-learning/source/**/*.json`) contains sensitive customer data and is excluded from git.

## Quick Links

- [Graphify](./graphify/) — Code intelligence skill
- [Graph Report](./graphify-out/GRAPH_REPORT.md) — Knowledge graph analysis
- [Interactive Graph](./graphify-out/graph.html) — Visual knowledge map
- [Architecture](./architecture/) — System design documents
- [Governance](./governance/) — Development policies
- [Knowledge](./knowledge/) — Service knowledge base
- [Learning Pipeline](./pipeline/) — AI improvement pipeline
- [CLAUDE.md](./CLAUDE.md) — Claude agent instructions

## Development

```bash
# Clone repository
git clone https://github.com/Doddy70/Wiguna-AI.git

# View interactive knowledge graph
open graphify-out/graph.html
```

## License

See [LICENSE](../LICENSE) for details.

---

*Last updated: 2026-08-26*
