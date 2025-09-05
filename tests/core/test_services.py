import pytest
from hypothesis import given
from hypothesis import strategies as st
from returns.result import Failure, Success

from src.core import services
from src.core.models import User
from src.core.protocols import Fetcher


# --- Technique 1: Unit-Testing ---
def test_simple_pipeline_logic():
    """A simple unit test for a deterministic function."""
    result = services.example_transform_service("  Test  ")
    # `returns` provides helpers to safely extract the content
    assert result.unwrap() == "transformed: test"


# --- Technique 3: Mocking with Protocols ---
class MockUserFetcher(Fetcher[int, User]):
    """A test double that satisfies the Fetcher protocol."""

    def __init__(self, user_to_return: User | None):
        self._user = user_to_return

    async def fetch_by_id(self, key: int) -> User | None:  # noqa: ARG002
        return self._user


@pytest.mark.asyncio
async def test_get_user_details_success_with_mock():
    """Tests the success path of get_user_details with a mock."""
    mock_fetcher = MockUserFetcher(User(id=1, name="Mocked User", age=30))
    result = await services.get_user_details(mock_fetcher, 1)

    assert isinstance(result, Success)
    assert result.unwrap().name == "Mocked User"


@pytest.mark.asyncio
async def test_get_user_details_not_found_with_mock():
    """Tests the failure path (user not found) with a mock."""
    mock_fetcher = MockUserFetcher(user_to_return=None)
    result = await services.get_user_details(mock_fetcher, 999)

    assert isinstance(result, Failure)
    assert "not found" in str(result.failure())


# --- Technique 2: Property-Based Testing ---
@given(st.text().filter(lambda s: s != "error"))
def test_example_transform_service_properties(s: str):
    """
    Tests properties of the transformation function.
    Hypothesis generates hundreds of different strings.
    """
    result = services.example_transform_service(s)
    # Property 1: The output should always be a Success object for any string.
    assert isinstance(result, Success)
    # Property 2: The output should always start with "transformed:".
    assert result.unwrap().startswith("transformed:")
    # Property 3: The transformed text should not have leading/trailing whitespace.
    assert result.unwrap().replace(
        "transformed: ", ""
    ).strip() == result.unwrap().replace("transformed: ", "")


def test_example_transform_service_failure():
    """
    Tests the failure path of the transformation function with non-string input.
    """
    result = services.example_transform_service("error")
    assert isinstance(result, Failure)
    assert isinstance(result.failure(), ValueError)
