# -*- coding: utf-8 -*-
"""

"""

import os, copy

from .color_scheme import ColorScheme
from .theme import Theme

class Compilation():
    """A class for creating a compilation of a theme and color scheme."""

    def __init__(self, name, theme=None, color_scheme=None):
        """Compilation constructor."""
        self.name = name

        # If no color scheme or theme is provided, we'll try to load one using
        # the current Compilation name.
        if color_scheme is None:
            color_scheme = self.name
        if theme is None:
            theme = self.name

        # If we were given strings (or we're trying to autoload based on
        # Compilation name), let's try to load 'em up.
        # TODO: Fancy error checking?
        if isinstance(color_scheme, str):
            color_scheme = ColorScheme(color_scheme)
        if isinstance(theme, str):
            theme = Theme(theme)

        self.color_scheme = color_scheme
        self.theme = theme
        self.options = {}
        self.preprocessors = list([lambda x: x])

    def export(self, directory, package, opts=None):
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

        # Run the options preprocessor if they weren't given to get options
        if opts is None:
            opts = self.preprocess_options()

        # Apply options to the theme and export it
        opts.update(self.theme.options)
        self.theme.export(directory, package, opts)

        # Apply options to the color scheme and export it
        opts.update(self.color_scheme.options)
        self.color_scheme.export(directory, package, opts)

        print("\tDone!")

    def preprocess_options(self, options=None):
        """Check if a preprocessors function reference exists and call it."""

        # Copy in any given options
        if options is None:
            opts = copy.copy(self.options)
        else:
            opts = copy.copy(options)

        # Run any specified options preprocessor functions
        # (This lets themes extend option functionality)
        for pp in self.preprocessors:
            if callable(pp):
                pp(opts)

        return opts

    def copy_all(self, compilation, key="comp"):
        """Inherit all options from another compilation."""

        # If we were given a string, try to load a Compilation using the string
        if isinstance(compilation, str):
            compilation = Compilation.get_by_name(compilation, key)

        if not isinstance(compilation, Compilation):
            raise Exception("Compilation.inherit() arg 1 must be of type" + \
                "Compilation or a valid string referencing a submodule in " + \
                "the `compilations` module.")

        # Copy the theme and color scheme from the compilation
        self.theme = copy.copy(compilation.theme)
        self.color_scheme = copy.copy(compilation.color_scheme)

        # Copy other important data from the compilation
        self.theme.icons_directory = compilation.theme.icons_directory
        self.theme.options = copy.copy(compilation.theme.options)
        self.color_scheme.options = copy.copy(compilation.color_scheme.options)
        self.options = copy.copy(compilation.options)

        # Fake the inherited data names
        self.color_scheme.options["ColorSchemeName"] = self.name
        self.theme.options["ThemeName"] = self.name

        # More name fakery
        self.theme.theme_templates = copy.copy(compilation.theme.theme_templates)
        for k in self.theme.theme_templates:
            self.theme.theme_templates[k] = self.theme.theme_templates[k].replace(compilation.theme.options["ThemeName"], self.name)

        # Even more name fakery
        self.color_scheme.color_scheme_templates = copy.copy(compilation.color_scheme.color_scheme_templates)
        for k in self.color_scheme.color_scheme_templates:
            self.color_scheme.color_scheme_templates[k] = self.color_scheme.color_scheme_templates[k].replace(compilation.color_scheme.options["ColorSchemeName"], self.name)

        # Copy the options preprocessors
        self.preprocessors = copy.copy(compilation.preprocessors)

    def inherit(self, compilation, key="comp"):
        """Inherit all options from another compilation."""

        # TODO: Deprecate this function? copy_all really does the job...

        if isinstance(compilation, str):
            compilation = Compilation.get_by_name(compilation, key)

        if not isinstance(compilation, Compilation):
            raise Exception("Compilation.inherit() arg 1 must be of type" + \
                "Compilation or a valid string referencing a submodule in " + \
                "the `compilations` module.")

        self.theme.icons_directory = compilation.theme.icons_directory
        self.theme.options = copy.copy(compilation.theme.options)
        self.color_scheme.options = copy.copy(compilation.color_scheme.options)
        self.options = copy.copy(compilation.options)

        self.color_scheme.options["ColorSchemeName"] = self.name
        self.theme.options["ThemeName"] = self.name

        self.preprocessors = copy.copy(compilation.preprocessors)

    @staticmethod
    def get_by_name(name, key="comp"):
        """Returns a pre-existing compilation by name."""

        comp_module = __import__("compilations." + name, globals(), locals(), [key], 0)
        if comp_module is not None:
            compilation = getattr(comp_module, key, None)
            if compilation is not None:
                return compilation
            else:
                raise Exception("Failed to load compilation '%s' from imported module '%s'" % (key, name))
        else:
            raise Exception("Failed to import compilation module '%s'" % name)
        return None
