import os
import sys
import logging
from PIL import Image
from ..conf import (
    FAVICON_SIZES,
    ,
)
from ..constants.constants_favicon import (
    FAVICON_TYPES,
)



class FaviconGenerator:
    def __init__(self, input_image_path, output_dir='favicons'):
        self.input_image_path = input_image_path
        self.output_dir = output_dir
        self.icon_types = FAVICON_TYPES

    def generate_icons(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        try:
            with Image.open(self.input_image_path) as img:
                for icon_type in self.icon_types:
                    fmt = icon_type["format"]
                    dimensions = icon_type["dimensions"]
                    prefix = icon_type["prefix"]
                    filename = f"{prefix}-{dimensions[0]}x{dimensions[1]}.{fmt}"

                    resized_icon = img.resize(dimensions, Image.ANTIALIAS)
                    output_path = os.path.join(self.output_dir, filename)
                    resized_icon.save(output_path, format=fmt.upper())
                    logging.info(f'{filename} generated.')
        except IOError as e:
            logging.error(f"Error processing file: {e}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) != 3:
        print("Usage: python favicon_generator.py <input_image> <output_directory>")
        sys.exit(1)

    input_image = sys.argv[1]
    output_directory = sys.argv[2]

    generator = FaviconGenerator(input_image, output_directory)
    generator.generate_icons()
















class FaviconGenerator:
    """
    Generate common favicon formats from a single source image.
    """

    def __init__(self, input_image_path, output_dir='favicons'):
        self.input_image_path = input_image_path
        self.output_dir = output_dir
        self.sizes = FAVICON_SIZES  # Standard favicon sizes
        # self.ms_tile_sizes = [70, 150, 310, 310]  # MS Tile sizes
        self.ms_tile_sizes = [70, 150, (310, 150), 310]  # Adding (310, 150) for wide tile
        self.apple_touch_sizes = [120, 152, 167, 180, 1024]  # Apple touch icon sizes

    def generate_png(self):
        self._generate_favicons('PNG')

    def generate_ico(self):
        ico_path = os.path.join(self.output_dir, 'favicon.ico')
        ico_images = [img.resize((size, size), Image.ANTIALIAS) for size in self.sizes for img in [Image.open(self.input_image_path)]]
        ico_images[0].save(ico_path, format='ICO', sizes=[(size, size) for size in self.sizes])
        logging.info('ICO file saved with all sizes.')

    def generate_svg(self):
        # SVG favicon generation would require a different approach
        logging.info("SVG favicon generation is not supported in this version.")

    def generate_jpg(self):
        self._generate_favicons('JPEG')

    def generate_apple_touch_icons(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        try:
            with Image.open(self.input_image_path) as img:
                for size in self.apple_touch_sizes:
                    icon = img.resize((size, size), Image.ANTIALIAS)
                    output_path = os.path.join(self.output_dir, f'apple-touch-icon-{size}x{size}.png')
                    icon.save(output_path, format='PNG')
                    logging.info(f'Apple Touch Icon of size{size}x{size} saved.')
        except IOError as e:
            logging.error(f"Error processing file: {e}")

    def generate_ms_tiles(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        try:
            with Image.open(self.input_image_path) as img:
                for size in self.ms_tile_sizes:
                    # Handle wide tile resizing
                    if isinstance(size, tuple):
                        tile_size = size
                        output_filename = f'ms-tile-{size[0]}x{size[1]}.png'
                    else:
                        tile_size = (size, size)
                        output_filename = f'ms-tile-{size}x{size}.png'

                    tile = img.resize(tile_size, Image.ANTIALIAS)
                    output_path = os.path.join(self.output_dir, output_filename)
                    tile.save(output_path, format='PNG')
                    logging.info(f'MS Tile {output_filename} saved.')
        except IOError as e:
            logging.error(f"Error processing file: {e}")


    def _generate_favicons(self, format):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        try:
            with Image.open(self.input_image_path) as img:
                for size in self.sizes:
                    favicon = img.resize((size, size), Image.ANTIALIAS)
                    output_path = os.path.join(self.output_dir, f'favicon-{size}x{size}.{format.lower()}')
                    favicon.save(output_path, format=format)
                    logging.info(f'Favicon of size {size}x{size} in {format} format saved.')
        except IOError as e:
            logging.error(f"Error processing file: {e}")



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
    # generator.generate_svg() # Uncomment when SVG support is added
    generator.generate_jpg()
















"""
Generate common favicon formats from a single source image.

Links:
- https://github.com/thatmattlove/favicons/blob/master/favicons/_generate.py
"""

# Standard Library
import json as _json
import math
import asyncio
from types import TracebackType
from typing import (
    Any,
    Type,
    Tuple,
    Union,
    Callable,
    Optional,
    Coroutine,
    Generator,
    Collection,
)
from pathlib import Path

# Third Party
from PIL import Image as PILImage

# Project
from favicons._util import svg_to_png, validate_path, generate_icon_types
from favicons._types import Color, FaviconProperties
from favicons._constants import HTML_LINK, SUPPORTED_FORMATS
from favicons._exceptions import FaviconNotSupportedError

LoosePath = Union[Path, str]
LooseColor = Union[Collection[int], str]


class Favicons:
    """Generate common favicon formats from a single source image."""

    def __init__(
        self,
        source: LoosePath,
        output_directory: LoosePath,
        background_color: LooseColor = "#000000",
        transparent: bool = True,
        base_url: str = "/",
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Initialize Favicons class."""
        self._validated = False
        self._output_directory = output_directory
        self._formats = tuple(generate_icon_types())
        self.transparent = transparent
        self.base_url = base_url
        self.background_color: Color = Color(background_color)
        self.generate: Union[Callable, Coroutine] = self.sgenerate
        self.completed: int = 0
        self._temp_source: Optional[Path] = None

        if isinstance(source, str):
            source = Path(source)

        self._source = source

        self._check_source_format()

    def _validate(self) -> None:

        self.source = validate_path(self._source)
        self.output_directory = validate_path(self._output_directory, create=True)

        if self.source.suffix.lower() not in SUPPORTED_FORMATS:
            raise FaviconNotSupportedError(self.source)

        self._validated = True

    def __enter__(self) -> "Favicons":
        """Enter Favicons context."""
        self._validate()
        self.generate = self.sgenerate
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> None:
        """Exit Favicons context."""
        self._close_temp_source()
        pass

    async def __aenter__(self) -> "Favicons":
        """Enter Favicons context."""
        self._validate()
        self.generate = self.agenerate
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> None:
        """Exit Favicons context."""
        self._close_temp_source()
        pass

    def _close_temp_source(self) -> None:
        """Close temporary file if it exists."""
        if self._temp_source is not None:
            try:
                self._temp_source.unlink()
            except FileNotFoundError:
                pass

    def _check_source_format(self) -> None:
        """Convert source image to PNG if it's in SVG format."""
        if self._source.suffix == ".svg":
            self._source = svg_to_png(self._source, self.background_color)

    @staticmethod
    def _get_center_point(background: PILImage, foreground: PILImage) -> Tuple:
        """Generate a tuple of center points for PIL."""
        bg_x, bg_y = background.size[0:2]
        fg_x, fg_y = foreground.size[0:2]
        x1 = math.floor((bg_x / 2) - (fg_x / 2))
        y1 = math.floor((bg_y / 2) - (fg_y / 2))
        x2 = math.floor((bg_x / 2) + (fg_x / 2))
        y2 = math.floor((bg_y / 2) + (fg_y / 2))
        return (x1, y1, x2, y2)

    def _generate_single(self, format_properties: FaviconProperties) -> None:
        with PILImage.open(self.source) as src:
            output_file = self.output_directory / str(format_properties)
            bg: Tuple[int, ...] = self.background_color.colors

            # If transparency is enabled, add alpha channel to color.
            if self.transparent:
                bg += (0,)

            # Create background.
            dst = PILImage.new("RGBA", format_properties.dimensions, bg)

            # Resize source image without changing aspect ratio.
            src.thumbnail(format_properties.dimensions)

            # Place source image on top of background image.
            dst.paste(src, box=self._get_center_point(dst, src))

            # Save new file.
            dst.save(output_file, format_properties.format)

            self.completed += 1

    async def _agenerate_single(self, format_properties: FaviconProperties) -> None:
        """Awaitable version of _generate_single."""

        return self._generate_single(format_properties)

    def sgenerate(self) -> None:
        """Generate favicons."""
        if not self._validated:
            self._validate()

        for fmt in self._formats:
            self._generate_single(fmt)

    async def agenerate(self) -> None:
        """Generate favicons."""
        if not self._validated:
            self._validate()

        await asyncio.gather(*(self._agenerate_single(fmt) for fmt in self._formats))

    def html_gen(self) -> Generator:
        """Get generator of HTML strings."""
        for fmt in self._formats:
            yield HTML_LINK.format(
                rel=fmt.rel,
                type=f"image/{fmt.format}",
                href=self.base_url + str(fmt),
            )

    def html(self) -> Tuple:
        """Get tuple of HTML strings."""
        return tuple(self.html_gen())

    def formats(self) -> Tuple:
        """Get image formats as list."""
        return tuple(f.dict() for f in self._formats)

    def json(self, *args: Any, **kwargs: Any) -> str:
        """Get image formats as JSON string."""
        return _json.dumps(self.formats(), *args, **kwargs)

    def filenames_gen(self, prefix: bool = False) -> Generator:
        """Get generator of favicon file names."""
        for fmt in self._formats:
            filename = str(fmt)
            if prefix:
                filename = self.base_url + filename
            yield filename

    def filenames(self, prefix: bool = False) -> Tuple:
        """Get tuple of favicon file names."""
        return tuple(self.filenames_gen(prefix=prefix))