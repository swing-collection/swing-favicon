# -*- coding: utf-8 -*-


"""
Favicon Configuration Settings
==============================

Default settings for the swing.favicon app. These can be overridden in your
Django project's settings.py by prefixing with FAVICON_.

Example in settings.py:
    FAVICON_THEME_COLOR = "#3498db"
    FAVICON_CACHE_MAX_AGE = 86400 * 30  # 30 days
"""

from django.conf import settings

# =============================================================================
# Path Settings
# =============================================================================

# Base path within static files where favicons are stored
FAVICON_BASE_PATH: str = getattr(settings, "FAVICON_BASE_PATH", "favicon")

# Source image path for favicon generation (relative to MEDIA_ROOT or absolute)
FAVICON_SOURCE_PATH: str = getattr(settings, "FAVICON_SOURCE_PATH", "")


# =============================================================================
# Cache Settings
# =============================================================================

# Cache-Control max-age in seconds (default: 1 day)
FAVICON_CACHE_MAX_AGE: int = getattr(settings, "FAVICON_CACHE_MAX_AGE", 60 * 60 * 24)

# Whether to mark responses as immutable (prevents revalidation)
FAVICON_CACHE_IMMUTABLE: bool = getattr(settings, "FAVICON_CACHE_IMMUTABLE", True)

# Whether to mark responses as public (allows CDN caching)
FAVICON_CACHE_PUBLIC: bool = getattr(settings, "FAVICON_CACHE_PUBLIC", True)


# =============================================================================
# Theme Settings
# =============================================================================

# Theme color for browser chrome (Android, Windows)
FAVICON_THEME_COLOR: str = getattr(settings, "FAVICON_THEME_COLOR", "#ffffff")

# Background color for MS tiles
FAVICON_MS_TILE_COLOR: str = getattr(settings, "FAVICON_MS_TILE_COLOR", "#ffffff")

# Safari pinned tab mask icon color (monochrome SVG)
FAVICON_SAFARI_MASK_COLOR: str = getattr(
    settings, "FAVICON_SAFARI_MASK_COLOR", "#000000"
)

# App name for web manifest
FAVICON_APP_NAME: str = getattr(settings, "FAVICON_APP_NAME", "")

# Short app name for web manifest
FAVICON_APP_SHORT_NAME: str = getattr(settings, "FAVICON_APP_SHORT_NAME", "")

# App description for web manifest
FAVICON_APP_DESCRIPTION: str = getattr(settings, "FAVICON_APP_DESCRIPTION", "")

# App start URL for PWA
FAVICON_START_URL: str = getattr(settings, "FAVICON_START_URL", "/")

# PWA display mode: fullscreen, standalone, minimal-ui, browser
FAVICON_DISPLAY_MODE: str = getattr(settings, "FAVICON_DISPLAY_MODE", "standalone")

# PWA orientation: any, natural, landscape, portrait
FAVICON_ORIENTATION: str = getattr(settings, "FAVICON_ORIENTATION", "any")

# PWA background color (splash screen)
FAVICON_BACKGROUND_COLOR: str = getattr(settings, "FAVICON_BACKGROUND_COLOR", "#ffffff")


# =============================================================================
# Size Settings
# =============================================================================

# Standard favicon sizes to generate
FAVICON_SIZES: list[int] = getattr(
    settings,
    "FAVICON_SIZES",
    [16, 32, 48, 64, 96, 128, 180, 192, 256, 512],
)

# Apple touch icon sizes to generate
FAVICON_APPLE_SIZES: list[int] = getattr(
    settings,
    "FAVICON_APPLE_SIZES",
    [57, 60, 72, 76, 114, 120, 144, 152, 167, 180],
)

# Microsoft tile sizes to generate
FAVICON_MS_TILE_SIZES: list[int | tuple[int, int]] = getattr(
    settings,
    "FAVICON_MS_TILE_SIZES",
    [70, 150, 270, 310, (310, 150)],
)


# =============================================================================
# Format Settings
# =============================================================================

# Enable SVG favicon support (modern browsers)
FAVICON_ENABLE_SVG: bool = getattr(settings, "FAVICON_ENABLE_SVG", True)

# Enable web manifest generation
FAVICON_ENABLE_MANIFEST: bool = getattr(settings, "FAVICON_ENABLE_MANIFEST", True)

# Enable browserconfig.xml generation
FAVICON_ENABLE_BROWSERCONFIG: bool = getattr(
    settings, "FAVICON_ENABLE_BROWSERCONFIG", True
)


# =============================================================================
# Feature Flags
# =============================================================================

# Auto-generate favicons on model save
FAVICON_AUTO_GENERATE: bool = getattr(settings, "FAVICON_AUTO_GENERATE", False)

# Serve favicons from database model instead of static files
FAVICON_USE_MODEL: bool = getattr(settings, "FAVICON_USE_MODEL", False)
