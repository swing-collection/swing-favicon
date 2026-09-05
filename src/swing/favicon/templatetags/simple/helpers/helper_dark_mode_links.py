# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""Get dark mode favicon links."""

# Import | Local
from ....conf import (
    FAVICON_DARK_BACKGROUND_COLOR,
    FAVICON_DARK_MODE_ENABLED,
    FAVICON_DARK_MODE_SUFFIX,
    FAVICON_DARK_THEME_COLOR,
)


def get_dark_mode_links(base_path: str) -> list[str]:
    """
    Generate dark mode favicon link tags.

    Uses prefers-color-scheme media query for automatic switching.

    Args:
        base_path: Base path to favicon files.

    Returns:
        List of HTML link tag strings for dark mode.
    """
    if not FAVICON_DARK_MODE_ENABLED:
        return []

    suffix = FAVICON_DARK_MODE_SUFFIX
    links = []

    # Dark mode theme color
    links.append(
        f'<meta name="theme-color" content="{FAVICON_DARK_THEME_COLOR}" '
        f'media="(prefers-color-scheme: dark)">'
    )

    # Dark mode SVG favicon (modern browsers)
    links.append(
        f'<link rel="icon" type="image/svg+xml" href="{base_path}/favicon{suffix}.svg" '
        f'media="(prefers-color-scheme: dark)">'
    )

    # Dark mode PNG favicon fallback
    links.append(
        f'<link rel="icon" type="image/png" sizes="32x32" '
        f'href="{base_path}/favicon-32x32{suffix}.png" '
        f'media="(prefers-color-scheme: dark)">'
    )

    return links


def get_dark_theme_color() -> str:
    """Get the dark mode theme color from settings."""
    return FAVICON_DARK_THEME_COLOR


def get_dark_background_color() -> str:
    """Get the dark mode background color from settings."""
    return FAVICON_DARK_BACKGROUND_COLOR
