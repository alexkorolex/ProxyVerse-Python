"""Module of POST requests of API"""

from proxyverse.enums import (
    GenerateListProxyDict,
    ProxiesDict,
    ApiKeyResetDict,
    ApiKeyDict,
    UserDict,
    BindIpDict,
    AddUserDataDict,
    UserDataIdDict,
)
from proxyverse.api.base_api import BaseAPIProxyVerse
from proxyverse.enums.generate_list import Protocols, Types, Servers, CountriesCodes


class PostRequestProxyVerse(BaseAPIProxyVerse):
    """Class PostRequestProxyVerse"""

    async def generate_list_proxies(
        self,
        protocol: Protocols,
        types: Types,
        period: int,
        server: Servers,
        amount: int,
        country: CountriesCodes,
        region: str | None,
        user_id: str | None,
    ) -> list[ProxiesDict]:
        """Method to generate list proxies

        Args:
            protocol (Protocols): http or ssl
            types (Types): sticky or rotating
            period (int): Can only be used in conjunction with sticky session. Available values 10 or 30
            server (Servers): nearest, us, eu or as. The server to which you will be connected. This param does not affect the outgoing IP.
            amount (int): The number of proxies received
            country (CountriesCodes): Abbreviated country code
            region (str | None): Region of proxy. Optional
            user_id (str | None): User id. Pass this value if you need to generate a proxy using a specified user account

        Returns:
            list[ProxiesDict]: List of dictionary proxies

        External:
            https://proxyverse.io/redoc/#operation/gateways_post

        """
        content: GenerateListProxyDict = await self._handle_proxy_list(
            protocol=protocol,
            types=types,
            period=period,
            server=server,
            amount=amount,
            country=country,
            region=region,
            user_id=user_id,
        )
        result: list[ProxiesDict] = await self._create_request(
            url="https://proxyverse.io/api/v1/gateways/generate",
            type_request="POST",
            content=content,
        )
        return result

    async def reset_api_key(self, user_id: str | None) -> ApiKeyDict:
        """Method to reset the API key

        Args:
            user_id (str | None): User id. If you are not reseller leave it blank

        Returns:
            ApiKeyDict: Class of API key requests dictionary

        Docs:
            https://proxyverse.io/redoc/#operation/user_reset_api_key

        """
        if user_id:
            content = ApiKeyResetDict(user_id=user_id)
        else:
            content = ApiKeyResetDict()  # type: ignore
        result: ApiKeyDict = await self._create_request(
            url="https://proxyverse.io/api/v1/user/api/reset",
            type_request="POST",
            content=content,
        )
        return result

    async def bind_ip_to_user(self, user_id: str | None, addr: str) -> UserDict:
        """Method to bind ip to the user

        Args:
            user_id (str | None): User id. Leave blank or don't send to use current account
            addr (str): Ip address

        Returns:
            UserDict: Class of user dictionary

        Docs:
            https://proxyverse.io/redoc/#operation/whitelist_bind
        """
        content: BindIpDict = await self._bind_ip_handle(
            user_id=user_id, addr=addr
        )
        result: UserDict = await self._create_request(
            url="https://proxyverse.io/api/v1/user/binds/bind",
            type_request="POST",
            content=content,
        )
        return result

    async def blacklist_domain(self, user_id: str | None, addr: str) -> UserDict:
        """Method to blacklist a domain. Only available to resellers. Block domain

        Args:
            user_id (int | None): user id. If you are not reseller leave it blank
            addr (str): https://example.com

        Returns:
            UserDict: Class of user dictionary

        Docs:
            https://proxyverse.io/redoc/#operation/blacklist_bind
        """
        content: BindIpDict = await self._bind_ip_handle(
            user_id=user_id, addr=addr
        )
        result: UserDict = await self._create_request(
            url="https://proxyverse.io/api/v1/user/binds/bl/bind",
            type_request="POST",
            content=content,
        )
        return result

    async def blacklist_remove_domain(self, user_id: str, addr: str) -> UserDict:
        """Method to remove a domain from blacklist of user. Only available to resellers. Removes blacklisted domain

        Args:
            user_id (str): User ID
            addr (str): https://example.com

        Returns:
            UserDict: Class of user dictionary

        Docs:
            https://proxyverse.io/redoc/#operation/blacklist_unbind
        """
        content: BindIpDict = await self._bind_ip_handle(
            user_id=user_id, addr=addr
        )
        result: UserDict = await self._create_request(
            url="https://proxyverse.io/api/v1/user/binds/bl/unbind",
            type_request="POST",
            content=content,
        )
        return result

    async def unbind_ip_from_user(self, user_id: str | None, addr: str) -> UserDict:
        """Unbind ip from user. Removes IP from binds

        Args:
            user_id (str | None): user id. Leave blank or don't send to use current account
            addr (str): ip. https://example.com

        Returns:
            UserDict: Class of user dictionary

        Docs:
            https://proxyverse.io/redoc/#operation/whitelist_unbind
        """
        content: BindIpDict = await self._bind_ip_handle(
            user_id=user_id, addr=addr
        )
        result: UserDict = await self._create_request(
            url="https://proxyverse.io/api/v1/user/binds/unbind",
            type_request="POST",
            content=content,
        )
        return result

    async def removes_all_ip_from_binds(self, user_id: str | None = None) -> UserDict:
        """Method to remove all IPs from binds. Removes all IP's from user binds

        Args:
            user_id (str | None, optional): user id. Leave blank or don't send to use current account. Defaults to None.

        Returns:
            UserDict: Class of user dictionary

        Docs:
            https://proxyverse.io/redoc/#operation/whitelist_unbind_all

        """
        content: dict = await self._handle_user_id(user_id=user_id)
        result: UserDict = await self._create_request(
            url="https://proxyverse.io/api/v1/user/binds/unbindall",
            type_request="POST",
            content=content,
        )
        return result

    async def create_user(self) -> UserDict:
        """Method to create a new user.
        Only available to resellers. Create user. Leave request body empty or pass empty json

        Returns:
            UserDict: Class of user dictionary

        Docs:
            https://proxyverse.io/redoc/#operation/user_create


        """
        result: UserDict = await self._create_request(
            url="https://proxyverse.io/api/v1/user/create",
            type_request="POST",
            content={},
        )
        return result

    async def add_user_data(
        self, user_id: str | None, data_string: str, expires_at: int, data: int = 0
    ) -> UserDict:
        """Method to add user data. Only available to resellers. Add data to User

        Args:
            user_id (str | None): user id. If you are not reseller leave it blank
            data_string (str): byte to subtract (optional)
            expires_at (int): amount of data to subtract, 64:B,128KB,423MB,22:GB,1TB (optional)
            data (int, optional): timestamp expiration date in future. Defaults to 0.

        Returns:
            UserDict: Class of user dictionary

        Docs:
            https://proxyverse.io/redoc/#operation/user_data_add

        """
        content: AddUserDataDict = await self._handle_add_user_data(
            user_id=user_id, data_string=data_string, expires_at=expires_at, data=data
        )
        result: UserDict = await self._create_request(
            url="https://proxyverse.io/api/v1/user/data/add",
            type_request="POST",
            content=content,
        )
        return result

    async def reset_sub_user(self, user_id: str | None) -> UserDict:
        """Method to reset the sub user. Only available to resellers. Reset Sub-user

        Args:
            user_id (str | None): user id. If you are not reseller leave it blank

        Returns:
            UserDict: Class of user dictionary

        Docs:
            https://proxyverse.io/redoc/#operation/user_data_reset

        """
        content: dict = await self._handle_user_id(user_id=user_id)
        result: UserDict = await self._create_request(
            url="https://proxyverse.io/api/v1/user/data/reset",
            type_request="POST",
            content=content,
        )
        return result

    async def subtract_user_data(
        self, user_id: str | None, data_string: str, expires_at: int, data: int = 0
    ) -> UserDict:
        """Only available to resellers. Subtract data from User. Either data or data_string must present

        Args:
            user_id (str | None): user id. If you are not reseller leave it blank
            data_string (str): byte to subtract (optional). Do not pass this value if you need just to update expires_at
            expires_at (int): amount of data to subtract, 64:B,128KB,423MB,22:GB,1TB (optional). Do not pass this value if you need just to update expires_at
            data (int, optional): timestamp expiration date in future. Use value -1 to remove expiration date. Defaults to 0.

        Returns:
            UserDict: Class of user dictionary

        Docs:
            https://proxyverse.io/redoc/#operation/user_data_subtract

        """
        content: AddUserDataDict = await self._handle_add_user_data(
            user_id=user_id, data_string=data_string, expires_at=expires_at, data=data
        )
        result: UserDict = await self._create_request(
            url="https://proxyverse.io/api/v1/user/data/subtract",
            type_request="POST",
            content=content,
        )
        return result

    async def delete_user(self, user_id: str) -> UserDataIdDict:
        """Method to delete a user

        Args:
            user_id (str): user id

        Returns:
            UserDataIdDict: Dictionary user data id

        Docs:
            https://proxyverse.io/redoc/#operation/user_delete

        """
        result: UserDataIdDict = await self._create_request(
            url="https://proxyverse.io/api/v1/user/delete",
            type_request="POST",
            content=UserDataIdDict(user_id=user_id),
        )
        return result

    async def user_info(self, user_id: str) -> UserDict:
        """Method to get user information. Only available to resellers. Get User information

        Args:
            user_id (str): user id

        Returns:
            UserDict: Class of user dictionary

        Docs:
            https://proxyverse.io/redoc/#operation/user_info

        """
        result: UserDict = await self._create_request(
            url="https://proxyverse.io/api/v1/user/info",
            type_request="POST",
            content=UserDataIdDict(user_id=user_id),
        )
        return result
