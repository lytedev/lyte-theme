# -*- coding: utf-8 -*-

"""Sublime Text 3/TextMate syntax theme builder.

This module is a part of the lyte theme for Sublime Text 3 and is used primarily for
constructing the syntax highligh color scheme.

Really, the only functionality this module offers is super-simple manipulation of
colors. My goal was to have simply a single primary (highlight) color and a general
idea of contrast and saturation and have a color scheme generated based on that. It
works alright, but hand-picking my colors was still working better for me. But who
knows. Somebody may find this script useful.

Example:
    See `lyte.py` for in-depth examples

        import theme_builder as tb
        primary_color = tb.Color("#2af")
        background = tb.Color("#111")
        foreground = background.invert()
        opts = {
            "background": background,
            "foreground": foreground,
            "keyword": primary_color,
            "string": primary_color.mod_hue(90),
            "comment": background.blend(fg)
        }
        template,_ = tb.format_template("my_template", opts)
        tb.write_theme("my_theme", template)

    Where `templates/my_template.tmTheme-template` would essentially be a .tmTheme
    file with `{background}`, `{foreground}`, `{comment}` etc. placeholders
    that would be replaced with the associated values in the `opts` dict. See
    string.format() and the Format Specification Mini-Language Python documentation
    for details.

    https://docs.python.org/2/library/functions.html#format

    Again, the existing `templates/lyte2.tmTheme-template` file is a good example.

"""

import operator, colorsys

class Color:
    """Manages and manipulates RGBA colors.

    Attributes:
        r (int): The red value of the color.
        g (int): The green value of the color.
        b (int): The blue value of the color.
        a (int): The alpha value of the color.
        alpha (bool): A flag indicating whether or not the color should
            manage its alpha value within the various methods.

    """
    # Overloads
    def __init__(self, r = -1, g = -1, b = -1, a = -1):
        """Color class initilizer

        Args:
            r: Generally the red value of the constructing color. However,
                if `r` is another color, we will just its attributes. If `r` is
                a string, we will try to parse it as a hexadecimal string. See
                `Color.from_string()` for more information.
            g (int): The green value of the color.
            b (int): The blue value of the color.
            a (int): The alpha value of the color. If `a` is specified and >= 0,
                we will assume we are managing the alpha value of this color.

        """
        if isinstance(r, str):
            self.from_string(r)
        elif isinstance(r, Color):
            self.from_color(r)
        else:
            if r < 0:
                r = 0
            if g < 0:
                g = r
            if b < 0:
                b = g
            if a < 0:
                self.alpha = False
                a = 255
            self.r = r
            self.g = g
            self.b = b
            self.a = a
            self.alpha = False

    def __str__(self):
        """The class's string format callback.

        Returns:
            See `Color.hex()`.

        """
        return self.hex()

    def __add__(a, b):
        """Adds two colors.

        Args:
            b: If `b` is not a color, we will try to convert it to a color using
                `Color.convert()`. Refer to `Color.convert()` for details.

        Returns:
            The sum of two colors.

        """
        b = a.convert(b)
        c = Color(a)
        c.r = c.r + b.r
        c.g = c.g + b.g
        c.b = c.b + b.b
        if c.alpha:
            c.a = c.a + b.a
        return c

    def __sub__(a, b):
        """Subtracts colors.

        Args:
            b: If `b` is not a color, we will try to convert it to a color using
                `Color.convert()`. Refer to `Color.convert()` for details.

        Returns:
            The difference of two colors.

        """
        b = a.convert(b)
        c = Color(a)
        c.r = c.r - b.r
        c.g = c.g - b.g
        c.b = c.b - b.b
        if c.alpha:
            c.a = c.a - b.a
        return c

    def __mul__(a, b):
        """Averages two colors.

        Args:
            b: If `b` is not a color, we will try to convert it to a color using
                `Color.convert()`. Refer to `Color.convert()` for details.

        Returns:
            The average of two colors.

        """
        b = a.convert(b)
        c = a + b
        return c / 2

    def __truediv__(a, b):
        """Divides two colors.

        Args:
            b: If `b` is not a color, we will try to convert it to a color using
                `Color.convert()`. Refer to `Color.convert()` for details.

        Returns:
            The quotient of two colors.

        """
        c = Color(a)
        if isinstance(b, float) or isinstance(b, int):
            c.r = c.r / b
            c.g = c.g / b
            c.b = c.b / b
            if c.alpha:
                c.a = c.a / b
        if isinstance(b, str):
            b = Color(b)
        if isinstance(b, Color):
            c.r = c.r * max(b.r, 1)
            c.g = c.g * max(b.g, 1)
            c.b = c.b * max(b.b, 1)
            if c.alpha:
                c.a = c.a * max(b.a, 1)
        return c

    def set_alpha(self, a):
        """Sets the `a` (or alpha value) attribute

        This will also enable this Color's tracking of its alpha value.

        """
        c = Color(self)
        c.alpha = True
        c.a = a
        return c

    # Constructor callbacks
    def from_string(self, s):
        """Parses the rgba values from a string.

        Args:
            s (string): The string to parse the rgba values from. Must be in format
                `#rgb`, `#rgba`, `#rrggbb`, or `#rrggbbaa`

        If `s` has a length of 3 or 4, we will first square each hex value and then
        parse as expected.

        """
        val = s.lstrip("#")
        lv = len(val)
        if (lv > 8):
            return None
        if lv == 3 or lv == 4:
            val = "".join([x * 2 for x in val])
            lv = lv * 2
        if lv % 4 == 0:
            self.r, self.g, self.b, self.a = tuple(int(val[i:i+lv/4], 16) for i in range(0, int(lv), int(lv/4)))
        if lv % 3 == 0:
            self.alpha = False
            self.a = 255
            self.r, self.g, self.b = tuple(int(val[i:i+int(lv/3)], 16) for i in range(0, int(lv), int(lv/3)))
        return self

    def from_rgba(self, rgba):
        """Loads rgba values from a tuple.

        Args:
            rgba (tuple): A tuple containing `(r, g, b[, a])`.

        """
        if len(rgba) > 3 and self.alpha:
            self.r, self.g, self.b, self.a = rgba
        else:
            self.r, self.g, self.b = rgba
        return self

    def from_color(self, color):
        """Loads rgba values from a color.

        Args:
            color (tuple): Another color whose values to copy.

        """
        self.r = color.r
        self.g = color.g
        self.b = color.b
        self.alpha = color.alpha
        if self.alpha:
            self.a = color.a
        else:
            self.a = 255
        return self

    def from_hsv(self, hue, saturation, value):
        """Loads rgba values from hue, saturation, and value channels.

        Args:
            hue (float): The hue rotation (0-360).
            saturation (float): The saturation of the hue (0-100).
            value (float): The value (lrightness?) of the color (0-100).

        // TODO: Enable this function to *also* take 0.0-1.0 floats.

        """
        r, g, b = colorsys.hsv_to_rgb(h / 360, s / 100, v / 100)
        return self.from_rgba((r * 255, g * 255, b * 255))

    # Alternate formats and conversions
    def hsv(self):
        """Creates hue, saturation, and value channels from the color.

        Returns:
            An unpacked tuple in the format of `(hue, saturation, value)` where `hue` is a
            measure in degrees from 0-360, `saturation` is a measure of the `hue`'s
            intensity from 0-100, and `value` is a measure of the color's lightness
            from 0-100.

        """
        h, s, v = colorsys.rgb_to_hsv(self.r / 255.0, self.g / 255.0, self. b / 255.0)
        return 360 * h, 100 * s, 100 * v

    def rgba(self):
        """Returns a tuple containing the attributes of the color.

        Returns:
            A packed tuple in the format of `(r, g, b[, a])` where `a` is only
            included if the color's `alpha` attribute is true.

        """
        if self.alpha:
            return (int(self.r), int(self.g), int(self.b), int(self.a))
        else:
            return (int(self.r), int(self.g), int(self.b))

    def hex(self):
        """Returns a string encoding the color in a hexadecimal format.

        Returns:
            A string in the format of `"#rrggbb[aa]"` where `aa` is only encoded if
            the color's `alpha` attribute is true.

        """
        d = 3
        if self.alpha:
            d = 4
        return ('#' + ("%02x" * d)) % self.rgba()

    def convert(self, b):
        """Attempts to convert `b` into a color.

        Args:
            b: The variable to attempt to convert into a color.

        If `b` is a float, we will see if it is a float <= 1.0. If so, we will take
        its value and multiply it by 255

        Once that is done - or if `b` was an integer to begin with, we will take `b`
        and initialize a new `Color`.

        If `b` is a string, we will use it to initialize a new `Color`.

        """
        if isinstance(b, float):
            if b <= 1.0:
                b = Color(int(b * 255))
            else:
                b = int(b)
        if isinstance(b, int):
            b = Color(b)
        if isinstance(b, str):
            b = Color(b)
        return b

    # Manipulations
    def blend(a, b, n = 0.5):
        """Creates a blend between two colors.

        Args:
            b (Color): The color to be blended with.
            n (float): The ratio of the blending.

        The higher that `n` is, the close to `b` the resulting color will be.

        """
        d = 3
        if a.alpha:
            d = 4
        av = a.rgba()
        bv = b.rgba()
        bl = ()
        for i in range(d):
            diff = bv[i] - av[i]
            r = av[i] + (diff * n)
            bl = bl + (r,)
        return Color(*bl)

    def reverse_blend(a, b, n = 0.5):
        """Pushes the color away from the specified color.

        Args:
            b (Color): The color to be blended with.
            n (float): The color to be pushed away from.

        The higher that `n` is, the further from `b` the resulting color will be.

        """
        d = 3
        if a.alpha:
            d = 4
        av = a.rgba()
        bv = b.rgba()
        bl = ()
        for i in range(d):
            diff = bv[i] - av[i]
            r = av[i] - (diff * n)
            bl = bl + (r,)
        return Color(*bl)

    def mod_saturate(self, ss):
        """Modifies the saturation channel of the color by `ss`.

        Args:
            ss: The amount by which to modify the color's saturation.

        Saturation should range from 0-100.

        """
        c = Color(self)
        h,s,v = c.hsv()
        s = s + ss
        c.from_hsv(h,s,v)
        return c

    def mod_hue(self, hs):
        """Modifies the hue channel of the color by `hs`.

        Args:
            hs: The amount by which to modify the color's hue.

        Hue should range from 0-360.

        """
        c = Color(self)
        h,s,v = c.hsv()
        h = h + hs
        c.from_hsv(h,s,v)
        return c

    def mod_value(self, vs):
        """Modifies the value channel of the color by `vs`.

        Args:
            vs: The amount by which to modify the color's value.

        Value should range from 0-100.

        """
        c = Color(self)
        h,s,v = c.hsv()
        v = v + vs
        c.from_hsv(h,s,v)
        return c

    def saturate(self, ss):
        """Sets the saturation channel of the color to `ss`.

        Args:
            ss: The amount to set the color's saturation.

        Saturation should range from 0-100.

        """
        c = Color(self)
        c = Color(self)
        h,s,v = c.hsv()
        s = ss
        c.from_hsv(h,s,v)
        return c

    def hue(self, hs):
        """Sets the hue channel of the color to `hs`.

        Args:
            hs: The amount to set the color's hue.

        Hue should range from 0-360.

        """
        c = Color(self)
        h,s,v = c.hsv()
        h = hs
        c.from_hsv(h,s,v)
        return c

    def value(self, vs):
        """Sets the value channel of the color to `vs`.

        Args:
            vs: The amount to set the color's value.

        Value should range from 0-100.

        """
        c = Color(self)
        h,s,v = c.hsv()
        v = vs
        c.from_hsv(h,s,v)
        return c

    def invert(self):
        """Returns an inversion of the color."""
        c = Color(self)
        c.r = abs(c.r - 255)
        c.g = abs(c.g - 255)
        c.b = abs(c.b - 255)
        if c.alpha:
            c.a = abs(c.a - 255)
        return c

def format_template(template_file, options):
    """Writes the formatted theme to the given file using the given template and options.
a
    Args:
        template_file (string): A `.tmTheme-template` file in the `templates` directory.
        options (dict): The dictionary with which to format the template.

    The function essentially loads the specified file's contents and runs
    `string.format(options)` over them.

    See string.format() and the Format Specification Mini-Language Python documentation
    for details:

    https://docs.python.org/2/library/functions.html#format

    """
    # Get template
    f = open('templates/' + template_file + ".tmTheme-template", 'r')
    template = f.read()
    f.close() # Close File
    # Format template
    for x in options.keys():
        options[x] = str(options[x])
    return template.format(**options), options

def write_theme(filename, template):
    """Writes your formatted template to `filename`.tmTheme.

    Args:
        filename (string): The name of the .tmTheme file you want to write to.
        template (string): The formatted template contents. See `format_template()`.

    """
    f = open(filename + ".tmTheme", 'w')
    f.write(template)
    f.close()
