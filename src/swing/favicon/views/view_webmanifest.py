# -*- coding: utf-8 -*-
"""
View for serving dynamically generated site.webmanifest.
"""

from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_control
from django.utils.decorators import method_decorator

from ..conf import FAVICON_CACHE_MAX_AGE
from ..utils.util_generate_manifest import generate_manifest


__all__ = ["WebManifestView"]


class WebManifestView(View):
    """
    View to serve dynamically generated site.webmanifest.

    The web app manifest provides PWA configuration including
    app name, icons, colors, and display settings.
    """

    @method_decorator(require_GET)
    @method_decorator(
        cache_control(
            max_age=FAVICON_CACHE_MAX_AGE,
            public=True,
        )
    )
    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Handle GET request for site.webmanifest or manifest.json.

        Returns:
            HttpResponse: JSON response with manifest content
        """
        content = generate_manifest()

        return HttpResponse(
            content,
            content_type="application/manifest+json",
        )
