# TGO vs WIGUNA — Architecture Separation

## Concept

```
TGO Upstream
    ↓
WIGUNA Customization
    ↓
WIGUNA AI OS
```

---

## TGO Upstream

TGO (Telegram Web Assistant) menyediakan:
- Core orchestration engine
- Agent framework
- Skill framework
- Knowledge Base / RAG infrastructure
- Workflow engine
- Tool system
- Web interface (TGO Web)

---

## WIGUNA Customization

Customization WIGUNA mencakup:
- Business logic (Bengkel Wiguna specific)
- Service catalog (AC, Oli, Sparepart, dll)
- Escalation rules
- Response policies
- Pak Ferdy Learning System
- Industry-specific knowledge

---

## Key Principle

**Jangan mengarang daftar customization yang belum diketahui.**

Daftar di atas adalah conceptual framework.
Detail customization akan di-extract dari:
1. Existing conversation Pak Ferdy
2. Business requirements
3. Actual implementation

---

## WIGUNA AI OS

Hasil gabungan:
- TGO base capabilities
- WIGUNA business layer
- Pak Ferdy guidance

Agent behavior yang spesifik untuk Bengkel Wiguna.
