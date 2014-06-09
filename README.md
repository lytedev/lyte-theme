# Lyte Theme

Lyte is a minimal, aesthetically pleasing theme for Sublime Text. Don't believe me? Check it out.

![Lyte Theme clean][3]

* **Font**: Consolas 9
* **Color Scheme**: Lyte (included in this theme)

Lyte also contains a simple Python script for constructing .tmTheme syntax highlighting files. Hopefully soon it will also contain functionality for constructing .sublime-theme Sublime theme files!

## Installation

### Package Controls

**Note**: Not yet available!

If you have the Package Control plugin installed, you can install this theme via the `Package Control: Install Package` command. Then look for the `Theme - Lyte` listing and install it!

### Git

If you'd like easier access to the code, to keep up to date faster, or customize the syntax highlighting, I highly suggest using Git to install the theme.

Open your Packages directory with the command `Preferences: Browse Packages`. While in the Packages directory, you just need to clone the repo as follows:

	git clone https://github.com/lytedev/lyte-theme/ Lyte

## Usage

### Theme

Add this to your `Preferences: Settings - User` file:

    "theme": "Lyte.sublime-theme",

You will need to restart Sublime for all changes to take effect.

### Syntax Highlighting

Add this to your `Preferences: Settings - User` file:

    "color_scheme": "Packages/Lyte/Lyte.tmTheme",

But you probably already have syntax highlighting you prefer. =) Hopefully this theme fits it well! If not, I suggest changing your syntax highlight background to `#111111`. Should make a world of difference.

### Customization

If you're looking to customize the theme, I suggest installation via the Git method. Once you have access to the files, check out `Lyte.sublime-theme` and two python scripts in the `src` directory, `lyte.py` and `theme_builder.py`.

### Recommendations

This is just my preference, but I very much prefer a clean environment. This theme, though made with everybody in mind, must have some bias towards my preferences. So, if you like what's in the screenshot, here are some of the more important preferences I use. Add them to your `Preferences: Settings - User`:

    "color_scheme": "Packages/Lyte/Lyte.tmTheme",
    "theme": "Lyte.sublime-theme",
	"overlay_scroll_bars": "enabled",
	"show_tab_close_buttons": false,
    "draw_minimap_border": false,
    "enable_tab_scrolling": false,
    "fade_fold_buttons": false,
    "font_face": "Consolas",
	"highlight_line": true,
    "font_size": 9,
    "caret_style": "phase",

## Credits

* Inspired by the [Nexus theme][1] and the [Devastate theme][2]
* Icons are shameless edits of the icons in the [Nexus theme][1]

[1]: https://github.com/EleazarCrusader/nexus-theme
[2]: https://github.com/vlakarados/devastate
[3]: https://raw.githubusercontent.com/lytedev/lyte-theme/master/assets/screenshots/lyte-theme-small-clean.png
