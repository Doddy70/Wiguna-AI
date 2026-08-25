# Source Organization — TGO Reference Strategy

## Purpose

Repository ini harus selalu dapat membedakan:
- **UPSTREAM CHANGE** (TGO source)
- **WIGUNA CUSTOM CHANGE** (customization)

---

## Strategy Options

### Option 1: Git Remote/Upstream Reference (Recommended)

Maintain remote connection ke TGO repository asli:

```bash
# Add TGO as upstream
git remote add upstream https://github.com/[tgo-owner]/[tgo-repo].git

# Fetch upstream changes
git fetch upstream

# View upstream branches
git branch -a
```

**Pros:**
- Selalu dapat pull upstream changes
- Clear separation between upstream vs custom
- Standard git workflow

**Cons:**
- Tergantung ketersediaan TGO repo public

---

### Option 2: Git Submodule

Jika TGO adalah separate repository:

```bash
git submodule add https://github.com/[tgo-owner]/[tgo-repo].git tgo/
```

**Pros:**
- Commit-level pinning ke upstream
- Clear boundary

**Cons:**
- Submodule management complexity
- Can be confusing for some workflows

---

### Option 3: Separate Clone/Reference

Clone terpisah untuk reference:

```
Wiguna-AI/
tgo-reference/  (separate clone, read-only)
```

**Pros:**
- Full isolation
- No coupling

**Cons:**
- Lose git relationship
- Manual sync required

---

## Recommended Approach

Pilih **Option 1 (Upstream Remote)** jika TGO repository public dan accessible.

Ini memungkinkan:
- Clear git history
- Easy upstream updates
- Transparent diff

---

## Status

**PENDING:** TGO upstream repository belum diidentifikasi.

Repository TGO production saat ini ada di:
- Local: `/www/tgo/repos/tgo-web/` (production server)
- Remote: Tidak diketahui dari context saat ini

Langkah selanjutnya:
1. Identifikasi TGO GitHub repo atau Git remote
2. Add sebagai upstream remote
3. Dokumentasikan URL upstream di sini

---

## Current State

```
Wiguna-AI/  (THIS REPOSITORY)
├── CLAUDE.md
├── README.md
├── architecture/
├── agents/
├── skills/
├── knowledge/
├── workflows/
├── tools/
├── graphify/
├── docs/
└── .gitignore

TGO Production Source: /www/tgo/repos/tgo-web/ (production server)
TGO Upstream Remote: NOT YET CONFIGURED
```
