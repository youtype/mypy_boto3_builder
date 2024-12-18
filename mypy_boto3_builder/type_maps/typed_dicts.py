"""
Collection of TypedDicts added by boto3.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.enums.service_module_name import ServiceModuleName
from mypy_boto3_builder.type_annotations.internal_import import InternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_annotations.type_typed_dict import TypedDictAttribute, TypeTypedDict
from mypy_boto3_builder.type_annotations.type_union import TypeUnion

WaiterConfigTypeDef = TypeTypedDict(
    "WaiterConfigTypeDef",
    (
        TypedDictAttribute("Delay", Type.int, required=False),
        TypedDictAttribute("MaxAttempts", Type.int, required=False),
    ),
)

PaginatorConfigTypeDef = TypeTypedDict(
    "PaginatorConfigTypeDef",
    (
        TypedDictAttribute("MaxItems", Type.int, required=False),
        TypedDictAttribute("PageSize", Type.int, required=False),
        TypedDictAttribute("StartingToken", Type.str, required=False),
    ),
)

ResponseMetadataTypeDef = TypeTypedDict(
    "ResponseMetadataTypeDef",
    (
        TypedDictAttribute("RequestId", Type.str, required=True),
        TypedDictAttribute("HostId", Type.str, required=False),
        TypedDictAttribute("HTTPStatusCode", Type.int, required=True),
        TypedDictAttribute("HTTPHeaders", Type.DictStrStr, required=True),
        TypedDictAttribute("RetryAttempts", Type.int, required=True),
    ),
)

# s3
CopySourceTypeDef = TypeTypedDict(
    "CopySourceTypeDef",
    (
        TypedDictAttribute("Bucket", Type.str, required=True),
        TypedDictAttribute("Key", Type.str, required=True),
        TypedDictAttribute("VersionId", Type.str, required=False),
    ),
)

# ec2
TagTypeDef = TypeTypedDict(
    "TagTypeDef",
    (
        TypedDictAttribute("Key", Type.str, required=False),
        TypedDictAttribute("Value", Type.str, required=False),
    ),
)


# dynamodb
EmptyResponseMetadataTypeDef = TypeTypedDict(
    "EmptyResponseMetadataTypeDef",
    (TypedDictAttribute("ResponseMetadata", ResponseMetadataTypeDef, required=True),),
)

# dynamodb
AttributeValueTypeDef: TypeTypedDict = TypeTypedDict(
    "AttributeValueTypeDef",
    (
        TypedDictAttribute("S", Type.str, required=False),
        TypedDictAttribute("N", Type.str, required=False),
        TypedDictAttribute("B", Type.bytes, required=False),
        TypedDictAttribute("SS", TypeSubscript(Type.Sequence, [Type.str]), required=False),
        TypedDictAttribute("NS", TypeSubscript(Type.Sequence, [Type.str]), required=False),
        TypedDictAttribute("BS", TypeSubscript(Type.Sequence, [Type.bytes]), required=False),
        TypedDictAttribute("M", Type.MappingStrAny, required=False),
        TypedDictAttribute("L", Type.SequenceAny, required=False),
        TypedDictAttribute("NULL", Type.bool, required=False),
        TypedDictAttribute("BOOL", Type.bool, required=False),
    ),
)

# cloudformation
GetTemplateOutputTypeDef = TypeTypedDict(
    "GetTemplateOutputTypeDef",
    (
        TypedDictAttribute("TemplateBody", Type.DictStrAny, required=True),
        TypedDictAttribute(
            "StagesAvailable",
            TypeSubscript(
                Type.list,
                [InternalImport(name="TemplateStageType", module_name=ServiceModuleName.literals)],
            ),
            required=True,
        ),
        TypedDictAttribute("ResponseMetadata", ResponseMetadataTypeDef, required=True),
    ),
)

# iam
# FIXME: https://github.com/boto/botocore/issues/2992
PolicyDocumentStatementTypeDef = TypeTypedDict(
    "PolicyDocumentStatementTypeDef",
    (
        TypedDictAttribute("Effect", Type.str, required=True),
        TypedDictAttribute(
            "Resource",
            TypeUnion((Type.str, TypeSubscript(Type.list, [Type.str]))),
            required=True,
        ),
        TypedDictAttribute("Sid", Type.str, required=True),
        TypedDictAttribute(
            "Action",
            TypeUnion((Type.str, TypeSubscript(Type.list, [Type.str]))),
            required=True,
        ),
    ),
)

PolicyDocumentDictTypeDef = TypeTypedDict(
    "PolicyDocumentDictTypeDef",
    (
        TypedDictAttribute("Version", Type.str, required=True),
        TypedDictAttribute(
            "Statement",
            TypeSubscript(Type.list, [PolicyDocumentStatementTypeDef]),
            required=True,
        ),
    ),
)


# cloudwatch events
CloudwatchEventStateTypeDef = TypeTypedDict(
    "CloudwatchEventStateTypeDef",
    (
        TypedDictAttribute("reason", Type.str, required=False),
        TypedDictAttribute("reasonData", Type.str, required=False),
        TypedDictAttribute("timestamp", Type.str, required=True),
        TypedDictAttribute("value", Type.str, required=True),
        TypedDictAttribute("actionsSuppressedBy", Type.str, required=False),
        TypedDictAttribute("actionsSuppressedReason", Type.str, required=False),
    ),
)

CloudwatchEventMetricStatsMetricTypeDef = TypeTypedDict(
    "CloudwatchEventMetricStatsMetricTypeDef",
    (
        TypedDictAttribute("metricName", Type.str, required=True),
        TypedDictAttribute("namespace", Type.str, required=True),
        TypedDictAttribute("dimensions", Type.DictStrStr, required=True),
    ),
)

CloudwatchEventMetricStatsTypeDef = TypeTypedDict(
    "CloudwatchEventMetricStatsTypeDef",
    (
        TypedDictAttribute("metric", CloudwatchEventMetricStatsMetricTypeDef, required=False),
        TypedDictAttribute("period", Type.str, required=True),
        TypedDictAttribute("stat", Type.str, required=True),
    ),
)

CloudwatchEventMetricTypeDef = TypeTypedDict(
    "CloudwatchEventMetricTypeDef",
    (
        TypedDictAttribute("id", Type.str, required=True),
        TypedDictAttribute("metricStat", CloudwatchEventMetricStatsTypeDef, required=False),
        TypedDictAttribute("returnData", Type.bool, required=True),
        TypedDictAttribute("expression", Type.str, required=False),
        TypedDictAttribute("label", Type.str, required=False),
        TypedDictAttribute("period", Type.int, required=False),
    ),
)

CloudwatchEventConfigurationTypeDef = TypeTypedDict(
    "CloudwatchEventDetailConfigurationTypeDef",
    (
        TypedDictAttribute("id", Type.str, required=False),
        TypedDictAttribute("description", Type.str, required=False),
        TypedDictAttribute(
            "metrics",
            TypeSubscript(Type.list, [CloudwatchEventMetricTypeDef]),
            required=False,
        ),
        TypedDictAttribute("actionsSuppressor", Type.str, required=False),
        TypedDictAttribute("actionsSuppressorWaitPeriod", Type.int, required=False),
        TypedDictAttribute("actionsSuppressorExtensionPeriod", Type.int, required=False),
        TypedDictAttribute("threshold", Type.int, required=False),
        TypedDictAttribute("evaluationPeriods", Type.int, required=False),
        TypedDictAttribute("alarmRule", Type.str, required=False),
        TypedDictAttribute("alarmName", Type.str, required=False),
        TypedDictAttribute("treatMissingData", Type.str, required=False),
        TypedDictAttribute("comparisonOperator", Type.str, required=False),
        TypedDictAttribute("timestamp", Type.str, required=False),
        TypedDictAttribute("actionsEnabled", Type.bool, required=False),
        TypedDictAttribute("okActions", TypeSubscript(Type.list, [Type.str]), required=False),
        TypedDictAttribute("alarmActions", TypeSubscript(Type.list, [Type.str]), required=False),
        TypedDictAttribute(
            "insufficientDataActions",
            TypeSubscript(Type.list, [Type.str]),
            required=False,
        ),
    ),
)

CloudwatchEventDetailTypeDef = TypeTypedDict(
    "CloudwatchEventDetailTypeDef",
    (
        TypedDictAttribute("alarmName", Type.str, required=True),
        TypedDictAttribute("operation", Type.str, required=False),
        TypedDictAttribute("configuration", CloudwatchEventConfigurationTypeDef, required=False),
        TypedDictAttribute(
            "previousConfiguration",
            CloudwatchEventConfigurationTypeDef,
            required=False,
        ),
        TypedDictAttribute("previousState", CloudwatchEventStateTypeDef, required=False),
        TypedDictAttribute("state", CloudwatchEventStateTypeDef, required=True),
    ),
)

CloudwatchEventTypeDef = TypeTypedDict(
    "CloudwatchEventTypeDef",
    (
        TypedDictAttribute("version", Type.str, required=True),
        TypedDictAttribute("id", Type.str, required=True),
        TypedDictAttribute("detail-type", Type.str, required=True),
        TypedDictAttribute("source", Type.str, required=True),
        TypedDictAttribute("account", Type.str, required=True),
        TypedDictAttribute("time", Type.str, required=True),
        TypedDictAttribute("region", Type.str, required=True),
        TypedDictAttribute("resources", TypeSubscript(Type.list, [Type.str]), required=True),
        TypedDictAttribute("detail", CloudwatchEventDetailTypeDef, required=True),
    ),
)
