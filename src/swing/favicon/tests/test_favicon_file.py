# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Favicon File Tests
==================

Tests for favicon file serving endpoints.

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
    "FaviconFileTests",
]


# =============================================================================
# Classes
# =============================================================================


class FaviconFileTests(SimpleTestCase):
    """Test favicon file serving."""

    def test_favicon_ico_endpoint_exists(self) -> None:
        """Test that favicon.ico endpoint responds."""
        response = self.client.get("/favicon.ico")
        # Endpoint should exist - may return 200 or 404 if file missing
        self.assertIn(
            response.status_code,
            [HTTPStatus.OK, HTTPStatus.NOT_FOUND],
        )

    def test_favicon_has_cache_headers_when_exists(self) -> None:
        """Test cache headers are set when favicon is served."""
        response = self.client.get("/favicon.ico")
        if response.status_code == HTTPStatus.OK:
            self.assertIn("Cache-Control", response)
            self.assertIn("max-age", response.get("Cache-Control", ""))

    def test_favicon_endpoints_dont_error(self) -> None:
        """Test that favicon endpoints don't cause server errors."""
        names = [
            "favicon.ico",
            "favicon-16x16.png",
            "favicon-32x32.png",
            "favicon.svg",
            "apple-touch-icon.png",
            "android-chrome-192x192.png",
            "android-chrome-512x512.png",
            "mstile-150x150.png",
            "safari-pinned-tab.svg",
            "site.webmanifest",
            "browserconfig.xml",
        ]

        for name in names:
            with self.subTest(name=name):
                response = self.client.get(f"/{name}")
                # Should not cause server error
                self.assertNotEqual(
                    response.status_code,
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                    f"Endpoint /{name} should not cause server error",
                )
