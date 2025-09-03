from typing import Protocol, TypeVar

from src.core.models import User

# TypeVars for generic keys and return values
KeyType = TypeVar("KeyType")
ReturnType = TypeVar("ReturnType")


class Fetcher(Protocol[KeyType, ReturnType]):
    """
    A generic contract for any component that can fetch data by a key.
    This could be a DB client, an API client, or an in-memory cache.
    """

    async def fetch_by_id(
        self, key: KeyType
    ) -> (
        ReturnType | None
    ): ...  # The '...' is intentional; Protocols only define the signature.


# Example of a more specific protocol
class UserFetcher(Fetcher[int, User]):
    """A specific fetcher protocol for retrieving User objects by their integer ID."""

    ...
