# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Base Favicon View Mixin
=======================

Provides common functionality for favicon views including caching,
file serving, content type detection, and ETag support.

"""

# Import | Standard Library
import hashlib
import mimetypes
from pathlib import Path

from django.contrib.staticfiles import finders
from django.http import FileResponse, Http404, HttpRequest, HttpResponse
from django.utils.decorators import method_decorator
from django.utils.http import http_date
from django.views import View
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET

# Import | Local
from ..conf import (
    FAVICON_BASE_PATH,
    FAVICON_CACHE_IMMUTABLE,
    FAVICON_CACHE_MAX_AGE,
    FAVICON_CACHE_PUBLIC,
)

# Content type mapping for favicon files
FAVICON_CONTENT_TYPES = {
    ".ico": "image/x-icon",
    ".png": "image/png",
    ".svg": "image/svg+xml",
    ".xml": "application/xml",
    ".webmanifest": "application/manifest+json",
    ".json": "application/json",
    ".webp": "image/webp",
}


class FaviconViewMixin:
    """
    Mixin providing common favicon serving functionality.

    This mixin can be used by any favicon view to provide consistent
    behavior for:
    - File path resolution
    - Content type detection
    - Cache headers
    - Security checks (path traversal prevention)

    Attributes:
        filename: Optional filename to serve. If None, derived from request.
        base_path: Base path within static files for favicon lookup.
    """

    filename: str | None = None
    base_path: str = FAVICON_BASE_PATH

    def get_filename(self, request: HttpRequest, *args, **kwargs) -> str:
        """
        Get filename from kwargs, class attribute, or URL path.

        Args:
            request: HTTP request object.
            *args: Positional arguments.
            **kwargs: Keyword arguments (may contain 'filename').

        Returns:
            str: The resolved filename.
        """
        return kwargs.get("filename") or self.filename or request.path.lstrip("/")

    def sanitize_filename(self, name: str) -> str:
        """
        Sanitize filename to prevent directory traversal.

        Args:
            name: Raw filename from request.

        Returns:
            str: Sanitized filename with path components removed.

        Raises:
            Http404: If filename is invalid.
        """
        # Get just the filename component
        sanitized = Path(name).name

        if not sanitized or ".." in sanitized:
            raise Http404("Invalid filename.")

        return sanitized

    def find_favicon_file(self, name: str) -> Path | None:
        """
        Find a favicon file in static directories.

        Searches in order:
        1. FAVICON_BASE_PATH + name
        2. 'favicon/' + name
        3. Root static directory

        Args:
            name: The filename to find.

        Returns:
            Path to the file if found, None otherwise.
        """
        search_paths = [
            f"{self.base_path}/{name}",
            f"favicon/{name}",
            name,
        ]

        for search_path in search_paths:
            result = finders.find(search_path)
            if result:
                return Path(result)

        return None

    def get_content_type(self, filename: str) -> str:
        """
        Determine content type for a favicon file.

        Args:
            filename: Name of the favicon file.

        Returns:
            str: MIME type for the file.
        """
        suffix = Path(filename).suffix.lower()
        return FAVICON_CONTENT_TYPES.get(
            suffix, mimetypes.guess_type(filename)[0] or "application/octet-stream"
        )

    def generate_etag(self, file_path: Path) -> str:
        """
        Generate ETag for a file based on path and modification time.

        Uses a combination of file path, size, and modification time
        to create a unique identifier without reading file contents.

        Args:
            file_path: Path to the file.

        Returns:
            str: Quoted ETag value (e.g., '"abc123"').
        """
        stat = file_path.stat()
        # Create hash from path + size + mtime
        etag_source = f"{file_path}:{stat.st_size}:{stat.st_mtime}"
        etag_hash = hashlib.md5(etag_source.encode()).hexdigest()[:16]
        return f'"{etag_hash}"'

    def check_not_modified(
        self, request: HttpRequest, file_path: Path, etag: str
    ) -> HttpResponse | None:
        """
        Check if client cache is still valid.

        Args:
            request: HTTP request with If-None-Match header.
            file_path: Path to the file.
            etag: Generated ETag value.

        Returns:
            304 Not Modified response if cache is valid, None otherwise.
        """
        if_none_match = request.META.get("HTTP_IF_NONE_MATCH")
        if if_none_match and if_none_match == etag:
            response = HttpResponse(status=304)
            response["ETag"] = etag
            return response
        return None

    def serve_file(
        self,
        file_path: Path,
        filename: str,
        request: HttpRequest | None = None,
    ) -> HttpResponse | FileResponse:
        """
        Serve a file as a FileResponse with ETag and Last-Modified headers.

        Args:
            file_path: Path to the file.
            filename: Original filename for content type detection.
            request: Optional request for If-None-Match checking.

        Returns:
            FileResponse with appropriate headers, or 304 Not Modified.

        Raises:
            Http404: If file cannot be read.
        """
        content_type = self.get_content_type(filename)

        try:
            # Generate ETag
            etag = self.generate_etag(file_path)

            # Check for conditional request
            if request:
                not_modified = self.check_not_modified(request, file_path, etag)
                if not_modified:
                    return not_modified

            # Get file stats for Last-Modified
            stat = file_path.stat()
            last_modified = http_date(stat.st_mtime)

            # FileResponse handles closing the file automatically
            response = FileResponse(
                open(file_path, "rb"),  # noqa: SIM115
                content_type=content_type,
            )

            # Add caching headers
            response["ETag"] = etag
            response["Last-Modified"] = last_modified
            response["Vary"] = "Accept-Encoding"

            return response

        except IOError as err:
            raise Http404(f"Unable to read file '{filename}'.") from err


@method_decorator(require_GET, name="dispatch")
@method_decorator(
    cache_control(
        max_age=FAVICON_CACHE_MAX_AGE,
        immutable=FAVICON_CACHE_IMMUTABLE,
        public=FAVICON_CACHE_PUBLIC,
    ),
    name="dispatch",
)
class BaseFaviconView(FaviconViewMixin, View):
    """
    Base class-based view for serving favicon files.

    Combines FaviconViewMixin with View and applies cache control
    decorators to provide a complete base class for favicon serving.

    Usage:
        class MyFaviconView(BaseFaviconView):
            filename = "my-favicon.ico"

        # Or in urls.py:
        path("favicon.ico", BaseFaviconView.as_view(filename="favicon.ico"))
    """

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse | FileResponse:
        """
        Handle GET requests to serve a favicon file.

        Args:
            request: The incoming HTTP request.
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Returns:
            HttpResponse containing the favicon file.

        Raises:
            Http404: If favicon file not found or invalid.
        """
        name = self.get_filename(request, *args, **kwargs)
        name = self.sanitize_filename(name)

        file_path = self.find_favicon_file(name)
        if file_path is None:
            raise Http404(f"Favicon '{name}' not found.")

        return self.serve_file(file_path, name, request)
