import anyio
import typer
from loguru import logger
from returns import pointfree as p
from returns.io import IOFailure, IOResultE, IOSuccess
from returns.pipeline import flow
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
    flow(
        example_transform_service(text),
        p.map_(lambda s: console.print(f"[bold green]Success:[/] {s}")),
        p.alt(lambda s: console.print(f"[bold red]Error:[/] {s}")),
    )


@app.command()
def get_user(user_id: int) -> None:
    """
    Retrieves and displays user information by ID.
    """
    logger.info(f"CLI command 'get-user' called for user_id: {user_id}")
    user_fetcher: InMemoryUserFetcher = InMemoryUserFetcher()

    result: IOResultE[User] = anyio.run(
        get_user_details(user_fetcher, user_id).awaitable
    )
    match result:
        case IOSuccess(user):
            table: Table = Table("Attribute", "Value")
            table.add_row("ID", str(user.id))
            table.add_row("Name", user.name)
            table.add_row("Age", str(user.age))
            console.print(table)
        case IOFailure(error):
            console.print(f"[bold red]Error:[/] {error}")
        case _:  # pragma: no cover
            console.print(f"[bold red]Error:[/] {result}")
            IOFailure(f"This should never happen: {result}")


def main() -> None:  # pragma: no cover
    setup_logging()
    app()


if __name__ == "__main__":  # pragma: no cover
    main()
