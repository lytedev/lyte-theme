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

    # Accent Colors (ripped from Base16-Monokai)
    "red": Color("#f92672"),
    "orange": Color("#fd971f"),
    "yellow": Color("#f4bf75"),
    "green": Color("#a6e22e"),
    "cyan": Color("#a1efe4"),
    "blue": Color("#66d9ef"),
    "indigo": Color("#ae81ff"),
    "brown": Color("#cc6633"),

    # Font info
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

options["active"] = options["green"]
