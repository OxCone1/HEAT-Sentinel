# Overlays: In-Game and Stream (OBS)

[Back to the README](../README.md) | [Русский](ru/overlays.md)

HEAT Sentinel has two separate overlays. The **in-game overlay** is drawn by the app on top of the game itself and is for you, the player. The **stream overlay** is a browser page meant for OBS and is for your viewers. They are configured independently and can be used together or on their own.

## In-Game Overlay

The in-game overlay is a transparent window that sits over the game and shows live information while you play.

- **Open the editor** from the Overlay tab in the app, or toggle the overlay with the global hotkey (rebindable in Settings; if the default combination is already taken by another app on your machine, no hotkey is bound and Settings will say so, so pick your own).
- **Hide it in one keystroke.** The hide hotkey (Ctrl+Shift+H by default, rebindable on the Overlay tab) takes the overlay off screen until you press it again, without switching it off or touching your layout. There is also a Hide overlay button next to Edit layout.
- **Add elements** from the "add element" menu:
  - stat tiles and strips (session and all-time win rate, K/D, damage, placement, battle count, best damage, streaks); middle-click a tile in the editor to switch it between the whole session and the tank you are in;
  - module gauges for vehicle abilities such as the SIS-90 (M1E1) and the PDU-1546S Combat Reboot (XM1 90), with the bar or the number switchable off;
  - **Team composition**: both rosters as class icons filled to each vehicle's remaining health, coloured by side and platoon. Hold ALT in battle to expand it to tank names and HP, or keep it open;
  - **Marks of Excellence** for the tank you are in (compact, meter or full, with a custom row layout) and **Marks: Goal**, which shows the target line, the DPM you need and what your last battle did;
  - free text.
- **Arrange and style** every element: drag, resize, recolour, merge several tiles into one continuous plate (and split them again), and align with optional snap-to-grid (off by default, toggled from the magnet icon in the toolbar).
- **Set visibility rules** so an element only appears when it is relevant, for example while aiming down the gunner sight, in chase camera, or only during an active round.
- **Capture it in OBS** if you want: turn on "Show in taskbar" in Settings > Overlay and the overlay becomes a window OBS can capture. Use this only for OBS.

## Stream Overlay (OBS)

While the app is running, the stream overlay is served on your PC at:

```
http://localhost:17504/overlay
```

Open it in any browser to enter the editor. The sidebar contains an element palette and the overlay settings. It is only reachable from the same PC the app runs on.

## Editing Basics

- **Add elements** by clicking them in the palette. Categories include: All-Time, Session, Recent, Agents, Tanks, Marks of Excellence, Maps, Streak, XP / Levels and Decoration.
- **Move and resize** elements by dragging them or their handles on the canvas.
- **Style** the overlay in Settings: canvas resolution, win/loss/draw colors, element background color and opacity, grid and snapping, tank images and agent portraits, language.
- **Presets** let you save and switch between layouts; layouts can also be exported as a shareable string.

## Setting Up the Overlay in OBS (Step by Step)

1. **Open the overlay** at `http://localhost:17504/overlay` in your browser.
2. **(Optional but recommended) Upload an alignment image.** In the sidebar, open Settings, find the Alignment section, and upload a screenshot of your game. Adjust its opacity. This puts your game screen behind the canvas so you can position elements precisely over the actual game UI.
3. **Turn on sync.** In Settings, set **Sync** to **"Sync upload"**. Your layout changes are now pushed to every consumer running in "Sync download" mode.
4. **Arrange your layout** the way you want it.
5. **Add a Browser source in OBS**, placed **above all other sources** in your scene:
   - URL: `http://localhost:17504/overlay`
   - Width and height: your screen resolution (for example 1920 x 1080)
6. **Switch the OBS copy to download mode.** Select the Browser source in OBS and click "Interact". In the interaction window, open the sidebar Settings and set **Sync** to **"Sync download"**. The OBS copy now automatically pulls the layout from your browser tab.
7. **Enter transparency mode.** Once you are done, still in the interaction window, press the round button in the bottom-right corner of the overlay, or flip the switch on the floating control bar next to it. The editor background and UI disappear, leaving only your elements on a transparent background: this is what your stream shows. The corner button stays visible in the interaction window, so you can always switch back to editor mode.
8. **Edit in real time.** Keep the browser tab open and make changes there; the OBS source picks them up automatically within seconds. When you are happy with the layout, remove the alignment image.

That is the whole trick: your browser tab is the editor, the OBS source is the display, and the sync keeps them in step while you stream.
