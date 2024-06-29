# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Favicon URLs Module
============================

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from typing import List

# Import | Libraries
from django.urls import path
from django.urls import re_path
from django.views.generic import RedirectView

# from example.core import views as core_views
from .views import FaviconFileView

# =============================================================================
# Variables
# =============================================================================

# Export
__all__: List[str] = ["app_name", "urlpatterns"]

# App Name
app_name = "favicon"

# URL Patterns
urlpatterns = [
    # ...,

    path(
        "favicon.ico",
        FaviconFileView.as_view(),
        name = "favicon"
    ),

    # path("android-chrome-192x192.png", core_views.favicon_file),
    # path("android-chrome-512x512.png", core_views.favicon_file),
    # path("apple-touch-icon.png", core_views.favicon_file),
    # path("browserconfig.xml", core_views.favicon_file),
    # path("favicon-16x16.png", core_views.favicon_file),
    # path("favicon-32x32.png", core_views.favicon_file),
    # path("favicon.ico", core_views.favicon_file),
    # path("mstile-150x150.png", core_views.favicon_file),
    # path("safari-pinned-tab.svg", core_views.favicon_file),
    # path("site.webmanifest", core_views.favicon_file),


    # path("favicon.ico", core_views.favicon),
    # path("favicon.ico", core_views.favicon),


]

# urlpatterns = [
#     re_path(r'^favicon\.ico$', RedirectView.as_view(url=conf.FAVICON_PATH, permanent=True), name='favicon'),
# ]
