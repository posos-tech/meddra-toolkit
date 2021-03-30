"""Sample integration test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

import pytest
from click.testing import CliRunner
from expecter import expect

from meddra_toolkit.cli import main


@pytest.fixture
def runner():
    return CliRunner()


def describe_cli():
    def describe_conversion():
        def when_integer(runner):
            result = runner.invoke(main)

            # expect(result.exit_code) == 1
