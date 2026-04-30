# -*- coding: utf-8 -*-


# Docstring
# =============================================================================

"""
Provides Favicon Exceptions Module
==================================


"""


# Imports
# =============================================================================

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
