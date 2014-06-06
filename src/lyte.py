#!/bin/python

"""A script for building .tmTheme syntax highlight themes for Sublime Text 3.

See `theme_builder.py`.

"""

import theme_builder as tb
import pprint as pp

def generate():
    #Template-building scheme

    template_file = "Lyte"
    output_theme_file = "Lyte"

    opts = {
     "bg":      "#111111",
     "fg":      "#f8f8f8",
     "comment": "#777777",
     "dark1":   "#1d1d1d",
     "dark2":   "#222222",
     "dark3":   "#333333",
     "dark4":   "#444444",

     "blue":    "#77aaff",
     "red":     "#ff7744",
     "indigo":  "#aa77ff",
     "magenta": "#ff4477",
     "cyan":    "#77ffff",
     "green":   "#aaff44"
    }

    template, _ = tb.format_template(template_file, opts)
    tb.write_theme("../" + output_theme_file, template)

    # Generate for Widgets also - nobody likes non-matching text inputs.
    template, _ = tb.format_template("Lyte", opts)
    # Here, we don't use write_theme because that only allows .tmTheme files.
    f = open("../Widgets.stTheme", 'w')
    f.write(template)
    f.close()

    print("Done.")

"""

Alternative generation schematic based on hue rotation

"""

def old_generate():
    # Change these as desired.
    bg_color					= "#111"
    contrast_ratio 				= 1
    highlight_contrast_factor 	= 0.5
    small_saturation_factor		= 5
    primary_hue 				= 205
    saturation_factor			= 0.8

    # Template-building scheme

    import theme_builder as tb
    import pprint

    contrast = 1 - contrast_ratio
    highlight_contrast = contrast * highlight_contrast_factor
    saturation = 100 * saturation_factor

    bg = tb.Color(bg_color)
    fg = bg.invert().blend(bg, contrast)
    hl = fg.blend(bg, 1 - highlight_contrast)

    primary = fg.saturate(saturation).hue(primary_hue) # Blue
    secondary = primary.mod_hue(170) # Red/Orange
    tertiary = primary.mod_hue(100).saturate(saturation * 0.8) # Magenta
    quadrary = primary.mod_hue(-135) # Green
    quintary = quadrary.mod_hue(-25) # Indigo?

    opts = {
        "background": bg,
        "caret": fg.reverse_blend(bg, 0.01),
        "foreground": fg,
        "line_highlight": hl,
        "selection": hl.blend(fg, 0.20).saturate(small_saturation_factor).hue(primary_hue),
        "selection_border": hl.blend(fg, 0.30).saturate(small_saturation_factor).hue(primary_hue),
        "bracket_highlight_foreground": fg,
        "variable": primary,
        "inherited_class": primary,
        "tag": primary,
        "class": primary,
        "keyword": primary.saturate(saturation * 0.3),
        "argument": secondary,
        "diff_delete": secondary,
        "function_definition": secondary,
        "support_class": secondary.saturate(saturation * 0.6),
        "numeric": tertiary,
        "diff_insert": quadrary,
        "lang_constant": quadrary,
        "user_constant": quadrary,
        "support_constant": quadrary,
        "storage": quadrary.saturate(saturation * 0.6),
        "support_function": quadrary.saturate(saturation * 0.6),
        "attribute": quadrary.saturate(saturation * 0.6),
        "string": quintary.saturate(saturation * 0.6),
        "diff_changed": quintary,
        "invalid_bg": tb.Color("#a30"),
        "invalid_fg": tb.Color("#fff"),
        "invalid_bg_dep": tb.Color("#620"),
        "invalid_fg_dep": tb.Color("#fff"),
        "diff_head": fg.blend(bg, 0.5),
        "comment": bg.blend(fg, 0.4)
    }

    template,_ = tb.format_template("LyteOld", opts)
    tb.write_theme("LyteOld", template)
    pp.pprint(_)

generate();
