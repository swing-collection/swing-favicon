# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Favicon Decorator Class
================================


"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Any, Dict, List

# Import | Libraries
from django.views.decorators.cache import cache_control


# Import | Local Modules
from services.projects.models.model_study import StudyModel
from core.base.models import BaseModel


# =============================================================================
# Variables
# =============================================================================

__all__ = ["serve_favicon", ]


# =============================================================================
# Classes
# =============================================================================

@cache_control(max_age=86400*365)  # Cache for 1 year
def serve_favicon(request, favicon_name):
    # ... your code to serve favicon
