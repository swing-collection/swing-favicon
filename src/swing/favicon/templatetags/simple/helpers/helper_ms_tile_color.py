# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""Get MS tile color from settings."""

from django.conf import settings


def get_ms_tile_color() -> str:
    """Get the MS tile color from settings."""
    return getattr(settings, "FAVICON_MS_TILE_COLOR", "#ffffff")
