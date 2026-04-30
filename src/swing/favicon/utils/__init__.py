# -*- coding: utf-8 -*-
"""
Favicon Utilities Module
========================

Utilities for generating and managing favicon files.
"""

from .util_generate_browserconfig import (
    generate_browserconfig,
    generate_browserconfig_dict,
)
from .util_generate_favicons import FaviconGenerator
from .util_generate_icon_types import generate_icon_types
from .util_generate_manifest import (
    generate_manifest,
    generate_manifest_dict,
    get_minimal_manifest_icons,
)
from .util_svg_to_png import svg_to_png
from .util_validate_path import validate_path

__all__ = [
    "FaviconGenerator",
    "generate_browserconfig",
    "generate_browserconfig_dict",
    "generate_icon_types",
    "generate_manifest",
    "generate_manifest_dict",
    "get_minimal_manifest_icons",
    "svg_to_png",
    "validate_path",
]
