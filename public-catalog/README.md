# HEAT Sentinel parts catalog

The vocabulary a build code is written in: every vehicle, module, equipment
item, perk and agent in World of Tanks HEAT, keyed by the technical name that
travels in a `sentinel://build/...` link, with display names for all twelve
languages the game ships.

**If you are building a loadout planner, start with the integration guide:**
[Build links for HEAT Sentinel](../docs/build-share-codes.md). It explains the
link format, the build object, the validation rules, and how to encode a code in
JavaScript or Python. This directory is just the data.

## Files

| File | Holds |
|------|-------|
| `catalog.json` | Manifest: catalog version, generation time, language list, counts, and a SHA-256 per file. |
| `vehicles.json` | Buildable hulls: power budget, agent, equipment slots, and module groups. |
| `equipment.json` | Equipment items: slot, family, names. |
| `perks.json` | Perks: grid row, tier, unlock level, names and descriptions. |
| `agents.json` | Agents: role, their hulls, their perks. |

Static data. Host a copy or fetch and cache it; re-fetch after a game patch and
compare `catalog.json`'s per-file SHA-256 to tell a real update from a re-upload.

## What is not in here

- **No numeric ids.** A build keyed on ids resolves to a *different* build after
  a patch, which is the whole reason the share format uses names. There is
  nothing here to accidentally use.
- **No account data.** The source this is generated from is one player's live
  catalog and carries their ownership, prices, agent levels, skill points and
  currency balances. None of it survives: the generator writes from an
  allow-list and refuses to write at all if a banned key reaches the output.
- **No artwork.** Icon *filenames* are here so you can wire up your own copies.
  The images are the game's and are not redistributed.
- **No balance numbers.** What a module does is the game's to describe. This
  names parts; it does not model them.

## Known gaps

- Around a third of perks carry an empty `name` and `description`, concentrated
  in the upper tiers, plus one equipment variant. The game client publishes no
  strings for those yet. They are real and a build may name them — fall back to
  the technical name. Expect this to shrink.
- Hulls with no module groups (bot stand-ins, unreleased vehicles) are not
  listed: there is no build to make for them.
- An agent with no perks and no vehicles is one the client ships without a grid
  yet.

## Updates

Regenerated from the game client after each patch and committed here, so the
files at `main` are the current vocabulary. Nothing is versioned per game build:
if a part exists in the game, it is in here; if it was removed, it is gone.

To detect a real update, compare the per-file `sha256` in `catalog.json` rather
than the HTTP headers -- a re-upload of identical content will not change them.
`generated` is the wall-clock time of the export, and `v` is the shape version:
a change that would break a consumer bumps it, adding a field does not.

If a patch lands and the catalog has not caught up, or a part is missing or
misnamed, open an issue.
