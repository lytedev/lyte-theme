# Lyte Theme

Lyte is a minimal, aesthetically pleasing theme for Sublime Text with fancy-schmancy border status indicators. Don't believe me? Check it out.

![Lyte Theme clean][3]

Maybe you don't like fancy-schmancy border status indicators, but you like flat, dark minimalism.

![Lyte Theme NoBorder][8]

* **Font**: Consolas 9
* **Color Scheme**: Lyte (included in this theme)
* **Icons in Gutter**: [Git Gutter Plugin][7]

Lyte also contains a simple Python script for constructing .tmTheme syntax highlighting files. Hopefully soon it will also contain functionality for constructing .sublime-theme Sublime theme files!

## Installation

### Package Controls

If you have the Package Control plugin installed, you can install this theme via the `Package Control: Install Package` command. Then look for the `Theme - Lyte` listing and install it!

If you *don't* have the Package Control plugin, well, you just should. [Here are the installation instructions.][4]

### Git

If you'd like easier access to the code, to keep up to date faster, or customize the syntax highlighting, I highly suggest using Git to install the theme.

Open your Packages directory with the command `Preferences: Browse Packages`. While in the Packages directory, you just need to clone the repo as follows:

    git clone https://github.com/lytedev/lyte-theme/ "Theme - Lyte"

## Usage

### Theme

Add this to your `Preferences: Settings - User` file:

    "theme": "Lyte.sublime-theme",

Or, for no colorful indicator borders,

    "theme": "Lyte-NoBorder.sublime-theme",

You will need to restart Sublime for all changes to take effect.

### Syntax Highlighting

Add this to your `Preferences: Settings - User` file:

    "color_scheme": "Packages/Theme - Lyte/Lyte.tmTheme",

But you probably already have syntax highlighting you prefer. =) Hopefully this theme fits it well! If not, I suggest changing your syntax highlight background to `#111111`. Should make a world of difference.

### Customization

If you're looking to customize the theme, I suggest installation via the Git method. Once you have access to the files, check out `Lyte.sublime-theme` and two python scripts in the `src` directory, `lyte.py` and `theme_builder.py`.

### Recommendations

This is just my preference, but I very much prefer a clean environment. This theme, though made with everybody in mind, must have some bias towards my preferences. So, if you like what's in the screenshot, here are some of the more important preferences I use. Add them to your `Preferences: Settings - User`:

    "color_scheme": "Packages/Theme - Lyte/Lyte.tmTheme",
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

If you don't like the colored border indicators, you can edit the theme and basically change all `layer1.opacity` values to 0. Or istead of `"theme": "Lyte.sublime-theme",`, use `"theme": "Lyte-NoBorder.sublime-theme",` in your User Settings.

## Credits

* Inspired by the [Nexus theme][1] and the [Devastate theme][2]
* Icons are shameless edits of the icons in the [Nexus theme][1]

## Changelog

See [`CHANGELOG.md`](CHANGELOG.md)

## License

This theme is licensed under the [Creative Commons Attribution-ShareAlike 3.0 License][6]. You are free to share and remix the theme, however please abide by the license terms when doing so.

The following details apply to the Creative Commons license "author specified" components:

* Attribution example: Based on the Lyte theme by [@lytedev](https://github.com/lytedev)

* Naming guidelines: If you create and distribute a derivative theme, please give your theme a unique and original name that does not directly include "Lyte" (or a close variant) in the main project title, repo name or Package Control name.

[1]: https://github.com/EleazarCrusader/nexus-theme
[2]: https://github.com/vlakarados/devastate
[3]: https://raw.githubusercontent.com/lytedev/lyte-theme/master/screenshots/lyte-theme-small-clean-file-folder-icons.png
[4]: https://sublime.wbond.net/installation
[6]: http://creativecommons.org/licenses/by-sa/3.0/
[7]: https://github.com/jisaacks/GitGutter
[8]: https://raw.githubusercontent.com/lytedev/lyte-theme/master/screenshots/lyte-theme-small-clean-file-folder-icons-noborder.png
