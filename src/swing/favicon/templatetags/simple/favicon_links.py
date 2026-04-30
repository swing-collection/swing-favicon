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

This module re-exports all template tags for backward compatibility.
"""

from django import template

# Import the individual tag modules to get their register instances
from .tag_favicon_links import favicon_links
from .tag_favicon_links_full import favicon_links_full
from .tag_favicon_links_minimal import favicon_links_minimal

# Create a unified register for this module
register = template.Library()

# Re-register all tags on this module's register
register.simple_tag(favicon_links)
register.simple_tag(favicon_links_minimal)
register.simple_tag(favicon_links_full)
