"""Common utility functions used throughout Favicons."""

# Standard Library
from typing import Mapping, Generator




# Project
from favicons._types import FaviconProperties
from favicons._constants import ICON_TYPES




def generate_icon_types() -> Generator[FaviconProperties, None, None]:
    """Get icon type objects."""
    for icon_type in ICON_TYPES:
        if isinstance(icon_type, Mapping):
            yield FaviconProperties(**icon_type)

