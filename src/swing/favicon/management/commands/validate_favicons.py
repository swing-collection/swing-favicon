# -*- coding: utf-8 -*-
"""
Validate Favicons Management Command
=====================================

Django management command to validate that all required favicon files exist.

Usage:
    python manage.py validate_favicons
    python manage.py validate_favicons --path static/favicon
    python manage.py validate_favicons --strict

"""

from pathlib import Path
from typing import Any

from django.core.management.base import BaseCommand, CommandParser
from django.contrib.staticfiles import finders

from swing_favicon.conf import FAVICON_BASE_PATH


# Required favicon files for different compliance levels
REQUIRED_MINIMAL = [
    "favicon.ico",
]

REQUIRED_STANDARD = REQUIRED_MINIMAL + [
    "favicon-16x16.png",
    "favicon-32x32.png",
    "apple-touch-icon.png",
]

REQUIRED_FULL = REQUIRED_STANDARD + [
    "favicon-64x64.png",
    "favicon-96x96.png",
    "favicon-192x192.png",
    "android-chrome-192x192.png",
    "android-chrome-512x512.png",
    "apple-touch-icon-180x180.png",
    "mstile-150x150.png",
    "safari-pinned-tab.svg",
    "site.webmanifest",
    "browserconfig.xml",
]


class Command(BaseCommand):
    """Management command to validate favicon files exist."""

    help = "Validate that required favicon files exist"

    def add_arguments(self, parser: CommandParser) -> None:
        """Add command arguments."""
        parser.add_argument(
            "--path",
            "-p",
            type=str,
            default="",
            help=f"Path to favicon directory (default: {FAVICON_BASE_PATH})",
        )
        parser.add_argument(
            "--level",
            "-l",
            type=str,
            choices=["minimal", "standard", "full"],
            default="standard",
            help="Validation level: minimal, standard, full (default: standard)",
        )
        parser.add_argument(
            "--strict",
            action="store_true",
            help="Exit with error code if validation fails",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        """Execute the command."""
        base_path = options["path"] or FAVICON_BASE_PATH
        level = options["level"]

        # Select required files based on level
        required_files = {
            "minimal": REQUIRED_MINIMAL,
            "standard": REQUIRED_STANDARD,
            "full": REQUIRED_FULL,
        }[level]

        self.stdout.write(f"Validating favicons at '{base_path}' (level: {level})...")
        self.stdout.write("")

        found = []
        missing = []
        warnings = []

        for filename in required_files:
            search_path = f"{base_path}/{filename}"
            file_found = finders.find(search_path)

            if file_found:
                found.append(filename)
                file_size = Path(file_found).stat().st_size
                self.stdout.write(
                    self.style.SUCCESS(f"  ✓ {filename} ({file_size:,} bytes)")
                )

                # Check file size warnings
                if file_size > 100_000 and filename.endswith(".png"):
                    warnings.append(f"{filename} is larger than 100KB")
                elif file_size < 100 and filename.endswith((".png", ".ico")):
                    warnings.append(f"{filename} seems too small")
            else:
                missing.append(filename)
                self.stdout.write(self.style.ERROR(f"  ✗ {filename} (missing)"))

        # Summary
        self.stdout.write("")
        self.stdout.write(f"Found: {len(found)}/{len(required_files)} files")

        if warnings:
            self.stdout.write("")
            self.stdout.write(self.style.WARNING("Warnings:"))
            for warning in warnings:
                self.stdout.write(self.style.WARNING(f"  - {warning}"))

        if missing:
            self.stdout.write("")
            self.stdout.write(self.style.ERROR("Missing files:"))
            for filename in missing:
                self.stdout.write(self.style.ERROR(f"  - {filename}"))

            self.stdout.write("")
            self.stdout.write(
                "Generate missing files with: "
                f"python manage.py generate_favicons SOURCE_IMAGE -o static/{base_path}"
            )

            if options["strict"]:
                exit(1)
        else:
            self.stdout.write("")
            self.stdout.write(
                self.style.SUCCESS("All required favicon files are present!")
            )
