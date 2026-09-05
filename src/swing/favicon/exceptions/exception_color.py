# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Favicon Color Exception
=======================

Raised when an invalid color value is provided for favicon generation
or configuration (e.g., theme_color, ms_tile_color).

"""

# Import | Standard Library
from collections.abc import Generator, Iterable

# Import | Local
from .exception_base import FaviconsError


class FaviconColorError(FaviconsError):
    """
    Raised when an invalid color value is provided.

    This exception is raised when a color parameter (such as theme_color
    or ms_tile_color) contains an invalid value.

    Args:
        color: The invalid color value (string, iterable, or generator).
        message: Custom error message template. Defaults to standard message.

    Example:
        if not is_valid_hex_color(color):
            raise FaviconColorError(color)

    """

    def __init__(
        self,
        color: str | Iterable | Generator,
        message: str = "Color '{color}' is not a valid color.",
    ) -> None:
        """
        Initialize the exception.

        Args:
            color: The invalid color value.
            message: Error message template with {color} placeholder.
        """
        if isinstance(color, Iterable) and not isinstance(color, str):
            color = str(color)
        elif isinstance(color, Generator):
            color = ",".join(color)
        super().__init__(message, color=color)
