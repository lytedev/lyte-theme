# -*- coding: utf-8 -*-
"""An example compilation module."""

from theme_builder.theme import Theme, theme_dir, icons_dir, basic_theme_templates
from theme_builder.color_scheme import ColorScheme, basic_color_scheme_templates, color_scheme_dir
from theme_builder.color import Color
from theme_builder.compilation import Compilation

theme = Theme("Lyte-Dark", icons_dir("lyte"), theme_dir("Lyte"), basic_theme_templates("Lyte", "Lyte-Dark"))
color_scheme = ColorScheme("Lyte-Dark", color_scheme_dir("Lyte"), basic_color_scheme_templates("Lyte", "Lyte-Dark"))

comp = Compilation("Lyte-Dark", theme, color_scheme)

comp.options = {
    # Colors

    "bg": Color(16, 16, 16),
    "fg": Color(250, 250, 250),

    "blue":       Color("#77aaff"),
    "red":        Color("#ff7744"),
    "indigo":     Color("#aa77ff"),
    "magenta":    Color("#ff4477"),
    "cyan":       Color("#77ffff"),
    "green":      Color("#aaff44"),

    # Other options
    "sidebar_indent": 12, 

    # Preprocessor options
    "tab_padding_x": 5,
    "tab_padding_y": 5,
    "text_height": 15,
    "borders": True,
    "text_shadow": True,
    "sidebar_arrows": True, 
    "sidebar_icons": True, 
}

def preprocessor(opts):
    """The preprocessor for the compilation."""  

    opts["tab_padding"] = "[{0}, {1}]".format(opts["tab_padding_x"], opts["tab_padding_y"])
    opts["tab_height"] = (opts["tab_padding_y"] * 2) + opts["text_height"]

    if opts["borders"]: 
        opts["border_border"] = "[0, 0, 0, 1]"
        opts["border_border_top"] = "[0, 1, 0, 0]"
        opts["border_border_right"] = "[0, 0, 1, 0]"
        opts["border_border_everywhere"] = "[1, 1, 1, 1]" # Border in the ground, border in the air
        opts["border_opacity"] = "1.0"
    else:
        opts["border_border"] = "[0, 0, 0, 0]"
        opts["border_border_top"] = "[0, 1, 0, 0]"
        opts["border_border_right"] = "[0, 0, 0, 0]"
        opts["border_border_everywhere"] = "[0, 0, 0, 0]" # Border in the ground, border in the air
        opts["border_opacity"] = "0.0"

    # opts["bg" + str(i)] = opts["bg"] / 0.5

    opts["bg1"] = opts["bg"] + 8
    opts["fg1"] = opts["fg"] - 8

    for i in range(2, 10):
        opts["bg" + str(i)] = opts["bg"] + (26 * (i - 1))
        opts["fg" + str(i)] = opts["fg"] - (16 * (i - 1))

    opts["comment"] = opts["bg"].blend(opts["fg"], 0.4)

    if opts["text_shadow"]:
        opts["text_shadow_color"] = opts["bg"].set_alpha(255)
        opts["text_shadow_offset"] = "[0, 1]"
    else:
        opts["text_shadow_color"] = opts["fg"].set_alpha(0)
        opts["text_shadow_offset"] = "[0, 0]"

    if opts["sidebar_arrows"]: 
        opts["sidebar_arrow_margin"] = [9, 7, 8, 6]
        opts["sidebar_arrow_opacity"] = 0.3
    else:
        opts["sidebar_arrow_margin"] = 0
        opts["sidebar_arrow_opacity"] = 0

    if opts["sidebar_icons"]: 
        opts["sidebar_icon_margin"] = [8, 8]
        opts["sidebar_icon_opacity"] = 0.3
    else:
        opts["sidebar_icon_margin"] = 0
        opts["sidebar_icon_opacity"] = 0

    opts["opaque_bg"] = opts["bg"].set_alpha(100)
    opts["minimap_overlay"] = opts["fg"].set_alpha(16)

    return opts

comp.preprocessor = preprocessor
