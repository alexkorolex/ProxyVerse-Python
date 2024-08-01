"""Module generate list"""

from typing import TypedDict, Literal, Optional
from proxyverse.enums.countries import CountriesCodes

Protocols = Literal["http", "ssl"]
Types = Literal["sticky", "rotating"]
Servers = Literal["us", "eu", "as", "nearest"]


class GenerateListProxyDict(TypedDict, total=False):
    """Class for generating a list of body"""

    protocol: Protocols
    type: Types
    period: int
    server: Servers
    amount: int
    country: CountriesCodes
    region: Optional[str]
    user_id: Optional[str]


class ProxiesDict(TypedDict):
    """Class for read dictionary proxies"""

    http: str
    https: str
    username: str
    password: str
