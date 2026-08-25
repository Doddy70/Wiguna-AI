# PRODUCTION SAFETY — WIGUNA-AI

**Tanggal:** 2026-08-25

---

## ABSOLUTE RULE

Production (`dash.bengkelwiguna.com`) adalah **canonical runtime**.

**JANGAN** melakukan mutation production tanpa explicit authorization.

---

## YANG DILARANG

### Production Infrastructure
- [ ] SSH write ke production
- [ ] Docker build production
- [ ] Docker restart production
- [ ] Docker recreate production
- [ ] Docker deploy production

### Production Configuration
- [ ] rsync ke production
- [ ] nginx modification
- [ ] aaPanel modification

### Production Data
- [ ] database mutation
- [ ] database migration
- [ ] restore production
- [ ] production data change

### Production Source
- [ ] sync seluruh repository ke production
- [ ] overwrite production dist
- [ ] patch compiled assets
- [ ] downgrade runtime config

---

## YANG BOLEH

### Development Only
- [x] Local development
- [x] Code analysis
- [x] Graphify analysis
- [x] Documentation creation
- [x] Build candidate (local)
- [x] Artifact comparison (local)

### Investigation (Read-Only)
- [ ] Read production logs
- [ ] Read production config
- [ ] Analyze errors
- [ ] Trace root cause

### Planning
- [ ] Identifikasi exact change-set
- [ ] Artifact comparison
- [ ] Deployment planning

---

## PRODUCTION FREEZE

Production infrastructure saat ini **FRAGILE**.

Anggap:
- NO BUILD
- NO DEPLOY
- NO RSYNC
- NO RESTORE
- NO NGINX CHANGE
- NO DATABASE CHANGE

---

## EMERGENCY AUTHORIZATION

Untuk membuka freeze, diperlukan **explicit authorization** dari owner.

Emergency authorization checklist:
- [ ] Root cause identified
- [ ] Exact change-set documented
- [ ] Rollback plan ready
- [ ] Owner approval obtained
- [ ] Verification plan ready

---

## SOURCE SAFETY

TGO upstream dan WIGUNA customization harus tetap **distinguishable**.

Jangan membuat copy TGO yang kehilangan hubungan dengan upstream.

---

## ORCHESTRATION SAFETY

Semua orchestration WIGUNA mengikuti prinsip:

**TGO WEB FIRST**

Jangan membuat hardcoded orchestration hanya karena implementation code lebih mudah.

---

## Owner

- Pak Ferdy (Human Supervisor / Teacher / Evaluator)
- Doddy Kapisha (Technical Owner)
