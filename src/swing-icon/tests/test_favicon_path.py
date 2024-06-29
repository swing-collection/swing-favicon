# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Favicon File Path Tests Class
======================================

This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.

"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Any, Dict, List
# from http import HTTPStatus

# Import | Libraries
# from django.test import SimpleTestCase
from django.test import TestCase
from django.contrib.staticfiles import finders

# Import | Local Modules


# =============================================================================
# Variables
# =============================================================================

__all__ = ["FaviconFilePathTests", ]


# =============================================================================
# Classes
# =============================================================================

class FaviconFilePathTests(TestCase):
    """
    Favicon File Path Tests Class
    =============================

    """

    def test_favicon_file_path(self):
        """
        Tests that favicon.ico exists in the path specified in
        FAVICON_PATH setting
        """

        absolute_path = finders.find('favicon.ico')
        assert absolute_path is not None