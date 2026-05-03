# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Favicon Template Tags
=====================

Django template tags for including favicon links in HTML templates.

Available Tag Libraries:
    simple.favicon_links: Main tag library with favicon_links tag.

Usage:
    In your Django template::

        {% load simple.favicon_links %}

        <head>
            {% favicon_links %}              {# Minimal set #}
            {% favicon_links "full" %}       {# All variants #}
            {% favicon_links "apple" %}      {# Apple touch icons only #}
        </head>

"""


# =============================================================================
# Imports
# =============================================================================
