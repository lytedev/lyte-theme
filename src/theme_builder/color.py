# -*- coding: utf-8 -*-

"""See class `Color`

Author: @lytedev on GitHub

"""

import colorsys

class Color:
    """Manages and manipulates RGBA colors.

    Attributes:
        red (int): The red value of the color.
        green (int): The green value of the color.
        blue (int): The blue value of the color.
        alpha (int): The alpha value of the color.

    """

    # Overloads
    def __init__(self, red=-1, green=-1, blue=-1, alpha=-1):
        """Color class initilizer

        Args:
            red: Generally the red value of the constructing color. However,
                if `red` is another color, we will just its attributes. If
                `red` is alpha string, we will try to parse it as alpha
                hexadecimal string. See `Color.from_string()` for more
                information.
            green (int): The green value of the color.
            blue (int): The blue value of the color.
            alpha (int): The alpha value of the color. If `alpha` is specified
                and >= 0, we will assume we are managing the alpha value of
                this color.

        """

        if isinstance(red, str):
            self.from_string(red)
        elif isinstance(red, Color):
            self.from_color(red)
        else:
            if red < 0:
                red = 0
            if green < 0:
                green = red
            if blue < 0:
                blue = green
            if alpha < 0:
                self.has_alpha = False
                alpha = 255
            else:
                self.has_alpha = True
            self.red = red
            self.green = green
            self.blue = blue
            self.alpha = alpha

    def __str__(self):
        """The class's string format callback.

        Returns:
            See `Color.hex()`.

        """

        return self.hex()

    def __add__(self, color):
        """Adds two colors.

        Args:
            color: If `color` is not a color, we will try to convert it to
                a color using `Color.convert()`. Refer to `Color.convert()`
                for details.

        Returns:
            The sum of two colors.

        """

        color = Color.convert(color)
        tmp_color = Color(self)
        tmp_color.red = tmp_color.red + color.red
        tmp_color.green = tmp_color.green + color.green
        tmp_color.blue = tmp_color.blue + color.blue
        if tmp_color.has_alpha:
            tmp_color.alpha = tmp_color.alpha + color.alpha

        return tmp_color

    def __sub__(self, color):
        """Subtracts colors.

        Args:
            color: If `color` is not a color, we will try to convert it to a
                color using `Color.convert()`. Refer to `Color.convert()`
                for details.

        Returns:
            The difference of two colors.

        """

        color = Color.convert(color)
        tmp_color = Color(self)
        tmp_color.red = tmp_color.red - color.red
        tmp_color.green = tmp_color.green - color.green
        tmp_color.blue = tmp_color.blue - color.blue
        if tmp_color.has_alpha:
            tmp_color.alpha = tmp_color.alpha - color.alpha

        return tmp_color

    def __mul__(self, color):
        """Averages two colors.

        Args:
            color: If `color` is not a color, we will try to convert it to a
                color using `Color.convert()`. Refer to `Color.convert()` for
                details.

        If self `has_alpha`, the resulting color will never have alpha.

        Returns:
            The average of two colors.

        """

        color = Color.convert(color)
        color_rgba = color.rgba()
        self_rgba = self.rgba()
        tmp_color = ()
        for i in range(len(self_rgba)):
            tmp_color += (((self_rgba[i] + color_rgba[i]) / 2),)

        return Color(tmp_color)

    def __truediv__(self, color):
        """Divides two colors.

        Args:
            color: If `color` is not a color, we will try to convert it to a
            color using `Color.convert()`. Refer to `Color.convert()` for
            details.

        Returns:
            The quotient of two colors.

        """

        tmp_color = Color(self)
        if isinstance(color, float) or isinstance(color, int):
            tmp_color.red = int(tmp_color.red / color)
            tmp_color.green = int(tmp_color.green / color)
            tmp_color.blue = int(tmp_color.blue / color)
            if tmp_color.has_alpha:
                tmp_color.alpha = int(tmp_color.alpha / color)
        else:
            if isinstance(color, str):
                color = Color(color)
            if isinstance(color, Color):
                tmp_color.red = int(tmp_color.red * max(color.red, 1))
                tmp_color.green = int(tmp_color.green * max(color.green, 1))
                tmp_color.blue = int(tmp_color.blue * max(color.blue, 1))
                if tmp_color.has_alpha:
                    tmp_color.alpha = int(tmp_color.alpha * max(color.alpha, 1))

        tmp_color.check_color_range()

        return tmp_color

    def check_color_range(self):
        """Ensures none of the colors values exceed their limits"""
        self.red = min(self.red, 255)
        self.red = max(self.red, 0)
        self.green = min(self.green, 255)
        self.green = max(self.green, 0)
        self.blue = min(self.blue, 255)
        self.blue = max(self.blue, 0)
        self.alpha = min(self.alpha, 255)
        self.alpha = max(self.alpha, 0)
        return self

    def set_alpha(self, alpha):
        """Sets the `alpha` (or alpha value) attribute

        This will also enable this Color's tracking of its alpha value.

        """

        tmp_color = Color(self)
        tmp_color.has_alpha = True
        tmp_color.alpha = alpha

        return tmp_color

    # Constructor callbacks
    def from_string(self, color_string):
        """Parses the rgba values from alpha string.

        Args:
            color_string (string): The string to parse the rgba values from.
                Must be in format `#rgb`, `#rgba`, `#rrggbb`, or `#rrggbbaa`.

        If `color_string` has alpha length of 3 or 4, we will first square each
        hex value and then parse as expected.

        """
        val = color_string.lstrip("#")
        val_len = len(val)
        if val_len > 8:
            return None
        if val_len == 3 or val_len == 4:
            val = "".join([x * 2 for x in val])
            val_len = val_len * 2
        if val_len % 4 == 0:
            vals = tuple(int(val[i:i + val_len / 4], 16) for i in range(0, int(val_len), int(val_len / 4)))
            self.red, self.green, self.blue, self.alpha = vals
            self.has_alpha = True
        if val_len % 3 == 0:
            self.has_alpha = False
            self.alpha = 255
            vals = tuple(int(val[i:i + int(val_len / 3)], 16) for i in range(0, int(val_len), int(val_len / 3)))
            self.red, self.green, self.blue = vals

        return self

    def from_rgba(self, rgba):
        """Loads rgba values from a tuple.

        Args:
            rgba (tuple): a tuple containing `(red, green, blue[, alpha])`.

        """
        if len(rgba) > 3 and self.has_alpha:
            self.red, self.green, self.blue, self.alpha = rgba
            self.has_alpha = True
        else:
            self.red, self.green, self.blue = rgba
            self.has_alpha = False

        return self

    def from_color(self, color):
        """Loads rgba values from a color.

        Args:
            color (tuple): Another color whose values to copy.

        """

        self.red = color.red
        self.green = color.green
        self.blue = color.blue
        self.has_alpha = color.has_alpha
        if self.has_alpha:
            self.alpha = color.alpha
        else:
            self.alpha = 255

        return self

    def from_hsv(self, hue, saturation, value):
        """Loads rgba values from hue, saturation, and value channels.

        Args:
            hue (float): The hue rotation (0-360).
            saturation (float): The saturation of the hue (0-100).
            value (float): The value (lrightness?) of the color (0-100).

        // TODO: Enable this function to *also* take 0.0-1.0 floats.

        """

        red, green, blue = colorsys.hsv_to_rgb(hue / 360, saturation / 100, value / 100)

        return self.from_rgba((red * 255, green * 255, blue * 255))

    # Alternate formats and conversions
    def hsv(self):
        """Creates hue, saturation, and value channels from the color.

        Returns:
            An unpacked tuple in the format of `(hue, saturation, value)` where
            `hue` is a measure in degrees from 0-360, `saturation` is a measure
            of the `hue`'s intensity from 0-100, and `value` is a measure of
            the color's lightness from 0-100.

        """
        hue, saturation, value = colorsys.rgb_to_hsv(self.red / 255.0, self.green / 255.0, self.blue / 255.0)

        return 360 * hue, 100 * saturation, 100 * value

    def rgba(self):
        """Returns a tuple containing the attributes of the color.

        Returns:
            A packed tuple in the format of `(red, green, blue[, alpha])`
            where `alpha` is only included if the color's `alpha` attribute is
            true.

        """

        if self.has_alpha:
            return (int(self.red), int(self.green), int(self.blue), int(self.alpha))
        else:
            return (int(self.red), int(self.green), int(self.blue))

    def rgba_array_string(self):
        """Returns a tuple containing the attributes of the color.

        Returns:
            A packed tuple in the format of `(red, green, blue[, alpha])`
            where `alpha` is only included if the color's `alpha` attribute is
            true.

        """

        if self.has_alpha:
            return "[" + str(int(self.red)) + ", " + str(int(self.green)) + ", " + str(int(self.blue)) + ", " + str(int(self.alpha)) + "]"
        else:
            return "[" + str(int(self.red)) + ", " + str(int(self.green)) + ", " + str(int(self.blue)) + "]"

    def hex(self):
        """Returns alpha string encoding the color in alpha hexadecimal format.

        Returns:
            A string in the format of `"#rrggbb[aa]"` where `aa` is only encoded
            if the color's `alpha` attribute is true.

        """

        length = 3
        if self.has_alpha:
            length = 4

        hex_string = "#"
        rgba = self.check_color_range().rgba()
        for i in range(length):
            digits = hex(rgba[i])[2:]
            if len(digits) < 2:
                digits = "0" + digits
            hex_string = hex_string + digits

        return hex_string

    # Manipulations
    def blend(self, b, ratio=0.5):
        """Creates a blend between two colors.

        Args:
            b (Color): The color to be blended with.
            ratio (float): The ratio of the blending.

        The higher that `n` is, the closer to `b` the resulting color will be.

        """

        b = self.convert(b)

        length = 3
        if self.has_alpha:
            length = 4
        self_vals = self.rgba()
        color_vals = b.rgba()
        tmp_vals = ()
        for i in range(length):
            diff = color_vals[i] - self_vals[i]
            tmp_val = self_vals[i] + (diff * ratio)
            tmp_vals = tmp_vals + (tmp_val,)

        red, green, blue = tmp_vals
        if length == 4:
            alpha = tmp_vals[3]
            return Color(red, green, blue, alpha)
        else:
            return Color(red, green, blue)

    def reverse_blend(self, color, ratio=0.5):
        """"Pushes" the color away from the specified color.

        Args:
            color (Color): The color to be reverse blended with.
            ratio (float): The color to be pushed away from.

        The higher that `ratio` is, the further from `color` the resulting
            color will be.

        """

        length = 3
        if self.has_alpha:
            length = 4
        self_vals = self.rgba()
        color_vals = color.rgba()
        tmp_vals = ()
        for i in range(length):
            diff = self_vals[i] - color_vals[i]
            val = color_vals[i] - (diff * ratio)
            tmp_vals = tmp_vals + (val,)

        return Color(tmp_vals)

    def mod_saturate(self, mod_saturation):
        """Modifies the saturation channel of the color by `ss`.

        Args:
            ss: The amount by which to modify the color's saturation.

        Saturation should range from 0-100.

        """

        tmp_color = Color(self)
        hue, saturation, value = tmp_color.hsv()
        saturation = saturation + mod_saturation
        tmp_color.from_hsv(hue, saturation, value)

        return tmp_color

    def mod_hue(self, mod_hue):
        """Modifies the hue channel of the color by `hs`.

        Args:
            hs: The amount by which to modify the color's hue.

        Hue should range from 0-360.

        """

        tmp_color = Color(self)
        hue, saturation, value = tmp_color.hsv()
        hue = hue + mod_hue
        tmp_color.from_hsv(hue, saturation, value)

        return tmp_color

    def mod_value(self, mod_value):
        """Modifies the value channel of the color by `vs`.

        Args:
            vs: The amount by which to modify the color's value.

        Value should range from 0-100.

        """

        tmp_color = Color(self)
        hue, saturation, value = tmp_color.hsv()
        value = value + mod_value
        tmp_color.from_hsv(hue, saturation, value)

        return tmp_color

    def saturate(self, new_saturation):
        """Sets the saturation channel of the color to `ss`.

        Args:
            ss: The amount to set the color's saturation.

        Saturation should range from 0-100.

        """

        tmp_color = Color(self)
        hue, saturation, value = tmp_color.hsv()
        saturation = new_saturation
        tmp_color.from_hsv(hue, saturation, value)

        return tmp_color

    def hue(self, new_hue):
        """Sets the hue channel of the color to `hs`.

        Args:
            hs: The amount to set the color's hue.

        Hue should range from 0-360.

        """

        tmp_color = Color(self)
        hue, saturation, value = tmp_color.hsv()
        hue = new_hue
        tmp_color.from_hsv(hue, saturation, value)

        return tmp_color

    def value(self, new_value):
        """Sets the value channel of the color to `new_value`.

        Args:
            new_value: The amount to set the color's value at.

        Values should range from 0-100.

        """

        tmp_color = Color(self)
        hue, saturation, value = tmp_color.hsv()
        value = new_value
        tmp_color.from_hsv(hue, saturation, value)

        return tmp_color

    def invert(self):
        """Returns the inversion of the color."""

        tmp_color = Color(self)
        tmp_color.red = abs(tmp_color.red - 255)
        tmp_color.green = abs(tmp_color.green - 255)
        tmp_color.blue = abs(tmp_color.blue - 255)
        if tmp_color.has_alpha:
            tmp_color.alpha = abs(tmp_color.alpha - 255)

        return tmp_color

    @staticmethod
    def convert(color):
        """Attempts to convert `color` into a color.

        Args:
            color: The variable to attempt to convert into a color.

        If `color` is a float, we will see if it is a float <= 1.0. If so, we
        will take its value and multiply it by 255.

        Once that is done - or if `color` was an integer to begin with, we will
        take `color` and initialize a new `Color`.

        If `color` is a string, we will use it to initialize a new `Color`.

        """

        if isinstance(color, float):
            if color <= 1.0:
                color = Color(int(color * 255))
            else:
                color = int(color)
        if isinstance(color, int):
            color = Color(color)
        if isinstance(color, str):
            color = Color(color)

        return color
