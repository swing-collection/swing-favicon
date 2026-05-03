# -*- coding: utf-8 -*-


# Docstring
# =============================================================================

"""
Swing Favicon - Django Favicon Management
==========================================

A Django app for serving and managing favicons with support for all modern
browser formats including ICO, PNG, SVG, Apple Touch Icons, Android Chrome
icons, Microsoft tiles, and Safari pinned tabs.

Features:
    - Multi-resolution ICO generation (16-256px packed)
    - PNG favicons in all standard sizes
    - Apple Touch Icons for iOS/macOS
    - Android Chrome icons with maskable PWA support
    - Microsoft tile icons for Windows
    - Safari pinned tab (mask-icon) support
    - Dynamic browserconfig.xml and site.webmanifest generation
    - Template tags for easy HTML integration
    - Caching with configurable Cache-Control headers

Quick Start:
    1. Add 'swing.favicon' to INSTALLED_APPS
    2. Include favicon URLs: path('', include('swing.favicon.urls'))
    3. Use template tags: {% load simple.favicon_links %} {% favicon_links %}

Configuration (settings.py):
    FAVICON_BASE_PATH = "favicon"        # Static files subdirectory
    FAVICON_THEME_COLOR = "#ffffff"      # Browser chrome color
    FAVICON_CACHE_MAX_AGE = 86400        # Cache duration in seconds

See Also:
    - conf: Configuration settings
    - views: Favicon serving views
    - utils: Favicon generation utilities
    - templatetags: Template tags for HTML output

"""


# Imports
# =============================================================================
