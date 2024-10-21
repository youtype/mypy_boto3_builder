from typing import TYPE_CHECKING

from mypy_boto3_builder.constants import TEMPLATES_PATH, StaticStubsPath, TemplatePath

if TYPE_CHECKING:
    from pathlib import Path


class TestConstants:
    def test_template_path(self) -> None:
        for key in dir(TemplatePath):
            if key.startswith("_"):
                continue

            path: Path = getattr(TemplatePath, key)
            assert path.is_absolute()
            assert path.exists()
            assert path.relative_to(TEMPLATES_PATH)

    def test_static_stubs_path(self) -> None:
        for key in dir(StaticStubsPath):
            if key.startswith("_"):
                continue
            path: Path = getattr(StaticStubsPath, key)
            assert path.is_absolute()
            assert path.exists()
