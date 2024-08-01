"""Module schemas of users"""

from typing import TypedDict, Optional


class CountUsersDict(TypedDict):
    """Class of count users dictionary"""

    count: int


class UserDict(TypedDict, total=False):
    """Class of user dictionary"""

    user_id: str
    data_left: int
    expires_at: int
    data_string: str
    whitelist: list[str]
    blacklist: list[str]
    created: str


class BindIpDict(TypedDict, total=False):
    """Class of dicionary request to bind IP address to user"""

    user_id: Optional[str]
    addr: str


class AddUserDataDict(TypedDict, total=False):
    """Class of dicionary request to add user data"""

    user_id: Optional[str]
    data: int
    data_string: str
    expires_at: int


class UserDataIdDict(TypedDict):
    """Dictionary user data id"""

    user_id: str
