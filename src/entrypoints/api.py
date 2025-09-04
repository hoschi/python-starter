from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException
from loguru import logger
from returns.result import Failure, Result, Success

from src.core.logging_config import setup_logging
from src.core.models import User
from src.core.services import example_transform_service, get_user_details


# This is a *concrete* implementation that satisfies the Fetcher protocol.
# Important: It does NOT need to inherit from `Fetcher`!
class InMemoryUserFetcher:
    """A concrete implementation of a user fetcher that uses an in-memory dictionary."""

    _users = {
        1: User(id=1, name="Alice", age=30),
        2: User(id=2, name="Bob", age=25),
    }

    async def fetch_by_id(self, key: int) -> User | None:
        logger.info(f"Fetching user {key} from in-memory store.")
        return self._users.get(key)


user_fetcher: InMemoryUserFetcher = InMemoryUserFetcher()  # Instance is created here


# Lifespan-Handler statt deprecated on_event
@asynccontextmanager
async def lifespan(_: object) -> AsyncGenerator[None, None]:
    setup_logging()
    logger.info("FastAPI application starting up...")
    yield


app: FastAPI = FastAPI(lifespan=lifespan)


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int) -> User:
    """
    API endpoint to retrieve a user by their ID.
    It uses the core service function to fetch the data.
    """
    result: Result[User, str] = await get_user_details(user_fetcher, user_id)
    match result:
        case Success(user):
            return user
        case Failure(error_message):
            raise HTTPException(status_code=404, detail=error_message)
        case _:
            # Fallback, falls Result nicht Success/Failure ist
            raise HTTPException(status_code=500, detail="Unbekannter Fehler")


@app.get("/transform/")
async def transform_text(text: str) -> dict[str, str]:
    """API endpoint to demonstrate a simple transformation service."""
    result = example_transform_service(text)
    match result:
        case Success(transformed_text):
            return {"original": text, "transformed": transformed_text}
        case Failure(error):
            raise HTTPException(status_code=400, detail=str(error))
        case _:
            raise HTTPException(status_code=500, detail="Unbekannter Fehler")


def main() -> None:
    """Main function to run the FastAPI application."""
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
