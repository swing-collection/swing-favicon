# -*- coding: utf-8 -*-
"""
Favicon Admin Configuration
===========================

Django admin interface for managing favicon images.
"""

from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import FaviconModel
from .conf import FAVICON_AUTO_GENERATE


@admin.register(FaviconModel)
class FaviconAdmin(admin.ModelAdmin):
    """Admin interface for FaviconModel."""

    list_display = ["__str__", "image_preview", "image_dimensions", "updated_at"]
    readonly_fields = ["image_preview_large", "image_dimensions", "created_at", "updated_at"]
    fieldsets = [
        (None, {"fields": ["image"]}),
        (
            _("Preview"),
            {
                "fields": ["image_preview_large", "image_dimensions"],
                "classes": ["collapse"],
            },
        ),
        (
            _("Metadata"),
            {
                "fields": ["created_at", "updated_at"],
                "classes": ["collapse"],
            },
        ),
    ]

    def image_preview(self, obj: FaviconModel) -> str:
        """Display small image preview in list view."""
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 32px; max-width: 32px;" />',
                obj.image.url,
            )
        return "-"

    image_preview.short_description = _("Preview")

    def image_preview_large(self, obj: FaviconModel) -> str:
        """Display large image preview in detail view."""
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 256px; max-width: 256px;" />',
                obj.image.url,
            )
        return "-"

    image_preview_large.short_description = _("Image Preview")

    def image_dimensions(self, obj: FaviconModel) -> str:
        """Display image dimensions."""
        if obj.image:
            try:
                return f"{obj.image.width} × {obj.image.height} px"
            except (AttributeError, FileNotFoundError):
                return "-"
        return "-"

    image_dimensions.short_description = _("Dimensions")

    def save_model(self, request, obj, form, change):
        """Save model and optionally generate favicon variants."""
        super().save_model(request, obj, form, change)

        if FAVICON_AUTO_GENERATE and obj.image:
            # Import here to avoid circular imports
            from .utils.util_generate_favicons import FaviconGenerator

            try:
                generator = FaviconGenerator(
                    obj.image.path,
                    output_dir=obj.get_output_directory(),
                )
                generator.generate_icons()
                self.message_user(
                    request,
                    _("Favicon variants generated successfully."),
                )
            except (IOError, OSError) as err:
                self.message_user(
                    request,
                    _("Error generating favicon variants: %s") % err,
                    level="ERROR",
                )
