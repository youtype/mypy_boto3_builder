"""
String to type annotation map that find type annotation in botocore syntax
"""
from typing import Dict

from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.type import Type

SYNTAX_TYPE_MAP: Dict[str, FakeAnnotation] = {
    "'string'": Type.str,
    "b'bytes'": Type.bytes,
    "123": Type.int,
    "123.0": Type.float,
    "123.4": Type.float,
    "None": Type.none,
    "True": Type.bool,
    "False": Type.bool,
    "file": Type.IO,
    "...": Type.Any,
}
