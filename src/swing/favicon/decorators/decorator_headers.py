# -*- coding: utf-8 -*-
"""Favicon headers decorator."""

from functools import wraps
from typing import Callable, Any

from django.http import HttpRequest, HttpResponse


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
