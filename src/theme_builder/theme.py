# -*- coding: utf-8 -*-

"""See class `Theme`

"""

import copy, os, shutil

from string import Template

from .color import Color

class Theme():
    """A class for creating a Sublime Text theme."""

    def __init__(self, name, icons_directory=None, theme_template_directory=None, theme_templates=None):
        """Theme constructor."""

        self.name = name

        # Default some properties based on name
        if theme_template_directory is None:
            theme_template_directory = theme_dir(self.name)

        if icons_directory is None:
            icons_directory = icons_dir(self.name)

        if theme_templates is None:
            theme_templates = basic_theme_templates(self.name)

        self.icons_directory = icons_directory
        self.theme_template_directory = theme_template_directory
        self.theme_templates = theme_templates

        self.options = {
            "ThemeName": self.name,
        }

    def set_iconset(self, name):
        """Changes the theme's iconset"""

        self.icons_directory = icons_dir(name)

    def export(self, directory, package, opts=None):
        """Exports the Theme to a file."""

        if opts is None:
            opts = copy.copy(self.options)

        opts["Package"] = package

        # Copy icons
        target_icons_directory = os.path.abspath(directory + os.sep + "icons" + os.sep)
        if os.access(target_icons_directory, os.F_OK):
            shutil.rmtree(target_icons_directory)
        shutil.copytree(self.icons_directory, target_icons_directory)
        opts["IconsDirectory"] = target_icons_directory[target_icons_directory.index(package):].replace("\\", "/")

        print(opts["IconsDirectory"])
        print(self.icons_directory)

        # Create an alternate version of the options data where all Colors are formatted
        # as array strings instead of hex-strings as expected by .sublime-theme files
        sublime_theme_options = copy.copy(opts)
        for key in sublime_theme_options:
            if isinstance(sublime_theme_options[key], Color):
                sublime_theme_options[key] = sublime_theme_options[key].rgba_array_string()

        # Process theme_templates
        for template in self.theme_templates:

            current_options = opts
            key = template
            # Our stupid way of detecting whether or not we should use array strings for colors
            if template[0:2] == "[]":
                template = template[2:]
                current_options = sublime_theme_options

            template_file = os.path.abspath(self.theme_template_directory + os.sep + template)
            target_file = os.path.abspath(directory + os.sep + self.theme_templates[key])
            file = open(template_file, 'r')
            template = Template(file.read())
            file.close()
            content = template.substitute(current_options)
            file = open(target_file, 'w')
            file.write(content)
            file.close()

def theme_dir(name):
    """Returns the standard theme template directory."""

    return os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + os.sep + os.path.pardir + os.sep + "theme_templates" + os.sep + name + os.sep)

def icons_dir(name):
    """Returns the standard icon-sets directory."""

    return os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + os.sep + os.path.pardir + os.sep + "iconsets" + os.sep + name + os.sep)

def basic_theme_templates(name, target_name=None):
    """Returns the standard theme template array."""

    if target_name is None:
        target_name = name
    return {
                # TODO: Remove the need for the "[]" prepended by moving the
                # Widget files to color schemes?
                "[]" + name + ".sublime-theme-template": ".." + os.sep + target_name + ".sublime-theme",
                name + "-Widget.sublime-settings-template": "Widget - " + target_name + ".sublime-settings",
                name + "-Widget.stTheme-template": "Widget - " + target_name + ".stTheme"
            }
