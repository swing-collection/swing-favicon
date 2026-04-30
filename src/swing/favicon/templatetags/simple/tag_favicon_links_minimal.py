# -*- coding: utf-8 -*-
"""Minimal favicon_links template tag."""

from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from .helpers import get_base_path, get_theme_color

register = template.Library()


@register.simple_tag
def favicon_links_minimal() -> str:
    """Output minimal favicon links (ico + 32x32 + apple-touch-icon)."""
    base_path = get_base_path()
    theme_color = get_theme_color()

    links = [
        f'<meta name="theme-color" content="{theme_color}">',
        f'<link rel="icon" href="{static(f"{base_path}/favicon.ico")}" type="image/x-icon">',
        f'<link rel="icon" sizes="32x32" href="{static(f"{base_path}/favicon-32x32.png")}" type="image/png">',
        f'<link rel="apple-touch-icon" href="{static(f"{base_path}/apple-touch-icon.png")}">',
    ]

    return mark_safe("\n".join(links))
