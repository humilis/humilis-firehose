#!/usr/bin/env python
# -*- coding: utf-8 -*-


from configparser import ConfigParser
import subprocess
import sys
import yaml


# Name of the layer that deploys the bucket
LAYER_NAME = "storage"


def get_aws_profile():
    """Produces the name of the AWS profile used for deployment."""
    parser = ConfigParser()
    parser.read(".humilis.ini")
    humilis_profile = parser.get("default", "profile")
    return parser.get("profile:{}".format(humilis_profile), "aws_profile")


def empty_bucket(humilis_outputs, stage="test"):
    """Empties the storage bucket associated to a deployment."""

    stage = stage.lower()
    with open(humilis_outputs, "r") as f:
        outputs = yaml.load(f.read())

    bucket = outputs[LAYER_NAME]["BucketName"]
    subprocess.call([
        "aws", "s3", "rm", "s3://{}/".format(bucket),
        "--recursive"], stdout=subprocess.PIPE)

if __name__ == "__main__":
    empty_bucket(*sys.argv[1:])
