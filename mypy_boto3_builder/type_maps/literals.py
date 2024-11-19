"""
Collection of Literals added by boto3.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.type_annotations.type_literal import TypeLiteral

QueueAttributeFilterType = TypeLiteral(
    "QueueAttributeFilterType",
    (
        "All",
        "AWSTraceHeader",
        "ApproximateFirstReceiveTimestamp",
        "ApproximateReceiveCount",
        "MessageDeduplicationId",
        "MessageGroupId",
        "SenderId",
        "SentTimestamp",
        "SequenceNumber",
        "Policy",
        "VisibilityTimeout",
        "MaximumMessageSize",
        "MessageRetentionPeriod",
        "ApproximateNumberOfMessages",
        "ApproximateNumberOfMessagesNotVisible",
        "CreatedTimestamp",
        "LastModifiedTimestamp",
        "QueueArn",
        "ApproximateNumberOfMessagesDelayed",
        "DelaySeconds",
        "ReceiveMessageWaitTimeSeconds",
        "RedrivePolicy",
        "FifoQueue",
        "ContentBasedDeduplication",
        "KmsMasterKeyId",
        "KmsDataKeyReusePeriodSeconds",
        "DeduplicationScope",
        "FifoThroughputLimit",
        "RedriveAllowPolicy",
        "SqsManagedSseEnabled",
    ),
)
