#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The script for generating all Lyte Sublime theme files.

See theme_builder/compilation.py for more information.

"""

import os.path

from theme_builder.color import Color
from theme_builder.compilation import Compilation

def main():
    """Application entry point"""

    # The Sublime package name
    package = "Theme - Lyte"

    # The themes to generate
    compilations = [
        "Lyte-Dark",
        "Lyte-Light",
        "Lyte-Solarized",
        "Lyte-Solarized-Light",
        "Lyte-Monokai",
        # "Lyte-Light",
        # "Lyte-Dark-NoBorder",
        # "Lyte-NoBorder-Light",
        "Lyte", # For legacy purposes - should be the same as Lyte-Dark
    ]

    # The directory to output the compilations to
    directory = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + os.sep + os.path.pardir + os.sep + os.path.pardir + os.sep + package)

    for compilation_name in compilations:
        compile_scripted_compilation(compilation_name, directory, package)

def compile_scripted_compilation(name, directory, package, key="comp"):
    """Compiles a script-based Compilation"""

    compilation = Compilation.get_by_name(name, key)
    compilation.export(directory, package)

if __name__ == "__main__":
    main()
