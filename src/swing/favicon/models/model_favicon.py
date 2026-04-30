# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Provides Favicon Model Class
============================

Model for storing and managing favicon source images with auto-generation
support for multiple sizes and formats.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Standard Library
from pathlib import Path

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Import | Local Modules


# =============================================================================
# Classes
# =============================================================================


class FaviconModel(models.Model):
    """
    Favicon model for storing favicon source images.

    This model stores the source image from which all favicon variants
    are generated. It supports auto-generation of multiple sizes and formats.

    Attributes:
        image: The source image file.
        name: Optional identifier for multiple favicon sets.
        is_active: Whether this favicon set is currently active.
        created_at: Timestamp when the record was created.
        updated_at: Timestamp when the record was last updated.
    """

    image = models.ImageField(
        upload_to="favicons/source/",
        verbose_name=_("Source Image"),
        help_text=_("Upload a square PNG or SVG image, minimum 512x512 pixels."),
    )
    name = models.CharField(
        max_length=100,
        blank=True,
        default="",
        verbose_name=_("Name"),
        help_text=_("Optional identifier for this favicon set."),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
        help_text=_("Whether this favicon set is currently in use."),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated"),
    )

    class Meta:
        """Meta options for FaviconModel."""

        verbose_name = _("Favicon")
        verbose_name_plural = _("Favicons")
        ordering = ["-updated_at"]

    def __str__(self) -> str:
        """Return string representation."""
        if self.name:
            return f"Favicon: {self.name}"
        return f"Favicon #{self.pk}" if self.pk else "Favicon (unsaved)"

    def get_output_directory(self) -> Path:
        """
        Get the output directory for generated favicon variants.

        Returns:
            Path to the output directory within MEDIA_ROOT.
        """
        output_dir = Path(settings.MEDIA_ROOT) / "favicons" / "generated"
        if self.pk:
            output_dir = output_dir / str(self.pk)
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir

    def get_generated_files(self) -> list[Path]:
        """
        Get list of generated favicon files.

        Returns:
            List of paths to generated favicon files.
        """
        output_dir = self.get_output_directory()
        if not output_dir.exists():
            return []
        return list(output_dir.glob("*"))

    def delete_generated_files(self) -> int:
        """
        Delete all generated favicon files.

        Returns:
            Number of files deleted.
        """
        files = self.get_generated_files()
        for file_path in files:
            try:
                file_path.unlink()
            except OSError:
                pass
        return len(files)


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "FaviconModel",
]
