"""
Generate common favicon formats from a single source image.
"""
import logging
import os
import sys

from PIL import Image

from ..conf import FAVICON_SIZES
from ..constants.constants_favicon import FAVICON_TYPES


class FaviconGenerator:
    """Generate common favicon formats from a single source image."""

    def __init__(self, input_image_path: str, output_dir: str = "favicons") -> None:
        self.input_image_path = input_image_path
        self.output_dir = output_dir
        self.icon_types = FAVICON_TYPES
        self.sizes = FAVICON_SIZES
        self.ms_tile_sizes = [70, 150, (310, 150), 310]
        self.apple_touch_sizes = [120, 152, 167, 180, 1024]

    def generate_icons(self) -> None:
        """Generate icons from icon_types configuration."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        try:
            with Image.open(self.input_image_path) as img:
                for icon_type in self.icon_types:
                    fmt = icon_type["format"]
                    dimensions = icon_type["dimensions"]
                    prefix = icon_type["prefix"]
                    filename = f"{prefix}-{dimensions[0]}x{dimensions[1]}.{fmt}"

                    resized_icon = img.resize(dimensions, Image.Resampling.LANCZOS)
                    output_path = os.path.join(self.output_dir, filename)
                    resized_icon.save(output_path, format=fmt.upper())
                    logging.info("%s generated.", filename)
        except IOError:
            logging.exception("Error processing file")

    def generate_png(self) -> None:
        """Generate PNG favicons."""
        self._generate_favicons("PNG")

    def generate_ico(self) -> None:
        """Generate ICO favicon with all sizes."""
        ico_path = os.path.join(self.output_dir, "favicon.ico")
        ico_images = [
            Image.open(self.input_image_path).resize(
                (size, size), Image.Resampling.LANCZOS
            )
            for size in self.sizes
        ]
        ico_images[0].save(
            ico_path, format="ICO", sizes=[(size, size) for size in self.sizes]
        )
        logging.info("ICO file saved with all sizes.")

    def generate_svg(self) -> None:
        """Generate SVG favicon (not supported yet)."""
        logging.info("SVG favicon generation is not supported in this version.")

    def generate_jpg(self) -> None:
        """Generate JPEG favicons."""
        self._generate_favicons("JPEG")

    def generate_apple_touch_icons(self) -> None:
        """Generate Apple touch icons."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        try:
            with Image.open(self.input_image_path) as img:
                for size in self.apple_touch_sizes:
                    icon = img.resize((size, size), Image.Resampling.LANCZOS)
                    output_path = os.path.join(
                        self.output_dir, f"apple-touch-icon-{size}x{size}.png"
                    )
                    icon.save(output_path, format="PNG")
                    logging.info("Apple Touch Icon of size %dx%d saved.", size, size)
        except IOError:
            logging.exception("Error processing file")

    def generate_ms_tiles(self) -> None:
        """Generate Microsoft tile icons."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        try:
            with Image.open(self.input_image_path) as img:
                for size in self.ms_tile_sizes:
                    if isinstance(size, tuple):
                        tile_size = size
                        output_filename = f"ms-tile-{size[0]}x{size[1]}.png"
                    else:
                        tile_size = (size, size)
                        output_filename = f"ms-tile-{size}x{size}.png"

                    tile = img.resize(tile_size, Image.Resampling.LANCZOS)
                    output_path = os.path.join(self.output_dir, output_filename)
                    tile.save(output_path, format="PNG")
                    logging.info("MS Tile %s saved.", output_filename)
        except IOError:
            logging.exception("Error processing file")

    def _generate_favicons(self, image_format: str) -> None:
        """Generate favicons in a specific format."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        try:
            with Image.open(self.input_image_path) as img:
                for size in self.sizes:
                    favicon = img.resize((size, size), Image.Resampling.LANCZOS)
                    output_path = os.path.join(
                        self.output_dir,
                        f"favicon-{size}x{size}.{image_format.lower()}",
                    )
                    favicon.save(output_path, format=image_format)
                    logging.info(
                        "Favicon of size %dx%d in %s format saved.",
                        size,
                        size,
                        image_format,
                    )
        except IOError:
            logging.exception("Error processing file")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) != 3:
        print("Usage: python favicon_generator.py <input_image> <output_directory>")
        sys.exit(1)

    input_image = sys.argv[1]
    output_directory = sys.argv[2]

    generator = FaviconGenerator(input_image, output_directory)
    generator.generate_png()
    generator.generate_ico()
    generator.generate_jpg()
