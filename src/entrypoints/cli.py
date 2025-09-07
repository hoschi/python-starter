import asyncio

import typer
from loguru import logger
from returns.result import Failure, Result, Success
from rich.console import Console
from rich.table import Table

from src.core.logging_config import setup_logging
from src.core.models import User
from src.core.services import example_transform_service, get_user_details
from src.entrypoints.api import InMemoryUserFetcher  # Reusing the same fetcher for demo

app: typer.Typer = typer.Typer()
console: Console = Console()


@app.command()
def transform(text: str) -> None:
    """
    Transforms a given text using the core service function.
    """
    logger.info(f"CLI command 'transform' called with text: '{text}'")
    result: Result[str, ValueError] = example_transform_service(text)
    result.map(lambda s: console.print(f"[bold green]Success:[/] {s}")).alt(
        lambda s: console.print(f"[bold red]Error:[/] {s}")
    )


@app.command()
def get_user(user_id: int) -> None:
    """
    Retrieves and displays user information by ID.
    """
    logger.info(f"CLI command 'get-user' called for user_id: {user_id}")
    user_fetcher: InMemoryUserFetcher = InMemoryUserFetcher()

    async def _get_user() -> Result[User, str]:
        return await get_user_details(user_fetcher, user_id)

    result: Result[User, str] = asyncio.run(_get_user())

    match result:
        case Success(user):
            table: Table = Table("Attribute", "Value")
            table.add_row("ID", str(user.id))
            table.add_row("Name", user.name)
            table.add_row("Age", str(user.age))
            console.print(table)
        case Failure(error):
            console.print(f"[bold red]Error:[/] {error}")
        case _:  # pragma: no cover
            console.print(f"[bold red]Error:[/] {result}")
            Failure(f"This should never happen: {result}")


def main() -> None:  # pragma: no cover
    setup_logging()
    app()


if __name__ == "__main__":  # pragma: no cover
    main()
