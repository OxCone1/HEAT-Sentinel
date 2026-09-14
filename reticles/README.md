# Shipped reticles

The gun sights the app installs alongside itself. They appear in the tray under
**Included reticles**, and applying one reads it straight out of this folder.

**Drawing a sight? Start here:** [Making a sight for HEAT
Sentinel](../docs/making-a-sight.md) — the coordinate system, the three formats,
how to anchor a picture to the aim point, and how to test it. This file is only
the folder format.

**Or use the builder:** [Sight
Forge](https://oxcone1.github.io/HEAT-Sentinel/forge/) draws a reticle with the
game's own renderer, runs a gun under it so the gated states can be seen, and
writes the `reticle.json` below along with the drawing. Source:
[`heat-forge/`](../heat-forge/README.md).

## What ships

Eight reticle packs (`kind: pack`). Each one is a single file that fits every gun
in the roster. It uses `when` gates to split single-shot guns (`magazine_max: 1`),
drums and carousels (per-round cells), long magazines (one gauge plus a count),
heat guns (`heat_gun`, `overheated`) and the second gun (`source: "secondary"`).
Each one arrives with `opts.show: "always"`, because the pack hides the native
loader and has to redraw it in third person as well as in the optic.

| id | What it looks like |
|---|---|
| `field-standard` | The stock HUD with the gaps filled in: the game's arcs, colours and spread circle, plus a per-round refill timer, a ready count, a heat gauge and the second gun |
| `recon-minimal` | Hairlines: the spread circle with ranging ticks riding outside it, and side tapes for ammo and heat |
| `neon-drift` | Cyan to magenta: a glowing reload ring on the spread circle, a fan of rounds, chromatic numbers |
| `brass-belt` | Drawn cartridges that fill from the base as they load, and a slim brass-to-red heat strip |
| `phosphor` | A fighter-jet head-up display: a gun cross on the spread circle and a data block beside it |
| `blueprint` | A technical drawing: registration marks, reload as a dimension line, rounds as outlined boxes |
| `ember` | Quiet and warm: the spread circle as four soft arcs, a vermilion dot, rounds as beads outside the bloom |
| `lockbox` | Amber electronics: double chevrons on the diagonals that close with the spread |

**The spread circle follows the game's own rule**: `max(spread, 30)` px across on
a `Common` crosshair, read out of the Battle HUD bundle, and every pack hides the
native aim-circle layers it redraws. The player's **Spread circle size** slider
(`opts.spread_scale`, 0.75 to 3) scales it from there.

**Loaders fill the way the game's do.** The primary run is the game's
`rotation 184.5, CounterClockwise`: first round at the bottom, climbing, each
round filling from its bottom end. The secondary, on the left, is bottom first
and clockwise.

## Layout

One folder per reticle. The folder name is the reticle's id, and the id is the
address it is stored and applied by — so renaming a folder is a breaking change
for anybody who applied it.

```
reticles/
  index.json                  generated; do not hand-edit
  schema/
    index.schema.json
    reticle.schema.json
  mil-ladder/
    reticle.json              the manifest
    sight.blk                 the drawing (or art.svg, art.png, pack.json)
    preview.png               optional thumbnail, shown in the tray
```

## The manifest

`reticle.json`, minimal:

```json
{
  "v": 1,
  "id": "mil-ladder",
  "name": "Mil ladder",
  "file": "sight.blk",
  "license": "CC-BY-4.0"
}
```

Everything else is optional: `author`, `source` (where the drawing came from,
for credit), `description`, `preview`, `tags`, `kind`, `unitRef`, `opts` (the
placement you recommend, applied *with* the reticle) and `image` (the anchor
and framing for a picture reticle). Field-by-field documentation lives in
[`schema/reticle.schema.json`](schema/reticle.schema.json).

`kind` is `blk`, `svg`, `image` or `pack`. Leave it out and it is inferred from
the extension and then from the file's own bytes — the same order the tray uses
when a user picks a file, so a reticle cannot ship as something other than what
an import would call it.

`svg` is vector art. It is flattened to drawable shapes on import rather than
handed to the game as a document, so it scales cleanly and can be recoloured;
convert text to outlines and flatten filters before exporting, because neither
converts. See [making-a-sight.md](../docs/making-a-sight.md) for the full list.

## The index

`index.json` is **generated**. It exists so the app reads one document instead
of walking a directory laid down by an installer, where a half-copied folder
would be a failure mode. Its shape mirrors
`sentinel-repo/public-catalog/catalog.json`: a version, a generation time,
counts, and a `bytes` + `sha256` per shipped file, so an update can be told
from a re-upload.

```bash
py scripts/build_reticle_index.py           # validate and write
py scripts/build_reticle_index.py --check   # fail if stale (what the build runs)
```

The generator refuses anything it cannot ship: an `id` that does not match its
folder, a `file` that is not a plain name inside that folder, a missing file, a
manifest with no `license`.

## What the app does with this

Nothing special, and that is the design. A shipped reticle is a **pointer to a
file on disk**, which is exactly what a sight the user picked themselves is —
so it applies, reloads and reports its file health through code that was
already there. An install with no reticles answers an empty list, and every
other part of the sight feature carries on.

`watcher/settings/sight.py` reads the index (repository in a dev tree,
`WOT_HEAT_BUNDLE_DIR` in an install), `GET /ui/sight` serves it as `builtin`,
and `PUT /ui/sight/apply` with `{"builtin": "<id>"}` applies one.

## Licensing

Every reticle needs a stated `license`, because an installer redistributes it.
If you did not draw it, get the author's permission, name them in `author`, and
link the original in `source`. "Found it on a forum" is not a licence.
