# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Demo URL Patterns
=================

Defines URL patterns for the demo project.

"""


# =============================================================================
# Imports
# =============================================================================

from django.contrib import admin
from django.urls import include, path

from .views import home


# =============================================================================
# URL Patterns
# =============================================================================

urlpatterns = [
    # Home page
    path(
        route="",
        view=home,
        name="home",
    ),
    # Admin
    path(
        route="admin/",
        view=admin.site.urls,
    ),
    # Favicon URLs
    path(
        route="",
        view=include(arg="swing.favicon.urls"),
    ),
]
