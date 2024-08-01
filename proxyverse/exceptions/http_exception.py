"""Module of the base class for exceptions"""


class HTTPException(Exception):
    """Base class for all HTTP-related exceptions."""

    def __init__(self, message: str, status_code: int, details: str = "") -> None:
        super().__init__(message)
        self.status_code = status_code
        self.details = details

    def __str__(self) -> str:
        return f"{self.status_code} - {self.args[0]}: {self.details}"
