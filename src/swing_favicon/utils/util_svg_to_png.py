"""Utility functions for SVG to PNG conversion."""

from pathlib import Path
from tempfile import mkstemp
from typing import Tuple


def svg_to_png(svg_path: Path, background_color: Tuple[int, ...]) -> Path:
    """Convert an SVG vector to a PNG file.

    Args:
        svg_path: Path to the SVG file.
        background_color: RGB tuple for background color.

    Returns:
        Path to the generated PNG file.

    Raises:
        ImportError: If svglib or reportlab is not installed.
    """
    try:
        from svglib.svglib import svg2rlg
        from reportlab.graphics import renderPM
        from reportlab.lib.colors import transparent
    except ImportError as err:
        raise ImportError(
            "svglib and reportlab are required for SVG conversion. "
            "Install with: pip install svglib reportlab"
        ) from err

    _, png_path = mkstemp(suffix=".tiff")

    png = Path(png_path)

    drawing = svg2rlg(str(svg_path))
    # Convert RGB tuple to hex color
    hex_color = "#{:02x}{:02x}{:02x}".format(*background_color[:3])
    renderPM.drawToFile(
        drawing,
        str(png),
        fmt="TIFF",
        bg=int(hex_color.replace("#", ""), 16),
        configPIL={"transparent": transparent},
    )

    return png
