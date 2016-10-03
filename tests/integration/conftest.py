"""Integration tests conftest."""

from collections import namedtuple
import os
import uuid

from humilis.environment import Environment
import pytest

NB_EVENTS = 10


@pytest.fixture(scope="session")
def settings():
    """Global test settings."""
    Settings = namedtuple('Settings',
                          'stage environment_path streams_layer_name '
                          'output_path')
    envfile = "tests/integration/humilis-firehose"
    stage = os.environ.get("STAGE", "DEV")
    return Settings(
        stage=stage,
        environment_path="{}.yaml".format(envfile),
        output_path="{}-{}.outputs.yaml".format(envfile, stage),
        streams_layer_name="streams")


@pytest.yield_fixture(scope="session")
def environment(settings):
    """The test environment: this fixtures creates it and takes care of
    removing it after tests have run."""
    env = Environment(settings.environment_path, stage=settings.stage)
    if os.environ.get("UPDATE", "yes") == "yes":
        env.create(update=True, output_file=settings.output_path)
    else:
        env.create(output_file=settings.output_path)
    yield env
    if os.environ.get("DESTROY", "yes") == "yes":
        # Empty the S3 bucket
        bucket = env.outputs["storage"]["BucketName"]
        os.system("aws s3 rm s3://{} --recursive".format(bucket))
        env.delete()


@pytest.fixture
def events():
    """A template for a Kinesis event data record."""
    return [{"id": str(uuid.uuid4())} for _ in range(NB_EVENTS)]
