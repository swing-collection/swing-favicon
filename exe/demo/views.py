# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""Demo views for swing-favicon."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    """Render the demo home page."""
    return render(request, "home.html")
