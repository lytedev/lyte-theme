# -*- coding: utf-8 -*-

"""Sublime Text 3 syntax theme/color scheme builder/helper.

This module is a part of the lyte theme for Sublime Text 3 and is used primarily for
constructing the syntax highligh color scheme.

Really, the only functionality this module offers is super-simple manipulation of
colors. My goal was to have simply a single primary (highlight) color and a general
idea of contrast and saturation and have a color scheme generated based on that. It
works alright, but hand-picking my colors was still working better for me. But who
knows. Somebody may find this script useful.

Example:
    See `lyte.py` for in-depth examples

        import theme_builder as tb
        primary_color = tb.Color("#2af")
        background = tb.Color("#111")
        foreground = background.invert()
        opts = {
            "background": background,
            "foreground": foreground,
            "keyword": primary_color,
            "string": primary_color.mod_hue(90),
            "comment": background.blend(fg)
        }
        template,_ = tb.format_template("my_template", opts)
        tb.write_theme("my_theme", template)

    Where `templates/my_template.tmTheme-template` would essentially be a .tmTheme
    file with `{background}`, `{foreground}`, `{comment}` etc. placeholders
    that would be replaced with the associated values in the `opts` dict. See
    string.format() and the Format Specification Mini-Language Python documentation
    for details.

    https://docs.python.org/2/library/functions.html#format

    Again, the existing `templates/lyte2.tmTheme-template` file is a good example.

"""

"""API Versioning and Documentation

See `README.md`

"""

