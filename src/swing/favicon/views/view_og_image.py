# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Open Graph Image View
=====================

Class-based view for generating dynamic Open Graph images.

Renders a 1200x630 PNG image with title, subtitle, and optional eyebrow text.
Falls back to a static image if Pillow is not available.

Usage::

    from swing.favicon.views import OgImageView

    urlpatterns = [
        path("og/<slug:slug>.png", OgImageView.as_view(), name="og_image"),
    ]

Query parameters:
    - title: Main title text (defaults to slug)
    - subtitle: Subtitle text
    - eyebrow: Small text above title

Configuration::

    # settings.py
    FAVICON_OG_FALLBACK_URL = "/static/og-image.svg"
    FAVICON_OG_CACHE_MAX_AGE = 86400
    FAVICON_OG_EYEBROW = "My App"

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import hashlib
from typing import Any

from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.templatetags.static import static
from django.utils.cache import patch_cache_control
from django.views import View

from ..utils.util_og_image import generate_og_image


# =============================================================================
# Configuration
# =============================================================================

OG_FALLBACK_URL: str = getattr(settings, "FAVICON_OG_FALLBACK_URL", "")
OG_CACHE_MAX_AGE: int = getattr(settings, "FAVICON_OG_CACHE_MAX_AGE", 86400)


# =============================================================================
# Classes
# =============================================================================


class OgImageView(View):
    """
    Open Graph Image View
    =====================

    Generates dynamic Open Graph (social share) images.

    Creates a 1200x630 PNG with:
    - Brand accent bar at top
    - Eyebrow text (e.g., app name)
    - Title text (wrapped to fit)
    - Subtitle text at bottom

    Attributes:
        fallback_url: Static URL to redirect to if image generation fails.
        cache_max_age: Cache duration in seconds.
        default_eyebrow: Default eyebrow text.
        default_subtitle: Default subtitle text.

    Example::

        # urls.py
        path("og/<slug:slug>.png", OgImageView.as_view(
            default_eyebrow="My App",
            default_subtitle="myapp.com",
        ), name="og_image"),

    Subclassing::

        class MyOgImageView(OgImageView):
            default_eyebrow = "My Brand"
            default_subtitle = "example.com"

            def get_title(self, request, slug):
                # Look up title from database
                article = Article.objects.get(slug=slug)
                return article.title

    """

    http_method_names = ["get", "head", "options"]

    # Configuration
    fallback_url: str = ""
    cache_max_age: int = OG_CACHE_MAX_AGE
    default_eyebrow: str = ""
    default_subtitle: str = ""

    def get(
        self,
        request: HttpRequest,
        slug: str = "",
        **kwargs: Any,
    ) -> HttpResponse | HttpResponseRedirect:
        """
        Handle GET request and return OG image.

        Args:
            request: HTTP request.
            slug: URL slug for the page (used as default title).
            **kwargs: Additional URL kwargs.

        Returns:
            PNG image response, or redirect to fallback image.
        """
        title = self.get_title(request, slug, **kwargs)
        subtitle = self.get_subtitle(request, slug, **kwargs)
        eyebrow = self.get_eyebrow(request, slug, **kwargs)

        # Generate image
        png = generate_og_image(
            title=title,
            subtitle=subtitle,
            eyebrow=eyebrow,
        )

        if png is None:
            return self.get_fallback_response(request)

        # Build response
        response = HttpResponse(png, content_type="image/png")

        # Strong ETag based on inputs for CDN caching
        etag = self.generate_etag(title, subtitle, eyebrow)
        response["ETag"] = etag

        # Cache control
        patch_cache_control(
            response,
            public=True,
            max_age=self.cache_max_age,
        )

        return response

    def get_title(
        self,
        request: HttpRequest,
        slug: str,
        **kwargs: Any,
    ) -> str:
        """
        Get the title for the OG image.

        Override this method to customize title generation, e.g., from database.

        Args:
            request: HTTP request with optional 'title' query param.
            slug: URL slug.
            **kwargs: Additional URL kwargs.

        Returns:
            Title string.
        """
        return request.GET.get("title", slug.replace("-", " ").title())

    def get_subtitle(
        self,
        request: HttpRequest,
        slug: str,
        **kwargs: Any,
    ) -> str:
        """
        Get the subtitle for the OG image.

        Args:
            request: HTTP request with optional 'subtitle' query param.
            slug: URL slug.
            **kwargs: Additional URL kwargs.

        Returns:
            Subtitle string.
        """
        return request.GET.get("subtitle", self.default_subtitle)

    def get_eyebrow(
        self,
        request: HttpRequest,
        slug: str,
        **kwargs: Any,
    ) -> str:
        """
        Get the eyebrow text for the OG image.

        Args:
            request: HTTP request with optional 'eyebrow' query param.
            slug: URL slug.
            **kwargs: Additional URL kwargs.

        Returns:
            Eyebrow string.
        """
        return request.GET.get("eyebrow", self.default_eyebrow)

    def generate_etag(self, title: str, subtitle: str, eyebrow: str) -> str:
        """
        Generate ETag for caching.

        Args:
            title: Title text.
            subtitle: Subtitle text.
            eyebrow: Eyebrow text.

        Returns:
            Quoted ETag string.
        """
        content = f"{title}|{subtitle}|{eyebrow}"
        etag_hash = hashlib.md5(content.encode("utf-8")).hexdigest()
        return f'"{etag_hash}"'

    def get_fallback_response(
        self,
        request: HttpRequest,
    ) -> HttpResponseRedirect | HttpResponse:
        """
        Return fallback response when image generation fails.

        Args:
            request: HTTP request.

        Returns:
            Redirect to fallback URL or 404 response.
        """
        fallback = self.fallback_url or OG_FALLBACK_URL
        if fallback:
            # If it's a static path, resolve it
            if not fallback.startswith(("http://", "https://", "/")):
                fallback = static(fallback)
            return HttpResponseRedirect(fallback)

        # No fallback configured, return 404
        return HttpResponse("Image generation unavailable", status=404)


# =============================================================================
# Exports
# =============================================================================

__all__ = ["OgImageView"]
