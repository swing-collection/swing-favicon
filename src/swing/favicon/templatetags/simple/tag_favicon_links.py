# -*- coding: utf-8 -*-
"""Main favicon_links template tag."""

from django import template
from django.utils.safestring import mark_safe

from .helpers import (
    get_android_links,
    get_apple_links,
    get_base_path,
    get_manifest_links,
    get_microsoft_links,
    get_safari_links,
    get_standard_links,
    get_theme_color,
)

from ...conf import FAVICON_SAFARI_MASK_COLOR

register = template.Library()


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
            - "safari": Safari pinned tab
            - "full": All favicon variants

    Usage:
        {% favicon_links %}
        {% favicon_links "full" %}
        {% favicon_links variant="apple" %}
    """
    base_path = get_base_path()
    theme_color = get_theme_color()
    safari_mask_color = FAVICON_SAFARI_MASK_COLOR

    links = []

    # Always include theme color
    links.append(f'<meta name="theme-color" content="{theme_color}">')

    if variant in ("minimal", "standard", "full"):
        links.extend(get_standard_links(base_path))

    if variant in ("apple", "full"):
        links.extend(get_apple_links(base_path))

    if variant in ("microsoft", "full"):
        links.extend(get_microsoft_links(base_path))

    if variant in ("android", "full"):
        links.extend(get_android_links(base_path))

    if variant in ("safari", "full"):
        links.extend(get_safari_links(base_path, safari_mask_color))

    if variant in ("minimal", "full"):
        links.extend(get_manifest_links(base_path))

    return mark_safe("\n".join(links))
