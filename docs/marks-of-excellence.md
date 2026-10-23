# Marks of Excellence

[Back to the README](../README.md) | [Русский](ru/marks-of-excellence.md)

Marks of Excellence live under **Battles > MoE**. Each tank can earn up to **three marks**, based on how much damage per minute you deal compared with other players in the same tank and the same game mode.

## How It Works

- **Damage per minute, not damage per battle.** A long battle and a quick stomp are put on the same footing, so there is no reward for stalling a match to farm damage.
- **Per tank and per mode.** Each battle is weighed against what regular players do in that tank and that mode, so a hard tank or a low-damage mode does not hold you back.
- **Your standing is your recent form.** It is the average of your last 50 countable battles in that tank. A new tank builds up from its very first game.
- **Mark lines** sit at the 65th, 85th and 95th percentile of regular players. Marks are **held, not permanent**: drop back under a line and that mark goes until you earn it back.
- **What counts:** PvP battles in the modes the calibration pack lists. Versus AI battles, other modes and bot-filled matches are left out. In a battle where you swapped tanks, only the tank you started in counts, and only for its own share of the battle. The tank's detail view lists every battle that was left out and exactly why.
- **Your record is protected.** Editing or deleting a battle never changes your marks.

## In the App

- Every tank's row shows its marks, its average on the scale, the battle that drops out of the window next, and what the next mark needs: either the damage rate for one battle, or a number of battles at your current level.
- Open a tank for its trend over the window, with each battle's gain or loss. Click a battle on the chart to open it in the battle list.
- **Click a mark stripe** to aim for that mark: the per-mode DPM targets and the in-battle projection follow it.
- A notification tells you when a mark is earned or lost (it can be turned off in Settings).
- The **Recent balance** button shows the notes for the latest calibration changes.

On the overlays, the Marks of Excellence element shows the tank you are in and, during a battle, projects where that battle would leave your average. It is available on the in-game overlay and the stream overlay.

## Calibration Packs

The numbers behind the marks (the damage baseline, the mark lines, each tank's and each mode's factor, the bot limit, the modes that count) are not built into the app. They come from **calibration packs** published in the [`moe/`](../moe/) folder of this repository, together with notes on what changed. The app checks for a new pack every half hour, and each battle is always scored with the pack that was in force on the day it was played.

Packs are tuned from real battle data and from community feedback. If a tank feels too easy or too hard, say so on the [Discord server](https://discord.gg/AjfcuhDDw5).

## The Public Marks Page

**[oxcone1.github.io/HEAT-Sentinel/marks](https://oxcone1.github.io/HEAT-Sentinel/marks/)** shows the current pack in the browser, no app needed: the mark lines, every tank's and mode's factor, and a battle calculator that answers "what does a mark actually cost on this tank?". It reads the same packs from this repository, so it is always up to date.
