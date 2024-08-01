"""Module of schemas"""

from proxyverse.enums.api_key import ApiKeyReset, ApiKeyDict
from proxyverse.enums.countries import CountryDict
from proxyverse.enums.generate_list import GenerateListBody, DictBodyProxy
from proxyverse.enums.users import (
    CountUsersDict,
    UserDict,
    BindIPDictRequest,
    AddUserDataRequest,
    UserDataID,
)

__all__ = [
    "GenerateListBody",
    "DictBodyProxy",
    "CountryDict",
    "ApiKeyReset",
    "ApiKeyDict",
    "CountUsersDict",
    "UserDict",
    "BindIPDictRequest",
    "AddUserDataRequest",
    "UserDataID",
]
