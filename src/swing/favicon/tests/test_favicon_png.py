# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Favicon PNG File Tests
======================

Tests for PNG favicon file serving.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from http import HTTPStatus

from django.test import SimpleTestCase

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================

__all__: list[str] = [
    "FaviconPNGTests",
]


# =============================================================================
# Classes
# =============================================================================


class FaviconPNGTests(SimpleTestCase):
    """
    Favicon PNG File Tests Class
    ============================

    """

    def test_favicon_ico_endpoint_responds(self) -> None:
        """Test that favicon.ico endpoint responds without error."""
        response = self.client.get("/favicon.ico")
        # Should not cause server error
        self.assertNotEqual(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    def test_favicon_has_cache_headers_when_served(self) -> None:
        """Test cache headers are present when favicon is served."""
        response = self.client.get("/favicon.ico")
        if response.status_code == HTTPStatus.OK:
            self.assertIn("Cache-Control", response)

    def test_favicon_content_type_when_served(self) -> None:
        """Test content type is image when favicon is served."""
        response = self.client.get("/favicon.ico")
        if response.status_code == HTTPStatus.OK:
            content_type = response.get("Content-Type", "").lower()
            self.assertTrue(
                "image" in content_type or "icon" in content_type,
                f"Expected image content type, got {content_type}",
            )
