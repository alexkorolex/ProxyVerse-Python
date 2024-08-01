"""Module of gone exception"""

from proxyverse.exceptions.http_exception import HTTPException


class GoneException(HTTPException):
    """Class of HTTP exceptions Gone"""

    def __init__(self, message: str, details: str = "") -> None:
        super().__init__(message, status_code=410, details=details)
