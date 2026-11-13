# Add-ons

The add-on catalog HEAT Sentinel shows under **Add-ons > Browse add-ons**.

- `index.json` lists every add-on and its releases. The app reads it, checks each release
  against your app version and your game version, and offers the newest one that fits.
- `<id>/<id>-<version>.heataddon` are the add-on files. Each one is signed; the app checks
  the signature after download, the same way it checks a file you install by hand.

Game versions in `index.json` are constraints that must all hold, for example
`"game": [">=1.2", "<1.4"]`. `=1.2` matches every 1.2.x release of the game.

Installed add-ons are checked for updates a minute after the app starts and every few hours
after that. Updates install on a click, or on their own when "Update add-ons automatically"
is on (never while the game is running).

You can still install a `.heataddon` file you were given with **From file**.
