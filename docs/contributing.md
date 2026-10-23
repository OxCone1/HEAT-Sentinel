# Contributing

[Back to the README](../README.md) | [Русский](ru/contributing.md)

The application itself is closed source, but everything that makes it work across languages, game versions and tastes is open and lives in this repository. Contributions are very welcome:

- **Reticles** for the [`reticles/`](../reticles/) catalogue. One folder per reticle, named after its id, holding a `reticle.json` manifest, the drawing (a pack exported from [Sight Forge](https://oxcone1.github.io/HEAT-Sentinel/forge/) is the easiest route) and an optional `preview.png`. Every reticle needs a stated `license`; if you did not draw it, you need the author's permission and credit. The manifest fields are documented in [`reticles/schema/reticle.schema.json`](../reticles/schema/reticle.schema.json).
- **Localisation**: translations of app strings and of the game data tables in [`game_locales/`](../game_locales/) and [`configs/`](../configs/)
- **Game data updates** after game patches
- **Marks of Excellence feedback**: tanks or modes that feel off, with battles to back it up
- **Calibrations and patterns** for new resolutions and game languages (see [Section 9](how-it-reads-the-game.md#calibrations-and-patterns))
- **Documentation** fixes and improvements

Open an issue to discuss an idea, or submit a pull request directly. If you found a bug in the app itself, an issue with steps to reproduce is the way to go.
