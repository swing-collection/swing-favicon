# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Utility Function Tests
======================

Tests for favicon utility functions including path validation,
icon type generation, color validation, and manifest generation.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from pathlib import Path
import tempfile

from django.test import SimpleTestCase, TestCase

from swing.favicon.exceptions import FaviconColorError, FaviconNotFoundError
from swing.favicon.utils.util_validate_color import (
    is_valid_color,
    is_valid_css_color,
    is_valid_hex_color,
    normalize_hex_color,
    validate_color,
)
from swing.favicon.utils.util_validate_path import validate_path

# =============================================================================
# Variables
# =============================================================================

__all__: list[str] = [
    "ValidatePathTests",
    "GenerateIconTypesTests",
    "ValidateColorTests",
]


# =============================================================================
# Classes
# =============================================================================


class ValidatePathTests(SimpleTestCase):
    """Tests for the validate_path utility function."""

    def test_validate_path_with_string(self) -> None:
        """Test that string path is converted to Path object."""
        with tempfile.TemporaryDirectory() as tmp:
            path = validate_path(tmp, must_exist=True)
            self.assertIsInstance(path, Path)

    def test_validate_path_with_path_object(self) -> None:
        """Test that Path object is returned unchanged."""
        with tempfile.TemporaryDirectory() as tmp:
            input_path = Path(tmp)
            result = validate_path(input_path, must_exist=True)
            self.assertEqual(input_path, result)

    def test_validate_path_raises_when_not_found(self) -> None:
        """Test that FaviconNotFoundError is raised for missing paths."""
        with self.assertRaises(FaviconNotFoundError):
            validate_path("/nonexistent/path/12345", must_exist=True)

    def test_validate_path_allows_missing_when_must_exist_false(self) -> None:
        """Test that missing paths are allowed when must_exist=False."""
        result = validate_path("/nonexistent/path/12345", must_exist=False)
        self.assertIsInstance(result, Path)

    def test_validate_path_creates_parent_directory_when_requested(self) -> None:
        """Test that create=True creates missing parent directories for files."""
        with tempfile.TemporaryDirectory() as tmp:
            new_file = Path(tmp) / "new_subdir" / "file.txt"
            self.assertFalse(new_file.parent.exists())
            validate_path(new_file, must_exist=False, create=True)
            self.assertTrue(new_file.parent.exists())


class ValidateColorTests(SimpleTestCase):
    """Tests for color validation utilities."""

    def test_is_valid_hex_color_6_digit(self) -> None:
        """Test 6-digit hex color validation."""
        self.assertTrue(is_valid_hex_color("#ff5500"))
        self.assertTrue(is_valid_hex_color("#FF5500"))
        self.assertTrue(is_valid_hex_color("#000000"))
        self.assertTrue(is_valid_hex_color("#ffffff"))

    def test_is_valid_hex_color_3_digit(self) -> None:
        """Test 3-digit hex color validation."""
        self.assertTrue(is_valid_hex_color("#f50"))
        self.assertTrue(is_valid_hex_color("#F50"))
        self.assertTrue(is_valid_hex_color("#000"))
        self.assertTrue(is_valid_hex_color("#fff"))

    def test_is_valid_hex_color_8_digit_rgba(self) -> None:
        """Test 8-digit hex color (RGBA) validation."""
        self.assertTrue(is_valid_hex_color("#ff550080"))
        self.assertTrue(is_valid_hex_color("#00000000"))
        self.assertTrue(is_valid_hex_color("#ffffffff"))

    def test_is_valid_hex_color_invalid(self) -> None:
        """Test invalid hex color detection."""
        self.assertFalse(is_valid_hex_color("ff5500"))  # Missing #
        self.assertFalse(is_valid_hex_color("#ff550"))  # Wrong length
        self.assertFalse(is_valid_hex_color("#gg5500"))  # Invalid chars
        self.assertFalse(is_valid_hex_color("red"))  # Named color

    def test_is_valid_css_color(self) -> None:
        """Test CSS color name validation."""
        self.assertTrue(is_valid_css_color("red"))
        self.assertTrue(is_valid_css_color("blue"))
        self.assertTrue(is_valid_css_color("transparent"))
        self.assertTrue(is_valid_css_color("rebeccapurple"))
        self.assertFalse(is_valid_css_color("notacolor"))

    def test_is_valid_color(self) -> None:
        """Test combined color validation."""
        self.assertTrue(is_valid_color("#ff5500"))
        self.assertTrue(is_valid_color("red"))
        self.assertFalse(is_valid_color("notacolor"))
        self.assertFalse(is_valid_color("#gg5500"))

    def test_validate_color_valid(self) -> None:
        """Test validate_color with valid colors."""
        self.assertEqual(validate_color("#ff5500"), "#ff5500")
        self.assertEqual(validate_color("red"), "red")

    def test_validate_color_invalid_raises(self) -> None:
        """Test validate_color raises FaviconColorError for invalid colors."""
        with self.assertRaises(FaviconColorError):
            validate_color("notacolor")
        with self.assertRaises(FaviconColorError):
            validate_color("#gg5500")

    def test_validate_color_empty_raises(self) -> None:
        """Test validate_color raises for empty color."""
        with self.assertRaises(FaviconColorError):
            validate_color("")

    def test_normalize_hex_color_3_to_6(self) -> None:
        """Test normalizing 3-digit hex to 6-digit."""
        self.assertEqual(normalize_hex_color("#f50"), "#ff5500")
        self.assertEqual(normalize_hex_color("#fff"), "#ffffff")
        self.assertEqual(normalize_hex_color("#000"), "#000000")

    def test_normalize_hex_color_6_unchanged(self) -> None:
        """Test 6-digit hex colors remain unchanged."""
        self.assertEqual(normalize_hex_color("#ff5500"), "#ff5500")
        self.assertEqual(normalize_hex_color("#ffffff"), "#ffffff")

    def test_normalize_hex_color_invalid_raises(self) -> None:
        """Test normalize_hex_color raises for invalid input."""
        with self.assertRaises(FaviconColorError):
            normalize_hex_color("red")
        with self.assertRaises(FaviconColorError):
            normalize_hex_color("#gg5500")


class GenerateIconTypesTests(TestCase):
    """Tests for icon type generation utilities."""

    def test_import_generate_icon_types(self) -> None:
        """Test that generate_icon_types module can be imported."""
        from swing.favicon.utils import util_generate_icon_types

        self.assertIsNotNone(util_generate_icon_types)


class GenerateManifestTests(TestCase):
    """Tests for manifest generation utilities."""

    def test_import_generate_manifest(self) -> None:
        """Test that generate_manifest module can be imported."""
        from swing.favicon.utils import util_generate_manifest

        self.assertIsNotNone(util_generate_manifest)


class GenerateBrowserconfigTests(TestCase):
    """Tests for browserconfig generation utilities."""

    def test_import_generate_browserconfig(self) -> None:
        """Test that generate_browserconfig module can be imported."""
        from swing.favicon.utils import util_generate_browserconfig

        self.assertIsNotNone(util_generate_browserconfig)


class SvgToPngTests(TestCase):
    """Tests for SVG to PNG conversion utilities."""

    def test_import_svg_to_png(self) -> None:
        """Test that svg_to_png module can be imported."""
        from swing.favicon.utils import util_svg_to_png

        self.assertIsNotNone(util_svg_to_png)
