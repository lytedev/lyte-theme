# -*- coding: utf-8 -*-
"""An example compilation module."""

from theme_builder.color import Color
from theme_builder.compilation import Compilation

comp = Compilation("Lyte-Solarized-Light")
comp.copy_all("Lyte-Solarized")

new_options = {
    # Colors
    "fg":         Color("#002b36"),
    "bg":         Color("#fdf6e3"),
    "max_fg":     Color("#657b83"),
    "max_bg":     Color("#839496"),
}

for x in new_options:
    comp.options[x] = new_options[x]
