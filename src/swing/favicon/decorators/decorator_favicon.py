# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Favicon Decorators
===========================

Decorators for adding favicon-related functionality to views.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from functools import wraps
from typing import Callable, Any

# Import | Libraries
from django.http import HttpRequest, HttpResponse
from django.views.decorators.cache import cache_control

# Import | Local Modules
from ..conf import (
    FAVICON_CACHE_MAX_AGE,
    FAVICON_CACHE_IMMUTABLE,
    FAVICON_CACHE_PUBLIC,
)


# =============================================================================
# Variables
# =============================================================================

__all__: list[str] = ["favicon_cache", "add_favicon_headers"]


# =============================================================================
# Decorators
# =============================================================================

def favicon_cache(
    max_age: int = FAVICON_CACHE_MAX_AGE,
    immutable: bool = FAVICON_CACHE_IMMUTABLE,
    public: bool = FAVICON_CACHE_PUBLIC,
) -> Callable:
    """
    Decorator to apply favicon-specific cache headers to a view.

    This is a convenience wrapper around Django's cache_control decorator
    with favicon-optimized defaults.

    Args:
        max_age: Cache duration in seconds (default: from settings).
        immutable: Whether to mark as immutable (default: from settings).
        public: Whether to mark as public (default: from settings).

    Returns:
        Decorated view function.

    Usage:
        @favicon_cache()
        def my_favicon_view(request):
            ...

        @favicon_cache(max_age=86400 * 365)  # 1 year
        def long_cached_favicon(request):
            ...
    """
    return cache_control(max_age=max_age, immutable=immutable, public=public)


def add_favicon_headers(view_func: Callable) -> Callable:
    """
    Decorator to add favicon-specific headers to response.

    Adds headers like X-Content-Type-Options for security.

    Args:
        view_func: The view function to decorate.

    Returns:
        Decorated view function.

    Usage:
        @add_favicon_headers
        def my_favicon_view(request):
            ...
    """

    @wraps(view_func)
    def wrapper(request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        response = view_func(request, *args, **kwargs)

        # Security headers
        response["X-Content-Type-Options"] = "nosniff"

        # Indicate this is a favicon response
        response["X-Favicon"] = "true"

        return response

    return wrapper
