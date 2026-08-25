# Change Management — WIGUNA-AI

## Principle

> "Production Source Drift bukan berarti sync seluruh local repository ke production."

## Definition

**Production Source Drift** terjadi ketika:
- LOCAL memiliki patch yang lebih baru
- PRODUCTION belum memiliki semua patch

## Correct Approach

```
CURRENT PRODUCTION
        ↓
LOCAL / KNOWN-GOOD
        ↓
COMPARE
        ↓
IDENTIFY EXACT REQUIRED CHANGE-SET
        ↓
PATCH ONLY REQUIRED FILES
        ↓
BUILD CANDIDATE
        ↓
VERIFY ARTIFACT
        ↓
PROMOTE
```

## Wrong Approach

```
LOCAL
        ↓
RSYNC WHOLE REPOSITORY
        ↓
BUILD
        ↓
DEPLOY
```

---

## Coherent Patch Set

Satu feature dapat terdiri dari beberapa file.

Contoh:
- `messageStore.ts`
- `ChatList.tsx`
- `ChatPage.tsx`

**Rules:**
- JANGAN deploy hanya satu file dari coherent patch
- JANGAN copy file lain yang tidak relevan

**Coherent Patch Set** = minimum file yang diperlukan agar feature contract konsisten.

---

## Production-Local Diff Matrix

Sebelum patch, WAJIB buat matrix:

| File | Local | Production | Required |
|------|-------|------------|----------|
| file A | new | old | YES |
| file B | changed | old | YES |
| file C | changed | old | NO |

Hanya file dengan `Required = YES` yang boleh masuk patch-set.

Jika status = `UNKNOWN` → **STOP. Jangan menebak.**

---

## Deployment Scope

Satu patch frontend HANYA boleh memengaruhi:
- Required source files
- Generated frontend artifact

JANGAN otomatis memengaruhi:
- Docker
- Nginx
- Database
- WAHA
- Bridge
- tgo-api
- tgo-ai
- RAG
- Workflow

---

## Build vs Deploy

| Activity | Description |
|----------|-------------|
| **Static Build** | `npm build` → `dist/` |
| **Docker Build** | `Dockerfile` → `IMAGE` |

Static build ≠ Docker build.

Static build cukup untuk perubahan React/TypeScript biasa.
