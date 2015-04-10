# -*- coding: utf-8 -*-
"""An example compilation module."""

from theme_builder.color import Color
from theme_builder.compilation import Compilation

comp = Compilation("Lyte-Solarized")
comp.copy_all("Lyte-Monokai")

new_options = {
    # Colors
    "bg":         Color("#002b36"),
    "fg":         Color("#fdf6e3"),
    "max_bg":     Color("#657b83"),
    "max_fg":     Color("#839496"),

    "red": Color("#dc322f"),
    "orange": Color("#cb4b16"),
    "yellow": Color("#b58900"),
    "green": Color("#859900"),
    "cyan": Color("#2aa198"),
    "blue": Color("#268bd2"),
    "indigo": Color("#6c71c4"),
    "brown": Color("#d33682"),
}

for x in new_options:
    comp.options[x] = new_options[x]


