# HEAT Snap streamer list

HEAT Snap is the HEAT Sentinel add-on that creates a Twitch clip of a streamer's broadcast when you destroy them, or when they destroy you. It only knows who a streamer is from `streamers.json` in this folder. Nobody outside this file is ever looked up.

## Accounts first, nicknames as a fallback

A nickname can change, and two accounts can show the same one. An entry keyed on the numeric in-game account id survives a rename and never matches the wrong player, so prefer it whenever the id is known.

An entry with no account id (`accounts` empty or missing) is matched by its nickname instead:

- `"name": "Name#12345"` (the in-game tag with its number) matches that one account exactly.
- `"name": "Name"` matches any player showing that nickname, case-insensitively. Anyone else using the same name would match too, and a rename breaks it.
- `"names": [...]` adds more nicknames for the same streamer.

Bots are never matched by name.

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
| `accounts` | no | In-game account ids (numbers) that belong to this streamer. When present, the only thing matched |
| `name` | no | In-game nickname. Display only when `accounts` is given; otherwise the match key (see above) |
| `names` | no | More nicknames to match when `accounts` is empty |

An entry needs `accounts` or a name, or it is skipped.

## Who is on the list, and opting out

The list is curated by the developer. You may be on it because you have streamed HEAT: your in-game nickname was seen on your public stream and linked to your Twitch channel.

To opt out, message the developer on Discord: <https://discord.com/users/376062591480365068>. Your entry is removed. The same link is on the About page in HEAT Sentinel. To be added, use the same link.

HEAT Snap downloads the list again every time its window is opened, so a removal reaches every user without an app update.
