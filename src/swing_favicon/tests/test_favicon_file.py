# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Favicon File Tests Class
=================================


"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Any, Dict, List
from http import HTTPStatus

# Import | Libraries
from django.test import SimpleTestCase

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================

__all__ = ["FaviconFileTests", ]


# =============================================================================
# Classes
# =============================================================================

class FaviconFileTests(SimpleTestCase):
    """
    """

    def test_get(self):
        names = [
            "android-chrome-192x192.png",
            "android-chrome-512x512.png",
            "apple-touch-icon.png",
            "browserconfig.xml",
            "favicon-16x16.png",
            "favicon-32x32.png",
            "favicon.ico",
            "mstile-150x150.png",
            "safari-pinned-tab.svg",
            "site.webmanifest",
        ]

        for name in names:
            with self.subTest(name):
                response = self.client.get(f"/{name}")

                self.assertEqual(
                    response.status_code,
                    HTTPStatus.OK
                )
                self.assertEqual(
                    response["Cache-Control"],
                    "max-age=86400, immutable, public",
                )
                self.assertGreater(
                    len(response.getvalue()),
                    0
                )
