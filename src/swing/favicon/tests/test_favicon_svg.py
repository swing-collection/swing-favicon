# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Favicon SVG File Tests
======================

Tests for SVG favicon file serving.

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
    "FaviconSVGTests",
]


# =============================================================================
# Classes
# =============================================================================


class FaviconSVGTests(SimpleTestCase):
    """
    Favicon SVG File Tests Class
    ============================

    """

    def test_favicon_svg_endpoint_responds(self) -> None:
        """Test that favicon.svg endpoint responds without error."""
        response = self.client.get("/favicon.svg")
        # Should not cause server error
        self.assertNotEqual(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    def test_favicon_svg_content_type_when_served(self) -> None:
        """Test content type is SVG when favicon.svg is served."""
        response = self.client.get("/favicon.svg")
        if response.status_code == HTTPStatus.OK:
            content_type = response.get("Content-Type", "").lower()
            self.assertTrue(
                "svg" in content_type,
                f"Expected SVG content type, got {content_type}",
            )

    def test_safari_pinned_tab_endpoint_responds(self) -> None:
        """Test that safari-pinned-tab.svg endpoint responds without error."""
        response = self.client.get("/safari-pinned-tab.svg")
        self.assertNotEqual(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
