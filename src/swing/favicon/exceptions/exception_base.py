# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Base Exception Class
====================

Base exception class for all favicon-related errors. Supports string
formatting with positional and keyword arguments, and serialization
to dict or JSON format.

"""

# Import | Standard Library
import json as _json
from typing import Any


class FaviconsError(Exception):
    """
    Base exception class for all favicon-related errors.

    This exception supports string formatting with positional and keyword
    arguments, and can be serialized to dict or JSON format.

    Args:
        message: Error message template with optional format placeholders.
        *args: Positional arguments for message formatting.
        **kwargs: Keyword arguments for message formatting.

    Example:
        raise FaviconsError("File {path} not found", path="/favicon.ico")

    """

    def __init__(self, message: str, *args: Any, **kwargs: Any):
        """
        Initialize the exception with a message template.

        Args:
            message: Error message template with {} placeholders.
            *args: Positional arguments for str.format().
            **kwargs: Keyword arguments for str.format().
        """
        self._message = message
        self._args = args
        self._kwargs = kwargs

    @property
    def message(self) -> str:
        """
        Get the formatted error message.

        Returns:
            The message with all placeholders replaced.
        """
        return self._message.format(*self._args, **self._kwargs)

    @property
    def kwargs(self) -> dict:
        """
        Get keyword arguments as a dictionary.

        Returns:
            Copy of the keyword arguments.
        """
        return dict(self._kwargs)

    def __repr__(self) -> str:
        """
        Get detailed string representation of the exception.

        Returns:
            String with class name and all arguments.
        """
        attrs = (
            f"message='{self.message}'",
            *(repr(a) for a in self.args),
            *(f"{k}={repr(v)}" for k, v in self.kwargs.items()),
        )

        return f"{self.__class__.__name__}({', '.join(attrs)})"

    def __str__(self) -> str:
        """
        Get the formatted error message.

        Returns:
            The formatted error message string.
        """
        return self.message

    def dict(self) -> dict:
        """
        Serialize exception to a dictionary.

        Returns:
            Dictionary with message, arguments, and keyword_arguments.
        """
        return {
            "message": self.message,
            "arguments": list(self.args),
            "keyword_arguments": self.kwargs,
        }

    def json(self) -> str:
        """
        Serialize exception to a JSON string.

        Returns:
            JSON representation of the exception.
        """
        return _json.dumps(self.dict())
