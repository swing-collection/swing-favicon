# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Simple Favicon Template Tags
============================

Simple template tags for including favicon links without complex configuration.

Available Tags:
    favicon_links: Output favicon link tags with optional variant selection.
    favicon_links_minimal: Output minimal favicon set (default).
    favicon_links_full: Output all favicon variants.
    favicon_links_safari: Output Safari pinned tab link only.

Usage:
    {% load simple.favicon_links %}
    {% favicon_links %}              {# Minimal #}
    {% favicon_links "full" %}       {# All variants #}
    {% favicon_links "apple" %}      {# Apple only #}
    {% favicon_links "microsoft" %}  {# MS tiles only #}
    {% favicon_links "android" %}    {# Android Chrome only #}
    {% favicon_links "safari" %}     {# Safari pinned tab only #}

"""


# =============================================================================
# Imports
# =============================================================================
