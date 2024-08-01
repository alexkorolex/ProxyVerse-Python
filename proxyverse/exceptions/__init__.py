"""Module of the exceptions"""

from proxyverse.exceptions.http_exception import HTTPException
from proxyverse.exceptions.internal_server_error import InternalServerError
from proxyverse.exceptions.bad_request import BadRequestException
from proxyverse.exceptions.forbidden import ForbiddenException
from proxyverse.exceptions.gateway_timeout import GatewayTimeoutException
from proxyverse.exceptions.gone import GoneException
from proxyverse.exceptions.proxy_auth_required import ProxyAuthRequiredException
from proxyverse.exceptions.too_many_requests import TooManyRequestsException


__all__ = [
    "ProxyAuthRequiredException",
    "TooManyRequestsException",
    "GoneException",
    "GatewayTimeoutException",
    "ForbiddenException",
    "BadRequestException",
    "InternalServerError",
    "HTTPException",
]
