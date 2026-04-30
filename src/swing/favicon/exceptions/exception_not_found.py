# -*- coding: utf-8 -*-
"""Favicon not found exception."""

# Import | Standard Library
from pathlib import Path

# Import | Local
from .exception_base import FaviconsError


class FaviconNotFoundError(FaviconsError):
    """Raised if the source favicon doesn't exist."""

    def __init__(self, file: Path) -> None:
        """Set message."""
        super().__init__("{} does not exit.", str(file))
