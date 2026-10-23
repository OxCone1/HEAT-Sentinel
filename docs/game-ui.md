# Game UI: In-Game Customization

[Back to the README](../README.md) | [Русский](ru/game-ui.md)

The **Game UI** tab changes the game's own interface. Everything here is applied to a running game within moments and comes back on its next launch. None of it reveals anything the game does not already show you.

## Battle HUD

Hide individual interface elements from a checklist: battle HUD parts, radar layers, vehicle nameplate rows, kill-feed entry types, world markers, capture bars, parts of the aim circle, event and mission panels, and elements on the Tab/scoreboard, map, deploy and hangar screens. Save a set of hidden elements as a named preset and switch between presets at any time.

## Sight (Custom Reticles)

The **Sight** tab applies **reticle packs**: complete redesigns of your crosshair, reload, magazine, overheat gauge and second gun, drawn beneath the game's HUD so every other widget stays on top.

- **A public catalogue.** The included reticles come from the [`reticles/`](../reticles/) folder of this repository, so new and updated designs arrive without an app update. Each pack fits every gun in the game: single-shot guns, drums and carousels, long magazines, heat-based guns and two-gun vehicles (the gun not firing is dimmed).
- **Your placement.** Each pack has its own on/off switch, placement (including a fixed aim point placement, where the frame stays still and the gun marker settles into it), a **Pack size** slider and a **Spread circle size** slider. The spread circle follows the game's own rule exactly.
- **Keep what you like.** Choose which of the game's own crosshair parts stay on screen alongside the pack.
- **Design your own with [Sight Forge](https://oxcone1.github.io/HEAT-Sentinel/forge/).** A browser tool that draws reticles with the same renderer the app uses in the game, runs a simulated gun underneath so you can see every reload and magazine state, and, while HEAT Sentinel is running, previews your design live on your battle HUD as you edit it.
- **Get featured.** Finished a design you are proud of? Share it on the Discord server or open a pull request against [`reticles/`](../reticles/) (see [Contributing](contributing.md)) and it can join the catalogue for everyone.

## Colors

A **COLORS** tab appears inside the game's own Settings screen, next to GAMEPLAY, VIDEO, AUDIO, MOUSE and CONTROLS. It covers vehicle markers, capture points, the HUD and the scoreboard, and comes with a preset strip and colour-blindness profiles (protanopia, deuteranopia, tritanopia). The same controls are in the app under Game UI > Colors.

- Save colours as named presets, switch between them, and export a preset as a share code for someone else to import.
- Clip team colours to the battlefield nameplates only, leaving the compass, kill feed, battle log, scoreboard and results screen on the game's own colours.
- Switch all overrides off without losing the colours you picked.

## Tags

Tag the players you meet: **Dangerous**, **Low skill**, **Friend**, **Hmmm**, **Hunt down** and **Charge**. Tag someone straight from the game, by clicking their nickname to open the game's own player menu, or in the app by right-clicking a player on a battle's scoreboard or a rival card.

- Tag icons appear next to the nickname on the in-game Tab scoreboard and the post-battle tables, and above their vehicle in battle while you hold the extended-info key.
- The game has room for three icons per player, so you choose each player's priority order. Icons can be recoloured to stay readable, and one switch turns all marking off.
- The killed-by card shows your lifetime 1v1 record against the player who destroyed you.
- Tags are private to your PC.

## Friends

A **SENTINEL FRIENDS** tab is added to the game's own hangar menu. It lists everyone you tagged as a friend, shows who is online, and sends a squad invite without leaving the game. Turn it on or off from Game UI > Friends.

## Notifications

Battle alerts for the moments the ping wheel does not cover, aimed at playing with random teammates who have no microphone.

- **Cover requests.** Call *Need cover* and see which allies are coming and how far away they are, either on one rangefinder ruler or as one chip per ally. Choose who may answer your request (your platoon, allies, tagged groups), in priority order, and whether tracking stops after a set time.
- **Help requests.** When an ally calls for help, their request shows so you can answer with *Moving to support*, or take it on automatically from the groups you choose. Hold the extended-info key to see nicknames.
- **Charger alert.** A warning in the middle of the screen when an ally you tagged **Charge** drives straight at you. The bar shrinks and turns from green to red as they close in, with the live distance. Set the watch radius, and optionally watch every other ally too, with stricter rules: on a collision course, fast, close and not braking, so a teammate rolling past or driving into cover next to you does not set it off.
- **Priority.** Drag the alerts into the order you want when two want the screen at once. The game's own alerts always come first.

Alerts hide while you are dead and during an ultimate's full-screen view.

## Minimap

- **Map on radar.** The real map is drawn under the radar, with adjustable strength, and moves smoothly with you. It follows the level you are on: drive into a bunker and the radar shows that bunker's own layout. It uses the map packs installed in the Tactics Board add-on. Level detection does not work in Kill Confirmed.
- **Class icons and level arrows.** Every dot on the radar and the tactical map gets its vehicle class icon, with a small arrow when that vehicle is above or below you. Enemies show only while the game itself shows them.

## QOL

Helpers that press the game's own menu buttons for you, and nothing else:

- **Auto-ready** as a platoon member when you get back to the lobby after a battle.
- **Auto-search** as the platoon leader, starting the battle search once every member is ready (with an optional grace window).
- **Platoon marks.** The game only marks your own platoon. This labels every platoon in the match, on both teams, on the Tab scoreboard and the results screens: letters for allied platoons, numbers for enemy ones.
- **Platoon range lines.** A thin line under each platoon mate in the platoon panel with their distance in metres. It fills as they come closer and greys out while they are dead or respawning.
- **Post-battle fast skip** (off by default). Leaves each post-match screen as soon as it appears and takes you straight back to the lobby, optionally stopping on the results overview. Nothing is lost: the battle is still recorded, and the game keeps the last results to reopen.
