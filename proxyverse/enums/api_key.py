"""Module of schema API KEY requests"""

from typing import TypedDict, Optional


class ApiKeyResetDict(TypedDict, total=False):
    """Class of API key requests"""

    user_id: Optional[str]


class ApiKeyDict(TypedDict):
    """Class of API key requests dictionary"""

    api_key: str
