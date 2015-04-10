# -*- coding: utf-8 -*-
"""The base Lyte Theme."""

from theme_builder.theme import Theme, theme_dir, icons_dir, basic_theme_templates
from theme_builder.color_scheme import ColorScheme, basic_color_scheme_templates, color_scheme_dir
from theme_builder.color import Color
from theme_builder.compilation import Compilation

# Initialize our theme - see the Theme class for details
theme = Theme("Lyte-Dark", icons_dir("Lyte"), theme_dir("Lyte"), basic_theme_templates("Lyte", "Lyte-Dark"))

# Initialize our color scheme - see the ColorScheme class for details
color_scheme = ColorScheme("Lyte-Dark", color_scheme_dir("Lyte-Old"), basic_color_scheme_templates("Lyte-Old", "Lyte-Dark"))

# Create our compilation using the new theme and color scheme
comp = Compilation("Lyte-Dark", theme, color_scheme)

# Load our options from options.py, this file is huge enough as-is
from .options import options
comp.options = options

# Define our options preprocessor - we have a lot of options
# that need to be built on top of the expected base options for this theme and
# the used templates
def preprocessor(opts):
    """The preprocessor for the Lyte-Dark theme compilation."""

    # Format our tab options
    opts["tab_padding"] = "[{0}, {1}]".format(opts["tab_padding_x"], opts["tab_padding_y"])
    opts["tab_height"] = (opts["tab_padding_y"] * 2) + opts["text_height"] + opts["borders"]

    # Selection a more $fg version of $bg for highlighting
    if "selection" not in opts:
        opts["selection"] = opts["bg"].blend(opts["fg"], 0.2)

    # Tabs have same font size as base by default
    if "tab_font_size" not in opts:
        opts["tab_font_size"] = opts["font_size"]

    # Tooltips are the same
    if "tooltip_font_size" not in opts:
        opts["tooltip_font_size"] = opts["font_size"]

    # You can figure it out
    if "sidebar_font_size" not in opts:
        opts["sidebar_font_size"] = opts["font_size"]

    if "sidebar_heading_font_size" not in opts:
        opts["sidebar_heading_font_size"] = opts["font_size"]

    if "sidebar_heading_font_size" not in opts:
        opts["sidebar_heading_font_size"] = opts["font_size"]

    # Default sidebar indentation
    if "sidebar_indent_x" not in opts:
        opts["sidebar_indent_x"] = 12
    if "sidebar_indent_y" not in opts:
        opts["sidebar_indent_y"] = 4

    # Default sidebar margins
    if "sidebar_margin_x" not in opts:
        opts["sidebar_margin_x"] = 20
    if "sidebar_margin_y" not in opts:
        opts["sidebar_margin_y"] = 1

    # The Lyte theme's staple: indicator borders! but only if they're enabled
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

    # Generate the in-between colors of our background and foreground (our base colors)
    n_alts = 10
    for i in range(1, n_alts):
        opts["fg" + str(i)] = opts["fg"].blend(opts["max_fg"], float(i)/(n_alts-1))
        opts["bg" + str(i)] = opts["bg"].blend(opts["max_bg"], float(i)/(n_alts-1))

    # Format some of the data as expected by the template
    opts["sidebar_indent"] = "[{0}, {1}]".format(opts["sidebar_indent_x"], opts["sidebar_indent_y"])
    opts["sidebar_margin"] = "[{0}, {1}]".format(opts["sidebar_margin_x"], opts["sidebar_margin_y"])

    # Our comment color - $bg blended with a bit of $fg is good enough contrast for comments
    if "comment" not in opts:
        opts["comment"] = opts["bg"].blend(opts["fg"], 0.4)

    # Our "active" color - used throughout the theme heavily
    if "active" not in opts:
        opts["active"] = opts["green"]

    # Our "dirty" color - used throughout the theme
    if "dirty" not in opts:
        opts["dirty"] = opts["red"]

    # Scrollbars same as active color
    opts["scrollbar_color"] = opts["active"]

    # Selection border
    if "selection_border" not in opts:
        opts["selection_border"] = opts["selection"].blend(opts["fg"], 0.5)

    # Find background highlight
    if "find" not in opts:
        opts["find"] = opts["red"].set_alpha(120)

    # Text shadow
    if opts["text_shadow"]:
        opts["text_shadow_color"] = opts["bg"].set_alpha(255)
        opts["text_shadow_offset"] = "[0, 1]"
    else:
        opts["text_shadow_color"] = opts["fg"].set_alpha(0)
        opts["text_shadow_offset"] = "[0, 0]"

    # Sidebar expand/collpase arrows
    if opts["sidebar_arrows"]:
        opts["sidebar_arrow_margin"] = [9, 7, 8, 6]
        opts["sidebar_arrow_opacity"] = 0.3
    else:
        opts["sidebar_arrow_margin"] = 0
        opts["sidebar_arrow_opacity"] = 0

    # Sidebar icons
    if opts["sidebar_icons"]:
        opts["sidebar_icon_margin"] = [8, 8]
        opts["sidebar_icon_opacity"] = 0.3
    else:
        opts["sidebar_icon_margin"] = 0
        opts["sidebar_icon_opacity"] = 0

    opts["opaque_bg"] = opts["bg"].set_alpha(100)
    opts["minimap_overlay"] = opts["fg"].set_alpha(16)

    return opts

# Add our preprocessor to the list - don't overwrite it!
comp.preprocessors.append(preprocessor)
