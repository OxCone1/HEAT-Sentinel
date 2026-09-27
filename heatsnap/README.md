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

## Getting on or off the list

The list is opt-in and kept by the developer. To be added, or to have the link between your in-game account and your Twitch channel removed, message the developer on Discord: <https://discord.com/users/376062591480365068>. The same link is on the About page in HEAT Sentinel.

HEAT Snap downloads the list again every time its window is opened, so a removal reaches every user without an app update.
