# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Favicon Constants
==========================

Static values for one way import.

Supports all modern favicon formats:
- Standard favicons (ICO, PNG, SVG)
- Apple Touch Icons (iOS/macOS)
- Android Chrome Icons (including maskable for PWA)
- Microsoft Tiles (Windows)
- Safari Pinned Tab (monochrome SVG)
- Web Manifest (PWA)
- browserconfig.xml (Windows)

"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from typing import NotRequired, TypedDict


# =============================================================================
# Types
# =============================================================================


class FaviconTypeConfig(TypedDict):
    """Configuration for a single generated favicon file."""

    format: str
    rel: str | None
    dimensions: tuple[int, int]
    prefix: str
    purpose: NotRequired[str]


# =============================================================================
# Constants
# =============================================================================

SUPPORTED_FORMATS = (
    ".svg",
    ".jpeg",
    ".jpg",
    ".png",
    ".tiff",
    ".tif",
)

HTML_LINK = '<link rel="{rel}" type="{type}" href="{href}" />'

# Multi-resolution ICO sizes (packed into single .ico file)
ICO_SIZES = (16, 24, 32, 48, 64, 128, 256)

# Android Chrome icon sizes (for PWA)
ANDROID_CHROME_SIZES = (36, 48, 72, 96, 144, 192, 384, 512)

# Maskable icon sizes (PWA safe zone icons)
MASKABLE_ICON_SIZES = (192, 512)

FAVICON_TYPES: tuple[FaviconTypeConfig, ...] = (
    # favicon.ico (multi-resolution handled separately)
    # -------------------------------------------------------------------------
    {"format": "ico", "rel": None, "dimensions": (64, 64), "prefix": "favicon"},
    # favicon.png (standard sizes)
    # -------------------------------------------------------------------------
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (16, 16),
        "prefix": "favicon",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (32, 32),
        "prefix": "favicon",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (48, 48),
        "prefix": "favicon",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (64, 64),
        "prefix": "favicon",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (96, 96),
        "prefix": "favicon",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (128, 128),
        "prefix": "favicon",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (180, 180),
        "prefix": "favicon",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (192, 192),
        "prefix": "favicon",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (256, 256),
        "prefix": "favicon",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (512, 512),
        "prefix": "favicon",
    },
    # Apple Touch Icons (iOS/macOS)
    # -------------------------------------------------------------------------
    {
        "format": "png",
        "rel": "apple-touch-icon",
        "dimensions": (57, 57),
        "prefix": "apple-touch-icon",
    },
    {
        "format": "png",
        "rel": "apple-touch-icon",
        "dimensions": (60, 60),
        "prefix": "apple-touch-icon",
    },
    {
        "format": "png",
        "rel": "apple-touch-icon",
        "dimensions": (72, 72),
        "prefix": "apple-touch-icon",
    },
    {
        "format": "png",
        "rel": "apple-touch-icon",
        "dimensions": (76, 76),
        "prefix": "apple-touch-icon",
    },
    {
        "format": "png",
        "rel": "apple-touch-icon",
        "dimensions": (114, 114),
        "prefix": "apple-touch-icon",
    },
    {
        "format": "png",
        "rel": "apple-touch-icon",
        "dimensions": (120, 120),
        "prefix": "apple-touch-icon",
    },
    {
        "format": "png",
        "rel": "apple-touch-icon",
        "dimensions": (144, 144),
        "prefix": "apple-touch-icon",
    },
    {
        "format": "png",
        "rel": "apple-touch-icon",
        "dimensions": (152, 152),
        "prefix": "apple-touch-icon",
    },
    {
        "format": "png",
        "rel": "apple-touch-icon",
        "dimensions": (167, 167),
        "prefix": "apple-touch-icon",
    },
    {
        "format": "png",
        "rel": "apple-touch-icon",
        "dimensions": (180, 180),
        "prefix": "apple-touch-icon",
    },
    {
        "format": "png",
        "rel": "apple-touch-icon",
        "dimensions": (1024, 1024),
        "prefix": "apple-touch-icon",
    },
    # Android Chrome Icons (PWA)
    # -------------------------------------------------------------------------
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (36, 36),
        "prefix": "android-chrome",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (48, 48),
        "prefix": "android-chrome",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (72, 72),
        "prefix": "android-chrome",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (96, 96),
        "prefix": "android-chrome",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (144, 144),
        "prefix": "android-chrome",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (192, 192),
        "prefix": "android-chrome",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (384, 384),
        "prefix": "android-chrome",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (512, 512),
        "prefix": "android-chrome",
    },
    # Maskable Icons (PWA safe zone)
    # -------------------------------------------------------------------------
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (192, 192),
        "prefix": "android-chrome-maskable",
        "purpose": "maskable",
    },
    {
        "format": "png",
        "rel": "icon",
        "dimensions": (512, 512),
        "prefix": "android-chrome-maskable",
        "purpose": "maskable",
    },
    # MS Tile (Windows)
    # -------------------------------------------------------------------------
    {
        "format": "png",
        "rel": None,
        "dimensions": (70, 70),
        "prefix": "mstile",
    },
    {
        "format": "png",
        "rel": None,
        "dimensions": (144, 144),
        "prefix": "mstile",
    },
    {
        "format": "png",
        "rel": None,
        "dimensions": (150, 150),
        "prefix": "mstile",
    },
    {
        "format": "png",
        "rel": None,
        "dimensions": (270, 270),
        "prefix": "mstile",
    },
    {
        "format": "png",
        "rel": None,
        "dimensions": (310, 310),
        "prefix": "mstile",
    },
    {
        "format": "png",
        "rel": None,
        "dimensions": (310, 150),
        "prefix": "mstile",
    },
    # Shortcut Icon
    # -------------------------------------------------------------------------
    {
        "format": "png",
        "rel": "shortcut icon",
        "dimensions": (196, 196),
        "prefix": "favicon",
    },
)


# =============================================================================
# Web Manifest Icon Configuration
# =============================================================================

MANIFEST_ICONS = [
    # Standard icons
    {"src": "/android-chrome-36x36.png", "sizes": "36x36", "type": "image/png"},
    {"src": "/android-chrome-48x48.png", "sizes": "48x48", "type": "image/png"},
    {"src": "/android-chrome-72x72.png", "sizes": "72x72", "type": "image/png"},
    {"src": "/android-chrome-96x96.png", "sizes": "96x96", "type": "image/png"},
    {"src": "/android-chrome-144x144.png", "sizes": "144x144", "type": "image/png"},
    {"src": "/android-chrome-192x192.png", "sizes": "192x192", "type": "image/png"},
    {"src": "/android-chrome-384x384.png", "sizes": "384x384", "type": "image/png"},
    {"src": "/android-chrome-512x512.png", "sizes": "512x512", "type": "image/png"},
    # Maskable icons (PWA safe zone)
    {
        "src": "/android-chrome-maskable-192x192.png",
        "sizes": "192x192",
        "type": "image/png",
        "purpose": "maskable",
    },
    {
        "src": "/android-chrome-maskable-512x512.png",
        "sizes": "512x512",
        "type": "image/png",
        "purpose": "maskable",
    },
]


# =============================================================================
# browserconfig.xml Tile Configuration
# =============================================================================

BROWSERCONFIG_TILES = {
    "square70x70logo": "/mstile-70x70.png",
    "square144x144logo": "/mstile-144x144.png",
    "square150x150logo": "/mstile-150x150.png",
    "square310x310logo": "/mstile-310x310.png",
    "wide310x150logo": "/mstile-310x150.png",
}
