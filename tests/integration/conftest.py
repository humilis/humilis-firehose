"""Fixtures for the integration tests suite."""

import pytest

from humilis.environment import Environment


@pytest.yield_fixture(scope="module")
def environment():
    """Create (and delete) a sample environment."""
    env = Environment("tests/integration/firehose.yaml")
    env.create()
    yield env
    env.delete()
