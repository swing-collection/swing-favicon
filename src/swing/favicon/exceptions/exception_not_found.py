# -*- coding: utf-8 -*-
"""
Favicon Not Found Exception
===========================

Raised when a requested favicon file does not exist at the expected path.

"""

# Import | Standard Library
from pathlib import Path

# Import | Local
from .exception_base import FaviconsError


class FaviconNotFoundError(FaviconsError):
    """
    Raised when a favicon file does not exist.

    This exception is raised when attempting to serve or process
    a favicon file that cannot be found at the specified path.

    Args:
        file: Path to the favicon file that was not found.

    Example:
        if not favicon_path.exists():
            raise FaviconNotFoundError(favicon_path)

    """

    def __init__(self, file: Path) -> None:
        """
        Initialize the exception.

        Args:
            file: Path to the favicon file that was not found.
        """
        super().__init__("{} does not exist.", str(file))
