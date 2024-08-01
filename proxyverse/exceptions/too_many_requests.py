"""Module exceptions of too many requests"""

from proxyverse.exceptions.http_exception import HTTPException


class TooManyRequestsException(HTTPException):
    """Class of representing a failed request of too many requests"""

    def __init__(self, message: str, details: str = "") -> None:
        super().__init__(message, status_code=429, details=details)
