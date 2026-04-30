# -*- coding: utf-8 -*-
"""
Generate browserconfig.xml for Windows tiles.

browserconfig.xml is an XML file that defines tile images and colors for
Windows 8/10/11 Start menu tiles and Internet Explorer 11+ pinned sites.
"""

from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString
from typing import Optional

from ..conf import FAVICON_MS_TILE_COLOR, FAVICON_BASE_PATH
from ..constants import BROWSERCONFIG_TILES


def generate_browserconfig(
    base_path: Optional[str] = None,
    tile_color: Optional[str] = None,
    tiles: Optional[dict] = None,
) -> str:
    """
    Generate browserconfig.xml content.

    Parameters:
        base_path: Base path for tile images (default: from settings)
        tile_color: Background color for tiles (default: from settings)
        tiles: Custom tile configuration dict (default: from constants)

    Returns:
        str: browserconfig.xml content as formatted XML string
    """
    base_path = base_path or f"/{FAVICON_BASE_PATH}"
    tile_color = tile_color or FAVICON_MS_TILE_COLOR
    tiles = tiles or BROWSERCONFIG_TILES

    # Create root element
    browserconfig = Element("browserconfig")
    msapplication = SubElement(browserconfig, "msapplication")
    tile = SubElement(msapplication, "tile")

    # Add tile images
    for tile_name, tile_src in tiles.items():
        # Prepend base_path if src doesn't start with /
        src = tile_src if tile_src.startswith("/") else f"{base_path}/{tile_src}"
        tile_element = SubElement(tile, tile_name)
        tile_element.set("src", src)

    # Add tile color
    tile_color_element = SubElement(tile, "TileColor")
    tile_color_element.text = tile_color

    # Convert to string with proper formatting
    xml_string = tostring(browserconfig, encoding="unicode")
    dom = parseString(f'<?xml version="1.0" encoding="utf-8"?>{xml_string}')

    return dom.toprettyxml(indent="    ", encoding=None).replace(
        '<?xml version="1.0" ?>\n', '<?xml version="1.0" encoding="utf-8"?>\n'
    )


def generate_browserconfig_dict(
    base_path: Optional[str] = None,
    tile_color: Optional[str] = None,
) -> dict:
    """
    Generate browserconfig data as a dictionary.

    Useful for testing or custom XML generation.

    Parameters:
        base_path: Base path for tile images
        tile_color: Background color for tiles

    Returns:
        dict: browserconfig data structure
    """
    base_path = base_path or f"/{FAVICON_BASE_PATH}"
    tile_color = tile_color or FAVICON_MS_TILE_COLOR

    return {
        "msapplication": {
            "tile": {
                "square70x70logo": {"src": f"{base_path}/mstile-70x70.png"},
                "square144x144logo": {"src": f"{base_path}/mstile-144x144.png"},
                "square150x150logo": {"src": f"{base_path}/mstile-150x150.png"},
                "square310x310logo": {"src": f"{base_path}/mstile-310x310.png"},
                "wide310x150logo": {"src": f"{base_path}/mstile-310x150.png"},
                "TileColor": tile_color,
            }
        }
    }
