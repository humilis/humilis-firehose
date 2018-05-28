"""A dummy module for testing purposes."""

import base64
import json
import os
import time


def transform(event, context):
    """Sample Firehose transform."""
    output = []
    if "body" in event:
        # We are calling this from the REST API
        event = event["body"]

    for record in event["records"]:
        payload = base64.b64decode(record["data"])
        output_record = {
            "recordId": record["recordId"],
            "result": "Ok",
            "data": base64.b64encode(payload)
        }
        output.append(output_record)

    return {"records": output}
