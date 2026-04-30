# -*- coding: utf-8 -*-
"""Get web manifest links."""

from django.templatetags.static import static


def get_manifest_links(base_path: str) -> list[str]:
    """Get web manifest links."""
    return [
        f'<link rel="manifest" href="{static(f"{base_path}/site.webmanifest")}">',
    ]
