"""Tests for the cookiecutter template."""

import pytest


@pytest.mark.template
def test_create_from_defaults(cookies, helpers):
    """Test creating the template without input."""
    result = cookies.bake()

    helpers.validate_cookies_result(result)
