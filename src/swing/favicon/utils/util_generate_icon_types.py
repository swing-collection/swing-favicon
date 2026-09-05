"""Common utility functions for favicon icon types."""

# Import | Standard Library
from typing import Generator

# Import | Local
from ..constants.constants_favicon import FAVICON_TYPES, FaviconTypeConfig


def generate_icon_types() -> Generator[FaviconTypeConfig, None, None]:
    """Get icon type objects."""
    for icon_type in FAVICON_TYPES:
        if isinstance(icon_type, dict):
            yield icon_type
