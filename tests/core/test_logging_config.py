import os
from unittest.mock import patch

from src.core.logging_config import setup_logging


def test_setup_logging_file_creation(monkeypatch):
    """
    Tests that the logger setup creates a log file when LOG_TO_FILE is true.
    """
    # Ensure the logs directory exists
    if not os.path.exists("logs"):
        os.makedirs("logs")

    log_file = "logs/app.log"
    # Clean up log file before test
    if os.path.exists(log_file):
        os.remove(log_file)

    # Use monkeypatch to set the environment variable for the test
    monkeypatch.setattr("src.core.config.settings.log_to_file", True)

    # We need to re-import the settings or patch the existing one
    with patch("src.core.logging_config.settings.log_to_file", True):
        setup_logging()

    assert os.path.exists(log_file)

    # Clean up log file after test
    if os.path.exists(log_file):
        os.remove(log_file)
