# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""Get Apple touch icon links."""

from django.templatetags.static import static


def get_apple_links(base_path: str) -> list[str]:
    """Get Apple touch icon links."""
    sizes = [57, 60, 72, 76, 114, 120, 144, 152, 167, 180]
    links = [
        # Default apple-touch-icon
        f'<link rel="apple-touch-icon" href="{static(f"{base_path}/apple-touch-icon.png")}">',
    ]

    for size in sizes:
        links.append(
            f'<link rel="apple-touch-icon" sizes="{size}x{size}" '
            f'href="{static(f"{base_path}/apple-touch-icon-{size}x{size}.png")}">'
        )

    # Safari pinned tab
    links.append(
        f'<link rel="mask-icon" href="{static(f"{base_path}/safari-pinned-tab.svg")}" color="#000000">'
    )

    return links
