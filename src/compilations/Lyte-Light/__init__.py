# -*- coding: utf-8 -*-
"""An example compilation module."""

from theme_builder.color import Color
from theme_builder.compilation import Compilation

comp = Compilation("Lyte-Light")
comp.copy_all("Lyte-Dark")
comp.theme.set_iconset("Lyte-Light")
print(comp.theme.icons_directory)

new_options = {
    # Colors
    "fg":         Color(16, 16, 16),
    "bg":         Color(250, 250, 250),
    "max_fg":     Color(120, 120, 120),
    "max_bg":     Color(128, 128, 128),

    "blue":       Color("#004488"),
    "red":        Color("#ff6600"),
    "indigo":     Color("#aa00ff"),
    "magenta":    Color("#cc0066"),
    "cyan":       Color("#00aaff"),
    "green":      Color("#33aa00"),
}

for x in new_options:
    comp.options[x] = new_options[x]
