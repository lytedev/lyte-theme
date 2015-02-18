from theme_builder.color import Color

options = {
    # Meta
    "author":     "lytedev",

    # Icon Set

    # Base Color Range
    "bg":         Color(16, 16, 16),
    "fg":         Color(250, 250, 250),
    "max_bg":     Color(120, 120, 120),
    "max_fg":     Color(128, 128, 128),

    # Accent Colors
    "red":        Color("#fd971f"),
    "green":      Color("#a6e22e"),
    "indigo":     Color("#e6db74"),
    "cyan":       Color("#66d9ef"),
    "blue":       Color("#ae81ff"),
    "magenta":    Color("#f92672"),

    "selection":  Color("#f92672").set_alpha(100),

    # Fonts
    "font_face": "", # System Default
    "font_size": 11,
    "sidebar_heading_font_size": 14,
    "bold_sidebar_heads": True,
    "bold_folder_names": True,

    # Preprocessor options
    "sidebar_margin_x": 15,
    "sidebar_margin_y": 1,
    "sidebar_indent_x": 12,
    "sidebar_indent_y": 3,
    "tab_padding_x": 5,
    "tab_padding_y": 5,
    "text_height": 15,
    "borders": 2,
    "text_shadow": True,
    "sidebar_arrows": True,
    "sidebar_icons": True,
}
