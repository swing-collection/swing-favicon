# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Favicon Model Class
============================


"""


# =============================================================================
# Import
# =============================================================================

# Import | Standard Library
from typing import Any, Dict, List

# Import | Libraries
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Import | Local Modules
from services.projects.models.model_study import StudyModel
from core.base.models import BaseModel


# =============================================================================
# Variables
# =============================================================================

__all__ = ["FaviconModel", ]


# =============================================================================
# Classes
# =============================================================================

class FaviconModel(BaseModel):
    """
    Favicon Model Class
    ===================
    """

    image = models.ImageField(upload_to='favicons/')

    def __str__(self):
        """
        """
        return "Favicon"