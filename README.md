
# CollexDesign Assets Library

A community-driven library of presets, templates, and starter projects for **[CollexDesign](https://collexdesign.metchi.workers.dev/)** a browser-based vector and assets editor

This repo is not an app on its own. It's a plain, browsable collection of `.json` project/preset files that CollexDesign can import directly, so presets can be added, updated, and shared independently of the app's own release cycle.

## What's in here

Each preset lives in its own folder and typically contains:

-   **`<name>.json`** the actual preset/project file, in CollexDesign's native project format. This is the file the app imports.
-   **`preview.png`** a quick visual reference so you know what the preset looks like before importing it.
-   **`README.md`** a short description of the preset: what it is, when to use it, and any notes specific to that asset.

Presets are grouped into top-level categories (e.g. `AppPresets/`), each with its own `README.md` explaining what belongs in that category.

## How to use a preset

1.  Browse the folders above to find something you want.
2.  Open CollexDesign: **[collexdesign.metchi.workers.dev](https://collexdesign.metchi.workers.dev/)**
3.  Use the app's **online import (ctrl o)** feature and point it at the preset's `.json` file (or browse this library directly from inside the app, if that's enabled).
4.  The preset loads as a new project you can edit freely importing never modifies anything in this repo.

## Contributing a preset

Want to add your own? Pull requests are welcome.

1.  Create a new folder under the right category (or propose a new category if nothing fits).
2.  Add your `.json` project file, a `preview.png`, and a short `README.md` describing it.
3.  Keep the JSON as the exported/native CollexDesign format, don't hand-edit it into something the app can't parse.
4.  Open a PR. Please don't include anything you don't have rights to distribute (fonts, images, etc.) keep presets original or properly licensed.

## Why a separate repo?

Keeping presets here instead of bundling them into the app means:

-   New presets can be added anytime, without waiting on an app release.
-   The library stays lightweight and easy to browse on GitHub itself.
-   Anyone can fork or contribute without touching CollexDesign's core code.

## Links

-   App: [collexdesign](https://collexdesign.metchi.workers.dev/)
- Discord: [Collex](https://discord.gg/RFNVxd6TzD)
