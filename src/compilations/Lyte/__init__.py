from ThemeBuilder.Compilation import Compilation

darkcomp = getattr(__import__("compilations." + "Lyte-Dark", globals(), locals(), ["comp"], 0), "comp", None)

comp = Compilation("Lyte")

comp.theme.options = darkcomp.theme.options
comp.colorscheme.options = darkcomp.colorscheme.options
comp.options = darkcomp.options