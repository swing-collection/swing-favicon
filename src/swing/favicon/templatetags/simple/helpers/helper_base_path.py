# -*- coding: utf-8 -*-
"""Get favicon base path from settings."""

from django.conf import settings


def get_base_path() -> str:
    """Get the favicon base path from settings."""
    return getattr(settings, "FAVICON_BASE_PATH", "favicon")
