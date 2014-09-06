# -*- coding: utf-8 -*-

"""

"""

import os, shutil

from string import Template

from ThemeBuilder.ThemeFileInterface import ThemeFileInterface

class ColorScheme(ThemeFileInterface):
	def __init__(self, name, templateDirectory = None, templates = None):
		self.name = name

		if templateDirectory is None:
			templateDirectory = colorSchemeDir(self.name)

		if templates is None:
			templates = basicColorSchemeTemplates(self.name)

		self.templateDirectory = templateDirectory
		self.templates = templates

		self.options = {
			"ColorSchemeName": self.name
		}

	def export(self, directory, package):
		self.options["Package"] = package

		print(self.templateDirectory)
		print(self.templates)

		# Process templates
		for template in self.templates:
			templateFile = os.path.abspath(self.templateDirectory + os.sep + template)
			targetFile = os.path.abspath(directory + os.sep + self.templates[template])
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
