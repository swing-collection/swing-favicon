# -*- coding: utf-8 -*-
"""
Favicon Not Supported Exception
================================

Raised when a favicon file has an unsupported format.
Supported formats are defined in constants.SUPPORTED_FORMATS.

"""

# Import | Standard Library
from pathlib import Path

# Import | Local
from ..constants.constants_favicon import SUPPORTED_FORMATS
from .exception_base import FaviconsError


class FaviconNotSupportedError(FaviconsError):
    """
    Raised when a favicon file format is not supported.

    This exception is raised when attempting to process a favicon
    with an extension that is not in SUPPORTED_FORMATS.

    Args:
        file: Path to the favicon file with unsupported format.

    Example:
        if path.suffix not in SUPPORTED_FORMATS:
            raise FaviconNotSupportedError(path)

    """

    def __init__(self, file: Path) -> None:
        """
        Initialize the exception.

        Args:
            file: Path to the favicon file with unsupported format.
        """
        one_of = ", ".join(f"'{f}'" for f in SUPPORTED_FORMATS)
        super().__init__(
            "Extension {extension} is not supported ({file}). Must be one of {one_of}.",
            extension=file.suffix,
            file=str(file),
            one_of=one_of,
        )
