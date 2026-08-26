# Wiguna-AI Pipeline

Pipeline untuk processing learning candidates dari Pak Ferdy conversations.

---

## Directory Structure

```
Wiguna-AI/
├── architecture/
│   ├── PAK-FERDY-LEARNING.md      # Concept & design
│   ├── WIGUNA-ORCHESTRATION.md    # Orchestration model
│   └── TGO-VS-WIGUNA.md           # Architecture separation
├── knowledge/
│   └── LEARNING-CANDIDATES.md     # Extracted candidates
└── pipeline/
    ├── learning_pipeline.py       # Pipeline code
    └── README.md                  # This file
```

---

## Learning Pipeline

### What It Does

```
Pak Ferdy Conversation
         ↓
Learning Extraction
         ↓
Classification
         ↓
Candidate Creation
         ↓
Human Review
         ↓
TGO Web Promotion
         ↓
Agent Runtime
```

### Classification Types

| Type | Destination |
|------|-------------|
| KNOWLEDGE | RAG / Knowledge Base |
| DECISION_KNOWLEDGE | RAG / Workflow |
| RESPONSE_POLICY | Skill |
| ESCALATION_RULE | Workflow |
| BUSINESS_RECOMMENDATION | RAG |
| SKILL | Skill |
| TOOL_REQUIREMENT | Tool |
| EXAMPLE_ONLY | Do not promote |
| TEMPORARY_GUIDANCE | Session only |

---

## Usage

### Python API

```python
from learning_pipeline import LearningPipeline

# Initialize pipeline
pipeline = LearningPipeline()

# Get all candidates
candidates = pipeline.get_candidates(status="CANDIDATE")

# Filter by classification
policies = pipeline.get_candidates(classification="RESPONSE_POLICY")

# Create new candidate
candidate = pipeline.create_candidate(
    original_statement="...",
    classification="KNOWLEDGE",
    topic="Service Scope",
    principle="...",
    confidence=0.85,
)

# Approve candidate
candidate.approve(reviewer="Pak Ferdy")

# Export to JSON
json_data = pipeline.export_to_json()

# Export to Markdown
md_data = pipeline.export_to_markdown()
```

### Command Line

```bash
# Run the pipeline
python3 learning_pipeline.py
```

---

## Candidates

| ID | Topic | Classification | Confidence | Status |
|----|-------|----------------|------------|--------|
| LC-001 | AC Major Service Escalation | ESCALATION_RULE | 0.95 | CANDIDATE |
| LC-002 | Reset AC Service Scope | KNOWLEDGE | 0.95 | CANDIDATE |
| LC-003 | Fortuner Oil Selection | BUSINESS_RECOMMENDATION | 0.90 | CANDIDATE |
| LC-004 | Stock Query Response | RESPONSE_POLICY | 0.95 | CANDIDATE |

---

## Next Steps

1. Review candidates with Pak Ferdy
2. Get approval decisions
3. Promote to TGO Web

---

## Documentation

- [LEARNING-CANDIDATE-PIPELINE.md](../../docs/onboarding/LEARNING-CANDIDATE-PIPELINE.md)
- [LEARNING-CANDIDATES.md](../knowledge/LEARNING-CANDIDATES.md)
- [PAK-FERDY-LEARNING.md](../architecture/PAK-FERDY-LEARNING.md)
