"""Module of base class for creating API requests"""

import json
from typing import NoReturn, Literal, Union, TypeVar, Dict, List
from httpx import Response, AsyncClient
from proxyverse.enums import (
    GenerateListProxyDict,
    ApiKeyResetDict,
    BindIpDict,
    AddUserDataDict,
    UserDataIdDict,
)
from proxyverse.enums.generate_list import (
    Protocols,
    Types,
    CountriesCodes,
    Servers,
)
from proxyverse.exceptions import (
    BadRequestException,
    ForbiddenException,
    ProxyAuthRequiredException,
    GoneException,
    TooManyRequestsException,
    GatewayTimeoutException,
    InternalServerError,
    HTTPException,
)


TypeRequest = Literal["GET", "POST"]
T = TypeVar("T", bound=Union[Dict, List[Dict], None])


class BaseAPIProxyVerse:
    """Class of Base configurations proxyverse API"""

    def __init__(self, API_KEY) -> NoReturn:  # type: ignore
        self.headers: dict = {"X-API-Key": API_KEY}

    async def _create_request(
        self,
        url: str,
        type_request: TypeRequest,
        content: Union[
            GenerateListProxyDict,
            ApiKeyResetDict,
            BindIpDict,
            UserDataIdDict,
            dict,
            None,
        ] = None,
    ) -> T:
        async with AsyncClient() as client:
            if type_request == "POST":
                response: Response = await client.post(
                    url=url,
                    headers=self.headers,
                    json=content,
                )
            else:
                response = await client.get(url=url, headers=self.headers)

            if response.status_code == 200:
                data: T = json.loads(response.text)
                return data
            else:
                await self.__error_handling(response)
                return None

    @staticmethod
    async def _bind_ip_handle(user_id: str | None, addr: str) -> BindIpDict:
        if user_id:
            content = BindIpDict(user_id=user_id, addr=addr)
        else:
            content = BindIpDict(addr=addr)
        return content

    @staticmethod
    async def _handle_user_id(user_id: str | None) -> dict:
        if user_id:
            content = {"user_id": user_id}
        else:
            content = {}
        return content

    @staticmethod
    async def _handle_add_user_data(
        user_id: str | None, data_string: str, expires_at: int, data: int = 0
    ) -> AddUserDataDict:
        if user_id:
            content = AddUserDataDict(
                user_id=user_id,
                data=data,
                data_string=data_string,
                expires_at=expires_at,
            )
        else:
            content = AddUserDataDict(
                data=data, data_string=data_string, expires_at=expires_at
            )
        return content

    @staticmethod
    async def _handle_proxy_list(
        protocol: Protocols,
        types: Types,
        period: int,
        server: Servers,
        amount: int,
        country: CountriesCodes,
        region: str | None,
        user_id: str | None,
    ) -> GenerateListProxyDict:
        content = GenerateListProxyDict(
            protocol=protocol,
            type=types,
            period=period,
            amount=amount,
            country=country,
            server=server,
        )
        if user_id:
            content["user_id"] = user_id
        if region:
            content["region"] = region
        return content

    async def __error_handling(self, response: Response) -> None:
        status_code = str(response.status_code)
        if status_code.startswith("4"):
            if status_code.startswith("40"):
                if status_code == "400":
                    raise BadRequestException("Bad request", response.text)
                elif status_code == "403":
                    raise ForbiddenException("Forbidden", response.text)
                elif status_code == "407":
                    raise ProxyAuthRequiredException("ProxyAuthRequired", response.text)
            else:
                if status_code == "410":
                    raise GoneException("Gone Exception", response.text)
                elif status_code == "429":
                    raise TooManyRequestsException(
                        "TooManyRequests Exception", response.text
                    )
        if status_code.startswith("5"):
            if status_code == "500":
                raise InternalServerError("Internal Server Error", response.text)
            elif status_code == "504":
                raise GatewayTimeoutException(
                    "Gateway Timeout Exception", response.text
                )
        raise HTTPException(
            message=response.text,
            status_code=response.status_code,
            details=response.text,
        )
