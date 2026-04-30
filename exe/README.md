# Demo Project for `swing-favicon`

Self-contained Django project for testing and showcasing the
`swing.favicon` reusable app in isolation.

## Quick Start

```bash
cd swing-favicon
poetry install
cd exe
poetry run python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser.

## Available Endpoints

| Endpoint                      | Description                         |
| ----------------------------- | ----------------------------------- |
| `/`                           | Demo home page with favicon preview |
| `/favicon.ico`                | Primary favicon (ICO)               |
| `/favicon-16x16.png`          | 16x16 PNG favicon                   |
| `/favicon-32x32.png`          | 32x32 PNG favicon                   |
| `/favicon-48x48.png`          | 48x48 PNG favicon                   |
| `/favicon-64x64.png`          | 64x64 PNG favicon                   |
| `/favicon-96x96.png`          | 96x96 PNG favicon                   |
| `/favicon-128x128.png`        | 128x128 PNG favicon                 |
| `/apple-touch-icon.png`       | Apple touch icon (180x180)          |
| `/android-chrome-192x192.png` | Android Chrome icon                 |
| `/android-chrome-512x512.png` | Android Chrome large icon           |
| `/admin/`                     | Django admin                        |

## Template Tags

```django
{% load simple.favicon_links %}

{# Minimal set (recommended) #}
{% favicon_links %}

{# Full set with all variants #}
{% favicon_links "full" %}

{# Specific variants #}
{% favicon_links "apple" %}
{% favicon_links "microsoft" %}
{% favicon_links "android" %}
```

## Configuration (settings.py)

```python
INSTALLED_APPS = [
    ...
    "swing.favicon",
]

FAVICON_BASE_PATH = "favicon"
FAVICON_THEME_COLOR = "#3498db"
FAVICON_MS_TILE_COLOR = "#3498db"
FAVICON_CACHE_MAX_AGE = 60 * 60 * 24  # 1 day
```

## Project Structure

```text
exe/
├── demo/
│   ├── __init__.py
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL routing
│   ├── views.py         # Demo views
│   ├── wsgi.py
│   └── templates/
│       └── home.html    # Demo home page
├── static/
│   └── favicon/         # Sample favicon files
├── manage.py
└── README.md
```
