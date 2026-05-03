# -*- coding: utf-8 -*-
"""
Color Validation Utilities
==========================

Functions for validating color values used in favicon configuration.

"""

# Import | Standard Library
import re
from typing import Optional

# Import | Local
from ..exceptions import FaviconColorError

# Regular expression for valid hex colors
HEX_COLOR_PATTERN = re.compile(r"^#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$")

# Named CSS colors
CSS_COLORS = {
    "black",
    "silver",
    "gray",
    "white",
    "maroon",
    "red",
    "purple",
    "fuchsia",
    "green",
    "lime",
    "olive",
    "yellow",
    "navy",
    "blue",
    "teal",
    "aqua",
    "aliceblue",
    "antiquewhite",
    "aquamarine",
    "azure",
    "beige",
    "bisque",
    "blanchedalmond",
    "blueviolet",
    "brown",
    "burlywood",
    "cadetblue",
    "chartreuse",
    "chocolate",
    "coral",
    "cornflowerblue",
    "cornsilk",
    "crimson",
    "cyan",
    "darkblue",
    "darkcyan",
    "darkgoldenrod",
    "darkgray",
    "darkgreen",
    "darkgrey",
    "darkkhaki",
    "darkmagenta",
    "darkolivegreen",
    "darkorange",
    "darkorchid",
    "darkred",
    "darksalmon",
    "darkseagreen",
    "darkslateblue",
    "darkslategray",
    "darkslategrey",
    "darkturquoise",
    "darkviolet",
    "deeppink",
    "deepskyblue",
    "dimgray",
    "dimgrey",
    "dodgerblue",
    "firebrick",
    "floralwhite",
    "forestgreen",
    "gainsboro",
    "ghostwhite",
    "gold",
    "goldenrod",
    "greenyellow",
    "grey",
    "honeydew",
    "hotpink",
    "indianred",
    "indigo",
    "ivory",
    "khaki",
    "lavender",
    "lavenderblush",
    "lawngreen",
    "lemonchiffon",
    "lightblue",
    "lightcoral",
    "lightcyan",
    "lightgoldenrodyellow",
    "lightgray",
    "lightgreen",
    "lightgrey",
    "lightpink",
    "lightsalmon",
    "lightseagreen",
    "lightskyblue",
    "lightslategray",
    "lightslategrey",
    "lightsteelblue",
    "lightyellow",
    "limegreen",
    "linen",
    "magenta",
    "mediumaquamarine",
    "mediumblue",
    "mediumorchid",
    "mediumpurple",
    "mediumseagreen",
    "mediumslateblue",
    "mediumspringgreen",
    "mediumturquoise",
    "mediumvioletred",
    "midnightblue",
    "mintcream",
    "mistyrose",
    "moccasin",
    "navajowhite",
    "oldlace",
    "olivedrab",
    "orange",
    "orangered",
    "orchid",
    "palegoldenrod",
    "palegreen",
    "paleturquoise",
    "palevioletred",
    "papayawhip",
    "peachpuff",
    "peru",
    "pink",
    "plum",
    "powderblue",
    "rosybrown",
    "royalblue",
    "saddlebrown",
    "salmon",
    "sandybrown",
    "seagreen",
    "seashell",
    "sienna",
    "skyblue",
    "slateblue",
    "slategray",
    "slategrey",
    "snow",
    "springgreen",
    "steelblue",
    "tan",
    "thistle",
    "tomato",
    "turquoise",
    "violet",
    "wheat",
    "whitesmoke",
    "yellowgreen",
    "rebeccapurple",
    "transparent",
}


def is_valid_hex_color(color: str) -> bool:
    """
    Check if a string is a valid hex color.

    Accepts formats: #RGB, #RRGGBB, #RRGGBBAA

    Args:
        color: Color string to validate.

    Returns:
        True if valid hex color, False otherwise.
    """
    return bool(HEX_COLOR_PATTERN.match(color))


def is_valid_css_color(color: str) -> bool:
    """
    Check if a string is a valid CSS named color.

    Args:
        color: Color name to validate.

    Returns:
        True if valid CSS color name, False otherwise.
    """
    return color.lower() in CSS_COLORS


def is_valid_color(color: str) -> bool:
    """
    Check if a string is a valid color (hex or CSS name).

    Args:
        color: Color string to validate.

    Returns:
        True if valid color, False otherwise.
    """
    return is_valid_hex_color(color) or is_valid_css_color(color)


def validate_color(color: str, name: Optional[str] = None) -> str:
    """
    Validate a color value and return it if valid.

    Args:
        color: Color string to validate.
        name: Optional name for error messages (e.g., "theme_color").

    Returns:
        The validated color string.

    Raises:
        FaviconColorError: If color is invalid.
    """
    if not color:
        raise FaviconColorError(
            color,
            f"Empty color value for {name}." if name else "Empty color value.",
        )

    if is_valid_color(color):
        return color

    raise FaviconColorError(
        color,
        (
            f"Invalid color '{color}' for {name}. "
            f"Must be a hex color (#RGB, #RRGGBB) or CSS color name."
            if name
            else f"Invalid color '{color}'. "
            f"Must be a hex color (#RGB, #RRGGBB) or CSS color name."
        ),
    )


def normalize_hex_color(color: str) -> str:
    """
    Normalize a hex color to 6-character format.

    Converts #RGB to #RRGGBB format.

    Args:
        color: Valid hex color string.

    Returns:
        Normalized 6-character hex color.

    Raises:
        FaviconColorError: If color is not a valid hex color.
    """
    if not is_valid_hex_color(color):
        raise FaviconColorError(color, f"'{color}' is not a valid hex color.")

    # Remove # prefix
    hex_part = color[1:]

    # Expand 3-character hex to 6-character
    if len(hex_part) == 3:
        hex_part = "".join(c * 2 for c in hex_part)

    # Handle 8-character RGBA (keep as-is)
    if len(hex_part) == 8:
        return f"#{hex_part}"

    return f"#{hex_part}"
