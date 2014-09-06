#!/usr/bin/env python

"""The script for generating all Lyte Sublime theme files.

See imported modules for details.

"""

import os.path
import importlib

def main():
	# The Sublime package name
	package = "Theme - Lyte"

	# The themes to generate
	compilations = [
		"Lyte", # For legacy purposes - should be the same as Lyte-Dark
		"Lyte-Dark",
		# "Lyte-Light",
		# "Lyte-Dark-NoBorder",
		# "Lyte-NoBorder-Light",
	]

	# The directory to output the compilations to
	directory = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + os.sep + os.path.pardir + os.sep + os.path.pardir + os.sep + package)

	for compilationName in compilations:
		compileScriptedCompilation(compilationName, directory, package)

def compileScriptedCompilation(name, directory, package, key = "comp"):
	c = getattr(__import__("compilations." + name, globals(), locals(), [key], 0), key, None)
	if c is not None:
		c.export(directory, package)
	else:
		raise Exception("Failed to import/load compilation '%s'" % name)

if __name__ == "__main__":
	main()
