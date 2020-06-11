"""
Base class for all structures that can be rendered to a class.
"""
from dataclasses import dataclass, field
from typing import List, Set

from botocore import xform_name

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.structures.attribute import Attribute
from mypy_boto3_builder.structures.method import Method
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.internal_import import InternalImport


@dataclass
class ClassRecord:
    """
    Base class for all structures that can be rendered to a class.
    """

    name: str
    methods: List[Method] = field(default_factory=lambda: [])
    attributes: List[Attribute] = field(default_factory=lambda: [])
    bases: List[FakeAnnotation] = field(default_factory=lambda: [])
    docstring: str = ""
    use_alias: bool = False

    @property
    def alias_name(self) -> str:
        if not self.use_alias:
            raise ValueError(f"Cannot get alias for { self.name } with no alias.")
        return InternalImport.get_alias(self.name)

    def render_alias(self) -> str:
        return f"{self.alias_name} = {self.name}"

    def get_types(self) -> Set[FakeAnnotation]:
        types: Set[FakeAnnotation] = set()
        for method in self.methods:
            types.update(method.get_types())
        for attribute in self.attributes:
            types.update(attribute.get_types())
        for base in self.bases:
            types.update(base.get_types())
        return types

    def get_required_import_records(self) -> Set[ImportRecord]:
        result: Set[ImportRecord] = set()
        for type_annotation in self.get_types():
            import_record = type_annotation.get_import_record()
            if not import_record:
                continue
            if import_record.is_builtins():
                continue
            if import_record.is_local():
                result.add(ImportRecord(ImportString("typing"), "TYPE_CHECKING"))
            result.add(import_record)

        return result

    def get_internal_imports(self) -> List[InternalImport]:
        result: List[InternalImport] = []
        for method in self.methods:
            for type_annotation in method.get_types():
                if not isinstance(type_annotation, InternalImport):
                    continue
                result.append(type_annotation)

        return result

    @property
    def variable_name(self) -> str:
        """
        Get a proper variable name for an instance of this class.
        """
        return xform_name(self.name)
