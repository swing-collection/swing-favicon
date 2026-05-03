# -*- coding: utf-8 -*-


# Docstring
# =============================================================================

"""
Favicon Exceptions
==================

Exception classes for favicon operations.

Exception Hierarchy:
    FaviconsError (base)
    ├── FaviconNotFoundError  - Raised when favicon file doesn't exist
    ├── FaviconNotSupportedError - Raised for unsupported file formats
    └── FaviconColorError - Raised for invalid color values

Example:
    from swing.favicon.exceptions import FaviconNotFoundError

    if not favicon_path.exists():
        raise FaviconNotFoundError(favicon_path)

"""


# Imports
# =============================================================================

# Import | Local
from .exception_base import FaviconsError
from .exception_color import FaviconColorError
from .exception_not_found import FaviconNotFoundError
from .exception_not_supported import FaviconNotSupportedError

__all__ = [
    "FaviconsError",
    "FaviconColorError",
    "FaviconNotFoundError",
    "FaviconNotSupportedError",
]
