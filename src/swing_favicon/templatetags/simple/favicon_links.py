# -*- coding: utf-8 -*-
"""
Favicon Template Tags
=====================

Template tags for outputting favicon link elements in HTML templates.

Usage:
    {% load favicon_links %}
    {% favicon_links %}                    {# Minimal set #}
    {% favicon_links_full %}               {# All formats #}
    {% favicon_links variant="apple" %}    {# Specific variant #}
"""

from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.safestring import mark_safe

register = template.Library()


def _get_base_path() -> str:
    """Get the favicon base path from settings."""
    return getattr(settings, "FAVICON_BASE_PATH", "favicon")


def _get_theme_color() -> str:
    """Get the theme color from settings."""
    return getattr(settings, "FAVICON_THEME_COLOR", "#ffffff")


def _get_ms_tile_color() -> str:
    """Get the MS tile color from settings."""
    return getattr(settings, "FAVICON_MS_TILE_COLOR", "#ffffff")


@register.simple_tag
def favicon_links(variant: str = "minimal") -> str:
    """
    Output favicon link tags.

    Args:
        variant: Which set of favicons to include:
            - "minimal": Just essential favicons (default)
            - "standard": Standard web favicons
            - "apple": Apple touch icons
            - "microsoft": Microsoft tiles
            - "android": Android/Chrome icons
            - "full": All favicon variants

    Usage:
        {% favicon_links %}
        {% favicon_links "full" %}
        {% favicon_links variant="apple" %}
    """
    base_path = _get_base_path()
    theme_color = _get_theme_color()

    links = []

    # Always include theme color
    links.append(f'<meta name="theme-color" content="{theme_color}">')

    if variant in ("minimal", "standard", "full"):
        links.extend(_get_standard_links(base_path))

    if variant in ("apple", "full"):
        links.extend(_get_apple_links(base_path))

    if variant in ("microsoft", "full"):
        links.extend(_get_microsoft_links(base_path))

    if variant in ("android", "full"):
        links.extend(_get_android_links(base_path))

    if variant in ("minimal", "full"):
        links.extend(_get_manifest_links(base_path))

    return mark_safe("\n".join(links))


@register.simple_tag
def favicon_links_minimal() -> str:
    """Output minimal favicon links (ico + 32x32 + apple-touch-icon)."""
    base_path = _get_base_path()
    theme_color = _get_theme_color()

    links = [
        f'<meta name="theme-color" content="{theme_color}">',
        f'<link rel="icon" href="{static(f"{base_path}/favicon.ico")}" type="image/x-icon">',
        f'<link rel="icon" sizes="32x32" href="{static(f"{base_path}/favicon-32x32.png")}" type="image/png">',
        f'<link rel="apple-touch-icon" href="{static(f"{base_path}/apple-touch-icon.png")}">',
    ]

    return mark_safe("\n".join(links))


@register.simple_tag
def favicon_links_full() -> str:
    """Output all favicon link variants."""
    return favicon_links(variant="full")


def _get_standard_links(base_path: str) -> list[str]:
    """Get standard favicon links."""
    sizes = [16, 32, 48, 64, 96, 128, 192, 256]
    links = [
        f'<link rel="icon" href="{static(f"{base_path}/favicon.ico")}" type="image/x-icon">',
        f'<link rel="shortcut icon" href="{static(f"{base_path}/favicon.ico")}" type="image/x-icon">',
    ]

    for size in sizes:
        links.append(
            f'<link rel="icon" sizes="{size}x{size}" '
            f'href="{static(f"{base_path}/favicon-{size}x{size}.png")}" type="image/png">'
        )

    # SVG favicon for modern browsers
    links.append(
        f'<link rel="icon" href="{static(f"{base_path}/favicon.svg")}" type="image/svg+xml">'
    )

    return links


def _get_apple_links(base_path: str) -> list[str]:
    """Get Apple touch icon links."""
    sizes = [57, 60, 72, 76, 114, 120, 144, 152, 167, 180]
    links = [
        # Default apple-touch-icon
        f'<link rel="apple-touch-icon" href="{static(f"{base_path}/apple-touch-icon.png")}">',
    ]

    for size in sizes:
        links.append(
            f'<link rel="apple-touch-icon" sizes="{size}x{size}" '
            f'href="{static(f"{base_path}/apple-touch-icon-{size}x{size}.png")}">'
        )

    # Safari pinned tab
    links.append(
        f'<link rel="mask-icon" href="{static(f"{base_path}/safari-pinned-tab.svg")}" color="#000000">'
    )

    return links


def _get_microsoft_links(base_path: str) -> list[str]:
    """Get Microsoft tile links."""
    ms_tile_color = _get_ms_tile_color()

    return [
        f'<meta name="msapplication-TileColor" content="{ms_tile_color}">',
        f'<meta name="msapplication-TileImage" content="{static(f"{base_path}/mstile-150x150.png")}">',
        f'<meta name="msapplication-config" content="{static(f"{base_path}/browserconfig.xml")}">',
    ]


def _get_android_links(base_path: str) -> list[str]:
    """Get Android/Chrome icon links."""
    return [
        f'<link rel="icon" sizes="192x192" href="{static(f"{base_path}/android-chrome-192x192.png")}" type="image/png">',
        f'<link rel="icon" sizes="512x512" href="{static(f"{base_path}/android-chrome-512x512.png")}" type="image/png">',
    ]


def _get_manifest_links(base_path: str) -> list[str]:
    """Get web manifest links."""
    return [
        f'<link rel="manifest" href="{static(f"{base_path}/site.webmanifest")}">',
    ]
