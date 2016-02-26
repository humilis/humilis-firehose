# -*- coding: utf-8 -*-
"""
Tests the input and output Kinesis streams
"""

import pytest
import uuid

import boto3
from humilis.environment import Environment


@pytest.fixture(scope="session", params=[1, 10, 100])
def events(request):
    """A batch of events to be sent to the delivery stream."""
    return [','.join([
        str(uuid.uuid4()).replace("-", ""),
        "2016-01-22T01:45:44.235+01:00",
        "1628457772.1449082074",
        "http://staging.findhotel.net/?lang=nl-NL",
        "http://staging.findhotel.net/"
        ]) + "\n" for _ in range(request.param)]


@pytest.fixture(scope="session")
def environment(settings):
    """The io-streams-test humilis environment."""
    env = Environment(settings.environment_path, stage=settings.stage)
    env.create()
    return env


@pytest.fixture(scope="session", params=['DeliveryStream1', 'DeliveryStream2'])
def stream_name(settings, environment, request):
    """The name of a delivery stream."""
    layer = [l for l in environment.layers if l.name == settings.layer_name][0]
    return layer.outputs.get(request.param)


@pytest.fixture(scope="session")
def firehose():
    """Boto3 kinesis client."""
    return boto3.client('firehose')


def test_put_record_batch(firehose, stream_name, events):
    """Put some records to Firehose and check they are delivered to S3."""
    resp = firehose.put_record_batch(
        DeliveryStreamName=stream_name,
        Records=[{"Data": event} for event in events])
    assert resp['ResponseMetadata']['HTTPStatusCode'] == 200
