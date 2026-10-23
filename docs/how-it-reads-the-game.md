# How HEAT Sentinel Reads the Game

[Back to the README](../README.md) | [Русский](ru/how-it-reads-the-game.md)

## Main Mode

HEAT Sentinel reads game values directly from the game client's own interface: the same numbers that are already drawn on your screen. The game's interface is built like a web page, and the game ships with a debugging port for it; the app switches that port on in the game's configuration file and reads the interface through it. No screenshots, no image recognition, no guessing. This makes it fast, exact and independent of your screen resolution and game language.

Important: the app only ever reads information that is already visible to you during normal play. It does not touch the game's memory, does not modify the game's executables, and does not expose anything hidden. See the [Disclaimer](../README.md#fair-play-and-disclaimer).

## Legacy OCR (Reserve)

Unofficial tools live at the mercy of game updates. Before the main mode existed, HEAT Sentinel read the game from screenshots, and that pipeline, **Legacy OCR**, is kept in reserve in case a future patch ever closes the main mode off. It no longer ships inside the installer (dropping it made the download roughly 180 MB smaller), and the app always uses the main mode.

How Legacy OCR works, for the curious:

1. **Screen watching.** Screenshots of the game at the right moments (lobby, end-of-battle screens, module screens).
2. **Pattern matching.** Small reference images, called **patterns**, recognize which screen is currently visible.
3. **Text recognition.** An OCR engine reads the text from specific regions of the screenshot. Where exactly each value lives is defined by **calibrations**.
4. **Parsing.** The recognized values are assembled into the same battle records the main mode produces.

All of it runs locally; screenshots never leave your PC. Its limits are why it is the reserve and not the default: it depends on screen resolution and game language, and it sees far less than the main mode.

## Calibrations and Patterns

These two words belong to Legacy OCR. The files live in this repository so the reserve path stays ready.

### Calibrations

A calibration is a JSON file (created with the LabelMe annotation tool) paired with a reference screenshot. It marks rectangles on the screen and labels them: "this box is the damage number", "this box is the player name", and so on. The OCR engine only reads inside those boxes, which is what makes recognition reliable.

Calibrations exist per screen type, per resolution, per game language. Naming convention:

```
<screen>_<width>x<height>_<LANG>.json      e.g. personal_1920x1080_EN.json
```

Screen types covered: lobby, team score screens (5v5 and 10v10), personal result, modules.

### Patterns

A pattern is a small cropped PNG image used to recognize which game screen is currently displayed and to anchor the reading positions. Naming convention:

```
<name>_pattern_<width>x<height>_<LANG>.png   e.g. lobby_pattern_1920x1080_EN.png
```

### What Exists Today

A **1920x1080 English** calibration and pattern set. Other resolutions and game languages are welcome from the community.

### Contributing New Calibrations

1. Download **Light-LabelMe** (`labelme.exe`) from the [Releases page](https://github.com/OxCone1/HEAT-Sentinel/releases). It is a trimmed build of the LabelMe annotation tool used to create all existing calibrations.
2. Take clean screenshots of each relevant game screen at your resolution and language.
3. Open a screenshot in Light-LabelMe and draw labeled regions, using the existing `1920x1080_EN` files in this repository as the reference for which labels are expected.
4. Crop the matching pattern images.
5. Submit a pull request to this repository following the naming conventions above, or open an issue and attach your files if pull requests are not your thing.
