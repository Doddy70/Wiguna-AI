# Graphify — Code Intelligence

Graphify digunakan untuk menganalisis codebase TGO dan WIGUNA-AI.

## Purpose

- Memahami dependency source code
- Memahami relationships antar module
- Memahami architecture
- Membantu Claude/Coding Agent navigasi code
- Menghasilkan code graph
- Mempercepat impact analysis

## Usage

```bash
# Full analysis
/graphify /Users/doddykapisha/Desktop/wgo/Wiguna-AI

# Update existing graph
/graphify /Users/doddykapisha/Desktop/wgo/Wiguna-AI --update

# Query the graph
/graphify query "How does authentication work?"
```

## Important

- **JANGAN install/deploy Graphify di production**
- Graphify hanya untuk **LOCAL DEVELOPMENT** environment
- Output tersimpan di `graphify-out/`

## Output Location

```
Wiguna-AI/
└── graphify-out/
    ├── graph.html      # Interactive visualization
    ├── graph.json      # Raw graph data
    └── GRAPH_REPORT.md # Analysis report
```

## Status

Graphify initialized: 2026-08-25
Corpus: 5 files (governance docs)
