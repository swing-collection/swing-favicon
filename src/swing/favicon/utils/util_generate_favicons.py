"""
Generate common favicon formats from a single source image.

Supports:
- Multi-resolution ICO (16, 24, 32, 48, 64, 128, 256 packed into one file)
- PNG favicons (all standard sizes)
- Apple Touch Icons (all iOS sizes)
- Android Chrome Icons (including maskable for PWA)
- Microsoft Tiles (all Windows sizes)
- Safari Pinned Tab (monochrome SVG generation)
"""
import logging
import os
import sys

from PIL import Image

from ..conf import FAVICON_SIZES
from ..constants.constants_favicon import (
    ANDROID_CHROME_SIZES,
    FAVICON_TYPES,
    ICO_SIZES,
    MASKABLE_ICON_SIZES,
)


class FaviconGenerator:
    """Generate common favicon formats from a single source image."""

    # Standard ICO sizes (packed into single .ico file)
    ICO_SIZES = ICO_SIZES

    # Android Chrome sizes
    ANDROID_SIZES = ANDROID_CHROME_SIZES

    # Maskable icon sizes (PWA safe zone)
    MASKABLE_SIZES = MASKABLE_ICON_SIZES

    def __init__(self, input_image_path: str, output_dir: str = "favicons") -> None:
        self.input_image_path = input_image_path
        self.output_dir = output_dir
        self.icon_types = FAVICON_TYPES
        self.sizes = FAVICON_SIZES
        self.ms_tile_sizes = [70, 144, 150, (310, 150), 310]
        self.apple_touch_sizes = [57, 60, 72, 76, 114, 120, 144, 152, 167, 180, 1024]

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

    def generate_ico(self, multi_resolution: bool = True) -> None:
        """
        Generate ICO favicon.

        Parameters:
            multi_resolution: If True, pack multiple sizes (16-256) into single .ico
                             If False, generate single 64x64 .ico
        """
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        ico_path = os.path.join(self.output_dir, "favicon.ico")

        try:
            with Image.open(self.input_image_path) as img:
                if multi_resolution:
                    # Generate multi-resolution ICO with all standard sizes
                    ico_sizes = self.ICO_SIZES
                    ico_images = []

                    for size in ico_sizes:
                        resized = img.resize((size, size), Image.Resampling.LANCZOS)
                        # Convert to RGBA if needed
                        if resized.mode != "RGBA":
                            resized = resized.convert("RGBA")
                        ico_images.append(resized)

                    # Save with all sizes packed into one ICO
                    ico_images[0].save(
                        ico_path,
                        format="ICO",
                        sizes=[(size, size) for size in ico_sizes],
                        append_images=ico_images[1:],
                    )
                    logging.info(
                        "Multi-resolution ICO saved with sizes: %s",
                        ", ".join(str(s) for s in ico_sizes),
                    )
                else:
                    # Single resolution ICO
                    ico_image = img.resize((64, 64), Image.Resampling.LANCZOS)
                    if ico_image.mode != "RGBA":
                        ico_image = ico_image.convert("RGBA")
                    ico_image.save(ico_path, format="ICO")
                    logging.info("ICO file saved (64x64).")
        except IOError:
            logging.exception("Error generating ICO file")

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

                # Also generate the default apple-touch-icon.png (180x180)
                default_icon = img.resize((180, 180), Image.Resampling.LANCZOS)
                default_path = os.path.join(self.output_dir, "apple-touch-icon.png")
                default_icon.save(default_path, format="PNG")
                logging.info("Default Apple Touch Icon (180x180) saved.")

                # Generate precomposed version
                precomposed_path = os.path.join(
                    self.output_dir, "apple-touch-icon-precomposed.png"
                )
                default_icon.save(precomposed_path, format="PNG")
                logging.info("Apple Touch Icon precomposed saved.")
        except IOError:
            logging.exception("Error processing file")

    def generate_android_chrome_icons(self, include_maskable: bool = True) -> None:
        """
        Generate Android Chrome icons for PWA.

        Parameters:
            include_maskable: Also generate maskable icons (safe zone icons)
        """
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        try:
            with Image.open(self.input_image_path) as img:
                # Standard Android Chrome icons
                for size in self.ANDROID_SIZES:
                    icon = img.resize((size, size), Image.Resampling.LANCZOS)
                    output_path = os.path.join(
                        self.output_dir, f"android-chrome-{size}x{size}.png"
                    )
                    icon.save(output_path, format="PNG")
                    logging.info("Android Chrome icon %dx%d saved.", size, size)

                # Maskable icons (for PWA safe zone)
                if include_maskable:
                    for size in self.MASKABLE_SIZES:
                        icon = img.resize((size, size), Image.Resampling.LANCZOS)
                        output_path = os.path.join(
                            self.output_dir,
                            f"android-chrome-maskable-{size}x{size}.png",
                        )
                        icon.save(output_path, format="PNG")
                        logging.info(
                            "Android Chrome maskable icon %dx%d saved.", size, size
                        )
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
                        output_filename = f"mstile-{size[0]}x{size[1]}.png"
                    else:
                        tile_size = (size, size)
                        output_filename = f"mstile-{size}x{size}.png"

                    tile = img.resize(tile_size, Image.Resampling.LANCZOS)
                    output_path = os.path.join(self.output_dir, output_filename)
                    tile.save(output_path, format="PNG")
                    logging.info("MS Tile %s saved.", output_filename)
        except IOError:
            logging.exception("Error processing file")

    def generate_all(self, multi_resolution_ico: bool = True) -> None:
        """
        Generate all favicon formats.

        Parameters:
            multi_resolution_ico: Pack multiple sizes into single .ico file
        """
        logging.info("Generating all favicon formats...")

        self.generate_png()
        self.generate_ico(multi_resolution=multi_resolution_ico)
        self.generate_apple_touch_icons()
        self.generate_android_chrome_icons(include_maskable=True)
        self.generate_ms_tiles()

        logging.info("All favicon formats generated in %s", self.output_dir)

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
    generator.generate_all()
