# Installation and First Launch

[Back to the README](../README.md) | [Русский](ru/installation.md)

## Download

Grab the latest installer from the [Download](../README.md#download) section of the README, or from the [Releases page](https://github.com/OxCone1/HEAT-Sentinel/releases).

## Installation Steps

1. **Run the installer** (`HEAT.Sentinel_<version>_x64-setup.exe`).
2. **Windows SmartScreen will most likely warn you.** This is expected for an unsigned application from a small developer: click "More info", then "Run anyway". Read [Security and Privacy](security-and-privacy.md) to understand exactly why this happens and how you can verify every build yourself.
3. **Launch HEAT Sentinel** from the Start Menu or desktop shortcut and follow the first-launch setup. It asks for your game folder, because the app switches on the interface debugging port in the game's configuration file: that port is how it reads the game's screens. If the game was already running, restart it once.
4. **Play the game.** The tracker runs in the background as long as the app is open and records every battle automatically.

## After Installing

There is no calibration step and nothing to walk through. The first time the game reaches the hangar with the app running, HEAT Sentinel reads your vehicles, their XP, their fitted modules, equipment and perks, and your agents straight from your account data, including tanks you have not played yet. When you change a loadout in the game, the change is picked up on its own.

If a game update ever resets the game's debugging setting, the app notices and restores it, and tells you when the game needs a restart to pick it up.

## Sessions

A session starts automatically with your first battle and carries over across battles (and across app/game restarts) until you end it. Two controls are available in the app:

- **New Session** ends the current session; your next battle starts a fresh one. Existing history is preserved either way.
- **Continue Last Session** re-attaches to the most recently played session, useful if you accidentally started a new one or reopened the app.

Session statistics in the app and overlays always reflect whichever session is currently active.

## Where Your Data Lives

All recorded data (battles, XP, loadouts, marks, settings) is stored in a local database in your Windows user profile. It survives app updates and reinstalls, and it is not removed on uninstall unless you ask for it, so you will not lose your history by upgrading.

## Moving Your Data to a New PC

Everything HEAT Sentinel records lives in one file, `heat_local.db`, kept in this folder:

```
%LOCALAPPDATA%\com.oxcone.heat-sentinel
```

Paste that path into the Explorer address bar to open the folder, then find `heat_local.db` inside it. There is no export step -- that file **is** the export. Copy it to the new machine (USB stick, cloud drive, anywhere), then import it there.

**On the old PC**

1. Quit HEAT Sentinel from the tray icon (right-click, Quit). Copying the file while the app is running can miss your most recent battles.
2. Copy `heat_local.db` somewhere you can reach from the new PC.

**On the new PC**

1. Install and launch HEAT Sentinel at least once, so it creates its own database.
2. Open **Settings -> Processing & Storage**. The storage backend must be set to **Local (SQLite)**.
3. Click **Import** and pick the `heat_local.db` you brought over.
4. Nothing is written yet. The app reads the file and shows what is inside: how many battles, XP records, loadouts and battle details it holds, and how many of those this PC already has.
5. Choose what should happen to records both PCs have (see below), then click **Import**. A progress bar runs to the end, and the capture service restarts afterwards so the new battles appear.

An import only adds to your history -- it never clears it. Battles already on the new PC stay where they are.

### What Gets Imported

| Imported | Not imported |
|----------|--------------|
| Battles, including ones you deleted | App settings |
| Vehicle and agent XP | Overlay layout and hotkeys |
| Vehicle loadouts | Statistics filters |
| Duplicate-detection fingerprints | Player tags |
| Per-tick battle detail (optional) | |

Settings describe the machine they are on, so yours stay exactly as you have set them here. The per-tick battle detail is what powers the detailed view of a single battle; it is by far the largest part of the file, so there is a checkbox to leave it out if you only want the battles themselves.

### Duplicate Records

Every battle carries an id derived from what happened in it and from the play session it happened in. The same battle therefore has the same id in both databases, and two different battles never share one -- which is what makes "do I already have this?" answerable without guesswork.

The dialog shows the overlap per row before you commit, and offers two ways to resolve it:

- **Keep the local record** (default) -- your existing rows win, and only genuinely new ones are added. Importing the same file twice is harmless: the second run adds nothing.
- **Use the imported record** -- the incoming version overwrites yours. Pick this when the file you are importing is the fuller or more recent one. Manual edits you made on this PC to those particular battles are lost.

Either way, the number added and the number that overlapped are reported when it finishes.

### If Something Goes Wrong

| Message | What it means |
|---------|---------------|
| *That is the database this app is already using* | You picked the live file rather than the copy brought from the other PC. |
| *This is a database, but its battles cannot be read* | The file is a SQLite database that HEAT Sentinel did not write. |
| *That file holds no records to import* | The file is one of ours but empty -- most likely a fresh install that never recorded a battle. |

The file you point at is never modified. The app works from a temporary copy of it, so an import that fails part-way leaves both databases exactly as they were, and you can simply try again.

## Updating

The app checks for updates on its own and can install them in place; release notes appear after each update. You can also simply install a newer release on top of the existing one; your data is preserved.
