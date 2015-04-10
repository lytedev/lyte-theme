# -*- coding: utf-8 -*-
"""Create a Light version of our Lyte-Dark theme."""

from theme_builder.color import Color
from theme_builder.compilation import Compilation

# Create our compilation with a unique name
comp = Compilation("Lyte-Light")

# Copy everything from the given theme name
comp.copy_all("Lyte-Monokai")

# Use the light icons
comp.theme.set_iconset("Lyte-Light")

# Modified theme options - we really just flip the background and foreground colors
# The theme processor will take care of everything else
new_options = {
    # Base Colors
    "fg":         Color(16, 16, 16),
    "bg":         Color(250, 250, 250),
    "max_fg":     Color(120, 120, 120),
    "max_bg":     Color(128, 128, 128),
}

for x in new_options:
    comp.options[x] = new_options[x]

# Need more info as to what's going on? Check out this theme's parent theme, Lyte-Dark
