# WIGUNA-AI — DEVELOPMENT REPOSITORY GOVERNANCE

## PURPOSE

Repository ini adalah **development/governance workspace** untuk WIGUNA OS yang berbasis TGO.

**BUKAN production deployment target.**

---

## PRODUCTION SAFETY

Production (`dash.bengkelwiguna.com`) adalah canonical runtime.

**JANGAN** melakukan mutation production tanpa explicit authorization.

---

## ORCHESTRATION POLICY

**TGO WEB FIRST**

Untuk semua kebutuhan:
- Agent
- Skills
- Tools
- Knowledge Base
- Workflow
- Routing
- Agent binding
- Skill behavior
- Knowledge binding

→ Gunakan TGO Web terlebih dahulu.

---

## CODE POLICY

Source code hanya diubah jika:

1. Capability memang belum tersedia di TGO Web
2. Capability gap terbukti
3. Perubahan memang diperlukan

**Jangan** menggunakan source code sebagai workaround orchestration.

---

## DOCKER POLICY

Tidak ada Docker build/deploy/restart production untuk pekerjaan orchestration/configuration.

---

## PRODUCTION FREEZE

Production infrastructure saat ini fragile.

Anggap:
- NO BUILD
- NO DEPLOY
- NO RSYNC
- NO RESTORE
- NO NGINX CHANGE
- NO DATABASE CHANGE

Kecuali ada explicit authorization dari owner.

---

## CURRENT DATE

`2026-08-25`

---

## WORKING CONTEXT

Local Development:
`/Users/doddykapisha/Desktop/wgo/Wiguna-AI`

Production Reference:
`https://dash.bengkelwiguna.com`
