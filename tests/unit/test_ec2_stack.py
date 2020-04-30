import json
import pytest

from aws_cdk import core
from ec2.ec2_stack import Ec2Stack


def get_template():
    app = core.App()
    Ec2Stack(app, "ec2")
    return json.dumps(app.synth().get_stack("ec2").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
