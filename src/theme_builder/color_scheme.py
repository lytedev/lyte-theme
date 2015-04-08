# -*-  coding: utf-8 -*-
"""Contains the Color Scheme class"""

import os, copy

from string import Template

class ColorScheme():
    """A class for creating a color scheme from a template."""

    def __init__(self, name, color_scheme_template_directory=None, color_scheme_templates=None):
        """ColorScheme constructor."""

        self.name = name

        # Default some properties based on the name
        if color_scheme_template_directory is None:
            color_scheme_template_directory = color_scheme_dir(self.name)

        if color_scheme_templates is None:
            color_scheme_templates = basic_color_scheme_templates(self.name)

        self.color_scheme_template_directory = color_scheme_template_directory
        self.color_scheme_templates = color_scheme_templates

        self.options = {"ColorSchemeName": self.name}

    def export(self, directory, package, opts=None):
        """Exports the color scheme to a file."""

        if opts is None:
            opts = copy.copy(self.options)

        opts["Package"] = package

        # Process color_scheme_templates
        for template in self.color_scheme_templates:
            template_file = os.path.abspath(self.color_scheme_template_directory + os.sep + template)
            target_file = os.path.abspath(directory + os.sep + self.color_scheme_templates[template])
            file = open(template_file, 'r')
            template = Template(file.read())
            file.close()
            content = template.substitute(opts)
            file = open(target_file, 'w')
            file.write(content)
            file.close()

def color_scheme_dir(name):
    """Returns the standard dirctory where color scheme templates are kept."""

    return os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + os.sep + os.path.pardir + os.sep + "color_scheme_templates" + os.sep + name + os.sep)

def basic_color_scheme_templates(name, target_name=None):
    """Returns the standard color scheme templates array"""

    if target_name is None:
        target_name = name

    return {name + ".tmTheme-template": target_name + ".tmTheme"}
