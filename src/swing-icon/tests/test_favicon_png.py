# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Favicon PNG File Tests Class
=====================================

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Any, Dict, List
from http import HTTPStatus

# Import | Libraries
from django.test import SimpleTestCase
from django.test import TestCase
from django.contrib.staticfiles import finders

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================

__all__ = ["FaviconPNGTests", ]


# =============================================================================
# Classes
# =============================================================================

class FaviconPNGTests(SimpleTestCase):
    """
    Favicon PNG File Tests Class
    ============================

    """

    def test_get(self):
        """
        """

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
            response["Content-Type"], "image/png"
        )
        self.assertGreater(
            len(response.getvalue()),
            0
        )
