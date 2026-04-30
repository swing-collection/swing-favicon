# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Favicon File View Function
===================================

This module contains a class-based view for serving favicon files in a Django
application. It utilizes caching mechanisms for efficient favicon delivery.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
import mimetypes
from pathlib import Path
from typing import Optional

# Import | Libraries
from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse, Http404
from django.views import View
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_control
from django.utils.decorators import method_decorator
from django.contrib.staticfiles import finders

# Import | Local Modules
from ..conf import (
    FAVICON_BASE_PATH,
    FAVICON_CACHE_MAX_AGE,
    FAVICON_CACHE_IMMUTABLE,
    FAVICON_CACHE_PUBLIC,
)


# =============================================================================
# Variables
# =============================================================================

__all__: list[str] = ["FaviconFileView"]

# Content type mapping for favicon files
CONTENT_TYPES = {
    ".ico": "image/x-icon",
    ".png": "image/png",
    ".svg": "image/svg+xml",
    ".xml": "application/xml",
    ".webmanifest": "application/manifest+json",
    ".json": "application/json",
}


# =============================================================================
# Classes
# =============================================================================

class FaviconFileView(View):
    """
    Class-based view to serve favicon files.

    This view reads favicon files from the static directory and returns them
    in an HTTP response. Caching directives are applied to optimize delivery.

    Attributes:
        filename: Optional filename to serve. If None, uses request path.

    Methods:
        get: Handles GET requests and serves the favicon file.
    """

    filename: Optional[str] = None

    @method_decorator(require_GET)
    @method_decorator(
        cache_control(
            max_age=FAVICON_CACHE_MAX_AGE,
            immutable=FAVICON_CACHE_IMMUTABLE,
            public=FAVICON_CACHE_PUBLIC,
        )
    )
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """
        Handle GET requests to serve a favicon file.

        Parameters:
            request: The incoming HTTP request.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments. May contain 'filename'.

        Returns:
            HttpResponse: An HTTP response object containing the favicon file.

        Raises:
            Http404: If the requested favicon file does not exist.
        """
        # Determine filename from kwargs, class attribute, or URL path
        name = kwargs.get("filename") or self.filename or request.path.lstrip("/")

        # Sanitize filename - prevent directory traversal
        name = Path(name).name
        if not name or ".." in name:
            raise Http404("Invalid filename.")

        # Try to find file in static files
        file_path = self._find_favicon_file(name)

        if file_path is None:
            raise Http404(f"Favicon '{name}' not found.")

        # Determine content type
        suffix = Path(name).suffix.lower()
        content_type = CONTENT_TYPES.get(
            suffix, mimetypes.guess_type(name)[0] or "application/octet-stream"
        )

        try:
            return FileResponse(
                open(file_path, "rb"),
                content_type=content_type,
            )
        except IOError as err:
            raise Http404(f"Unable to read favicon '{name}'.") from err

    def _find_favicon_file(self, name: str) -> Optional[Path]:
        """
        Find a favicon file in static directories.

        Searches in order:
        1. FAVICON_BASE_PATH + name
        2. 'favicon/' + name
        3. Root static directory

        Parameters:
            name: The filename to find.

        Returns:
            Path to the file if found, None otherwise.
        """
        # Search paths in priority order
        search_paths = [
            f"{FAVICON_BASE_PATH}/{name}",
            f"favicon/{name}",
            name,
        ]

        for search_path in search_paths:
            found = finders.find(search_path)
            if found:
                file_path = Path(found)
                if file_path.is_file():
                    return file_path

        # Fallback: check BASE_DIR/static directly
        if hasattr(settings, "BASE_DIR"):
            for search_path in search_paths:
                file_path = settings.BASE_DIR / "static" / search_path
                if file_path.is_file():
                    return file_path

        return None
