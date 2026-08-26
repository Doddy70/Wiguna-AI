# Pak Ferdy WAHA Source

Source: Actual WhatsApp conversation from WAHA API.

## Source Details

| Field | Value |
|-------|-------|
| **Source** | WAHA API |
| **URL** | `https://dash.bengkelwiguna.com/api/waha/api/Minna/chats/10187830259813@lid/messages` |
| **Chat ID** | `10187830259813@lid` |
| **Session** | Minna |
| **Extracted** | 2026-08-25 |
| **Messages** | 10 |

## Credentials Used

No credentials stored. API accessed via standard WAHA session key.

## Files

| File | Description |
|------|-------------|
| `2026-08-25-pak-ferdy-conversation.json | Raw JSON from WAHA API |

## Notes

- `fromMe: true` = AI Agent message
- `fromMe: false` = Pak Ferdy message
- Timestamps in Unix epoch format
- `PushName` indicates WhatsApp display name

## Extraction

```bash
curl -X GET \
  "https://dash.bengkelwiguna.com/api/waha/api/Minna/chats/10187830259813@lid/messages" \
  -H "X-Api-Key: waha-static-api-key-2024"
```

## Read-Only Notice

This directory contains READ-ONLY extracted conversation data.
No credentials stored.
No production modification.
