# -*- coding: utf-8 -*-
"""
Favicon Utilities
=================

Utilities for generating and managing favicon files.

Exported Classes:
    FaviconGenerator: Generate all favicon formats from a source image.

Exported Functions:
    generate_browserconfig: Generate browserconfig.xml content.
    generate_browserconfig_dict: Generate browserconfig data as dict.
    generate_manifest: Generate site.webmanifest content.
    generate_manifest_dict: Generate manifest data as dict.
    get_minimal_manifest_icons: Get minimal PWA icon set.
    generate_icon_types: Iterator over favicon type configurations.
    svg_to_png: Convert SVG to PNG file.
    validate_path: Validate and normalize file paths.
    validate_color: Validate color values.
    is_valid_color: Check if color is valid.
    is_valid_hex_color: Check if color is valid hex format.
    normalize_hex_color: Normalize hex color to 6-character format.

Example:
    from swing.favicon.utils import FaviconGenerator, generate_manifest

    # Generate all favicons
    generator = FaviconGenerator("logo.png", "static/favicon")
    generator.generate_all()

    # Generate manifest content
    manifest_json = generate_manifest(name="My App")

    # Validate colors
    from swing.favicon.utils import validate_color
    validate_color("#ff5500", name="theme_color")

"""

# Import | Local
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
from .util_validate_color import (
    is_valid_color,
    is_valid_css_color,
    is_valid_hex_color,
    normalize_hex_color,
    validate_color,
)
from .util_validate_path import validate_path

__all__ = [
    "FaviconGenerator",
    "generate_browserconfig",
    "generate_browserconfig_dict",
    "generate_icon_types",
    "generate_manifest",
    "generate_manifest_dict",
    "get_minimal_manifest_icons",
    "is_valid_color",
    "is_valid_css_color",
    "is_valid_hex_color",
    "normalize_hex_color",
    "svg_to_png",
    "validate_color",
    "validate_path",
]
