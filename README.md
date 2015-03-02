# Lyte Theme

Lyte is a set of themes for Sublime Text with fancy-schmancy border file status indicators that aims to be minimal, flat, and retina ready.

![Lyte-Dark Theme][9]

* **Font**: Monaco
* **Color Scheme**: Lyte-Dark (included in this theme)

![Lyte-Light Theme][10]
![Lyte-Solarized][11]
![Lyte-Solarized-Light][12]

## Installation

### Package Controls

If you have the Package Control plugin installed, you can install this theme via the `Package Control: Install Package` command. Then look for the `Theme - Lyte` listing and install it!

If you *don't* have the Package Control plugin, well, you just should. [Here are the installation instructions.][4]

### Git

If you'd like easier access to the code, to keep up to date faster, or customize the syntax highlighting or theme files, I highly suggest using Git to install the theme.

Open your Packages directory with the command `Preferences: Browse Packages`. While in the Packages directory, you just need to clone the repo as follows:

    git clone https://github.com/lytedev/lyte-theme/ "Theme - Lyte"

## Usage

Add this to your `Preferences: Settings - User` file:

    "theme": "Lyte-Dark.sublime-theme",

Or, for the included alternatives,

    "theme": "Lyte-Light.sublime-theme",
    "theme": "Lyte-Solarized.sublime-theme",
    "theme": "Lyte-Solarized-Light.sublime-theme",

You will need to restart Sublime for all changes to take effect.

## Syntax Highlighting

Add this to your `Preferences: Settings - User` file:

    "color_scheme": "Packages/Theme - Lyte/Lyte-Dark/Lyte-Dark.tmTheme",

Or, for the included alternatives,

    "color_scheme": "Packages/Theme - Lyte/Lyte-Light/Lyte-Light.tmTheme",
    "color_scheme": "Packages/Theme - Lyte/Lyte-Solarized/Lyte-Solarized.tmTheme",
    "color_scheme": "Packages/Theme - Lyte/Lyte-Solarized-Light/Lyte-Solarized-Light.tmTheme",

But you probably already have syntax highlighting you prefer. =) Hopefully this theme fits it well! If not, I suggest changing your syntax highlight background to `#111111`. Should make a world of difference.

## Customization

If you're looking to customize the theme, I suggest installation via the Git method. Once you have access to the files, check out `Lyte.sublime-theme` and two python scripts in the `src` directory, `lyte.py` and `theme_builder.py`.

TODO: Explain the theme-building process.

## Recommendations

This is just my preference, but I very much prefer a clean and dark environment. This theme, though made with everybody in mind, has some bias towards my preferences. So, if you like what's in the first screenshot, here are some of the more important preferences I use. Add them to your `Preferences: Settings - User`:

    "color_scheme": "Packages/Theme - Lyte/Lyte-Dark/Lyte-Dark.tmTheme",
    "theme": "Lyte-Dark.sublime-theme",
    "overlay_scroll_bars": "enabled",
    "show_tab_close_buttons": false,
    "draw_minimap_border": false,
    "enable_tab_scrolling": false,
    "fade_fold_buttons": true,
    "highlight_line": true,
    "caret_style": "phase",
    "highlight_modified_tabs": true, 

## Credit

* Inspired by the [Nexus theme][1] and the [Devastate theme][2]
* Most icons are shameless edits of the icons in the [Nexus theme][1]

## Changelog

See [`CHANGELOG.md`](CHANGELOG.md)

## License

This theme is licensed under the [Creative Commons Attribution-ShareAlike 3.0 License][6]. You are free to share and remix the theme, however please abide by the license terms when doing so.

The following details apply to the Creative Commons license "author specified" components:

* Attribution example: Based on the Lyte theme by [@lytedev](https://github.com/lytedev)

* Naming guidelines: If you create and distribute a derivative theme, please give your theme a unique and original name that does not directly include "Lyte" (or a close variant) in the main project title, repo name or Package Control name.

[1]: https://github.com/EleazarCrusader/nexus-theme
[2]: https://github.com/vlakarados/devastate
[4]: https://sublime.wbond.net/installation
[6]: http://creativecommons.org/licenses/by-sa/3.0/
[7]: https://github.com/jisaacks/GitGutter
[9]: https://raw.githubusercontent.com/lytedev/lyte-theme/master/screenshots/dark.png
[10]: https://raw.githubusercontent.com/lytedev/lyte-theme/master/screenshots/light.png
[11]: https://raw.githubusercontent.com/lytedev/lyte-theme/master/screenshots/solarized-dark.png
[12]: https://raw.githubusercontent.com/lytedev/lyte-theme/master/screenshots/solarized-light.png
