# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Favicon Views Module
=============================

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Local Modules
from .view_browserconfig import BrowserConfigView
from .view_favicon_file import FaviconFileView
from .view_favicon_file_f import favicon_file_view
from .view_webmanifest import WebManifestView

__all__ = [
    "BrowserConfigView",
    "FaviconFileView",
    "favicon_file_view",
    "WebManifestView",
]
