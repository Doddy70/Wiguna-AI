# CANONICAL SERVICE RECOMMENDATION GATE
## Pak Ferdy Service Recommendation Protocol

**Source:** WAHA [17:11:03] - 2026-08-25
**Status:** READY_FOR_REVIEW
**Mode:** READ-ONLY

---

## PURPOSE

Dokumentasi ini adalah canonical gate untuk service recommendation behavior yang diajarkan Pak Ferdy.

---

## TRIGGER

### When Pak Ferdy's Rule Activates

Customer says something equivalent to:

| Indonesian | English |
|------------|----------|
| "servis rutin" | "routine service" |
| "paket service" | "service package" |
| "perawatan berkala" | "regular maintenance" |
| "mau ganti oli" | "want to change oil" |
| "service AC" | "AC service" |

### When NOT Triggered

- Safety-critical issues (directed to bengkel immediately)
- Customer already specified exact package
- Customer explicitly asks for pricing only

---

## REQUIRED DISCOVERY DATA

### The Four Questions

Pak Ferdy explicitly stated:

```
Type mobil:
Tahun pembuatan:
Automatic atau manual:
Keluhannya:
```

### Why Four Fields

| Field | Purpose |
|-------|---------|
| Type mobil | Identify vehicle category (sedan/SUV/LCGC) |
| Tahun | Determine generation/recommendations |
| Automatic/manual | Affects oil capacity, transmission fluid |
| Keluhan | Understand customer concern |

---

## VEHICLE CONTEXT RESOLUTION

### After Discovery

1. **Identify vehicle context**
2. **Do NOT invent vehicle data**
3. **Use trusted reference**
4. **State limitation if reference unavailable**

### Acceptable References

- Google search
- Chat history (previous conversation)
- Customer-provided specs
- Known vehicle data

### Unacceptable

- Inventing cc/oil capacity
- Assuming typical vehicle specs
- Guessing transmission type

---

## PACKAGE RECOMMENDATION ORDER

Pak Ferdy explicitly taught this order:

```
1. Paket Siaga
2. Paket AJAG
3. Paket Gaspol
4. Paket IJIG (s/d ban R16)
```

### Why This Order

Pak Ferdy's teaching is explicit — this is the canonical order.

Do not reorder based on price, popularity, or assumption.

---

## BOOKING GATE

### When Booking Data Is Requested

| Condition | Action |
|-----------|--------|
| Customer has NOT selected package | DO NOT ask for booking data |
| Customer has selected package | Ask booking data |
| Customer explicitly asks for booking | Ask booking data |
| Safety-critical issue | Direct to bengkel immediately |

### Wrong Behavior

```
Customer: "servis rutin dong"
Agent: "Mau booking kapan?"
```

### Correct Behavior

```
Customer: "servis rutin dong"
Agent: [Discovery questions]
Agent: [Identify package]
Agent: "Paket Siaga/AJAG/Gaspol/IJIG"
Agent: [Customer selects]
Agent: "Data bookingnya: Nama, HP, mobil, jadwal"
```

---

## NEGATIVE BEHAVIOR (MUST NOT DO)

### Do NOT

- [ ] Immediately recommend a package
- [ ] Call Gaspol "Hero Package"
- [ ] Push only one package
- [ ] Ask booking data before recommendation
- [ ] Skip vehicle context
- [ ] Skip customer complaint
- [ ] Assume oil viscosity/capacity
- [ ] Infer engine cc without reference
- [ ] Invent vehicle specifications

### Evidence This Is Wrong

```
Customer: "servis rutin"
Agent: [NO discovery]
Agent: "Mau booking kapan?"
```

This violates Pak Ferdy's teaching.

---

## RELATION TO EXISTING CANDIDATES

### LC-006: Discovery Before Booking

**Status:** SUPERSEDED by canonical gate

Pak Ferdy's 17:11 teaching contains all LC-006 content.

### LC-005: Early Closing Prevention

**Status:** RETAINED

Booking gate is one aspect of closing behavior. LC-005 covers broader closing policy.

### LC-003: GASPOL Oil Brand

**Status:** RETAINED

Separate correction about oil brand. Not conflicting.

---

## CLASSIFICATION

| Field | Value |
|-------|-------|
| Type | RESPONSE_POLICY |
| Destination | SKILL |
| Source | WAHA [17:11:03] |
| Confidence | 0.95 |

---

## EVIDENCE

### Pak Ferdy Teaching [17:11:03]

```
Terima kasih Minna. Tp saya ingin ajarkan anda bahwa kalau ada konsumen yg
menanyakan servis rutin, anda harus tanya lengkap dulu datanya dan keluhannya.

Type mobil:
Tahun pembuatan:
Automatic atau manual:
Keluhannya:

Setelah itu anda harus cari informasi mengenai cc mobilnya via google atau
referensi chat sebelumnya. Lalu tentukan oli rekomendasinya dan kapasitasnya
sebelum menawarkan paket servis yaitu, mulai dr urutan:

1. Paket siaga
2. Paket Ajag
3. Paket Gaspol
4. Paket Ijig (s/d ban R16)

Kalau konsumen sudah memilih paket yg tepat, baru di tanyakan untuk data bookingnya.
```

### Agent Acknowledgment [17:11:17]

```
Baik Pak Ferdy, terima kasih atas instruksinya. Mulai sekarang:

1. Menanyakan detail kendaraan dan keluhan
2. Mencari informasi cc mesin dari referensi
3. Menentukan oli dan kapasitas
4. Menawarkan paket sesuai urutan: Siaga > AJAG > Gaspol > IJIG
5. Setelah paket dipilih, baru data booking
```

---

## GENERALIZATION

### Applies To

All customer service conversations about routine service/maintenance.

### Does NOT Apply To

- Safety-critical issues (immediate bengkel referral)
- Explicit package requests (go directly to package)
- Pricing-only queries (answer directly)

---

## STOP

Read-only documentation. No production mutation.
