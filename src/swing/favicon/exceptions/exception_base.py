# -*- coding: utf-8 -*-
"""Base exception class for favicons."""

# Import | Standard Library
import json as _json
from typing import Any, Dict


class FaviconsError(Exception):
    """Raise an error while running favicons."""

    def __init__(self, message: str, *args: Any, **kwargs: Any):
        """Favicons Base Exception."""
        self._message = message
        self._args = args
        self._kwargs = kwargs

    @property
    def message(self) -> str:
        """Format message with args & kwargs."""
        return self._message.format(*self._args, **self._kwargs)

    @property
    def kwargs(self) -> Dict:
        """Keyword arguments as a dict."""
        return dict(self._kwargs)

    def __repr__(self) -> str:
        """Representation of exception."""
        attrs = (
            f"message='{self.message}'",
            *(repr(a) for a in self.args),
            *(f"{k}={repr(v)}" for k, v in self.kwargs.items()),
        )

        return f"{self.__class__.__name__}({', '.join(attrs)})"

    def __str__(self) -> str:
        """Represent exception as string."""
        return self.message

    def dict(self) -> Dict:
        """Represent exception as dict."""
        return {
            "message": self.message,
            "arguments": list(self.args),
            "keyword_arguments": self.kwargs,
        }

    def json(self) -> str:
        """Represent exception as JSON string."""
        return _json.dumps(self.dict())
