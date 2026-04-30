# -*- coding: utf-8 -*-
"""
View for serving dynamically generated browserconfig.xml.
"""

from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_control
from django.utils.decorators import method_decorator

from ..conf import FAVICON_CACHE_MAX_AGE
from ..utils.util_generate_browserconfig import generate_browserconfig


__all__ = ["BrowserConfigView"]


class BrowserConfigView(View):
    """
    View to serve dynamically generated browserconfig.xml.

    browserconfig.xml provides Windows 8/10/11 with tile configuration
    for pinned sites and Start menu tiles.
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
        Handle GET request for browserconfig.xml.

        Returns:
            HttpResponse: XML response with browserconfig content
        """
        content = generate_browserconfig()

        return HttpResponse(
            content,
            content_type="application/xml",
        )
