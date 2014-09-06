# -*- coding: utf-8 -*-

"""

"""

from ThemeBuilder.ThemeFileInterface import ThemeFileInterface

class ColorScheme(ThemeFileInterface):
	def __init__(self, name):
		self.name = name

		self.options = {"ColorSchemeName": self.name}
