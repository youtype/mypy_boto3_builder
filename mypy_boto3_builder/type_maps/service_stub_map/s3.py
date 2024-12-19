"""
S3 service injected methods.

Copyright 2024 Vlad Emelianov
"""

from botocore.client import BaseClient

from mypy_boto3_builder.import_helpers.import_helper import Import
from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.named_unions import FileobjTypeDef, PresignedPostConditionsTypeDef
from mypy_boto3_builder.type_maps.typed_dicts import CopySourceTypeDef
from mypy_boto3_builder.utils.type_checks import get_optional

callback_arg = Argument(
    "Callback",
    get_optional(TypeSubscript(Type.Callable, (Type.Ellipsis, Type.Any))),
    Type.Ellipsis,
)

config_arg = Argument(
    "Config",
    get_optional(ExternalImport(Import.boto3 + "s3" + "transfer", "TransferConfig")),
    Type.Ellipsis,
)

extra_args_arg = Argument("ExtraArgs", get_optional(Type.DictStrAny), Type.Ellipsis)

source_client_arg = Argument(
    "SourceClient",
    get_optional(ExternalImport.from_class(BaseClient)),
    Type.Ellipsis,
)

copy_method = Method(
    name="copy",
    arguments=(
        Argument.self(),
        Argument("CopySource", CopySourceTypeDef),
        Argument("Bucket", Type.str),
        Argument("Key", Type.str),
        extra_args_arg,
        callback_arg,
        source_client_arg,
        config_arg,
    ),
    return_type=Type.none,
    docstring="Copy an object from one S3 location to another.",
)

download_file_method = Method(
    name="download_file",
    arguments=(
        Argument.self(),
        Argument("Bucket", Type.str),
        Argument("Key", Type.str),
        Argument("Filename", Type.str),
        extra_args_arg,
        callback_arg,
        config_arg,
    ),
    return_type=Type.none,
    docstring="Download an object from S3 to a file.",
)

download_fileobj_method = Method(
    name="download_fileobj",
    arguments=(
        Argument.self(),
        Argument("Bucket", Type.str),
        Argument("Key", Type.str),
        Argument("Fileobj", FileobjTypeDef),
        extra_args_arg,
        callback_arg,
        config_arg,
    ),
    return_type=Type.none,
    docstring="Download an object from S3 to a file-like object.",
)

generate_presigned_post_method = Method(
    name="generate_presigned_post",
    arguments=(
        Argument.self(),
        Argument("Bucket", Type.str),
        Argument("Key", Type.str),
        Argument("Fields", get_optional(Type.DictStrAny), Type.Ellipsis),
        Argument("Conditions", get_optional(PresignedPostConditionsTypeDef), Type.Ellipsis),
        Argument("ExpiresIn", Type.int, TypeConstant(3600)),
    ),
    return_type=Type.DictStrAny,
    docstring="Generate a presigned URL for POST requests.",
)

upload_file_method = Method(
    name="upload_file",
    arguments=(
        Argument.self(),
        Argument("Filename", Type.str),
        Argument("Bucket", Type.str),
        Argument("Key", Type.str),
        extra_args_arg,
        callback_arg,
        config_arg,
    ),
    return_type=Type.none,
    docstring="Upload a file to S3.",
)

upload_fileobj_method = Method(
    name="upload_fileobj",
    arguments=(
        Argument.self(),
        Argument("Fileobj", FileobjTypeDef),
        Argument("Bucket", Type.str),
        Argument("Key", Type.str),
        extra_args_arg,
        callback_arg,
        config_arg,
    ),
    return_type=Type.none,
    docstring="Upload a file-like object to S3.",
)

bucket_load_method = Method(
    name="load",
    arguments=[Argument.self()],
    return_type=Type.none,
    docstring="Calls s3.Client.list_buckets() to update the attributes of the Bucket resource.",
)

object_summary_load_method = Method(
    name="load",
    arguments=[Argument.self()],
    return_type=Type.none,
    docstring="Calls s3.Client.head_object to update the attributes of the ObjectSummary resource.",
)


CLIENT_METHODS = (
    copy_method,
    download_file_method,
    download_fileobj_method,
    generate_presigned_post_method,
    upload_file_method,
    upload_fileobj_method,
)
BUCKET_METHODS = (
    bucket_load_method,
    copy_method.copy().remove_argument("Bucket"),
    download_file_method.copy().remove_argument("Bucket"),
    download_fileobj_method.copy().remove_argument("Bucket"),
    upload_file_method.copy().remove_argument("Bucket"),
    upload_fileobj_method.copy().remove_argument("Bucket"),
)
OBJECT_METHODS = (
    copy_method.copy().remove_argument("Bucket", "Key"),
    download_file_method.copy().remove_argument("Bucket", "Key"),
    download_fileobj_method.copy().remove_argument("Bucket", "Key"),
    upload_file_method.copy().remove_argument("Bucket", "Key"),
    upload_fileobj_method.copy().remove_argument("Bucket", "Key"),
)
OBJECT_SUMMARY_METHODS = (object_summary_load_method,)
