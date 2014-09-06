from ThemeBuilder.Theme import Theme, themeDir, iconsDir, basicThemeTemplates
from ThemeBuilder.ColorScheme import ColorScheme, basicColorSchemeTemplates
from ThemeBuilder.Color import Color
from ThemeBuilder.Compilation import Compilation

theme = Theme("Lyte-Dark", iconsDir("lyte"), themeDir("Lyte"), basicThemeTemplates("Lyte", "Lyte-Dark"))
colorScheme = ColorScheme("Lyte-Dark", themeDir("Lyte"), basicColorSchemeTemplates("Lyte", "Lyte-Dark"))

comp = Compilation("Lyte-Dark", theme, colorScheme)

colors = {
	"bg":         Color(25, 25, 25),
	"fg":         Color("#f8f8f8"),
	"comment":    Color("#777777"),
	"secondary1": Color("#1d1d1d"),
	"secondary2": Color("#222222"),
	"secondary3": Color("#333333"),
	"secondary4": Color("#444444"),
	"blue":       Color("#77aaff"),
	"red":        Color("#ff7744"),
	"indigo":     Color("#aa77ff"),
	"magenta":    Color("#ff4477"),
	"cyan":       Color("#77ffff"),
	"green":      Color("#aaff44")
}

comp.theme.options.update(colors)

print(comp.colorScheme.templateDirectory)