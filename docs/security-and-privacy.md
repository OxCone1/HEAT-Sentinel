# Security and Privacy

[Back to the README](../README.md) | [Русский](ru/security-and-privacy.md)

The "great, another crypto miner" jokes are funny, and honestly fair as far as random internet executables go. But I take the security aspect seriously, so here is the full picture:

- **Every release is built by GitHub Actions.** No hand-built binaries from a random machine; the build pipeline is reproducible automation.
- **Every release is scanned on VirusTotal.** Each published build, both the app installer and the bundled capture engine, is uploaded to VirusTotal, and the scan links are published right in the [Download](../README.md#download) section of the README.
- **Updates are signed.** The in-app updater only installs a release whose signature matches the key built into the app.

## About Antivirus False Positives

The data capture engine is Python code compiled with **Nuitka** into a folder of ordinary program files. It used to be packed with PyInstaller into one self-extracting executable, a format some antivirus vendors flag generically because malware uses it too; moving to Nuitka removed most of those false positives. If you still see a handful of detections with generic names on an otherwise clean report, this is almost certainly why. The full report is always linked, judge for yourself.

## About Windows SmartScreen

SmartScreen warns about the installer because it is not code-signed. Code signing certificates cost serious money per year, which is not reasonable for a free hobby project, so the warning is unavoidable for now. "More info", then "Run anyway". The VirusTotal reports above exist precisely so you do not have to take my word for it.

## Privacy

- **No account, no registration.** The app never asks you to sign up for anything.
- **All data is stored locally** in a database on your machine: battles, XP, loadouts, marks, tags, settings.
- **Nothing is shared with anyone.** There is no telemetry and no data collection.
- **The local server stays on your PC.** The overlays are fed by a small server inside the app that only accepts connections from the same computer.

## What Goes Over the Network

Out of the box, only downloads, and none of them carry your data:

- the update check against this repository's releases;
- the Marks of Excellence calibration packs and the reticle catalogue, fetched from this repository;
- Discord Rich Presence, if enabled, which talks to the Discord app on your own PC.

The add-ons stay off until you switch them on:

- **Tactics Board** downloads the map packs you install from this repository. The map on the radar uses the same packs.
- **HEAT Snap** downloads the public streamer list from this repository, and talks to Twitch with the account you connect: it checks who in your battle is live and creates the clips.
- **HEAT Sabotage** talks to Twitch with the channel you connect: it manages the channel-point rewards it created and posts the chat lines you set.

The full details are in the [Privacy Policy](../PRIVACY.md).
