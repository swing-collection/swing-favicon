"""Utility functions for path validation."""

# Import | Standard Library
from pathlib import Path

# Import | Local
from ..exceptions import FaviconNotFoundError, FaviconsError


def validate_path(
    path: Path | str, must_exist: bool = True, create: bool = False
) -> Path:
    """Validate a path and ensure it's a Path object.

    Args:
        path: The path to validate (string or Path object).
        must_exist: If True, raise error if path doesn't exist.
        create: If True, create the directory if it doesn't exist.

    Returns:
        The validated Path object.

    Raises:
        FaviconsError: If the path is invalid.
        FaviconNotFoundError: If must_exist is True and path doesn't exist.
    """
    if isinstance(path, str):
        try:
            path = Path(path)
        except TypeError as err:
            raise FaviconsError("{path} is not a valid path.", path=path) from err

    if create:
        if path.is_dir() and not path.exists():
            path.mkdir(parents=True)
        elif not path.is_dir() and not path.parent.exists():
            path.parent.mkdir(parents=True)

    if must_exist and not path.exists():
        raise FaviconNotFoundError(path)

    return path
