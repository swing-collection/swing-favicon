# -*- coding: utf-8 -*-


# Docstring
# =============================================================================

"""
Favicon Models
==============

Django models for storing favicon data in the database.

Exported Models:
    FaviconModel: Model for storing uploaded favicon images and metadata.

Example:
    from swing.favicon.models import FaviconModel

    favicon = FaviconModel.objects.create(
        name="Site Favicon",
        source_image=uploaded_file,
    )
    favicon.generate_all_sizes()

"""


# Imports
# =============================================================================

# Import | Local
from .model_favicon import FaviconModel

__all__ = ["FaviconModel"]
