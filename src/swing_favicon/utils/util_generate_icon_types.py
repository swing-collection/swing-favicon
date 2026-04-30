"""Common utility functions for favicon icon types."""

from typing import Generator

from ..constants.constants_favicon import FAVICON_TYPES


def generate_icon_types() -> Generator[dict, None, None]:
    """Get icon type objects."""
    for icon_type in FAVICON_TYPES:
        if isinstance(icon_type, dict):
            yield icon_type
