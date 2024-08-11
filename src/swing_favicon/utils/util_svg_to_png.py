"""Common utility functions used throughout Favicons."""

# Standard Library
from typing import Union, Mapping, Generator
from pathlib import Path
from tempfile import mkstemp



# Project
from favicons._types import Color


def svg_to_png(svg_path: Path, background_color: Color) -> Path:
    """Convert an SVG vector to a PNG file."""
    # Third Party
    from svglib.svglib import svg2rlg
    from reportlab.graphics import renderPM
    from reportlab.lib.colors import transparent

    _, png_path = mkstemp(suffix=".tiff")

    png = Path(png_path)

    drawing = svg2rlg(str(svg_path))
    renderPM.drawToFile(
        drawing,
        str(png),
        fmt="TIFF",
        bg=int(background_color.as_hex().replace("#", ""), 16),
        configPIL={"transparent": transparent},
    )

    return png