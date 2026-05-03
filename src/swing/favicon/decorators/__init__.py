# -*- coding: utf-8 -*-


# Docstring
# =============================================================================

"""
Favicon Decorators
==================

Decorators for favicon view functions.

Available Decorators:
    favicon_cache: Apply favicon-specific caching headers to a view.
    add_favicon_headers: Add favicon-related HTTP headers to responses.

Example:
    from swing.favicon.decorators import favicon_cache

    @favicon_cache
    def my_favicon_view(request):
        return FileResponse(open('favicon.ico', 'rb'))

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
