# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Exception Tests
===============

Tests for favicon exception classes to ensure proper error handling
and message formatting.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from pathlib import Path

from django.test import SimpleTestCase

from swing.favicon.exceptions import (
    FaviconColorError,
    FaviconNotFoundError,
    FaviconNotSupportedError,
    FaviconsError,
)

# =============================================================================
# Variables
# =============================================================================

__all__: list[str] = [
    "FaviconsErrorTests",
    "FaviconNotFoundErrorTests",
    "FaviconNotSupportedErrorTests",
    "FaviconColorErrorTests",
]


# =============================================================================
# Classes
# =============================================================================


class FaviconsErrorTests(SimpleTestCase):
    """Tests for the base FaviconsError exception."""

    def test_base_error_with_message(self) -> None:
        """Test that base error accepts and stores message."""
        error = FaviconsError("Test error message")
        self.assertIn("Test error message", str(error))

    def test_base_error_is_exception(self) -> None:
        """Test that FaviconsError inherits from Exception."""
        self.assertTrue(issubclass(FaviconsError, Exception))

    def test_base_error_can_be_raised(self) -> None:
        """Test that FaviconsError can be raised and caught."""
        with self.assertRaises(FaviconsError):
            raise FaviconsError("Test error")


class FaviconNotFoundErrorTests(SimpleTestCase):
    """Tests for FaviconNotFoundError exception."""

    def test_not_found_with_path(self) -> None:
        """Test that not found error includes path in message."""
        path = Path("/test/favicon.ico")
        error = FaviconNotFoundError(path)
        self.assertIn("favicon.ico", str(error))

    def test_not_found_inherits_from_base(self) -> None:
        """Test that FaviconNotFoundError inherits from FaviconsError."""
        self.assertTrue(issubclass(FaviconNotFoundError, FaviconsError))

    def test_not_found_is_catchable_as_base(self) -> None:
        """Test that FaviconNotFoundError can be caught as FaviconsError."""
        try:
            raise FaviconNotFoundError(Path("/test/path"))
        except FaviconsError as e:
            self.assertIsInstance(e, FaviconNotFoundError)

    def test_not_found_message_mentions_existence(self) -> None:
        """Test that error message indicates file doesn't exist."""
        error = FaviconNotFoundError(Path("/test/favicon.ico"))
        message = str(error).lower()
        self.assertTrue(
            "exist" in message or "not found" in message,
            f"Expected existence mention, got: {message}",
        )


class FaviconNotSupportedErrorTests(SimpleTestCase):
    """Tests for FaviconNotSupportedError exception."""

    def test_not_supported_with_path(self) -> None:
        """Test that not supported error includes extension."""
        path = Path("/test/favicon.bmp")
        error = FaviconNotSupportedError(path)
        self.assertIn(".bmp", str(error))

    def test_not_supported_inherits_from_base(self) -> None:
        """Test that FaviconNotSupportedError inherits from FaviconsError."""
        self.assertTrue(issubclass(FaviconNotSupportedError, FaviconsError))

    def test_not_supported_mentions_valid_formats(self) -> None:
        """Test that error message lists valid formats."""
        error = FaviconNotSupportedError(Path("/test/file.bmp"))
        message = str(error)
        # Should mention at least one supported format
        self.assertTrue(
            ".png" in message or ".ico" in message or ".svg" in message,
            f"Expected supported formats mentioned, got: {message}",
        )


class FaviconColorErrorTests(SimpleTestCase):
    """Tests for FaviconColorError exception."""

    def test_color_error_with_invalid_string(self) -> None:
        """Test that color error accepts invalid color string."""
        error = FaviconColorError("not-a-color")
        self.assertIn("not-a-color", str(error))

    def test_color_error_inherits_from_base(self) -> None:
        """Test that FaviconColorError inherits from FaviconsError."""
        self.assertTrue(issubclass(FaviconColorError, FaviconsError))

    def test_color_error_with_list(self) -> None:
        """Test that color error handles list input."""
        error = FaviconColorError(["red", "blue"])
        self.assertIsNotNone(error)

    def test_color_error_message_mentions_color(self) -> None:
        """Test that error message mentions 'color'."""
        error = FaviconColorError("#xyz")
        message = str(error).lower()
        self.assertIn("color", message)
