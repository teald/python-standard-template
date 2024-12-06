"""Configurations and general fixtures for template tests."""

import pytest


def pytest_configure(config):
    """Programatic configuration for pytest in this directory."""
    # You can include an optional description here using the format:
    #    "mark_name: description here"
    marks = [
        "template",
        "conformance",
    ]

    for mark in marks:
        config.addinivalue_line("markers", mark)


class Helpers:
    """Class for helper methods.

    These should all be static methods; no state allowed :)
    """

    @staticmethod
    def validate_cookies_result(pytest_cookies_result):
        """Raise AssertionError for bad return codes, stderr output."""


@pytest.fixture(scope="session")
def helpers() -> Helpers:
    """Return instance of the Helpers class, which has helper methods."""

    return Helpers()
