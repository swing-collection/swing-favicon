# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Favicon Static File View
========================

Simple view function for serving a static favicon.png file from the
project's static directory with caching headers applied.

"""


# =============================================================================
# Imports
# =============================================================================

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

# =============================================================================
# Views
# =============================================================================


@require_GET
@cache_control(
    max_age=FAVICON_CACHE_MAX_AGE,
    immutable=FAVICON_CACHE_IMMUTABLE,
    public=FAVICON_CACHE_PUBLIC,
)
def favicon(request: HttpRequest) -> FileResponse:
    """Serve favicon.png from static directory."""

    file = (settings.BASE_DIR / "static" / "favicon.png").open("rb")
    return FileResponse(file)
