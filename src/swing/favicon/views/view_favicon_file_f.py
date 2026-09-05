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
# Imports
# =============================================================================

from django.conf import settings
from django.http import FileResponse, Http404, HttpRequest
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET

# Import | Local
from ..conf import (
    FAVICON_CACHE_IMMUTABLE,
    FAVICON_CACHE_MAX_AGE,
    FAVICON_CACHE_PUBLIC,
)

# =============================================================================
# Variables
# =============================================================================

__all__: list[str] = [
    "favicon_file_view",
]


# =============================================================================
# Classes
# =============================================================================


@require_GET
@cache_control(
    max_age=FAVICON_CACHE_MAX_AGE,
    immutable=FAVICON_CACHE_IMMUTABLE,
    public=FAVICON_CACHE_PUBLIC,
)
def favicon_file_view(request: HttpRequest) -> FileResponse:
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

    # Sanitize filename - prevent directory traversal
    # Import | Standard Library
    from pathlib import Path

    name = Path(name).name
    if not name or ".." in name:
        raise Http404("Invalid filename.")

    file_path = settings.BASE_DIR / "static" / name
    static_dir = (settings.BASE_DIR / "static").resolve()

    # Ensure the file path is within the expected directory
    if not file_path.is_file():
        raise Http404(f"File '{name}' not found.")

    # Security check: ensure resolved path is within static directory
    if not file_path.resolve().is_relative_to(static_dir):
        raise Http404(f"File '{name}' not found.")

    try:
        # FileResponse handles closing the file automatically
        return FileResponse(
            open(file_path, "rb"),  # noqa: SIM115
            content_type="application/octet-stream",
        )
    except IOError as exc:
        raise Http404(f"Unable to read file '{name}'.") from exc
