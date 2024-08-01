
```markdown
# Proxyverse

Proxyverse is a Python package for interacting with the Proxyverse API. It provides methods for making GET and POST requests to retrieve information about countries and generate proxy lists.

## Installation

You can install the package via PyPI using pip:

```bash
pip install proxyverse
```

## Usage

### Importing the Package

```python
from proxyverse import ApiProxyVerse
```

### Example Usage

#### Creating an Instance

To use the package, you need to create an instance of `ApiProxyVerse` with your API key:

```python
api_key = "your_api_key_here"
proxy_verse = ApiProxyVerse(api_key)
```

#### Getting the List of Countries

You can get a list of countries with the following method:

```python
import asyncio

async def get_countries():
    countries = await proxy_verse.get_request_verse.get_countries()
    print(countries)

asyncio.run(get_countries())
```

#### Generating a List of Proxies

To generate a list of proxies, use the `generate_list_proxies` method. Here’s an example:

```python
async def generate_proxies():
    proxies = await proxy_verse.post_request_verse.generate_list_proxies(
        protocol="http",
        types="sticky",
        period=10,
        server="us",
        amount=5,
        country="US",
        region=None,
        user_id=None
    )
    print(proxies)

asyncio.run(generate_proxies())
```

## API Reference

### `ApiProxyVerse`

#### `__init__(API_KEY: str)`

Constructor for `ApiProxyVerse`.

- **API_KEY**: Your API key for accessing the Proxyverse API.

#### `async get_countries() -> List[Dict]`

Gets a list of countries from the Proxyverse API.

- **Returns**: A list of dictionaries representing countries.

#### `async generate_list_proxies(
    protocol: str,
    types: str,
    period: int,
    server: str,
    amount: int,
    country: str,
    region: Optional[str] = None,
    user_id: Optional[str] = None
) -> List[Dict]`

Generates a list of proxies with specified parameters.

- **protocol**: Protocol type (e.g., "http" or "ssl").
- **types**: Proxy type (e.g., "sticky" or "rotating").
- **period**: Session period, only applicable to "sticky" proxies (10 or 30).
- **server**: Server location (e.g., "nearest", "us", "eu", "as").
- **amount**: Number of proxies to generate.
- **country**: Abbreviated country code.
- **region**: Optional region for the proxy.
- **user_id**: Optional user ID for generating a proxy for a specific account.

- **Returns**: A list of dictionaries representing proxies.


## Contact

For questions or support, please contact [alexkorolex](https://github.com/alexkorolex).
