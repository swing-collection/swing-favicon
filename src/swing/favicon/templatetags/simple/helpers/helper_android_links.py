# -*- coding: utf-8 -*-
"""Get Android/Chrome icon links."""

from django.templatetags.static import static


def get_android_links(base_path: str) -> list[str]:
    """Get Android/Chrome icon links."""
    return [
        f'<link rel="icon" sizes="192x192" href="{static(f"{base_path}/android-chrome-192x192.png")}" type="image/png">',
        f'<link rel="icon" sizes="512x512" href="{static(f"{base_path}/android-chrome-512x512.png")}" type="image/png">',
    ]
