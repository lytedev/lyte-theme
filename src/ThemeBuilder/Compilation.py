# -*- coding: utf-8 -*-

"""

"""

import os
import shutil

from ThemeBuilder.ThemeFileInterface import ThemeFileInterface
from ThemeBuilder.ColorScheme import ColorScheme
from ThemeBuilder.Theme import Theme

class Compilation(ThemeFileInterface):
	def __init__(self, name, theme = None, colorscheme = None, iconset = None):
		self.name = name

		if iconset is None:
			iconset = self.name
		if colorscheme is None:
			colorscheme = self.name
		if theme is None:
			theme = self.name

		if isinstance(colorscheme, str):
			colorscheme = ColorScheme(colorscheme)
		if isinstance(theme, str):
			theme = Theme(theme)

		self.iconset = iconset
		self.colorscheme = colorscheme
		self.theme = theme

	def export(self, directory, package):
		directory = os.path.abspath(directory + os.sep + self.name)

		print(directory)
		# Create directory if it doesn't exist
		if not os.access(directory, os.F_OK):
			os.mkdir(directory)

		# Make sure we can write to the directory
		if not os.access(directory, os.W_OK):
			raise Exception("Cannot write to directory", directory)

		print("Exporting compilation '%s'" % self.name)
		print("\tDirectory: '%s'" % directory)
		print("\tTheme: '%s'" % self.theme.name)
		print("\tColor Scheme: '%s'" % self.colorscheme.name)
		print("\tIcon Set: '%s'" % self.iconset)

		self.theme.export(directory, package)
