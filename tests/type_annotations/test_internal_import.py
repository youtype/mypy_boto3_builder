from typing import Dict

import pytest

from mypy_boto3_builder.type_annotations.internal_import import (
    InternalImport,
    AliasInternalImport,
)


class TestInternalImport:
    def setup_method(self) -> None:
        self.result = InternalImport("MyClass")

    def test_init(self) -> None:
        assert self.result.name == "MyClass"

    def test_render(self) -> None:
        assert self.result.render() == '"MyClass"'
        self.result.stringify = False
        assert self.result.render() == "MyClass"
        self.result.use_alias = True
        assert self.result.render() == "_MyClass"

    def test_get_import_record(self) -> None:
        assert self.result.get_import_record().render() == ""

    def test_copy(self) -> None:
        assert self.result.copy().name == "MyClass"


class TestAliasInternalImport:
    def test_init(self) -> None:
        result = AliasInternalImport("MyClass")
        assert result.stringify == False
        assert result.use_alias == True
        assert result.render() == "_MyClass"
