# Lyte Theme

![Lyte Theme clean][3]

[Alternative screenshot with all default preferences except theme and color_scheme][4]

Lyte is a minimal, aesthetically pleasing theme for Sublime Text 3.

Lyte also contains a simple Python script for constructing .tmTheme syntax highlighting files. Hopefully soon it will also contain functionality for constructing .sublime-theme Sublime theme files!

## Installation

### Package Control

**Note**: Not yet available!

If you have the Package Control plugin installed, you can install this theme via the `Package Control: Install Package` command. Then look for the `Theme - Lyte` listing and install it!

### Git

If you'd like easier access to the code, to keep up to date faster, or customize the syntax highlighting, I highly suggest using Git to install the theme.

Open your Packages directory with the command `Preferences: Browse Packages`. While in the Packages directory, you just need to clone the repo as follows:

	git clone https://github.com/lytedev/lyte-theme/ Lyte

## Usage

### Theme

Add this to your `Preferences: Settings - User` file:

    "color_scheme": "Packages/Lyte/Lyte.tmTheme",

You will need to restart Sublime for all changes to take effect.

### Syntax Highlighting

Add this to your `Preferences: Settings - User` file:

    "color_scheme": "Packages/Lyte/Lyte.tmTheme",

But you probably already have syntax highlighting you prefer. =) Hopefully this theme fits it well! If not, I suggest changing your syntax highlight background to `#111111`. Should make a world of difference.

### Customization

If you're looking to customize the theme, I suggest installation via the Git method. Once you have access to the files, check out `Lyte.sublime-theme` and two python scripts in the `src` directory, `lyte.py` and `theme_builder.py`.

## Credits

* Inspired by the [Nexus theme][1] and the [Devastate theme][2]
* Icons are shameless edits of the icons in the [Nexus theme][1]

[1]: https://github.com/EleazarCrusader/nexus-theme
[2]: https://github.com/vlakarados/devastate
[3]: https://raw.githubusercontent.com/lytedev/lyte-theme/master/assets/screenshots/lyte-theme-small-clean.png
[4]: https://raw.githubusercontent.com/lytedev/lyte-theme/master/assets/screenshots/lyte-theme-fhd-grid.png
