#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The script for generating all Lyte Sublime theme files.

See imported modules for details.

"""

import os.path

def main():
    """Application entry point"""

    # The Sublime package name
    package = "Theme - Lyte"

    # The themes to generate
    compilations = [
        "Lyte-Dark",
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

    comp_module = __import__("compilations." + name, globals(), locals(), [key], 0)
    if comp_module is not None:
        compilation = getattr(comp_module, key, None)
        if compilation is not None:
            compilation.export(directory, package)
        else:
            raise Exception("Failed to load compilation '%s' from imported module '%s'" % (key, name))
    else:
        raise Exception("Failed to import compilation module '%s'" % name)

if __name__ == "__main__":
    main()
