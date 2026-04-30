# -*- coding: utf-8 -*-
"""
Favicon Template Tags
=====================

Template tags for outputting favicon link elements in HTML templates.

Usage:
    {% load simple.favicon_links %}
    {% favicon_links %}                    {# Minimal set #}
    {% favicon_links_full %}               {# All formats #}
    {% favicon_links variant="apple" %}    {# Specific variant #}
    {% favicon_links variant="safari" %}   {# Safari pinned tab #}

This module re-exports all template tags for backward compatibility.

Supported variants:
- minimal: Essential favicons + manifest (default)
- standard: Standard web favicons
- apple: Apple touch icons
- microsoft: Microsoft tiles
- android: Android/Chrome icons
- safari: Safari pinned tab (mask-icon)
- full: All favicon variants
"""

from django import template

# Import the individual tag modules to get their register instances
from .tag_favicon_links import favicon_links
from .tag_favicon_links_full import favicon_links_full
from .tag_favicon_links_minimal import favicon_links_minimal
from .tag_favicon_links_safari import favicon_links_safari

# Create a unified register for this module
register = template.Library()

# Re-register all tags on this module's register
register.simple_tag(favicon_links)
register.simple_tag(favicon_links_minimal)
register.simple_tag(favicon_links_full)
register.simple_tag(favicon_links_safari)
