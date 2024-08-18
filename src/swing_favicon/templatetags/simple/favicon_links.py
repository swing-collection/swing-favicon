from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.html import format_html

register = template.Library()

@register.simple_tag
def favicon_links():
    """
    Template tag to output favicon link tags. It supports standard favicons
    and icons for Apple and Windows devices.

    Usage in templates:
        {% load favicon_tags %}
        {% favicon_links %}
    """

    favicon_base_path = getattr(
        settings, 'FAVICON_BASE_PATH', 'favicon_manager/images'
    )

    html = format_html(
        '<link rel="icon" href="{}" type="image/x-icon">'
        '<link rel="icon" sizes="16x16" href="{}" type="image/png">'
        '<link rel="icon" sizes="32x32" href="{}" type="image/png">'
        '<link rel="apple-touch-icon" sizes="180x180" href="{}">'
        '<meta name="msapplication-TileColor" content="#ffffff">'
        '<meta name="msapplication-TileImage" content="{}">',
        static(f'{favicon_base_path}/favicon.ico'),
        static(f'{favicon_base_path}/favicon-16x16.png'),
        static(f'{favicon_base_path}/favicon-32x32.png'),
        static(f'{favicon_base_path}/apple-touch-icon.png'),
        static(f'{favicon_base_path}/mstile-150x150.png')
    )

    return html



# from django import template

# register = template.Library()

# @register.simple_tag
# def favicon_links():
#     return """
#     <link rel="icon" href="{% static 'favicon_manager/images/favicon.ico' %}" type="image/x-icon">
#     <link rel="icon" sizes="16x16" href="{% static 'favicon_manager/images/favicon-16x16.png' %}" type="image/png">
#     <link rel="icon" sizes="32x32" href="{% static 'favicon_manager/images/favicon-32x32.png' %}" type="image/png">
#     """
