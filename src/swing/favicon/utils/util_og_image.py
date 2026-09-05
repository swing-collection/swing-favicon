# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Open Graph Image Generator
==========================

Generates 1200x630 PNG Open Graph images for social media sharing.

The service uses Pillow for image generation. When Pillow is not available,
functions return None and callers should fall back to static images.

Configuration in settings.py::

    FAVICON_OG_WIDTH = 1200
    FAVICON_OG_HEIGHT = 630
    FAVICON_OG_BG_COLOR = "#1a365d"
    FAVICON_OG_FG_COLOR = "#ffffff"
    FAVICON_OG_ACCENT_COLOR = "#58aff4"
    FAVICON_OG_EYEBROW = "My App"

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import io
import logging
import textwrap
from pathlib import Path
from typing import TYPE_CHECKING

from django.conf import settings

if TYPE_CHECKING:
    from PIL.ImageFont import FreeTypeFont, ImageFont

logger = logging.getLogger(__name__)


# =============================================================================
# Configuration
# =============================================================================

# Image dimensions (Open Graph standard)
OG_WIDTH: int = getattr(settings, "FAVICON_OG_WIDTH", 1200)
OG_HEIGHT: int = getattr(settings, "FAVICON_OG_HEIGHT", 630)

# Colors (RGB tuples or hex strings)
OG_BG_COLOR: str | tuple[int, int, int] = getattr(
    settings, "FAVICON_OG_BG_COLOR", "#1a365d"
)
OG_FG_COLOR: str | tuple[int, int, int] = getattr(
    settings, "FAVICON_OG_FG_COLOR", "#ffffff"
)
OG_ACCENT_COLOR: str | tuple[int, int, int] = getattr(
    settings, "FAVICON_OG_ACCENT_COLOR", "#58aff4"
)

# Text defaults
OG_DEFAULT_EYEBROW: str = getattr(settings, "FAVICON_OG_EYEBROW", "")
OG_DEFAULT_SUBTITLE: str = getattr(settings, "FAVICON_OG_SUBTITLE", "")


# =============================================================================
# Helper Functions
# =============================================================================


def _hex_to_rgb(hex_color: str | tuple[int, int, int]) -> tuple[int, int, int]:
    """Convert hex color string to RGB tuple."""
    if isinstance(hex_color, tuple):
        return hex_color
    hex_str = hex_color.lstrip("#")
    r, g, b = (int(hex_str[i : i + 2], 16) for i in (0, 2, 4))
    return (r, g, b)


def _load_font(size: int) -> "FreeTypeFont | ImageFont | None":
    """
    Best-effort load of a system font, falling back to default.

    Searches common font locations on macOS and Linux.

    Args:
        size: Font size in pixels.

    Returns:
        ImageFont object or None if loading fails.
    """
    try:
        from PIL import ImageFont  # pylint: disable=import-outside-toplevel

        candidates = [
            # macOS
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
            "/Library/Fonts/Arial Bold.ttf",
            # Linux
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
            # Windows (WSL)
            "/mnt/c/Windows/Fonts/arialbd.ttf",
        ]
        for candidate in candidates:
            if Path(candidate).exists():
                return ImageFont.truetype(candidate, size)
        return ImageFont.load_default()
    except Exception:  # pylint: disable=broad-except
        return None


# =============================================================================
# Main Function
# =============================================================================


def generate_og_image(
    *,
    title: str,
    subtitle: str = "",
    eyebrow: str = "",
    width: int | None = None,
    height: int | None = None,
    bg_color: str | tuple[int, int, int] | None = None,
    fg_color: str | tuple[int, int, int] | None = None,
    accent_color: str | tuple[int, int, int] | None = None,
) -> bytes | None:
    """
    Render an Open Graph image and return its bytes.

    Generates a 1200x630 PNG with:
    - Accent bar at top
    - Eyebrow text (small, accent color)
    - Title text (large, wrapped to 3 lines max)
    - Subtitle text (small, muted color)

    Args:
        title: Main title text (required).
        subtitle: Optional subtitle at bottom.
        eyebrow: Optional small text above title (e.g., app name).
        width: Image width in pixels (default: 1200).
        height: Image height in pixels (default: 630).
        bg_color: Background color as hex string or RGB tuple.
        fg_color: Foreground/title color as hex string or RGB tuple.
        accent_color: Accent color for eyebrow and bar.

    Returns:
        PNG image bytes, or None if Pillow is not available.

    Example::

        from swing.favicon.utils import generate_og_image

        png = generate_og_image(
            title="My Blog Post Title",
            subtitle="example.com",
            eyebrow="My App",
        )
        if png:
            response = HttpResponse(png, content_type="image/png")
    """
    try:
        from PIL import Image, ImageDraw  # pylint: disable=import-outside-toplevel
    except ImportError:
        logger.info("Pillow not available; OG image generation disabled.")
        return None

    # Use defaults
    width = width or OG_WIDTH
    height = height or OG_HEIGHT
    bg = _hex_to_rgb(bg_color or OG_BG_COLOR)
    fg = _hex_to_rgb(fg_color or OG_FG_COLOR)
    accent = _hex_to_rgb(accent_color or OG_ACCENT_COLOR)
    eyebrow = eyebrow or OG_DEFAULT_EYEBROW
    subtitle = subtitle or OG_DEFAULT_SUBTITLE

    # Create image
    image = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(image)

    # Accent bar at top (12px height)
    draw.rectangle((0, 0, width, 12), fill=accent)

    # Eyebrow text (small, accent color)
    if eyebrow:
        eyebrow_font = _load_font(36)
        if eyebrow_font is not None:
            draw.text((60, 60), eyebrow, fill=accent, font=eyebrow_font)

    # Title (wrapped to ~22 chars per line, max 3 lines)
    title_font = _load_font(72)
    wrapped = textwrap.wrap(title.strip(), width=22)[:3]
    if title_font is not None:
        y = 200
        for line in wrapped:
            draw.text((60, y), line, fill=fg, font=title_font)
            y += 90

    # Subtitle (muted color, bottom-left)
    if subtitle:
        sub_font = _load_font(32)
        if sub_font is not None:
            muted = tuple(int(c * 0.8) for c in fg)  # 80% brightness
            draw.text((60, height - 80), subtitle, fill=muted, font=sub_font)

    # Encode to PNG
    buffer = io.BytesIO()
    image.save(buffer, format="PNG", optimize=True)
    return buffer.getvalue()


# =============================================================================
# Exports
# =============================================================================

__all__ = ["generate_og_image"]
