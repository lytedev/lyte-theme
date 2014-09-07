# -*- coding: utf-8 -*-

"""

"""

import os

from theme_builder.color_scheme import ColorScheme
from theme_builder.theme import Theme

class Compilation():
    """A class for creating a compilation of a theme and color scheme."""
    
    def __init__(self, name, theme=None, color_scheme=None):
        """Compilation constructor."""
        self.name = name

        if color_scheme is None:
            color_scheme = self.name
        if theme is None:
            theme = self.name

        if isinstance(color_scheme, str):
            color_scheme = ColorScheme(color_scheme)
        if isinstance(theme, str):
            theme = Theme(theme)

        self.color_scheme = color_scheme
        self.theme = theme
        self.options = {}

    def export(self, directory, package):
        """Exports the Compilation to a file."""
        directory = os.path.abspath(directory + os.sep + self.name)

        # Create directory if it doesn't exist
        if not os.access(directory, os.F_OK):
            os.mkdir(directory)

        # Make sure we can write to the directory
        if not os.access(directory, os.W_OK):
            raise Exception("Cannot write to directory", directory)

        print("Exporting compilation '%s'" % self.name)
        print("\tTheme: '%s'" % self.theme.name)
        print("\tColor Scheme: '%s'" % self.color_scheme.name)

        self.theme.options.update(self.options)
        self.theme.export(directory, package)

        self.color_scheme.options.update(self.options)
        self.color_scheme.export(directory, package)

        print("\tDone!")
        print()

