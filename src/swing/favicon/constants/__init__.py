# -*- coding: utf-8 -*-


# Docstring
# =============================================================================

"""
Favicon Constants
=================

Static configuration values for favicon generation and serving.

Exported Constants:
    FAVICON_TYPES: List of favicon type configurations (format, rel, dimensions).
    ICO_SIZES: Tuple of sizes to pack into multi-resolution ICO files.
    ANDROID_CHROME_SIZES: Tuple of Android Chrome icon sizes.
    MASKABLE_ICON_SIZES: Tuple of PWA maskable icon sizes.
    MANIFEST_ICONS: List of icon configs for site.webmanifest.
    BROWSERCONFIG_TILES: Dict of Windows tile configurations.
    SUPPORTED_FORMATS: Tuple of supported input image formats.
    HTML_LINK: Template string for generating HTML link tags.

"""


# Imports
# =============================================================================

# Import | Local
from .constants_favicon import (
    ANDROID_CHROME_SIZES,
    BROWSERCONFIG_TILES,
    FAVICON_TYPES,
    HTML_LINK,
    ICO_SIZES,
    MANIFEST_ICONS,
    MASKABLE_ICON_SIZES,
    SUPPORTED_FORMATS,
)

__all__ = [
    "ANDROID_CHROME_SIZES",
    "BROWSERCONFIG_TILES",
    "FAVICON_TYPES",
    "HTML_LINK",
    "ICO_SIZES",
    "MANIFEST_ICONS",
    "MASKABLE_ICON_SIZES",
    "SUPPORTED_FORMATS",
]
