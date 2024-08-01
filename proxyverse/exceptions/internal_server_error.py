"""Module of the internal error handling"""

from proxyverse.exceptions.http_exception import HTTPException


class InternalServerError(HTTPException):
    """Class representing internal server error"""

    def __init__(self, message: str, details: str = "") -> None:
        super().__init__(message, status_code=500, details=details)
