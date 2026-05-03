# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Template Tags Tests
===================

Tests for favicon template tags to ensure proper HTML generation.

"""


# =============================================================================
# Imports
# =============================================================================

from django.template import Context, Template
from django.test import override_settings, SimpleTestCase

# =============================================================================
# Variables
# =============================================================================

__all__: list[str] = [
    "FaviconLinksTagTests",
    "FaviconLinksFullTagTests",
    "FaviconLinksMinimalTagTests",
    "FaviconLinksSafariTagTests",
]


# =============================================================================
# Classes
# =============================================================================


class FaviconLinksTagTests(SimpleTestCase):
    """Tests for the favicon_links template tag."""

    def test_favicon_links_renders(self) -> None:
        """Test that favicon_links tag renders without error."""
        template = Template("{% load simple.favicon_links %}{% favicon_links %}")
        html = template.render(Context({}))
        self.assertIn("<link", html)

    def test_favicon_links_contains_ico(self) -> None:
        """Test that favicon_links includes .ico favicon."""
        template = Template("{% load simple.favicon_links %}{% favicon_links %}")
        html = template.render(Context({}))
        self.assertIn("favicon.ico", html)

    def test_favicon_links_contains_manifest(self) -> None:
        """Test that favicon_links includes site.webmanifest."""
        template = Template("{% load simple.favicon_links %}{% favicon_links %}")
        html = template.render(Context({}))
        self.assertIn("site.webmanifest", html)


class FaviconLinksFullTagTests(SimpleTestCase):
    """Tests for the favicon_links_full template tag."""

    def test_favicon_links_full_renders(self) -> None:
        """Test that favicon_links_full tag renders without error."""
        template = Template("{% load simple.favicon_links %}{% favicon_links_full %}")
        html = template.render(Context({}))
        self.assertIn("<link", html)

    def test_favicon_links_full_contains_apple_touch(self) -> None:
        """Test that favicon_links_full includes apple-touch-icon."""
        template = Template("{% load simple.favicon_links %}{% favicon_links_full %}")
        html = template.render(Context({}))
        self.assertIn("apple-touch-icon", html)

    def test_favicon_links_full_contains_android_chrome(self) -> None:
        """Test that favicon_links_full includes android-chrome icons."""
        template = Template("{% load simple.favicon_links %}{% favicon_links_full %}")
        html = template.render(Context({}))
        self.assertIn("android-chrome", html)

    def test_favicon_links_full_contains_mstile(self) -> None:
        """Test that favicon_links_full includes Microsoft tile."""
        template = Template("{% load simple.favicon_links %}{% favicon_links_full %}")
        html = template.render(Context({}))
        self.assertIn("mstile", html)


class FaviconLinksMinimalTagTests(SimpleTestCase):
    """Tests for the favicon_links_minimal template tag."""

    def test_favicon_links_minimal_renders(self) -> None:
        """Test that favicon_links_minimal tag renders without error."""
        template = Template(
            "{% load simple.favicon_links %}{% favicon_links_minimal %}"
        )
        html = template.render(Context({}))
        self.assertIn("<link", html)

    def test_favicon_links_minimal_has_fewer_links(self) -> None:
        """Test that minimal has fewer links than full."""
        minimal_template = Template(
            "{% load simple.favicon_links %}{% favicon_links_minimal %}"
        )
        full_template = Template(
            "{% load simple.favicon_links %}{% favicon_links_full %}"
        )
        minimal_html = minimal_template.render(Context({}))
        full_html = full_template.render(Context({}))
        self.assertLess(
            minimal_html.count("<link"),
            full_html.count("<link"),
        )


class FaviconLinksSafariTagTests(SimpleTestCase):
    """Tests for the favicon_links_safari template tag."""

    def test_favicon_links_safari_renders(self) -> None:
        """Test that favicon_links_safari tag renders without error."""
        template = Template("{% load simple.favicon_links %}{% favicon_links_safari %}")
        html = template.render(Context({}))
        self.assertIn("<link", html)

    def test_favicon_links_safari_contains_mask_icon(self) -> None:
        """Test that favicon_links_safari includes mask-icon."""
        template = Template("{% load simple.favicon_links %}{% favicon_links_safari %}")
        html = template.render(Context({}))
        self.assertIn("mask-icon", html)

    def test_favicon_links_safari_has_color_attribute(self) -> None:
        """Test that Safari tag includes color attribute."""
        template = Template("{% load simple.favicon_links %}{% favicon_links_safari %}")
        html = template.render(Context({}))
        # Should have a color attribute (any valid hex color)
        self.assertIn('color="#', html)
