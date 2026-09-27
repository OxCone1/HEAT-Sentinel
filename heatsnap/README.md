# HEAT Snap streamer list

HEAT Snap is the HEAT Sentinel add-on that creates a Twitch clip of a streamer's broadcast when you destroy them, or when they destroy you. It only knows who a streamer is from `streamers.json` in this folder. It never guesses from nicknames.

## Why accounts, not nicknames

A nickname can change, and two accounts can show the same one. Each entry is keyed on the numeric in-game account id, which never changes, so a rename does not break the link.

## Format

```json
{
  "schema": 1,
  "updated": "2026-09-28",
  "streamers": [
    {
      "twitch": "channel_login",
      "twitch_id": "123456789",
      "accounts": [555000111],
      "name": "InGameName"
    }
  ]
}
```

| Field | Required | Meaning |
|---|---|---|
| `twitch` | yes | Twitch login, lowercase, as it appears in `twitch.tv/<login>` |
| `twitch_id` | no | Numeric Twitch user id. Preferred when present, because it survives a Twitch rename |
| `accounts` | yes | One or more in-game account ids (numbers) that belong to this streamer |
| `name` | no | Last known in-game nickname. Display only, never used for matching |

## Getting on the list

The list is opt-in. Only streamers who ask to be added are listed.

1. In HEAT Sentinel, open **Add-ons > HEAT Snap**, then **Streamer list > Copy my entry**. That copies your entry with your in-game account id already filled in.
2. Open an issue or a pull request on this repository with that entry.

To be removed, open an issue or a pull request that deletes your entry.
