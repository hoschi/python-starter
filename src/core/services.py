from loguru import logger
from returns.result import Failure, Result, Success
from toolz import pipe

from src.core.models import User
from src.core.protocols import Fetcher


def example_transform_service(text: str) -> Result[str, Exception]:
    """
    An example of a pure function pipeline for data transformation.
    This function is easily testable and has no side effects.
    """
    logger.debug(f"Transforming text: '{text}'")
    try:
        transformed_text = pipe(
            text,
            lambda s: s.strip(),
            lambda s: s.lower(),
        )
        return Success(f"transformed: {transformed_text}")
    except Exception as e:
        logger.error(f"Transformation failed for text: '{text}' with error: {e}")
        return Failure(e)


# Richtig: Wir nutzen Dependency Inversion und programmieren gegen den abstrakten Fetcher-Protocol.
# Falsch wäre: eine konkrete Klasse wie `SupabaseFetcher` hier zu importieren,
# da dies unsere Kernlogik an eine externe Implementierung koppeln würde.
async def get_user_details(
    user_fetcher: Fetcher[int, User],  # Programming against the abstraction!
    user_id: int,
) -> Result[User, str]:
    """
    Fetches user details without knowing where they come from.
    """
    logger.info(f"Fetching details for user_id: {user_id}")
    maybe_user = await user_fetcher.fetch_by_id(user_id)
    if maybe_user is None:
        logger.warning(f"User with id {user_id} not found.")
        return Failure(f"User with ID {user_id} not found.")

    logger.success(f"Successfully fetched user: {maybe_user.name}")
    return Success(maybe_user)
