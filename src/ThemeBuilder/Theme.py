# -*- coding: utf-8 -*-

"""

"""

import os

from string import Template

from ThemeBuilder.ThemeFileInterface import ThemeFileInterface

class Theme(ThemeFileInterface):
	def __init__(self, name, templateDirectory = None, templates = None):
		self.name = name

		if templateDirectory is None:
			templateDirectory = themeDir(self.name)

		print(templateDirectory)

		if templates is None:
			templates = basicTemplates(self.name)

		self.templateDirectory = templateDirectory
		self.templates = templates

		self.options = {
			"ThemeName": self.name,
		}

	def export(self, directory, package):
		self.options["Package"] = package

		for template in self.templates:
			templateFile = self.templateDirectory + os.sep + template
			targetFile = directory + os.sep + self.templates[template]
			file = open(templateFile, 'r')
			template = Template(file.read())
			content = template.substitute(self.options)
			file = open(targetFile, 'w')
			file.write(content)

def themeDir(name):
	return os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + os.sep + os.path.pardir + os.sep + "theme_templates" + os.sep + name + os.sep)

def basicTemplates(name, targetName = None):
	if targetName is None:
		targetName = name
	return {
				name + ".sublime-theme-template": targetName + ".sublime-theme",
				name + "-Widget.sublime-settings-template": "Widget.sublime-settings"
			}
