# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Favicon Views Module
====================

Views for serving favicon files, browserconfig.xml, and site.webmanifest.

Exported Views:
    BaseFaviconView: Base class for all favicon views with caching.
    FaviconViewMixin: Mixin providing common favicon functionality.
    FaviconFileView: Class-based view for serving favicon files from static.
    favicon_file_view: Function-based view for serving favicon files.
    BrowserConfigView: Dynamic browserconfig.xml generation for Windows tiles.
    WebManifestView: Dynamic site.webmanifest generation for PWA support.

Example:
    In urls.py::

        from swing.favicon.views import FaviconFileView, WebManifestView

        urlpatterns = [
            path('favicon.ico', FaviconFileView.as_view()),
            path('site.webmanifest', WebManifestView.as_view()),
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
from .view_webmanifest import WebManifestView

__all__ = [
    "BaseFaviconView",
    "BrowserConfigView",
    "FaviconFileView",
    "FaviconViewMixin",
    "favicon_file_view",
    "WebManifestView",
]
