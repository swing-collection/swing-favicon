# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Favicon Tests Module
====================

Comprehensive test suite for the swing.favicon Django application.

Test Categories:
    - test_favicon_file: Favicon file serving tests
    - test_favicon_path: Static file path tests
    - test_favicon_png: PNG favicon tests
    - test_favicon_svg: SVG favicon tests
    - test_templatetags: Template tag tests
    - test_security: Security and path traversal tests
    - test_exceptions: Exception class tests
    - test_utils: Utility function tests
    - test_management_commands: Management command tests
    - test_views: View tests (manifest, browserconfig, emoji)

Running Tests:
    python manage.py test swing.favicon
    python manage.py test swing.favicon.tests.test_security
    pytest src/swing/favicon/tests/

"""


# =============================================================================
# Imports
# =============================================================================

# Test modules are discovered automatically by Django's test runner.
# Explicit imports are not needed here as tests are run via:
#   python manage.py test swing.favicon.tests
#
# Each test file exports its test classes via __all__.
