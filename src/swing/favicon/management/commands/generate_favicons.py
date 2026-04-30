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

# Import | Standard Library
from pathlib import Path
from typing import Any

from django.conf import settings
from django.core.management.base import (
    BaseCommand,
    CommandError,
    CommandParser,
)

# Import | Local
from ...conf import FAVICON_APPLE_SIZES, FAVICON_SIZES
from ...utils.util_generate_favicons import FaviconGenerator


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

    def _validate_source(self, source: str) -> Path:
        """Validate source file exists and is a file."""
        source_path = Path(source)
        if not source_path.exists():
            raise CommandError(f"Source file not found: {source_path}")
        if not source_path.is_file():
            raise CommandError(f"Source path is not a file: {source_path}")
        return source_path

    def _get_output_dir(self, output: str) -> Path:
        """Get output directory path."""
        if output:
            return Path(output)
        return Path(settings.BASE_DIR) / "static" / "favicon"

    def _parse_sizes(self, sizes_str: str) -> list[int]:
        """Parse comma-separated sizes string."""
        if not sizes_str:
            return FAVICON_SIZES
        try:
            return [int(s.strip()) for s in sizes_str.split(",")]
        except ValueError as err:
            raise CommandError(f"Invalid sizes format: {err}") from err

    def _parse_formats(self, formats_str: str) -> list[str]:
        """Parse and validate formats string."""
        formats = formats_str.lower().split(",")
        valid_formats = {"png", "ico", "apple", "ms", "all"}
        for fmt in formats:
            if fmt.strip() not in valid_formats:
                raise CommandError(
                    f"Invalid format '{fmt}'. Valid: {', '.join(valid_formats)}"
                )
        return formats

    def _run_generation(
        self, generator: FaviconGenerator, formats: list[str], sizes: list[int]
    ) -> None:
        """Run the actual favicon generation."""
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

    def handle(self, *args: Any, **options: Any) -> None:
        """Execute the command."""
        source_path = self._validate_source(options["source"])
        output_dir = self._get_output_dir(options["output"])
        sizes = self._parse_sizes(options["sizes"])
        formats = self._parse_formats(options["formats"])

        # Dry run mode
        if options["dry_run"]:
            self._handle_dry_run(source_path, output_dir, formats, sizes)
            return

        # Create output directory
        if not output_dir.exists():
            output_dir.mkdir(parents=True)
            self.stdout.write(f"Created output directory: {output_dir}")

        # Check for existing files
        if not options["force"]:
            self._check_existing_files(output_dir)

        # Generate favicons
        self._generate_favicons(source_path, output_dir, formats, sizes)

    def _handle_dry_run(
        self, source_path: Path, output_dir: Path, formats: list[str], sizes: list[int]
    ) -> None:
        """Handle dry run mode output."""
        self.stdout.write(self.style.NOTICE("Dry run mode - no files will be created"))
        self.stdout.write(f"Source: {source_path}")
        self.stdout.write(f"Output: {output_dir}")
        self.stdout.write(f"Formats: {', '.join(formats)}")
        self.stdout.write(f"Sizes: {', '.join(map(str, sizes))}")
        self._show_planned_files(formats, sizes)

    def _check_existing_files(self, output_dir: Path) -> None:
        """Check and warn about existing files."""
        existing = list(output_dir.glob("favicon*"))
        if existing:
            self.stdout.write(
                self.style.WARNING(
                    f"Found {len(existing)} existing favicon files. "
                    "Use --force to overwrite."
                )
            )

    def _generate_favicons(
        self, source_path: Path, output_dir: Path, formats: list[str], sizes: list[int]
    ) -> None:
        """Generate favicon files."""
        self.stdout.write(f"Generating favicons from {source_path}...")

        try:
            generator = FaviconGenerator(str(source_path), str(output_dir))
            generator.sizes = sizes
            self._run_generation(generator, formats, sizes)

            self.stdout.write(
                self.style.SUCCESS(f"Successfully generated favicons in {output_dir}")
            )
            self._list_generated_files(output_dir)

        except Exception as err:
            raise CommandError(f"Error generating favicons: {err}") from err

    def _list_generated_files(self, output_dir: Path) -> None:
        """List generated files with sizes."""
        generated = list(output_dir.glob("*"))
        self.stdout.write(f"Generated {len(generated)} files:")
        for file_path in sorted(generated):
            size = file_path.stat().st_size
            self.stdout.write(f"  - {file_path.name} ({size:,} bytes)")

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
