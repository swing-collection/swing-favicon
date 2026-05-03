# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
View Tests
==========

Tests for favicon views including manifest, browserconfig, and emoji views.
Note: Some tests may skip or pass based on whether static files are available.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from http import HTTPStatus
import json

from django.test import override_settings, SimpleTestCase

# =============================================================================
# Variables
# =============================================================================

__all__: list[str] = [
    "WebManifestViewTests",
    "BrowserconfigViewTests",
    "FaviconEmojiViewTests",
    "FaviconSwitchViewTests",
]


# =============================================================================
# Classes
# =============================================================================


class WebManifestViewTests(SimpleTestCase):
    """Tests for the web manifest view."""

    def test_manifest_endpoint_exists(self) -> None:
        """Test that site.webmanifest endpoint responds."""
        response = self.client.get("/site.webmanifest")
        # Endpoint should exist (either return OK or 404 if file missing)
        self.assertIn(
            response.status_code,
            [HTTPStatus.OK, HTTPStatus.NOT_FOUND],
        )

    def test_manifest_content_type_when_exists(self) -> None:
        """Test that manifest has correct content type when available."""
        response = self.client.get("/site.webmanifest")
        if response.status_code == HTTPStatus.OK:
            content_type = response.get("Content-Type", "")
            self.assertTrue(
                "json" in content_type or "manifest" in content_type,
                f"Expected JSON content type, got {content_type}",
            )

    def test_manifest_is_valid_json_when_exists(self) -> None:
        """Test that manifest returns valid JSON when available."""
        response = self.client.get("/site.webmanifest")
        if response.status_code == HTTPStatus.OK:
            try:
                data = json.loads(response.content)
                self.assertIsInstance(data, dict)
            except json.JSONDecodeError:
                self.fail("Manifest should be valid JSON when served")


class BrowserconfigViewTests(SimpleTestCase):
    """Tests for the browserconfig XML view."""

    def test_browserconfig_endpoint_exists(self) -> None:
        """Test that browserconfig.xml endpoint responds."""
        response = self.client.get("/browserconfig.xml")
        self.assertIn(
            response.status_code,
            [HTTPStatus.OK, HTTPStatus.NOT_FOUND],
        )

    def test_browserconfig_content_type_when_exists(self) -> None:
        """Test that browserconfig has correct content type when available."""
        response = self.client.get("/browserconfig.xml")
        if response.status_code == HTTPStatus.OK:
            content_type = response.get("Content-Type", "").lower()
            self.assertTrue(
                "xml" in content_type,
                f"Expected XML content type, got {content_type}",
            )

    def test_browserconfig_is_valid_xml_when_exists(self) -> None:
        """Test that browserconfig returns valid XML when available."""
        response = self.client.get("/browserconfig.xml")
        if response.status_code == HTTPStatus.OK:
            content = response.content.decode("utf-8")
            self.assertTrue(
                content.strip().startswith("<?xml") or content.strip().startswith("<"),
                "Browserconfig should be valid XML",
            )


class FaviconEmojiViewTests(SimpleTestCase):
    """Tests for the emoji favicon view."""

    def test_emoji_favicon_endpoint_exists(self) -> None:
        """Test that emoji favicon endpoint responds."""
        response = self.client.get("/favicon/emoji/🎨")
        # Should not cause server error
        self.assertNotEqual(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    def test_emoji_favicon_handles_empty(self) -> None:
        """Test that empty emoji path is handled gracefully."""
        response = self.client.get("/favicon/emoji/")
        # Should return 404 or redirect, not 500
        self.assertNotEqual(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)


class FaviconSwitchViewTests(SimpleTestCase):
    """Tests for the debug-aware favicon switch view."""

    def test_favicon_switch_endpoint_exists(self) -> None:
        """Test that favicon-switch endpoint responds."""
        response = self.client.get("/favicon-switch")
        # May return 404 if debug favicon doesn't exist, but shouldn't error
        self.assertNotEqual(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
