# -*- coding: utf-8 -*-

"""

"""

import copy, os, shutil

from string import Template

from ThemeBuilder.ThemeFileInterface import ThemeFileInterface
from ThemeBuilder.Color import Color

class Theme(ThemeFileInterface):
	def __init__(self, name, iconsDirectory = None, templateDirectory = None, templates = None):
		self.name = name

		if templateDirectory is None:
			templateDirectory = themeDir(self.name)

		if iconsDirectory is None:
			iconsDirectory = iconsDir(self.name)

		if templates is None:
			templates = basicThemeTemplates(self.name)

		self.iconsDirectory = iconsDirectory
		self.templateDirectory = templateDirectory
		self.templates = templates

		self.options = {
			"ThemeName": self.name,
		}

	def export(self, directory, package):
		self.options["Package"] = package

		# Copy icons
		targetIconsDirectory = os.path.abspath(directory + os.sep + "icons" + os.sep)
		if os.access(targetIconsDirectory, os.F_OK):
			shutil.rmtree(targetIconsDirectory)
		shutil.copytree(self.iconsDirectory, targetIconsDirectory)
		self.options["IconsDirectory"] = targetIconsDirectory[targetIconsDirectory.index(package):].replace("\\", "\\\\")

		sublimeThemeOptions = copy.copy(self.options)
		for key in sublimeThemeOptions:
			if isinstance(sublimeThemeOptions[key], Color):
				sublimeThemeOptions[key] = sublimeThemeOptions[key].rgba_array()

		# Process templates
		for template in self.templates:

			key = template
			curOpts = self.options
			if template[0:2] == "[]":
				template = template[2:]
				curOpts = sublimeThemeOptions

			templateFile = os.path.abspath(self.templateDirectory + os.sep + template)
			targetFile = os.path.abspath(directory + os.sep + self.templates[key])
			file = open(templateFile, 'r')
			template = Template(file.read())
			file.close()
			content = template.substitute(curOpts)
			file = open(targetFile, 'w')
			file.write(content)
			file.close()

def themeDir(name):
	return os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + os.sep + os.path.pardir + os.sep + "theme_templates" + os.sep + name + os.sep)

def iconsDir(name):
	return os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + os.sep + os.path.pardir + os.sep + "iconsets" + os.sep + name + os.sep)

def basicThemeTemplates(name, targetName = None):
	if targetName is None:
		targetName = name
	return {
				"[]" + name + ".sublime-theme-template": targetName + ".sublime-theme",
				name + "-Widget.sublime-settings-template": "Widget.sublime-settings",
				name + "-Widget.stTheme-template": "Widget.stTheme"
			}
