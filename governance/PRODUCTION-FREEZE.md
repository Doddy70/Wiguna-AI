# PRODUCTION FREEZE — ACTIVE

**Tanggal:** 2026-08-25

---

## Status

Production infrastructure saat ini **FRAGILE**.

---

## Yang DILARANG

### Infrastructure Changes
- [ ] Docker build
- [ ] Docker deploy
- [ ] Docker restart
- [ ] Docker recreate
- [ ] Docker compose
- [ ] Nginx modification
- [ ] aaPanel modification

### Data Changes
- [ ] Database mutation
- [ ] Database migration
- [ ] Restore production
- [ ] Production data change

### File Transfer
- [ ] rsync ke production
- [ ] SCP ke production
- [ ] rsync --delete
- [ ] Copy dist tanpa comparison

### Source Changes
- [ ] Sync seluruh repository ke production
- [ ] Overwrite production dist
- [ ] Patch compiled assets
- [ ] Downgrade runtime config

---

## Yang BOLEH

### Development Only
- [x] Local development
- [x] Code analysis
- [x] Graphify analysis
- [x] Documentation creation
- [ ] Build candidate (local)
- [ ] Artifact comparison (local)

### Investigation
- [ ] Read production logs
- [ ] Read production config (read-only)
- [ ] Analyze errors
- [ ] Trace root cause

### Planning
- [ ] Identifikasi exact change-set
- [ ] Artifact comparison
- [ ] Deployment planning

---

## Emergency Authorization

Untuk membuka freeze, diperlukan **explicit authorization** dari owner.

Emergency authorization checklist:
- [ ] Root cause identified
- [ ] Exact change-set documented
- [ ] Rollback plan ready
- [ ] Owner approval obtained
- [ ] Verification plan ready

---

## Review Schedule

Freeze akan di-review secara berkala.

Owner: Pak Ferdy / Doddy Kapisha
