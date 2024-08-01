"""Module of the forbidden exceptions"""

from proxyverse.exceptions.http_exception import HTTPException


class ForbiddenException(HTTPException):
    """Class ForbiddenException"""

    def __init__(self, message: str, details: str = "") -> None:
        super().__init__(message, status_code=403, details=details)
