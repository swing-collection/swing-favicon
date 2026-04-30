# -*- coding: utf-8 -*-
"""
Generate Favicons Management Command
=====================================

Django management command to generate favicon variants from a source image.

Usage:
    python manage.py generate_favicons source.png
    python manage.py generate_favicons source.png --output static/favicon
    python manage.py generate_favicons source.png --formats png,ico
    python manage.py generate_favicons source.png --sizes 16,32,64,128

"""

from pathlib import Path
from typing import Any

from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.conf import settings

from swing_favicon.utils.util_generate_favicons import FaviconGenerator
from swing_favicon.conf import FAVICON_SIZES, FAVICON_APPLE_SIZES


class Command(BaseCommand):
    """Management command to generate favicon variants from a source image."""

    help = "Generate favicon variants from a source image"

    def add_arguments(self, parser: CommandParser) -> None:
        """Add command arguments."""
        parser.add_argument(
            "source",
            type=str,
            help="Path to the source image (PNG or SVG recommended)",
        )
        parser.add_argument(
            "--output",
            "-o",
            type=str,
            default="",
            help="Output directory (default: static/favicon)",
        )
        parser.add_argument(
            "--formats",
            "-f",
            type=str,
            default="all",
            help="Comma-separated list of formats: png,ico,apple,ms,all (default: all)",
        )
        parser.add_argument(
            "--sizes",
            "-s",
            type=str,
            default="",
            help="Comma-separated list of sizes (default: from settings)",
        )
        parser.add_argument(
            "--force",
            action="store_true",
            help="Overwrite existing files",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Show what would be generated without creating files",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        """Execute the command."""
        source_path = Path(options["source"])

        # Validate source file
        if not source_path.exists():
            raise CommandError(f"Source file not found: {source_path}")

        if not source_path.is_file():
            raise CommandError(f"Source path is not a file: {source_path}")

        # Determine output directory
        if options["output"]:
            output_dir = Path(options["output"])
        else:
            output_dir = Path(settings.BASE_DIR) / "static" / "favicon"

        # Parse sizes
        if options["sizes"]:
            try:
                sizes = [int(s.strip()) for s in options["sizes"].split(",")]
            except ValueError as err:
                raise CommandError(f"Invalid sizes format: {err}") from err
        else:
            sizes = FAVICON_SIZES

        # Parse formats
        formats = options["formats"].lower().split(",")
        valid_formats = {"png", "ico", "apple", "ms", "all"}
        for fmt in formats:
            if fmt.strip() not in valid_formats:
                raise CommandError(
                    f"Invalid format '{fmt}'. Valid: {', '.join(valid_formats)}"
                )

        # Dry run mode
        if options["dry_run"]:
            self.stdout.write(self.style.NOTICE("Dry run mode - no files will be created"))
            self.stdout.write(f"Source: {source_path}")
            self.stdout.write(f"Output: {output_dir}")
            self.stdout.write(f"Formats: {', '.join(formats)}")
            self.stdout.write(f"Sizes: {', '.join(map(str, sizes))}")
            self._show_planned_files(formats, sizes)
            return

        # Create output directory
        if not output_dir.exists():
            output_dir.mkdir(parents=True)
            self.stdout.write(f"Created output directory: {output_dir}")

        # Check for existing files
        if not options["force"]:
            existing = list(output_dir.glob("favicon*"))
            if existing:
                self.stdout.write(
                    self.style.WARNING(
                        f"Found {len(existing)} existing favicon files. "
                        "Use --force to overwrite."
                    )
                )

        # Generate favicons
        self.stdout.write(f"Generating favicons from {source_path}...")

        try:
            generator = FaviconGenerator(str(source_path), str(output_dir))

            # Override sizes if specified
            if options["sizes"]:
                generator.sizes = sizes

            # Generate based on requested formats
            if "all" in formats or "png" in formats:
                self.stdout.write("  Generating PNG favicons...")
                generator.generate_png()

            if "all" in formats or "ico" in formats:
                self.stdout.write("  Generating ICO favicon...")
                generator.generate_ico()

            if "all" in formats or "apple" in formats:
                self.stdout.write("  Generating Apple touch icons...")
                generator.generate_apple_touch_icons()

            if "all" in formats or "ms" in formats:
                self.stdout.write("  Generating Microsoft tiles...")
                generator.generate_ms_tiles()

            self.stdout.write(
                self.style.SUCCESS(f"Successfully generated favicons in {output_dir}")
            )

            # List generated files
            generated = list(output_dir.glob("*"))
            self.stdout.write(f"Generated {len(generated)} files:")
            for file_path in sorted(generated):
                size = file_path.stat().st_size
                self.stdout.write(f"  - {file_path.name} ({size:,} bytes)")

        except Exception as err:
            raise CommandError(f"Error generating favicons: {err}") from err

    def _show_planned_files(self, formats: list[str], sizes: list[int]) -> None:
        """Show files that would be generated."""
        self.stdout.write("\nFiles that would be generated:")

        if "all" in formats or "png" in formats:
            for size in sizes:
                self.stdout.write(f"  - favicon-{size}x{size}.png")

        if "all" in formats or "ico" in formats:
            self.stdout.write("  - favicon.ico")

        if "all" in formats or "apple" in formats:
            for size in FAVICON_APPLE_SIZES:
                self.stdout.write(f"  - apple-touch-icon-{size}x{size}.png")

        if "all" in formats or "ms" in formats:
            self.stdout.write("  - mstile-70x70.png")
            self.stdout.write("  - mstile-150x150.png")
            self.stdout.write("  - mstile-310x150.png")
            self.stdout.write("  - mstile-310x310.png")
