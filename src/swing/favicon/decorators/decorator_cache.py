# -*- coding: utf-8 -*-
"""Favicon cache decorator."""

from typing import Callable

from django.views.decorators.cache import cache_control

from ..conf import (
    FAVICON_CACHE_MAX_AGE,
    FAVICON_CACHE_IMMUTABLE,
    FAVICON_CACHE_PUBLIC,
)


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
