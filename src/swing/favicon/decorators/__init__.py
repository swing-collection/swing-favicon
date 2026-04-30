# -*- coding: utf-8 -*-


# Docstring
# =============================================================================

"""
Provides Favicon Decorators Module
=================================


"""


# Imports
# =============================================================================

# Import | Local
from .decorator_cache import favicon_cache
from .decorator_headers import add_favicon_headers

__all__ = [
    "favicon_cache",
    "add_favicon_headers",
]
