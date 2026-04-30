# -*- coding: utf-8 -*-
"""Safari favicon_links template tag."""

from django import template

from .tag_favicon_links import favicon_links

register = template.Library()


@register.simple_tag
def favicon_links_safari() -> str:
    """Output Safari pinned tab link."""
    return favicon_links(variant="safari")
