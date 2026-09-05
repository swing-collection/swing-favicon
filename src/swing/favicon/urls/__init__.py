# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Favicon URLs Module
============================

URL patterns for serving favicon files. Supports all common favicon formats
including ICO, PNG, SVG, and web manifests.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from typing import TYPE_CHECKING

from django.urls import path, re_path
from django.urls.resolvers import URLPattern, URLResolver

# Import | Local
# Import | Local Modules
from ..views import BrowserConfigView, FaviconFileView, OgImageView, WebManifestView

if TYPE_CHECKING:
    pass  # pylint: disable=unnecessary-pass


# =============================================================================
# Variables
# =============================================================================

# Export
__all__: list[str] = ["app_name", "urlpatterns"]

# App Name
app_name = "favicon"


# =============================================================================
# URL Patterns
# =============================================================================

urlpatterns: list[URLPattern | URLResolver] = [
    # Primary favicon
    path("favicon.ico", FaviconFileView.as_view(), name="favicon"),
    # Standard PNG favicons
    path("favicon-16x16.png", FaviconFileView.as_view(), name="favicon-16"),
    path("favicon-32x32.png", FaviconFileView.as_view(), name="favicon-32"),
    path("favicon-48x48.png", FaviconFileView.as_view(), name="favicon-48"),
    path("favicon-64x64.png", FaviconFileView.as_view(), name="favicon-64"),
    path("favicon-96x96.png", FaviconFileView.as_view(), name="favicon-96"),
    path("favicon-128x128.png", FaviconFileView.as_view(), name="favicon-128"),
    path("favicon-192x192.png", FaviconFileView.as_view(), name="favicon-192"),
    path("favicon-256x256.png", FaviconFileView.as_view(), name="favicon-256"),
    path("favicon-512x512.png", FaviconFileView.as_view(), name="favicon-512"),
    # SVG favicon (modern browsers)
    path("favicon.svg", FaviconFileView.as_view(), name="favicon-svg"),
    # Android Chrome icons (PWA)
    path(
        "android-chrome-36x36.png", FaviconFileView.as_view(), name="android-chrome-36"
    ),
    path(
        "android-chrome-48x48.png", FaviconFileView.as_view(), name="android-chrome-48"
    ),
    path(
        "android-chrome-72x72.png", FaviconFileView.as_view(), name="android-chrome-72"
    ),
    path(
        "android-chrome-96x96.png", FaviconFileView.as_view(), name="android-chrome-96"
    ),
    path(
        "android-chrome-144x144.png",
        FaviconFileView.as_view(),
        name="android-chrome-144",
    ),
    path(
        "android-chrome-192x192.png",
        FaviconFileView.as_view(),
        name="android-chrome-192",
    ),
    path(
        "android-chrome-384x384.png",
        FaviconFileView.as_view(),
        name="android-chrome-384",
    ),
    path(
        "android-chrome-512x512.png",
        FaviconFileView.as_view(),
        name="android-chrome-512",
    ),
    # Maskable icons (PWA safe zone)
    path(
        "android-chrome-maskable-192x192.png",
        FaviconFileView.as_view(),
        name="android-chrome-maskable-192",
    ),
    path(
        "android-chrome-maskable-512x512.png",
        FaviconFileView.as_view(),
        name="android-chrome-maskable-512",
    ),
    # Apple Touch Icons
    path("apple-touch-icon.png", FaviconFileView.as_view(), name="apple-touch-icon"),
    path(
        "apple-touch-icon-57x57.png",
        FaviconFileView.as_view(),
        name="apple-touch-icon-57",
    ),
    path(
        "apple-touch-icon-60x60.png",
        FaviconFileView.as_view(),
        name="apple-touch-icon-60",
    ),
    path(
        "apple-touch-icon-72x72.png",
        FaviconFileView.as_view(),
        name="apple-touch-icon-72",
    ),
    path(
        "apple-touch-icon-76x76.png",
        FaviconFileView.as_view(),
        name="apple-touch-icon-76",
    ),
    path(
        "apple-touch-icon-114x114.png",
        FaviconFileView.as_view(),
        name="apple-touch-icon-114",
    ),
    path(
        "apple-touch-icon-120x120.png",
        FaviconFileView.as_view(),
        name="apple-touch-icon-120",
    ),
    path(
        "apple-touch-icon-144x144.png",
        FaviconFileView.as_view(),
        name="apple-touch-icon-144",
    ),
    path(
        "apple-touch-icon-152x152.png",
        FaviconFileView.as_view(),
        name="apple-touch-icon-152",
    ),
    path(
        "apple-touch-icon-167x167.png",
        FaviconFileView.as_view(),
        name="apple-touch-icon-167",
    ),
    path(
        "apple-touch-icon-180x180.png",
        FaviconFileView.as_view(),
        name="apple-touch-icon-180",
    ),
    path(
        "apple-touch-icon-precomposed.png",
        FaviconFileView.as_view(),
        name="apple-touch-icon-precomposed",
    ),
    # Microsoft Tiles
    path("mstile-70x70.png", FaviconFileView.as_view(), name="mstile-70"),
    path("mstile-144x144.png", FaviconFileView.as_view(), name="mstile-144"),
    path("mstile-150x150.png", FaviconFileView.as_view(), name="mstile-150"),
    path("mstile-270x270.png", FaviconFileView.as_view(), name="mstile-270"),
    path("mstile-310x150.png", FaviconFileView.as_view(), name="mstile-310x150"),
    path("mstile-310x310.png", FaviconFileView.as_view(), name="mstile-310"),
    # browserconfig.xml (Windows) - Dynamic generation
    path("browserconfig.xml", BrowserConfigView.as_view(), name="browserconfig"),
    # Safari Pinned Tab (mask-icon)
    path("safari-pinned-tab.svg", FaviconFileView.as_view(), name="safari-pinned-tab"),
    path("mask-icon.svg", FaviconFileView.as_view(), name="mask-icon"),
    # Web Manifest (PWA) - Dynamic generation
    path("site.webmanifest", WebManifestView.as_view(), name="webmanifest"),
    path("manifest.json", WebManifestView.as_view(), name="manifest"),
    # Open Graph Image - Dynamic generation
    path("og/<slug:slug>.png", OgImageView.as_view(), name="og-image"),
    # Dynamic route for any favicon file (catch-all, should be last)
    re_path(
        r"^(?P<filename>favicon[a-z0-9\-]*\.(ico|png|svg))$",
        FaviconFileView.as_view(),
        name="favicon-dynamic",
    ),
]
