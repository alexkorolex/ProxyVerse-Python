"""Module of exception bad request exception"""

from proxyverse.exceptions.http_exception import HTTPException


class BadRequestException(HTTPException):
    """Exception raised for HTTP 400 Bad Request errors."""

    def __init__(self, message: str, details: str = "") -> None:
        super().__init__(message, status_code=400, details=details)
