# -*- coding: utf-8 -*-
"""Favicon not supported exception."""

from pathlib import Path

from .exception_base import FaviconsError
from ..constants.constants_favicon import SUPPORTED_FORMATS


class FaviconNotSupportedError(FaviconsError):
    """Raised if the source favicon file format is not supported."""

    def __init__(self, file: Path) -> None:
        """Set message."""
        one_of = ", ".join(f"'{f}'" for f in SUPPORTED_FORMATS)
        super().__init__(
            "Extension {extension} is not supported ({file}). Must be one of {one_of}.",
            extension=file.suffix,
            file=str(file),
            one_of=one_of,
        )
