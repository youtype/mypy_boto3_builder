from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation


class RemoveArgument(FakeAnnotation):
    """
    Annotation to mark argumnet for removal.
    """

    def render(self, parent_name: str = "") -> str:
        return "None"

    def copy(self) -> FakeAnnotation:
        return self

    def get_import_record(self) -> ImportRecord:
        return ImportRecord.empty()
