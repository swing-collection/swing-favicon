# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""Get standard favicon links."""

from django.templatetags.static import static


def get_standard_links(base_path: str) -> list[str]:
    """Get standard favicon links."""
    sizes = [16, 32, 48, 64, 96, 128, 192, 256]
    links = [
        f'<link rel="icon" href="{static(f"{base_path}/favicon.ico")}" type="image/x-icon">',
        f'<link rel="shortcut icon" href="{static(f"{base_path}/favicon.ico")}" type="image/x-icon">',
    ]

    for size in sizes:
        links.append(
            f'<link rel="icon" sizes="{size}x{size}" '
            f'href="{static(f"{base_path}/favicon-{size}x{size}.png")}" type="image/png">'
        )

    # SVG favicon for modern browsers
    links.append(
        f'<link rel="icon" href="{static(f"{base_path}/favicon.svg")}" type="image/svg+xml">'
    )

    return links
