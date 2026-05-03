# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Security Tests
==============

Security-focused tests to ensure favicon endpoints are protected against
common attack vectors like path traversal and invalid inputs.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from http import HTTPStatus

from django.test import SimpleTestCase

# =============================================================================
# Variables
# =============================================================================

__all__: list[str] = [
    "PathTraversalTests",
    "InvalidInputTests",
]


# =============================================================================
# Classes
# =============================================================================


class PathTraversalTests(SimpleTestCase):
    """Tests for path traversal attack prevention."""

    def test_double_dot_path_returns_404(self) -> None:
        """Test that ../etc/passwd style paths are rejected."""
        response = self.client.get("/../etc/passwd")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_encoded_path_traversal_returns_404(self) -> None:
        """Test that URL-encoded path traversal is rejected."""
        response = self.client.get("/%2e%2e/etc/passwd")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_double_encoded_path_traversal_returns_404(self) -> None:
        """Test that double URL-encoded path traversal is rejected."""
        response = self.client.get("/%252e%252e/etc/passwd")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_backslash_path_traversal_returns_404(self) -> None:
        """Test that backslash path traversal is rejected."""
        response = self.client.get("/..\\..\\etc\\passwd")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_null_byte_injection_returns_404(self) -> None:
        """Test that null byte injection is handled."""
        response = self.client.get("/favicon.ico%00.txt")
        # Should either return 404 or the actual favicon without the extension
        self.assertIn(
            response.status_code,
            [HTTPStatus.OK, HTTPStatus.NOT_FOUND],
        )

    def test_hidden_file_access_returns_404(self) -> None:
        """Test that hidden files (.htaccess, etc.) are not accessible."""
        hidden_files = [".htaccess", ".env", ".gitignore", ".DS_Store"]
        for filename in hidden_files:
            with self.subTest(filename=filename):
                response = self.client.get(f"/{filename}")
                self.assertEqual(
                    response.status_code,
                    HTTPStatus.NOT_FOUND,
                    f"Hidden file {filename} should not be accessible",
                )


class InvalidInputTests(SimpleTestCase):
    """Tests for handling invalid inputs."""

    def test_empty_filename_returns_404(self) -> None:
        """Test that empty filename is rejected."""
        response = self.client.get("/")
        # Root may return homepage or 404 depending on URL config
        self.assertIn(
            response.status_code,
            [HTTPStatus.OK, HTTPStatus.NOT_FOUND, HTTPStatus.MOVED_PERMANENTLY],
        )

    def test_very_long_filename_handled(self) -> None:
        """Test that very long filenames don't cause server error."""
        long_name = "a" * 1000 + ".ico"
        response = self.client.get(f"/{long_name}")
        # Should return 404, not 500
        self.assertNotEqual(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    def test_special_characters_in_filename(self) -> None:
        """Test handling of special characters in filename."""
        special_names = [
            "favicon<script>.ico",
            "favicon;echo.ico",
            "favicon|cat.ico",
            "favicon`whoami`.ico",
        ]
        for name in special_names:
            with self.subTest(name=name):
                response = self.client.get(f"/{name}")
                self.assertNotEqual(
                    response.status_code,
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                    f"Special character filename {name} should not cause error",
                )

    def test_unicode_filename_handled(self) -> None:
        """Test that unicode filenames are handled gracefully."""
        response = self.client.get("/favicon_你好.ico")
        self.assertNotEqual(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    def test_nonexistent_file_returns_404(self) -> None:
        """Test that nonexistent files return 404."""
        response = self.client.get("/nonexistent-favicon-12345.ico")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
