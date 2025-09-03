import uvicorn
from fastapi import FastAPI, HTTPException
from loguru import logger
from returns.result import Failure, Success

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


app = FastAPI()
user_fetcher = InMemoryUserFetcher()  # Instance is created here


@app.on_event("startup")
def startup_event():
    setup_logging()
    logger.info("FastAPI application starting up...")


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    """
    API endpoint to retrieve a user by their ID.
    It uses the core service function to fetch the data.
    """
    # The concrete instance is passed to the service function here
    result = await get_user_details(user_fetcher, user_id)

    match result:
        case Success(user):
            return user
        case Failure(error_message):
            raise HTTPException(status_code=404, detail=error_message)


@app.get("/transform/")
async def transform_text(text: str):
    """API endpoint to demonstrate a simple transformation service."""
    result = example_transform_service(text)
    match result:
        case Success(transformed_text):
            return {"original": text, "transformed": transformed_text}
        case Failure(error):
            raise HTTPException(status_code=400, detail=str(error))


def main():
    """Main function to run the FastAPI application."""
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
