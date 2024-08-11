# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Favicon File View Function
===================================

This module contains a view function for serving favicon files in a Django
application. It utilizes caching mechanisms for efficient favicon delivery
and ensures only GET requests are handled.

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Any, Dict, List
from pathlib import Path

# Import | Libraries
from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse, Http404
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import cache_page

# Import | Local Modules
from ..conf import (
    FAVICON_CACHE_MAX_AGE,
    FAVICON_CACHE_IMMUTABLE,
    FAVICON_CACHE_PUBLIC
)


# =============================================================================
# Variables
# =============================================================================

__all__ = ["favicon_file_view", ]


# =============================================================================
# Classes
# =============================================================================

@require_GET
@cache_control(
    max_age = FAVICON_CACHE_MAX_AGE,
    immutable = FAVICON_CACHE_IMMUTABLE,
    public = FAVICON_CACHE_PUBLIC
)
def favicon_file_view(request: HttpRequest) -> HttpResponse:
    """
    Favicon File View Function
    ==========================

    Serves a favicon file in response to a GET request.

    This view reads a favicon file from the 'static' directory and returns
    it in an HTTP response.
    Caching directives are applied to optimize delivery.

    Parameters:
    - request (HttpRequest): The incoming HTTP request.

    Returns:
    - HttpResponse: An HTTP response object containing the favicon file.

    Raises:
    - Http404: If the requested favicon file does not exist or is not
    accessible.

    """

    # name = request.path.lstrip("/")
    # file = (settings.BASE_DIR / "static" / name).open("rb")
    # return FileResponse(file)

    name = request.path.lstrip("/")
    file_path = settings.BASE_DIR / "static" / name

    # Ensure the file path is within the expected directory
    if not file_path.is_file() or not file_path.resolve().parent == (
        settings.BASE_DIR / "static"
    ).resolve():
        raise Http404(f"File '{name}' not found.")

    try:
        with file_path.open("rb") as file:
            return FileResponse(file)
    except IOError:
        raise Http404(f"Unable to read file '{name}'.")
