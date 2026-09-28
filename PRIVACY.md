# Privacy Policy

**Application:** WoT: HEAT Sentinel ("HEAT Sentinel", "the app")
**Publisher:** OxCone ("we", "the developer")
**Last updated:** 28 September 2026

WoT: HEAT Sentinel is an unofficial statistics gathering app. It is not affiliated with, endorsed by, or sponsored by Wargaming Group Limited. All in-game assets and trademarks belong to their respective owners.

---

## 1. Summary

HEAT Sentinel has no accounts, no registration, no telemetry, no analytics and no advertising. Everything the app records is written to your own machine. We operate no server that receives your battle data, and we cannot read your statistics.

A few things do involve a network, and all of them are described in full in [Section 4](#4-network-activity): the update check against GitHub, the optional Discord Rich Presence integration, the optional HEAT Snap add-on (off by default), and the local overlay server that serves data to your browser or OBS.

---

## 2. Scope

This policy covers the HEAT Sentinel desktop application for Windows and this documentation repository. It does not cover World of Tanks: HEAT itself, Wargaming services, Discord, GitHub, OBS, or any other third-party product you use alongside the app. Those services are governed by their own privacy policies.

---

## 3. Data the app processes and stores locally

HEAT Sentinel reads information that the game already displays to you during normal play and keeps it so that it is not lost when the game discards it. The following categories are stored on your computer:

| Category | Examples |
|----------|----------|
| Battle records | Outcome, map, mode, vehicle, agent, damage, assistance, kills, personal and team performance figures |
| Progression | XP totals and history, session aggregates, all-time aggregates |
| Loadouts and configuration | Vehicle loadouts, modules, consumables detected in the hangar |
| Player identifiers shown in game | Your in-game nickname, and the nicknames of platoon mates and other players as they appear on battle result screens |
| Head-to-head and platoon records | Per-map and per-player records derived from the battle data above |
| Application data | Settings, overlay layouts and colours, calibration and pattern files, log files |

In Legacy OCR capture mode the app takes screenshots of the game window in order to read numbers from them. Those screenshots are processed on your machine and are not transmitted anywhere. The default capture mode does not use screenshots at all: it reads the game's own interface state directly on your computer.

The app does not read, collect or store your Wargaming credentials, email address, payment information, chat messages, voice audio, keystrokes outside its own windows, or any file outside its own data directories.

### Where the data lives

All writable data is stored under your Windows local application data directory:

```
%LOCALAPPDATA%\com.oxcone.heat-sentinel\
```

This includes `heat_local.db` (the statistics database), `config.json`, your calibrations and patterns, overlay settings and log files.

### Retention and deletion

Data is kept until you delete it. There is no expiry and no remote copy. To remove everything, uninstall the app and delete the directory listed above. Deleting that directory removes your entire statistics history permanently and cannot be undone.

---

## 4. Network activity

### 4.1 Update check

The app checks for new versions by requesting a release manifest from GitHub:

```
https://github.com/OxCone1/HEAT-Sentinel/releases/latest/download/latest.json
```

This request carries no battle data and no identifier created by the app. As with any HTTP request, GitHub receives your IP address and standard request metadata, handled under GitHub's own privacy policy. Updates are signed and verified against a public key bundled with the app.

### 4.2 Discord Rich Presence (optional, enabled by default)

If Discord is running on the same machine, the app can publish what you are currently playing to your Discord profile: vehicle, map, game mode and, if the score option is enabled, live score information. This is sent to Discord over its local inter-process channel, and Discord then displays it to whoever can see your profile according to your Discord settings.

Both the integration and the score display are on by default and can be turned off at any time in Settings. With Discord not running, or the integration disabled, nothing is published. Once data reaches Discord it is subject to Discord's privacy policy, not this one.

### 4.3 Local overlay server

The capture engine runs an HTTP server on port `17504` and a WebSocket server on port `17505` so that the in-game overlay and OBS browser sources can display live data. These servers listen on all network interfaces, not only the loopback address, and they do not require authentication.

In practice this means any device on the same local network that can reach those ports can read the live battle and statistics data the overlay uses. On a home network this is normally what makes the OBS setup work from a second machine. On a shared, public or untrusted network, restrict the ports with your firewall, or close the app while on that network.

Nothing on these ports is reachable from the internet unless you deliberately forward the ports on your router.

### 4.4 HEAT Snap (optional add-on, off by default)

HEAT Snap creates Twitch clips of streamers you meet in battle. It does nothing until you switch it on under Add-ons and connect your own Twitch account. While it is on:

- **Streamer list.** The app downloads the public streamer list, curated by the developer, from this repository (`heatsnap/streamers.json`) at launch, every few hours, and each time the HEAT Snap window is opened. The request carries nothing about you.
- **Twitch sign-in.** You approve the connection on twitch.tv in your own browser. HEAT Snap asks only for permission to create clips (`clips:edit`). The resulting tokens are stored encrypted in your local database and are sent only to Twitch. Signing out revokes them.
- **Live check.** When a player on the streamer list is in your battle, the app asks Twitch whether that streamer's channel is live. Twitch receives the channel names being checked, from your Twitch account. Players who are not on the list are never looked up.
- **Clips.** When you destroy a listed streamer who is live, or one destroys you, the app asks Twitch to create a clip of that streamer's broadcast. The clip is created on your Twitch account, like a clip made on twitch.tv, and appears in your Twitch clip manager. Your list of clips, with the map and vehicles involved, is kept in your local database.

Nothing about your battles is sent to Twitch beyond the channel being clipped. Twitch handles this data under its own privacy policy. Switching the add-on off stops all of it.

### 4.5 Links to external sites

The app contains links to GitHub, the community Discord server, Twitch and donation pages. Following a link opens your browser and hands you over to that site, which then applies its own policies. No data from the app is attached to those links.

### 4.6 What the app does not send

The app does not upload your database, screenshots, logs or settings. There is no crash reporting service, no analytics SDK, no advertising identifier, and no profile of you held by the developer. Nothing is sold, rented or shared with third parties, because nothing is collected in the first place.

---

## 5. Data about other players

Battle result screens contain the nicknames and performance figures of other players in your match. When the app records a battle, those values are stored in your local database as part of your own record of the match. They are visible only to you, are never transmitted by the app, and are exactly the information the game already showed you on screen.

The HEAT Snap streamer list is the one exception to "local only": it is a public file in this repository that links a streamer's in-game account id, or in-game nickname, to their Twitch channel. The developer curates it, and a streamer may be on it without having asked, because they have streamed HEAT publicly and their in-game nickname was visible on that stream. To opt out, message the developer on Discord at <https://discord.com/users/376062591480365068> (the same link is on the About page in the app) and the entry is removed. The next time any user opens HEAT Snap, it is gone.

If you publish screenshots, exported data or overlay captures yourself, you are responsible for whatever they reveal about other players.

---

## 6. Contributions to this repository

This repository accepts community contributions: calibration data, screen patterns, game data and localisation files. The HEAT Snap streamer list is kept by the developer; see Section 5.

Anything you submit through a pull request or issue becomes publicly visible, including your GitHub username and the contents of the files, and remains part of the public repository history. Before submitting, check that screenshots, calibration images and sample data do not contain your nickname, friend list, Discord overlay, browser tabs or anything else you would rather not publish. Do not include personal information in contributed files.

---

## 7. Children

HEAT Sentinel is not directed at children. It is a companion tool for a game with its own age requirements, and it collects no information from anyone.

---

## 8. Security

Every release is built by GitHub Actions rather than on a personal machine, and every published build is scanned on VirusTotal with the report linked in the README. The installer is not code-signed, which is why Windows SmartScreen warns about it. Details are in the Security and Privacy section of the [README](./README.md).

The app is provided "as is", without warranty of any kind. Because all data is local, protecting it is ultimately a matter of the security of your own machine and your own backups.

---

## 9. Future online features

A hosted platoon exchange service, which would let platooned players share live combat state with each other, is currently a design document and is not implemented in any released version. No such feature is active in the app today.

If an online feature is ever released, it will be opt-in, it will require an explicit action by you, and this policy will be updated before that release with a description of the data involved, where it is stored and how long it is kept.

---

## 10. Your choices

- Turn Discord Rich Presence, or just the score display, off in Settings.
- Leave HEAT Snap off, or switch it off under Add-ons. Sign out of Twitch in its window to revoke its access.
- Restrict or block ports `17504` and `17505` in your firewall if you do not use the browser or OBS overlays.
- Switch capture mode between the default direct-read mode and the Legacy OCR mode in the app configuration.
- Delete `%LOCALAPPDATA%\com.oxcone.heat-sentinel\` to erase all stored data.
- Uninstall the app at any time.

---

## 11. Changes to this policy

This policy may be updated as the app changes. The date at the top reflects the most recent revision, and the full history of edits is visible in this repository's commit log. Material changes, in particular any change that introduces transmission of data off your machine, will be announced in the release notes.

---

## 12. Contact

- Issues and questions: [github.com/OxCone1/HEAT-Sentinel/issues](https://github.com/OxCone1/HEAT-Sentinel/issues)
- Community Discord: [discord.gg/AjfcuhDDw5](https://discord.gg/AjfcuhDDw5)
