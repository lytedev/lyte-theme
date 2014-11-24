# -*- coding: utf-8 -*-
"""An example compilation module."""

from theme_builder.color import Color
from theme_builder.compilation import Compilation

comp = Compilation("Lyte-Solarized")
comp.copy_all("Lyte-Dark")

new_options = {
    # Colors
    "bg":         Color("#002b36"),
    "fg":         Color("#fdf6e3"),
    "max_bg":     Color("#657b83"),
    "max_fg":     Color("#839496"),

    "blue":       Color("#268bd2"),
    "red":        Color("#b58900"),
    "indigo":     Color("#6c71c4"),
    "magenta":    Color("#d33682"),
    "cyan":       Color("#2aa198"),
    "green":      Color("#859900"),
}

for x in new_options:
    comp.options[x] = new_options[x]


