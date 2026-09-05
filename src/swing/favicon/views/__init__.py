# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Favicon Views Module
====================

Views for serving favicon files, browserconfig.xml, site.webmanifest,
and Open Graph images.

All views are class-based and follow the single-symbol-per-file convention.

Exported Views:
    BaseFaviconView: Base class for all favicon views with caching.
    FaviconViewMixin: Mixin providing common favicon functionality.
    FaviconFileView: Class-based view for serving favicon files from static.
    BrowserConfigView: Dynamic browserconfig.xml generation for Windows tiles.
    WebManifestView: Dynamic site.webmanifest generation for PWA support.
    OgImageView: Dynamic Open Graph image generation.

Legacy (deprecated):
    favicon_file_view: Function-based view (use FaviconFileView instead).

Example:
    In urls.py::

        from swing.favicon.views import (
            FaviconFileView,
            WebManifestView,
            OgImageView,
        )

        urlpatterns = [
            path('favicon.ico', FaviconFileView.as_view()),
            path('site.webmanifest', WebManifestView.as_view()),
            path('og/<slug:slug>.png', OgImageView.as_view()),
        ]

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Local
# Import | Local Modules
from .view_base import BaseFaviconView, FaviconViewMixin
from .view_browserconfig import BrowserConfigView
from .view_favicon_file import FaviconFileView
from .view_favicon_file_f import favicon_file_view
from .view_og_image import OgImageView
from .view_webmanifest import WebManifestView

__all__ = [
    # Class-based views
    "BaseFaviconView",
    "BrowserConfigView",
    "FaviconFileView",
    "FaviconViewMixin",
    "OgImageView",
    "WebManifestView",
    # Legacy (deprecated)
    "favicon_file_view",
]
