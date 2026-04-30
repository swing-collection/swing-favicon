# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Favicon SVG File Tests Class
=====================================

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from http import HTTPStatus

# Import | Libraries
from django.test import SimpleTestCase

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================

__all__: list[str] = ["FaviconSVGTests", ]


# =============================================================================
# Classes
# =============================================================================

class FaviconSVGTests(SimpleTestCase):
    """
    Favicon SVG File Tests Class
    ============================

    """

    def test_get(self):
        """Test fetching favicon.ico returns OK status."""
        response = self.client.get("/favicon.ico")

        self.assertEqual(
            response.status_code,
            HTTPStatus.OK
        )
        self.assertEqual(
            response["Cache-Control"],
            "max-age=86400, immutable, public"
        )
        self.assertEqual(
            response["Content-Type"],
            "image/svg+xml"
        )
        self.assertTrue(
            response.content.startswith(b"<svg")
        )
