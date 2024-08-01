"""Module of the proxy auth reuired exceptions"""

from proxyverse.exceptions.http_exception import HTTPException


class ProxyAuthRequiredException(HTTPException):
    """Class representing of proxy authentication"""

    def __init__(self, message: str, details: str = "") -> None:
        super().__init__(message, status_code=407, details=details)
