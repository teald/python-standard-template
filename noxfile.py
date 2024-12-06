"""Automations for delivering/testing the Python Standard Template.

WARNING: THIS FILE IS NOT A PART OF THE TEMPLATE!!! If you are looking
for applying standards or starting a new template, please go to the
GitLab repository and follow the instructions in ``README.md``:

  + https://gitlab.com/nsf-noirlab/general-resources/standard-python-template
"""

import nox


class SessionVariables:
    """Container class for constants used in various sessions."""

    all_pythons_supported = ["3.10", "3.11", "3.12", "3.13"]


@nox.session(python=SessionVariables.all_pythons_supported)
def run_tests(session: nox.Session):
    """Execute template tests."""
    session.install("pytest", "pytest-cookies")

    session.run("pytest", "tests/", *session.posargs)
