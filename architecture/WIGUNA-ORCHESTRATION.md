# WIGUNA Orchestration Model

## Component Roles

| Component | Role | Description |
|-----------|------|-------------|
| **WORKFLOW** | WHEN / WHERE | Routing logic — kapan dan ke mana request diarahkan |
| **AGENT** | WHO | Role dan tanggung jawab — siapa yang menangani |
| **SKILL** | HOW | Kapabilitas — bagaimana task dijalankan |
| **KNOWLEDGE / RAG** | WHAT | Informasi — apa yang harus diketahui |
| **TOOL** | ACTION / LIVE DATA | Aksi — apa yang dilakukan / data real-time |

---

## Architecture Flow

```
Customer Input
      ↓
   Workflow
   (WHEN / WHERE)
      ↓
    Agent
    (WHO)
      ↓
    Skill
    (HOW)
      ↓
Knowledge / Tool
(WHAT / ACTION)
      ↓
   Response
```

---

## Example — AC Service Query

```
"Kendaraan saya AC-nya bocor"

Customer Input
      ↓
Workflow: DETECT_SERVICE_TYPE → AC_SERVICE
      ↓
Agent: SERVICE_AGENT
      ↓
Skill: AC_DIAGNOSIS_SKILL
      ↓
Knowledge: AC_SERVICE_CATALOG
Tool: -
      ↓
Response: AC Service info + escalation if needed
```

---

## Example — Oli Fortuner

```
"Berapa oli untuk Fortuner?"

Customer Input
      ↓
Workflow: DETECT_SERVICE_TYPE → OIL_SERVICE
      ↓
Agent: SERVICE_AGENT
      ↓
Skill: OIL_RECOMMENDATION_SKILL
      ↓
Knowledge: OIL_CATALOG + PAK FERDY RECOMMENDATION
Tool: -
      ↓
Response: 10W-30 diesel first, 15W-40 + 1L alternative
```

---

## Orchestration Policy

**TGO WEB FIRST**

Semua routing, binding, dan configuration dilakukan melalui TGO Web.

Jangan hardcode orchestration dalam source code sebagai workaround.
