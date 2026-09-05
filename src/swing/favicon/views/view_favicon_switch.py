# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Debug-Aware Favicon View
========================

View that serves different favicon files based on Django's DEBUG setting.
Useful for visually distinguishing development from production environments.

"""

from django.conf import settings
from django.http import FileResponse, HttpRequest
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET

# Import | Local
from ..conf import (
    FAVICON_CACHE_IMMUTABLE,
    FAVICON_CACHE_MAX_AGE,
    FAVICON_CACHE_PUBLIC,
)


@require_GET
@cache_control(
    max_age=FAVICON_CACHE_MAX_AGE,
    immutable=FAVICON_CACHE_IMMUTABLE,
    public=FAVICON_CACHE_PUBLIC,
)
def favicon(request: HttpRequest) -> FileResponse:
    """
    Serve favicon based on DEBUG setting.

    Returns a different favicon file depending on whether Django is running
    in DEBUG mode, allowing visual distinction between environments.

    Args:
        request: The incoming HTTP request.

    Returns:
        FileResponse containing the appropriate favicon image.

    Raises:
        Http404: If the favicon file does not exist.
    """
    name = "favicon-debug.png" if settings.DEBUG else "favicon.png"
    file_path = settings.BASE_DIR / "static" / name

    if not file_path.is_file():
        from django.http import Http404

        raise Http404(f"Favicon '{name}' not found.")

    # FileResponse handles closing the file automatically
    return FileResponse(
        open(file_path, "rb"),  # noqa: SIM115
        content_type="image/png",
    )
