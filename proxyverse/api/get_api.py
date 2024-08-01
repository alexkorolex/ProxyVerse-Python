"""Module methods GET of API"""

from proxyverse.api.base_api import BaseAPIProxyVerse
from proxyverse.enums import CountryDict, CountUsersDict, UserDict


class GetRequestProxyVerse(BaseAPIProxyVerse):
    """Class of proxyverse get requests"""

    async def get_countries(self) -> list[CountryDict]:
        """Method to get list countries

        Returns:
            list[CountryDict]: List of country dictionaries

        Docs:
            https://proxyverse.io/redoc/#operation/country_list
        """
        result: list[CountryDict] = await self._create_request(
            url="https://proxyverse.io/api/v1/gateways/list",
            type_request="GET",
        )
        return result

    async def get_count_users(self) -> CountUsersDict:
        """Method to get count users

        Returns:
            CountUsersDict: Class of count users dictionary

        Docs:
            https://proxyverse.io/redoc/#operation/user_count

        """
        result: CountUsersDict = await self._create_request(
            url="https://proxyverse.io/api/v1/users/count",
            type_request="GET",
        )
        return result

    async def get_list_users(self) -> list[UserDict]:
        """Method to get list of users

        Returns:
            list[UserDict]: List of users dictionaries

        Docs:
            https://proxyverse.io/redoc/#operation/user_list
        """
        result: list[UserDict] = await self._create_request(
            url="https://proxyverse.io/api/v1/users/list", type_request="GET"
        )
        return result
