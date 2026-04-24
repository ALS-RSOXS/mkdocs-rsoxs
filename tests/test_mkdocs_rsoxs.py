"""Tests for mkdocs_rsoxs."""

from typer.testing import CliRunner

from mkdocs_rsoxs import __version__


def test_version() -> None:
    """Test that version is defined."""
    assert __version__ is not None
    assert isinstance(__version__, str)
