

from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import cache_page
from ..conf import (
    FAVICON_CACHE_MAX_AGE,
    FAVICON_CACHE_IMMUTABLE,
    FAVICON_CACHE_PUBLIC
)


@require_GET
@cache_control(
    max_age = FAVICON_CACHE_MAX_AGE,
    immutable = FAVICON_CACHE_IMMUTABLE,
    public = FAVICON_CACHE_PUBLIC
)
def favicon(request: HttpRequest) -> HttpResponse:
    """
    """

    if settings.DEBUG:
        name = "favicon-debug.png"
    else:
        name = "favicon.png"
    file = (settings.BASE_DIR / "static" / name).open("rb")
    return FileResponse(file)