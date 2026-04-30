# -*- coding: utf-8 -*-
"""Demo views for swing-favicon."""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    """Render the demo home page."""
    return render(request, "home.html")
