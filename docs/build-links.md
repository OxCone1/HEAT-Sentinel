# Build Links

[Back to the README](../README.md) | [Русский](ru/build-links.md)

## Sharing a build

Any build in HEAT Sentinel can leave the app as a **share code** -- one line of
text -- or as a **build link**:

```
sentinel://build/HEAT1.eyJ2IjoxLCJ2ZWhpY2xlIjoi...
```

Send either to anyone. Clicking a link opens HEAT Sentinel, decodes the build
against your own game data, and shows it beside whatever is fitted on that tank
right now. Nothing is written until you press Apply.

**Builds > Export** gives you both: *Copy code* for places that mangle links,
*Copy link* for everywhere else. To take one in, use **Builds > Import**, or
just click a link.

A build travels as the parts it is made of, and nothing else. Names of modules,
equipment and perks, the vehicle, your label for it, and the module you starred
as the point of the build. **Not** the battles, win rate or damage behind it --
a record is earned, not transferred, and it accumulates the more its owner plays.

**A link never spends anything.** A build naming parts you do not own is not
applied silently: those parts are listed and skipped, and buying them takes a
separate hold-to-confirm that shows the exact cost.

**If you already have the build**, the app names which of your builds it is and
offers to take the sender's label and starred module -- rather than making a
second card you cannot tell from the first.

The `sentinel:` scheme is claimed for your Windows user the first time HEAT
Sentinel runs. If a link does nothing, the app has not been installed and
launched yet -- paste the code into Builds > Import instead.

## Building from scratch

The **Build Composer** designs a loadout from nothing, or starts from a fitted
vehicle or any saved or past build. It enforces the energy budget, the
equipment slots and the one-legendary / one-perk-per-group limits live as you
build, so whatever it produces can be applied as it is.

## For loadout planner sites

If you run a build planner on the web, you can hand players a link instead of a
list of module names to copy across by hand. It needs no API key, no server and
no partnership: a build link is a string you generate offline.

- **[Build links for HEAT Sentinel](build-share-codes.md)** -- the
  integration guide. The link format, the build object, the rules a valid build
  follows, and encoders in JavaScript and Python.
- **[`public-catalog/`](../public-catalog/)** -- the vocabulary, as JSON. Every
  vehicle, module, equipment item, perk and agent, keyed by the technical name a
  code is written in, with display names in all twelve languages the game ships.

The catalog carries no account data, no numeric ids and no artwork, and is
regenerated after game patches. `catalog.json` holds a SHA-256 per file, so you
can tell a real update from a re-upload.
