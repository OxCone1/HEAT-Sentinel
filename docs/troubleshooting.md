# Troubleshooting

[Back to the README](../README.md) | [Русский](ru/troubleshooting.md)

If a new version will not install or the app misbehaves after an update, work through these steps in order. Most update problems come from an old copy still running in the background.

1. **In-app update did not work? Download from GitHub directly.** If the built-in updater fails to apply a release, grab the installer straight from the [Releases page](https://github.com/OxCone1/HEAT-Sentinel/releases) and run it yourself.

2. **Installing over an existing version.** When you run the downloaded `.exe`:
   - **Preferably choose "Add or repair components"** (the repair option) if the installer offers it.
   - If that option is not shown, choose **"Do not uninstall"**. Do not remove the existing install first.

3. **Update still did not go through? Close every instance of HEAT Sentinel.** This means **both** the main app (HEAT Sentinel) **and** the capture engine (`heat-capture`). Open **Task Manager** and confirm that neither process is still running before trying the installer again.

4. **Still stuck? Uninstall the app first, then reinstall.** During uninstall there is a **second step** with an option to delete application data. **Do NOT click "delete application data."** Leaving it unchecked preserves your battle history and settings. After uninstalling, install the fresh release.

5. **Nothing above helped? Reboot and start over.** Restart your PC, then run the installer from the beginning.

6. **The app says it cannot reach the game after a game update?** Restart the game once. Game updates can reset the debugging setting the app reads through; the app restores it, but the game only picks it up on its next start.

7. **If none of this works, send your logs.** The logs are in `%LOCALAPPDATA%\HEAT Sentinel\logs`. Archive them into a single archive (`.zip` / `.7z`) and send it to the **Discord server** or to the developer's **personal DMs**. Both links are available on the **About page inside the app**.
   - If the archive is too large for Discord's file upload limit, upload it to any file exchange service and paste the link instead.
