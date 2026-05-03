# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Favicon Django Application Configuration
=========================================

This module contains the Django AppConfig for the swing.favicon application.
It registers the app with Django and configures app-specific settings.

Example:
    Add to INSTALLED_APPS in settings.py::

        INSTALLED_APPS = [
            ...
            'swing.favicon',
        ]

"""


# =============================================================================
# Imports
# =============================================================================

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

# =============================================================================
# Classes
# =============================================================================


class FaviconConfig(AppConfig):
    """
    Django application configuration for swing.favicon.

    This AppConfig registers the favicon app with Django's application
    registry and provides metadata such as the app name and label.

    Attributes:
        name: Full Python path to the application module.
        label: Short unique name for the application.
        verbose_name: Human-readable name for the application.
        default_auto_field: Default primary key field type.
    """

    # Full Python path to the application
    name = "swing.favicon"

    # Short name for the application
    label = "favicon"

    # Human-readable name for the application
    verbose_name = _("Website Favicon")

    # Filesystem path to the application directory,
    # path = "/usr/lib/pythonX.Y/dist-packages/django/contrib/admin"

    # default = True

    # The implicit primary key type to add to models within this app.
    default_auto_field = "django.db.models.BigAutoField"

    # def ready(self):
    #     """
    #     Apps Config Ready Function
    #     """

    # Implicitly connect signal handlers decorated with @receiver.
    # from .. import signals

    # Explicitly connect a signal handler.
    # request_finished.connect(signals.my_callback)
