"""Module of schemas"""

from proxyverse.enums.api_key import ApiKeyResetDict, ApiKeyDict
from proxyverse.enums.countries import CountryDict
from proxyverse.enums.generate_list import GenerateListProxyDict, ProxiesDict
from proxyverse.enums.users import (
    CountUsersDict,
    UserDict,
    BindIpDict,
    AddUserDataDict,
    UserDataIdDict,
)

__all__ = [
    "GenerateListProxyDict",
    "ProxiesDict",
    "CountryDict",
    "ApiKeyResetDict",
    "ApiKeyDict",
    "CountUsersDict",
    "UserDict",
    "BindIpDict",
    "AddUserDataDict",
    "UserDataIdDict",
]
