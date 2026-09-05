# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Generate site.webmanifest for PWA support.

The Web App Manifest is a JSON file that provides information about a web
application, including icons, name, colors, and PWA configuration.

References:
- https://developer.mozilla.org/en-US/docs/Web/Manifest
- https://web.dev/add-manifest/
"""

# Import | Standard Library
import json
from typing import Any

# Import | Local
from ..conf import (
    FAVICON_APP_DESCRIPTION,
    FAVICON_APP_NAME,
    FAVICON_APP_SHORT_NAME,
    FAVICON_BACKGROUND_COLOR,
    FAVICON_BASE_PATH,
    FAVICON_DISPLAY_MODE,
    FAVICON_ORIENTATION,
    FAVICON_START_URL,
    FAVICON_THEME_COLOR,
)
from ..constants import MANIFEST_ICONS


def generate_manifest(
    name: str | None = None,
    short_name: str | None = None,
    description: str | None = None,
    theme_color: str | None = None,
    background_color: str | None = None,
    display: str | None = None,
    orientation: str | None = None,
    start_url: str | None = None,
    base_path: str | None = None,
    icons: list | None = None,
    include_maskable: bool = True,
) -> str:
    """
    Generate site.webmanifest content.

    Parameters:
        name: Full app name (default: from settings)
        short_name: Short app name for home screen (default: from settings)
        description: App description (default: from settings)
        theme_color: Browser chrome color (default: from settings)
        background_color: Splash screen background (default: from settings)
        display: Display mode - fullscreen, standalone, minimal-ui, browser
        orientation: Screen orientation - any, natural, landscape, portrait
        start_url: Start URL when launched from home screen
        base_path: Base path for icon URLs
        icons: Custom icon list (default: from constants)
        include_maskable: Whether to include maskable icons for PWA

    Returns:
        str: site.webmanifest content as JSON string
    """
    manifest = generate_manifest_dict(
        name=name,
        short_name=short_name,
        description=description,
        theme_color=theme_color,
        background_color=background_color,
        display=display,
        orientation=orientation,
        start_url=start_url,
        base_path=base_path,
        icons=icons,
        include_maskable=include_maskable,
    )

    return json.dumps(manifest, indent=2, ensure_ascii=False)


def generate_manifest_dict(
    name: str | None = None,
    short_name: str | None = None,
    description: str | None = None,
    theme_color: str | None = None,
    background_color: str | None = None,
    display: str | None = None,
    orientation: str | None = None,
    start_url: str | None = None,
    base_path: str | None = None,
    icons: list | None = None,
    include_maskable: bool = True,
) -> dict[str, Any]:
    """
    Generate manifest data as a dictionary.

    Parameters:
        name: Full app name
        short_name: Short app name for home screen
        description: App description
        theme_color: Browser chrome color
        background_color: Splash screen background
        display: Display mode
        orientation: Screen orientation
        start_url: Start URL when launched
        base_path: Base path for icon URLs
        icons: Custom icon list
        include_maskable: Whether to include maskable icons

    Returns:
        dict: Web manifest data structure
    """
    # Use settings defaults
    name = name or FAVICON_APP_NAME
    short_name = short_name or FAVICON_APP_SHORT_NAME or name
    description = description or FAVICON_APP_DESCRIPTION
    theme_color = theme_color or FAVICON_THEME_COLOR
    background_color = background_color or FAVICON_BACKGROUND_COLOR
    display = display or FAVICON_DISPLAY_MODE
    orientation = orientation or FAVICON_ORIENTATION
    start_url = start_url or FAVICON_START_URL
    base_path = base_path or f"/{FAVICON_BASE_PATH}"

    # Build icon list with base path
    if icons is None:
        icons = []
        for icon in MANIFEST_ICONS:
            # Skip maskable icons if not requested
            if not include_maskable and icon.get("purpose") == "maskable":
                continue

            # Prepend base_path to src
            icon_copy = icon.copy()
            src = icon_copy["src"]
            if not src.startswith("http"):
                # Handle src that already has leading slash
                if src.startswith("/"):
                    icon_copy["src"] = f"{base_path}{src}"
                else:
                    icon_copy["src"] = f"{base_path}/{src}"
            icons.append(icon_copy)

    manifest: dict[str, Any] = {}

    # Required fields
    if name:
        manifest["name"] = name
    if short_name:
        manifest["short_name"] = short_name

    # Optional fields
    if description:
        manifest["description"] = description

    # Icons
    manifest["icons"] = icons

    # Display settings
    manifest["display"] = display
    manifest["orientation"] = orientation
    manifest["start_url"] = start_url

    # Colors
    manifest["theme_color"] = theme_color
    manifest["background_color"] = background_color

    # Scope
    manifest["scope"] = "/"

    return manifest


def get_minimal_manifest_icons(base_path: str | None = None) -> list[dict]:
    """
    Get minimal icon set for manifest (192 and 512 only).

    This is the recommended minimal set for PWA support.

    Parameters:
        base_path: Base path for icon URLs

    Returns:
        list: List of icon dictionaries for 192x192 and 512x512
    """
    base_path = base_path or f"/{FAVICON_BASE_PATH}"

    return [
        {
            "src": f"{base_path}/android-chrome-192x192.png",
            "sizes": "192x192",
            "type": "image/png",
        },
        {
            "src": f"{base_path}/android-chrome-512x512.png",
            "sizes": "512x512",
            "type": "image/png",
        },
        {
            "src": f"{base_path}/android-chrome-maskable-192x192.png",
            "sizes": "192x192",
            "type": "image/png",
            "purpose": "maskable",
        },
        {
            "src": f"{base_path}/android-chrome-maskable-512x512.png",
            "sizes": "512x512",
            "type": "image/png",
            "purpose": "maskable",
        },
    ]
