# -*- coding: utf-8 -*-
"""Favicon color exception."""

# Import | Standard Library
from collections.abc import Generator, Iterable

# Import | Local
from .exception_base import FaviconsError


class FaviconColorError(FaviconsError):
    """Raised if an input color is invalid."""

    def __init__(
        self,
        color: str | Iterable | Generator,
        message: str = "Color '{color}' is not a valid color.",
    ) -> None:
        """Set message."""
        if isinstance(color, Iterable):
            color = str(color)
        elif isinstance(color, Generator):
            color = ",".join(color)
        super().__init__(message, color=color)
