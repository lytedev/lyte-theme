from ThemeBuilder.Theme import Theme, themeDir, basicTemplates
from ThemeBuilder.Compilation import Compilation

theme = Theme("Lyte-Dark", themeDir("Lyte"), basicTemplates("Lyte", "Lyte-Dark"))

comp = Compilation("Lyte-Dark", theme, "Lyte", "Lyte")

