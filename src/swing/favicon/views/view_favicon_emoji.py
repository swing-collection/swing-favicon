


# https://adamj.eu/tech/2022/01/18/how-to-add-a-favicon-to-your-django-site/

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

    return HttpResponse(
        (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
            + '<text y=".9em" font-size="90">👾</text>'
            + "</svg>"
        ),
        content_type="image/svg+xml",
    )
