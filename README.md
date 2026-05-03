<p align="center">
    <img src="https://github.com/scape-agency/swing.dj/blob/85830584264bca52c02e1f0dcfa3648f84783805/res/swing-logo.png" width="20%" height="20%" alt="Django Swing Logo">
</p>
<h1 align='center' style='border-bottom: none;'>Swing Favicon</h1>
<h3 align='center'>Django Swing Collection</h3>
<br/>

---

A comprehensive Django application for managing and serving favicons across all modern browsers and platforms. Supports PWA manifests, Microsoft tiles, Apple touch icons, Safari pinned tabs, and more.

## Features

- 🎨 **Multi-format Support** - ICO, PNG, SVG, WebP
- 📱 **PWA Ready** - Web manifest with maskable icons
- 🍎 **Apple Touch Icons** - All iOS device sizes
- 🪟 **Microsoft Tiles** - browserconfig.xml support
- 🦁 **Safari Pinned Tab** - Monochrome mask icons
- ⚡ **Smart Caching** - Configurable cache headers
- 🛠️ **Management Commands** - Generate favicons from source
- 🏷️ **Template Tags** - Easy HTML integration

## Installation

```bash
pip install swing-favicon
```

Or with Poetry:

```bash
poetry add swing-favicon
```

## Quick Start

### 1. Add to INSTALLED_APPS

```python
# settings.py
INSTALLED_APPS = [
    # ...
    "swing.favicon",
]
```

### 2. Include URLs

```python
# urls.py
from django.urls import include, path

urlpatterns = [
    path("", include("swing.favicon.urls")),
    # ...
]
```

### 3. Add Template Tags

```html
{% load simple.favicon_links %}
<!DOCTYPE html>
<html>
    <head>
        {% favicon_links %}
    </head>
</html>
```

### 4. Place Favicon Files

Place your favicon files in your static directory:

```
static/
└── favicon/
    ├── favicon.ico
    ├── favicon.svg
    ├── favicon-16x16.png
    ├── favicon-32x32.png
    ├── apple-touch-icon.png
    ├── android-chrome-192x192.png
    ├── android-chrome-512x512.png
    ├── mstile-150x150.png
    └── safari-pinned-tab.svg
```

## Configuration

All settings are optional and have sensible defaults.

### Path Settings

```python
# Base path within static files
FAVICON_BASE_PATH = "favicon"

# Source image for generation
FAVICON_SOURCE_PATH = ""
```

### Cache Settings

```python
# Cache-Control max-age (default: 1 day)
FAVICON_CACHE_MAX_AGE = 86400

# Mark as immutable (prevents revalidation)
FAVICON_CACHE_IMMUTABLE = True

# Allow CDN caching
FAVICON_CACHE_PUBLIC = True
```

### Theme Settings

```python
# Browser chrome color (Android, Windows)
FAVICON_THEME_COLOR = "#ffffff"

# Microsoft tile background
FAVICON_MS_TILE_COLOR = "#ffffff"

# Safari pinned tab color
FAVICON_SAFARI_MASK_COLOR = "#000000"
```

### PWA Settings

```python
# App name for manifest
FAVICON_APP_NAME = "My App"
FAVICON_APP_SHORT_NAME = "App"
FAVICON_APP_DESCRIPTION = "My awesome app"

# PWA behavior
FAVICON_START_URL = "/"
FAVICON_DISPLAY_MODE = "standalone"  # fullscreen, minimal-ui, browser
FAVICON_ORIENTATION = "any"  # natural, landscape, portrait
FAVICON_BACKGROUND_COLOR = "#ffffff"
```

### Size Settings

```python
# Standard favicon sizes
FAVICON_SIZES = [16, 32, 48, 64, 96, 128, 180, 192, 256, 512]

# Apple touch icon sizes
FAVICON_APPLE_SIZES = [57, 60, 72, 76, 114, 120, 144, 152, 167, 180]

# Microsoft tile sizes
FAVICON_MS_TILE_SIZES = [70, 150, 270, 310, (310, 150)]
```

### Feature Flags

```python
# Enable SVG favicon
FAVICON_ENABLE_SVG = True

# Enable web manifest generation
FAVICON_ENABLE_MANIFEST = True

# Enable browserconfig.xml
FAVICON_ENABLE_BROWSERCONFIG = True

# Auto-generate on model save
FAVICON_AUTO_GENERATE = False
```

## Template Tags

### favicon_links (Default/Minimal)

Essential favicons for most use cases:

```html
{% load simple.favicon_links %} {% favicon_links %}
```

Outputs: ICO, 32px PNG, Apple touch icon, manifest

### favicon_links_full

All favicon variants for maximum compatibility:

```html
{% load simple.favicon_links %} {% favicon_links_full %}
```

Outputs: All sizes, all platforms, all formats

### favicon_links_minimal

Absolute minimum for basic support:

```html
{% load simple.favicon_links %} {% favicon_links_minimal %}
```

Outputs: ICO and manifest only

### favicon_links_safari

Safari pinned tab support:

```html
{% load simple.favicon_links %} {% favicon_links_safari %}
```

Outputs: mask-icon link with color

## Management Commands

### Generate Favicons

Generate all favicon variants from a source image:

```bash
python manage.py generate_favicons source.png
python manage.py generate_favicons source.svg --output static/favicon
python manage.py generate_favicons source.png --formats png,ico,apple
python manage.py generate_favicons source.png --sizes 16,32,64,128
python manage.py generate_favicons source.png --dry-run
```

### Validate Favicons

Check that all required favicon files exist:

```bash
python manage.py validate_favicons
```

## URL Endpoints

The app provides the following URL patterns:

| Endpoint                                     | Description              |
| -------------------------------------------- | ------------------------ |
| `/favicon.ico`                               | Primary favicon          |
| `/favicon.svg`                               | SVG favicon              |
| `/favicon-{size}x{size}.png`                 | PNG favicons (16-512px)  |
| `/apple-touch-icon.png`                      | Default Apple touch icon |
| `/apple-touch-icon-{size}x{size}.png`        | Apple touch icons        |
| `/android-chrome-{size}x{size}.png`          | Android Chrome icons     |
| `/android-chrome-maskable-{size}x{size}.png` | Maskable PWA icons       |
| `/mstile-{size}x{size}.png`                  | Microsoft tiles          |
| `/site.webmanifest`                          | PWA web manifest         |
| `/browserconfig.xml`                         | Microsoft browser config |
| `/safari-pinned-tab.svg`                     | Safari pinned tab icon   |

## Development

### Running Tests

```bash
# Run all tests
make test

# Run specific test file
python manage.py test swing.favicon.tests.test_security

# With pytest
pytest src/swing/favicon/tests/
```

### Linting

```bash
make lint
make format
```

## Colophon

Made with ❤️ by **[Scape Press](https://www.scape.press)**

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the BSD-3-Clause license. See the [LICENSE](LICENSE) file for details.

---
