from typer.testing import CliRunner

from src.entrypoints.cli import app

runner = CliRunner()


def test_transform_command_success():
    """
    Tests the 'transform' CLI command with a sample string.
    """
    result = runner.invoke(app, ["transform", "  Some Text  "])
    assert result.exit_code == 0
    assert "Success:" in result.stdout
    assert "transformed: some text" in result.stdout


def test_get_user_command_success():
    """
    Tests the 'get-user' CLI command for a user that exists.
    """
    result = runner.invoke(app, ["get-user", "1"])
    assert result.exit_code == 0
    assert "Alice" in result.stdout
    assert "30" in result.stdout


def test_get_user_command_not_found():
    """
    Tests the 'get-user' CLI command for a user that does not exist.
    """
    result = runner.invoke(app, ["get-user", "999"])
    assert result.exit_code == 0
    assert "Error:" in result.stdout
    assert "User with ID 999 not found" in result.stdout
