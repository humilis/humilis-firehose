"""Test creating and deleting and environment."""

import lambdautils.utils as utils


def test_s3_delivery(environment, events):
    """Test S3 delivery."""
    delivery_stream = environment.outputs["delivery"]["DeliveryStream1"]
    utils.send_to_delivery_stream(events, delivery_stream)


def test_es_delivery(environment, events):
    delivery_stream = environment.outputs["delivery"]["DeliveryStream2"]
    utils.send_to_delivery_stream(events, delivery_stream)
    delivery_stream = environment.outputs["delivery"]["DeliveryStream3"]
    utils.send_to_delivery_stream(events, delivery_stream)
