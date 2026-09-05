# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""Full favicon_links template tag."""

from django import template

# Import | Local
from .tag_favicon_links import favicon_links

register = template.Library()


@register.simple_tag
def favicon_links_full() -> str:
    """Output all favicon link variants."""
    return favicon_links(variant="full")
