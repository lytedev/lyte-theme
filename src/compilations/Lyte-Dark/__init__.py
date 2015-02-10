# -*- coding: utf-8 -*-
"""An example compilation module."""

from theme_builder.theme import Theme, theme_dir, icons_dir, basic_theme_templates
from theme_builder.color_scheme import ColorScheme, basic_color_scheme_templates, color_scheme_dir
from theme_builder.color import Color
from theme_builder.compilation import Compilation

theme = Theme("Lyte-Dark", icons_dir("Lyte"), theme_dir("Lyte"), basic_theme_templates("Lyte", "Lyte-Dark"))
color_scheme = ColorScheme("Lyte-Dark", color_scheme_dir("Lyte"), basic_color_scheme_templates("Lyte", "Lyte-Dark"))

comp = Compilation("Lyte-Dark", theme, color_scheme)

from .options import options
comp.options = options

def preprocessor(opts):
    """The preprocessor for the compilation."""

    opts["tab_padding"] = "[{0}, {1}]".format(opts["tab_padding_x"], opts["tab_padding_y"])
    opts["tab_height"] = (opts["tab_padding_y"] * 2) + opts["text_height"] + opts["borders"]

    if "tab_font_size" not in opts:
        opts["tab_font_size"] = opts["font_size"]

    if "tooltip_font_size" not in opts:
        opts["tooltip_font_size"] = opts["font_size"]

    if "sidebar_font_size" not in opts:
        opts["sidebar_font_size"] = opts["font_size"]

    if "sidebar_heading_font_size" not in opts:
        opts["sidebar_heading_font_size"] = opts["font_size"]

    if "sidebar_indent_x" not in opts:
        opts["sidebar_indent_x"] = 12

    if "sidebar_indent_y" not in opts:
        opts["sidebar_indent_y"] = 4

    if "sidebar_margin_x" not in opts:
        opts["sidebar_margin_x"] = 20

    if "sidebar_margin_y" not in opts:
        opts["sidebar_margin_y"] = 1

    if "sidebar_heading_font_size" not in opts:
        opts["sidebar_heading_font_size"] = opts["font_size"]

    if opts["borders"] > 0:
        b = opts["borders"];
        opts["border_border"] = "[0, 0, 0, {0}]".format(b)
        opts["border_border_top"] = "[0, {0}, 0, 0]".format(b)
        opts["border_border_right"] = "[0, 0, {0}, 0]".format(b)
        opts["border_border_left"] = "[{0}, 0, 0, 0]".format(b)
        opts["border_border_everywhere"] = "[{0}, {0}, {0}, {0}]".format(b) # Border in the ground, border in the air
        opts["border_opacity"] = "1.0"
    else:
        opts["border_border"] = "[0, 0, 0, 0]"
        opts["border_border_top"] = "[0, 0, 0, 0]"
        opts["border_border_right"] = "[0, 0, 0, 0]"
        opts["border_border_left"] = "[0, 0, 0, 0]"
        opts["border_border_everywhere"] = "[0, 0, 0, 0]" # Border in the ground, border in the air
        opts["border_opacity"] = "0.0"

    n_alts = 10
    for i in range(1, n_alts):
        opts["fg" + str(i)] = opts["fg"].blend(opts["max_fg"], float(i)/(n_alts-1))
        opts["bg" + str(i)] = opts["bg"].blend(opts["max_bg"], float(i)/(n_alts-1))

    opts["sidebar_indent"] = "[{0}, {1}]".format(opts["sidebar_indent_x"], opts["sidebar_indent_y"])
    opts["sidebar_margin"] = "[{0}, {1}]".format(opts["sidebar_margin_x"], opts["sidebar_margin_y"])
    opts["selection"] = opts["bg"].blend(opts["max_bg"], 0.25)
    opts["comment"] = opts["bg"].blend(opts["fg"], 0.4)
    opts["active"] = opts["cyan"]
    opts["dirty"] = opts["red"]
    opts["scrollbar_color"] = opts["active"]

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

comp.preprocessors.append(preprocessor)
