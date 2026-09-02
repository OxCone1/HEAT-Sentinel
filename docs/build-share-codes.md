# Build links for HEAT Sentinel

**Send a loadout from your website straight into a player's game.**

If you run a build planner for World of Tanks HEAT, this is how you stop asking
people to copy six module names across by hand. You produce a link. They click
it. HEAT Sentinel opens, shows them the build against the tank they actually
have, and writes it into the game on one more click.

```
sentinel://build/HEAT1.eyJ2IjoxLCJ2ZWhpY2xlIjoiYTAyX20xZTFfMTIwIiwibW9k...
```

Nothing here needs our permission, an API key, a server, or a partnership. A
build link is a string you can generate offline, and the format is published so
that it stays generatable. This page is everything you need to make one.

---

## Contents

1. [How it works](#how-it-works)
2. [Quick start](#quick-start)
3. [The parts catalog](#the-parts-catalog) — the vocabulary, as downloadable JSON
4. [The build object](#the-build-object)
5. [Rules a valid build follows](#rules-a-valid-build-follows)
6. [Making the code](#making-the-code)
7. [Making the link](#making-the-link)
8. [What the player sees](#what-the-player-sees)
9. [Compatibility](#compatibility)

---

## How it works

```
your planner  ──▶  build object  ──▶  HEAT1. code  ──▶  sentinel:// link
                                                              │
                                                       player clicks
                                                              │
                                                              ▼
                                          HEAT Sentinel opens and stages it
                                                              │
                                                     player clicks Apply
                                                              ▼
                                                    the loadout is in the game
```

The app is the part that talks to the game client; your side never does. All you
produce is a string.

### Why parts travel as names, not numbers

A loadout in the game is a set of numeric ids, and **ids are not portable**.
Hundreds of the game's modules already carry an internal code naming a different
id than the one they are published under today, so a build sent as ids would
silently resolve to a *different* build after a patch, or on another account.

Technical names — `a02_m1e1_120`, `utility_1_3`, `recovery_system_ability` — are
unique within a vehicle and have never moved. So that is what travels.
**Everything in a build code is a technical name, and nothing in it is an id.**
The catalog below is how you learn the names; it deliberately publishes no ids
at all, so there is nothing to accidentally use.

---

## Quick start

```js
const build = {
  v: 1,
  vehicle: 'a02_m1e1_120',
  modules: [
    'ability_1_2', 'ability_2_1', 'toughness_1_5',
    'toughness_2_7', 'firepower_1_4', 'utility_1_1',
  ],
  equipment: ['recovery_system_ability', 'fail_safe_circuit'],
  perks: [
    'perk_chopper_trait_2', 'perk_chopper_ability_1',
    'perk_chopper_extension_2', 'perk_chopper_ultimate_1',
  ],
  name: 'Hull-Down',
  starred: 'toughness_2_7',
}

const json  = JSON.stringify(build)
const bytes = new TextEncoder().encode(json)
let bin = ''; for (const b of bytes) bin += String.fromCharCode(b)
const code  = 'HEAT1.' + btoa(bin)
  .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')

const link = `sentinel://build/${code}`
```

Put `link` in an `<a href>`. That is the whole integration.

That build is real: six modules, one per group on the M1E1, 70 of its 100 power
spent, one legendary, and Chopper's four perks one per row. It encodes to

```
HEAT1.eyJ2IjoxLCJ2ZWhpY2xlIjoiYTAyX20xZTFfMTIwIiwibW9kdWxlcyI6WyJhYmlsaXR5XzFfMiIsImFiaWxpdHlfMl8xIiwidG91Z2huZXNzXzFfNSIsInRvdWdobmVzc18yXzciLCJmaXJlcG93ZXJfMV80IiwidXRpbGl0eV8xXzEiXSwiZXF1aXBtZW50IjpbInJlY292ZXJ5X3N5c3RlbV9hYmlsaXR5IiwiZmFpbF9zYWZlX2NpcmN1aXQiXSwicGVya3MiOlsicGVya19jaG9wcGVyX3RyYWl0XzIiLCJwZXJrX2Nob3BwZXJfYWJpbGl0eV8xIiwicGVya19jaG9wcGVyX2V4dGVuc2lvbl8yIiwicGVya19jaG9wcGVyX3VsdGltYXRlXzEiXSwibmFtZSI6Ikh1bGwtRG93biIsInN0YXJyZWQiOiJ0b3VnaG5lc3NfMl83In0
```

Every name in it comes from the catalog below.

---

## The parts catalog

Five JSON files, keyed by technical name, with display names for all twelve
languages the game ships inline. Static data — host a copy, or fetch and cache
it. Re-fetch after a game patch: the app tells a player when a build names a
part their client cannot place, but a planner *offering* a part that no longer
exists is a planner offering a broken build.

| File | Holds |
|------|-------|
| `catalog.json` | Manifest: catalog version, when it was generated, the language list, counts, and a SHA-256 per file so you can tell a real update from a re-upload. |
| `vehicles.json` | Every buildable hull: its power budget, its agent, its equipment slots and what fits them, and its module groups. |
| `equipment.json` | Every equipment item: slot, family, names. |
| `perks.json` | Every perk: its grid row, its tier, the agent level it unlocks at, names and descriptions. |
| `agents.json` | Every agent: role, which hulls carry them, which perks they own. |

### `vehicles.json`

```jsonc
{
  "v": 1,
  "vehicles": [
    {
      "key": "a02_m1e1_120",            // put this in the build's `vehicle`
      "name": { "en": "M1E1", "ru": "M1E1", "ja": "M1E1", /* … */ },
      "agent": "chopper",               // look this up in agents.json
      "power": 100,                     // the budget a layout must fit inside
      "equipmentSlots": ["FirstEquipment", "SecondEquipment"],
      "baseEquipment": ["recovery_system_ability", "fail_safe_circuit"],
      "availableEquipment": ["fail_safe_circuit", "hull_reinforcement_kit", /* … */],
      "groups": [
        {
          "title": { "en": "Demolition Charges", /* … */ },
          "kind":  { "en": "ABILITY MOD", /* … */ },
          "modules": [
            {
              "n": "ability_1_1",       // put this in the build's `modules`
              "name":     { "en": "GGM-743", /* … */ },
              "subtitle": { "en": "Gun motor", /* … */ },
              "rarity": "Common",       // Common | Uncommon | Rare | Epic | Legendary
              "legendary": false,       // only ONE legendary may be installed
              "tier": 1,
              "power": 5,               // what it spends of the 100
              "icon": "m61_vulcan_motor.png"
            }
          ]
        }
      ]
    }
  ]
}
```

**Groups are the slots.** A layout takes **at most one module from each group**,
and a group may be left empty. The order of `modules` in a build does not
matter — the app places each name into whichever group owns it.

### `equipment.json`

```jsonc
{
  "n": "rebuild_kit_ability",
  "slot": "FirstEquipment",              // or SecondEquipment
  "family": "recovery_system",           // variants of one piece share a family
  "name": { "en": "Rebuild Kit", /* … */ },
  "icon": "ico_rebuild_kit_big.png"
}
```

`family` groups the variants of a single item — plain and charged Phantom
Curtain are one piece with two entries, and a hull grants one of them. A planner
that offers both without saying so is offering the same choice twice.

### `perks.json`

```jsonc
{
  "v": 1,
  "slots": 4,                            // a build activates four perks
  "rows": [
    { "row": 1, "order": 0, "title": { "en": "Trait", /* … */ } },
    { "row": 2, "order": 1, "title": { "en": "Ability", /* … */ } },
    { "row": 3, "order": 2, "title": { "en": "Attribute", /* … */ } },  // perk_<agent>_extension_*
    { "row": 4, "order": 3, "title": { "en": "Ultimate", /* … */ } }
  ],
  "perks": [
    {
      "n": "perk_chopper_trait_1",
      "row": 1,
      "tier": 1,
      "unlockLevel": 1,                  // agent level needed: 1, 10, 20, 30
      "name": { "en": "Echo Shield", /* … */ },
      "description": { "en": "…", /* … */ }
    }
  ]
}
```

Each agent has sixteen perks: four rows by four tiers. Which four a player runs
is up to them; the catalog just says what exists.

**Some perks have an empty `name` and `description`.** Around a third of them
do, concentrated in the upper tiers: the game client itself publishes no strings
for those yet. They are real, a build may name them, and they will gain names in
a later catalog. Fall back to the technical name and expect this to shrink, not
grow. The same is true of one equipment variant.

### `agents.json`

```jsonc
{
  "key": "chopper",
  "name":     { "en": "Chopper", /* … */ },
  "lastName": { "en": "…", /* … */ },
  "role": "Defender",                    // Defender | Marksman | Assault
  "vehicles": ["a02_m1e1_120", "gb01_challenger"],
  "perks": ["perk_chopper_ability_1", /* … 16 … */]
}
```

Every vehicle has exactly one eligible agent, so the perks available to a build
follow from the vehicle. An agent listed with **no** perks and no vehicles is
one the client ships without a grid yet — show it or skip it, but do not expect
to build for it.

### What the catalog deliberately does not contain

- **No numeric ids.** See above.
- **No ownership, prices or balances.** What a part costs, and whether a given
  player has it, is a fact about that player's account. The catalog is generated
  through an allow-list and a leak check precisely so none of that can escape
  into it.
- **No artwork.** Icon *filenames* are there so you can wire up your own copies;
  the images themselves are the game's and are not redistributed here.
- **No stats or balance numbers.** What a module *does* is the game's to
  describe. The catalog names parts; it does not model them.

---

## The build object

```jsonc
{
  "v": 1,
  "vehicle": "a02_m1e1_120",
  "modules": ["ability_1_2", "ability_2_1", "toughness_1_5",
              "toughness_2_7", "firepower_1_4", "utility_1_1"],
  "equipment": ["recovery_system_ability", "fail_safe_circuit"],
  "perks": ["perk_chopper_trait_2", "perk_chopper_ability_1",
            "perk_chopper_extension_2", "perk_chopper_ultimate_1"],
  "name": "Hull-Down",
  "starred": "toughness_2_7"
}
```

A slot left empty is simply absent from `modules`, and an unused perk slot is
`""` — `["perk_chopper_trait_2", "", "", ""]` is a build with one perk.

| Field | Type | Required | Meaning |
|-------|------|----------|---------|
| `v` | number | yes | Format version of the object. `1` today. |
| `vehicle` | string | yes | A `key` from `vehicles.json`. The one field without which a code is not a build. |
| `modules` | string[] | yes | Module technical names, one per **filled** group. **Order does not matter** — an empty group is simply absent, not a hole. |
| `equipment` | string[] | yes | Equipment technical names, **positional**: `[FirstEquipment, SecondEquipment]`. At most 2. |
| `perks` | string[] | yes | Perk technical names in **activation order**, at most 4. `""` is a real value meaning "this slot is empty" — it is not a gap to filter out. |
| `name` | string | no | Your label for the build. Travels on purpose, and is what the player sees it called. Keep it under 40 characters; anything past 60 is trimmed. |
| `starred` | string | no | The module the build is *about* — the one thing a reader should look at first. A **label, not a part**: it must name a module already in `modules`. |
| `unnamed` | number | no | Only ever written by the app, when it held a part it could not name. You will not need it. |

### What must not be in it

- **No numeric ids.** They will not resolve.
- **No battles, win rate or damage.** A build code carried performance figures
  in early versions and no longer does; readers ignore the field if it is
  present. A record is earned, not transferred: it accumulates the more its
  owner plays, so your site's 61%-over-200-battles says nothing about the
  receiving player's tank, agent level or skill — and printed beside their own
  builds it would read exactly as if it did. Put your statistics on your page,
  where they mean something.
- **No ownership or price.** Resolved locally, against the player's account.
- **No power total.** Derived from the modules against the player's own copy of
  the catalog, so a rebalance patch cannot make a code lie.
- **No player identity.** A code says nothing about who made it.

---

## Rules a valid build follows

The app checks all of this on arrival and tells the player what it found, so a
code that breaks a rule is not dangerous — it is just a worse experience than
one that does not. Check it on your side:

| Rule | Where the numbers come from |
|------|-----------------------------|
| At most one module per group | `vehicles[].groups` |
| Total module `power` ≤ the vehicle's `power` | `vehicles[].power`, `modules[].power` |
| At most one module with `legendary: true` | `modules[].legendary` |
| Equipment must be in the hull's `availableEquipment` | `vehicles[].availableEquipment` |
| Equipment goes in the slot its entry declares | `equipment[].slot` |
| At most one equipment per `family` | `equipment[].family` |
| At most 4 perks, positional, `""` for empty | `perks.json → slots` |
| Perks must belong to the vehicle's agent | `agents[].perks`, `vehicles[].agent` |
| At most one perk per grid row | `perks[].row` |

A perk's technical name carries the agent that owns it (`perk_chopper_trait_2`),
which makes the agent check a string comparison if you would rather not join
through `agents.json`. Note that row 3 reads "Attribute" but its perks are named
`extension` — go by `row`, not by the name.

The power budget is the one that bites: it is why two legendaries never fit, and
it is the constraint a planner exists to help with.

---

## Making the code

```
HEAT1.<base64url(utf8(json))>
```

Three layers, outside in:

1. **Prefix** `HEAT1.` — a literal, including the dot. It makes a code
   recognisable in a chat log, and it is what a future format version would
   change. `HEAT2.` would be a different envelope; a reader that does not know
   it should refuse rather than guess.
2. **base64url** — standard base64 with `+` → `-`, `/` → `_`, and trailing `=`
   padding stripped. This is what lets a code survive a URL, a Discord message
   and a spreadsheet cell without escaping.
3. **UTF-8 JSON** — the build object. Not compressed, not encrypted, not signed.
   UTF-8 matters: build names arrive in every script.

A typical code is 200–400 characters.

### JavaScript

```js
const PREFIX = 'HEAT1.'

export function encodeBuild(build) {
  const bytes = new TextEncoder().encode(JSON.stringify(build))
  let bin = ''
  for (const b of bytes) bin += String.fromCharCode(b)
  return PREFIX + btoa(bin)
    .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '')
}

export function decodeBuild(text) {
  const s = (text || '').trim()
  const body = s.startsWith(PREFIX) ? s.slice(PREFIX.length) : s
  const padded = body.replace(/-/g, '+').replace(/_/g, '/')
    + '='.repeat((4 - (body.length % 4)) % 4)
  const bin = atob(padded)
  const bytes = Uint8Array.from(bin, (c) => c.charCodeAt(0))
  return JSON.parse(new TextDecoder().decode(bytes))
}
```

### Python

```python
import base64
import json

PREFIX = "HEAT1."

def encode_build(build: dict) -> str:
    raw = json.dumps(build, separators=(",", ":")).encode("utf-8")
    return PREFIX + base64.urlsafe_b64encode(raw).decode().rstrip("=")

def decode_build(text: str) -> dict:
    body = text.strip()
    if body.startswith(PREFIX):
        body = body[len(PREFIX):]
    body += "=" * (-len(body) % 4)
    return json.loads(base64.urlsafe_b64decode(body).decode("utf-8"))
```

### Reading a code someone pastes at you

If your planner also *accepts* codes — so a player can load a build they already
have and tweak it — be forgiving, because codes get mangled in transit:

1. Trim whitespace.
2. Starts with `HEAT1.` → strip the prefix, base64url-decode, parse JSON.
3. Starts with `{` → parse it as raw build JSON. Pasting the object works.
4. Otherwise → try base64url-decoding the whole thing anyway. This catches a
   code whose prefix was eaten by whatever it travelled through.
5. Anything that throws is not a build. Say so; do not throw at your caller.

Then treat what you got as untrusted: require `vehicle`, coerce the three
arrays, cap `equipment` at 2 and `perks` at 4, keep `starred` only if it names a
module the build actually contains, and drop everything you do not recognise.

---

## Making the link

```
sentinel://build/<code>
```

All of these are accepted, so you do not have to worry about which one a chat
client mangles into which:

| Form | Note |
|------|------|
| `sentinel://build/<code>` | Canonical. Use this one. |
| `sentinel:build/<code>` | Some clients drop the `//`. |
| `sentinel://<code>` | Route omitted; assumed to be a build. |
| `sentinel:<code>` | Shortest form. |

Matching is case-insensitive, a trailing `/` is ignored, and the payload may be
percent-encoded. Because the code is base64url it needs no escaping in practice.

The `build/` segment exists so the scheme can grow. Use it: a link written
without it still works today, but a link written *with* it will not be ambiguous
with whatever route gets added next.

### If the app is not installed

Nothing happens — a browser silently drops an unregistered scheme, which is a
bad dead end for a player who does not know what the link was for. Put a plain
text copy of the code next to the link, and say what the link needs:

```html
<a href="sentinel://build/HEAT1.…">Open in HEAT Sentinel</a>
<p>No app? <code>HEAT1.…</code> — paste it into Builds → Import.</p>
```

The scheme is claimed by HEAT Sentinel the first time it runs, per user, so
"installed" really means "installed and launched once".

---

## What the player sees

Clicking a link **writes nothing**. It:

1. Opens or focuses HEAT Sentinel and goes to the Builds page for that vehicle.
2. Decodes and validates the build against the player's own copy of the catalog.
3. Puts it in the *incoming* slot, drawn beside whatever is fitted on that tank
   right now — which is the comparison that decides whether they want it.
4. Names anything their client cannot place, and anything their account does not
   own, before they act.

Saving and applying are separate, deliberate clicks after that. This matters to
you in one specific way: **a link naming parts the player does not own is not a
failure.** They are told, and those parts are skipped unless they explicitly
choose to buy them behind a hold-to-confirm showing the exact cost. So you can
publish an aspirational build without worrying that a click will spend somebody's
currency.

**If they already have the build.** A code that decodes to a loadout already in
their saved builds is not imported twice — there would be two cards nobody could
tell apart. Instead the app names the build they have and offers the one thing
that is genuinely different: your `name` and your `starred` module. That is a
good reason to set both.

---

## Compatibility

- `HEAT1.` codes stay readable. New optional fields may be added; a reader that
  ignores unknown fields keeps working.
- A field's meaning will not change under it. A breaking change gets a new
  prefix, and old links keep working.
- The `sentinel://` scheme and the `build/` route are stable.
- Catalog files carry their own `v`. A change that would break a consumer bumps
  it; adding a field does not.
- Technical names come from the game client. If the game ever renames one, that
  is a game-side break, not a format break — and it is exactly why none of this
  uses ids.

Found something wrong, or need a field the catalog does not carry? Open an issue
on the HEAT Sentinel repository.
