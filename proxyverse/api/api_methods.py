"""Module for union class methods of ProxyVerse"""

from proxyverse.api.get_api import GetRequestProxyVerse
from proxyverse.api.post_api import PostRequestProxyVerse


class ApiProxyVerse:
    """Class of proxyverse API endpoints"""

    def __init__(self, api_key: str) -> None:
        self.post_request_verse: PostRequestProxyVerse = PostRequestProxyVerse(api_key)
        self.get_request_verse: GetRequestProxyVerse = GetRequestProxyVerse(api_key)
