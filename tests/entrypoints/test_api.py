import pytest
from httpx import AsyncClient

from src.entrypoints.api import app


@pytest.fixture(scope="module")
async def test_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_read_user_success(test_client: AsyncClient):
    """Tests successful user retrieval."""
    response = await test_client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Alice"


@pytest.mark.asyncio
async def test_read_user_not_found(test_client: AsyncClient):
    """Tests the case where a user is not found."""
    response = await test_client.get("/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User with ID 999 not found."}


@pytest.mark.asyncio
async def test_transform_text_success(test_client: AsyncClient):
    """Tests the transformation endpoint."""
    response = await test_client.get("/transform/?text=  Hello World  ")
    assert response.status_code == 200
    assert response.json() == {
        "original": "  Hello World  ",
        "transformed": "transformed: hello world",
    }


@pytest.mark.asyncio
async def test_transform_text_error(test_client: AsyncClient):
    """Tests the transformation endpoint."""
    response = await test_client.get("/transform/?text=error")
    assert response.status_code == 400
    assert response.json() == {"detail": "error"}
