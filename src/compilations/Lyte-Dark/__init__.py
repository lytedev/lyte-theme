# -*- coding: utf-8 -*-
"""An example compilation module."""

from theme_builder.theme import Theme, theme_dir, icons_dir, basic_theme_templates
from theme_builder.color_scheme import ColorScheme, basic_color_scheme_templates, color_scheme_dir
from theme_builder.color import Color
from theme_builder.compilation import Compilation

theme = Theme("Lyte-Dark", icons_dir("lyte"), theme_dir("Lyte"), basic_theme_templates("Lyte", "Lyte-Dark"))
color_scheme = ColorScheme("Lyte-Dark", color_scheme_dir("Lyte"), basic_color_scheme_templates("Lyte", "Lyte-Dark"))

comp = Compilation("Lyte-Dark", theme, color_scheme)

tab_padding = 5, 5

if isinstance(tab_padding, int):
    tab_padding = (tab_padding, tab_padding)

options = {
    # Colors
    "fg":         Color("#f8f8f8"),
    "comment":    Color("#777777"),
    "bg":         Color(17, 17, 17),
    "secondary1": Color(25, 25, 25),
    "secondary2": Color("#222222"),
    "secondary3": Color("#333333"),
    "secondary4": Color("#444444"),
    "blue":       Color("#77aaff"),
    "red":        Color("#ff7744"),
    "indigo":     Color("#aa77ff"),
    "magenta":    Color("#ff4477"),
    "cyan":       Color("#77ffff"),
    "green":      Color("#aaff44"),

    "tab_padding": "[{0}, {1}]".format(tab_padding[0], tab_padding[1]),
    "tab_height": (tab_padding[1] * 2) + 15,
}

comp.theme.options.update(options)
comp.color_scheme.options.update(options)
