# -*- coding: utf-8 -*-
"""An example compilation module."""

from copy import copy
from theme_builder.compilation import Compilation

# This compilation depends on the Lyte-Dark compilation.
dark_comp_module = __import__("compilations." + "Lyte-Dark", globals(), locals(), ["comp"], 0)
dark_comp = getattr(dark_comp_module, "comp", None)

comp = Compilation("Lyte")

comp.theme.options = copy(dark_comp.theme.options)
comp.color_scheme.options = copy(dark_comp.color_scheme.options)
comp.options = copy(dark_comp.options)

comp.color_scheme.options["ColorSchemeName"] = "Lyte"
comp.theme.options["ThemeName"] = "Lyte"

__all__ = ["comp"]
