"""Pytest configuration and fixtures."""

import pytest

BASE = "http://localhost:8000/mkdocs-rsoxs"


@pytest.fixture
def sample_data() -> dict[str, str]:
    """Provide sample data for tests."""
    return {"key": "value"}
