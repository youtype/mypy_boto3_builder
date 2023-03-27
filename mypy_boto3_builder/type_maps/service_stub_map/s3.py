"""
S3 service injected methods.
"""

from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient
from botocore.response import StreamingBody

from mypy_boto3_builder.structures.argument import Argument
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.type_annotations.type import Type
from mypy_boto3_builder.type_annotations.type_constant import TypeConstant
from mypy_boto3_builder.type_annotations.type_subscript import TypeSubscript
from mypy_boto3_builder.type_maps.typed_dicts import s3_copy_source_type

callback_arg = Argument(
    "Callback",
    TypeSubscript(Type.Callable, [Type.Ellipsis, Type.Any]),
    Type.Ellipsis,
)

config_arg = Argument(
    "Config",
    ExternalImport.from_class(TransferConfig),
    Type.Ellipsis,
)

copy_method = Method(
    "copy",
    [
        Argument("self", None),
        Argument("CopySource", s3_copy_source_type),
        Argument("Bucket", Type.str),
        Argument("Key", Type.str),
        Argument("ExtraArgs", Type.DictStrAny, Type.Ellipsis),
        callback_arg,
        Argument(
            "SourceClient",
            ExternalImport.from_class(BaseClient),
            Type.Ellipsis,
        ),
        config_arg,
    ],
    Type.none,
)

download_file_method = Method(
    "download_file",
    [
        Argument("self", None),
        Argument("Bucket", Type.str),
        Argument("Key", Type.str),
        Argument("Filename", Type.str),
        Argument("ExtraArgs", Type.DictStrAny, Type.Ellipsis),
        callback_arg,
        config_arg,
    ],
    Type.none,
)

download_fileobj_method = Method(
    "download_fileobj",
    [
        Argument("self", None),
        Argument("Bucket", Type.str),
        Argument("Key", Type.str),
        Argument(
            "Fileobj",
            TypeSubscript(Type.Union, [Type.IOAny, ExternalImport.from_class(StreamingBody)]),
        ),
        Argument("ExtraArgs", Type.DictStrAny, Type.Ellipsis),
        callback_arg,
        config_arg,
    ],
    Type.none,
)

generate_presigned_post_method = Method(
    "generate_presigned_post",
    [
        Argument("self", None),
        Argument("Bucket", Type.str),
        Argument("Key", Type.str),
        Argument("Fields", Type.DictStrAny, Type.Ellipsis),
        Argument(
            "Conditions",
            TypeSubscript(Type.Union, [Type.ListAny, Type.DictStrAny]),
            Type.Ellipsis,
        ),
        Argument("ExpiresIn", Type.int, TypeConstant(3600)),
    ],
    Type.DictStrAny,
)

upload_file_method = Method(
    "upload_file",
    [
        Argument("self", None),
        Argument("Filename", Type.str),
        Argument("Bucket", Type.str),
        Argument("Key", Type.str),
        Argument("ExtraArgs", Type.DictStrAny, Type.Ellipsis),
        callback_arg,
        config_arg,
    ],
    Type.none,
)

upload_fileobj_method = Method(
    "upload_fileobj",
    [
        Argument("self", None),
        Argument(
            "Fileobj",
            TypeSubscript(Type.Union, [Type.IOAny, ExternalImport.from_class(StreamingBody)]),
        ),
        Argument("Bucket", Type.str),
        Argument("Key", Type.str),
        Argument("ExtraArgs", Type.DictStrAny, Type.Ellipsis),
        callback_arg,
        config_arg,
    ],
    Type.none,
)


CLIENT_METHODS = [
    copy_method,
    download_file_method,
    download_fileobj_method,
    generate_presigned_post_method,
    upload_file_method,
    upload_fileobj_method,
]
BUCKET_METHODS = [
    copy_method.copy().remove_argument("Bucket"),
    download_file_method.copy().remove_argument("Bucket"),
    download_fileobj_method.copy().remove_argument("Bucket"),
    upload_file_method.copy().remove_argument("Bucket"),
    upload_fileobj_method.copy().remove_argument("Bucket"),
]
OBJECT_METHODS = [
    copy_method.copy().remove_argument("Bucket", "Key"),
    download_file_method.copy().remove_argument("Bucket", "Key"),
    download_fileobj_method.copy().remove_argument("Bucket", "Key"),
    upload_file_method.copy().remove_argument("Bucket", "Key"),
    upload_fileobj_method.copy().remove_argument("Bucket", "Key"),
]
