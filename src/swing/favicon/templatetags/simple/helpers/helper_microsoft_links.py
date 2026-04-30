# -*- coding: utf-8 -*-
"""Get Microsoft tile links."""

from django.templatetags.static import static

# Import | Local
from .helper_ms_tile_color import get_ms_tile_color


def get_microsoft_links(base_path: str) -> list[str]:
    """Get Microsoft tile links."""
    ms_tile_color = get_ms_tile_color()

    return [
        f'<meta name="msapplication-TileColor" content="{ms_tile_color}">',
        f'<meta name="msapplication-TileImage" content="{static(f"{base_path}/mstile-150x150.png")}">',
        f'<meta name="msapplication-config" content="{static(f"{base_path}/browserconfig.xml")}">',
    ]
