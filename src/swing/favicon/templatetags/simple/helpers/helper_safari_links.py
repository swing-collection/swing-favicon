# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""Get Safari pinned tab (mask-icon) links."""

from django.templatetags.static import static


def get_safari_links(base_path: str, mask_color: str = "#000000") -> list[str]:
    """
    Get Safari pinned tab links.

    Safari's pinned tabs require a monochrome SVG icon (mask-icon).
    The color attribute specifies the icon color when the tab is active.

    Parameters:
        base_path: Base path within static files
        mask_color: Hex color for the active icon (default: black)

    Returns:
        list[str]: List of HTML link tags for Safari pinned tab
    """
    return [
        f'<link rel="mask-icon" href="{static(f"{base_path}/safari-pinned-tab.svg")}" color="{mask_color}">',
    ]
