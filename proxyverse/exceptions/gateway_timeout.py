"""Module of the gateway timeout"""

from proxyverse.exceptions.http_exception import HTTPException


class GatewayTimeoutException(HTTPException):
    """Class of gateway timeout"""

    def __init__(self, message: str, details: str = "") -> None:
        super().__init__(message, status_code=504, details=details)
