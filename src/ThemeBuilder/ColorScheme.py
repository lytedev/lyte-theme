# -*- coding: utf-8 -*-

"""

"""

import os, shutil

from string import Template

from ThemeBuilder.ThemeFileInterface import ThemeFileInterface

class ColorScheme(ThemeFileInterface):
	def __init__(self, name, colorSchemeTemplateDirectory = None, colorSchemeTemplates = None):
		self.name = name

		if colorSchemeTemplateDirectory is None:
			colorSchemeTemplateDirectory = colorSchemeDir(self.name)

		if colorSchemeTemplates is None:
			colorSchemeTemplates = basicColorSchemeTemplates(self.name)

		self.colorSchemeTemplateDirectory = colorSchemeTemplateDirectory
		self.colorSchemeTemplates = colorSchemeTemplates

		self.options = {
			"ColorSchemeName": self.name
		}

	def export(self, directory, package):
		self.options["Package"] = package

		# Process colorSchemeTemplates
		for template in self.colorSchemeTemplates:
			templateFile = os.path.abspath(self.colorSchemeTemplateDirectory + os.sep + template)
			targetFile = os.path.abspath(directory + os.sep + self.colorSchemeTemplates[template])
			file = open(templateFile, 'r')
			template = Template(file.read())
			file.close()
			content = template.substitute(self.options)
			file = open(targetFile, 'w')
			file.write(content)
			file.close()

def colorSchemeDir(name):
	return os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + os.sep + os.path.pardir + os.sep + "color_scheme_templates" + os.sep + name + os.sep)

def basicColorSchemeTemplates(name, targetName = None):
	if targetName is None:
		targetName = name
	return {
				name + ".tmTheme-template": targetName + ".tmTheme",
			}
