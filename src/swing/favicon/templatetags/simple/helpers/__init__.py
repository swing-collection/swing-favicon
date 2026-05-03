# -*- coding: utf-8 -*-
"""Helper functions for favicon template tags."""

# Import | Local
from .helper_android_links import get_android_links
from .helper_apple_links import get_apple_links
from .helper_base_path import get_base_path
from .helper_dark_mode_links import (
    get_dark_background_color,
    get_dark_mode_links,
    get_dark_theme_color,
)
from .helper_manifest_links import get_manifest_links
from .helper_microsoft_links import get_microsoft_links
from .helper_ms_tile_color import get_ms_tile_color
from .helper_safari_links import get_safari_links
from .helper_standard_links import get_standard_links
from .helper_theme_color import get_theme_color

__all__ = [
    "get_android_links",
    "get_apple_links",
    "get_base_path",
    "get_dark_background_color",
    "get_dark_mode_links",
    "get_dark_theme_color",
    "get_manifest_links",
    "get_microsoft_links",
    "get_ms_tile_color",
    "get_safari_links",
    "get_standard_links",
    "get_theme_color",
]
