"""Global conftest."""
import pytest
from collections import namedtuple


@pytest.fixture(scope="session")
def settings():
    """Global test settings."""
    Settings = namedtuple('Settings', 'stage environment_path layer_name')
    return Settings(stage="DEV",
                    environment_path="firehose.yaml",
                    layer_name="firehose")
