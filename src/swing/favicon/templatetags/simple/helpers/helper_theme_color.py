# -*- coding: utf-8 -*-
"""Get theme color from settings."""

from django.conf import settings


def get_theme_color() -> str:
    """Get the theme color from settings."""
    return getattr(settings, "FAVICON_THEME_COLOR", "#ffffff")
