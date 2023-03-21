from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.collection import Collection
from mypy_boto3_builder.type_annotations.external_import import ExternalImport


class TestPaginator:
    @property
    def collection(self) -> Collection:
        return Collection(
            name="name",
            attribute_name="attribute",
            parent_name="Parent",
            service_name=ServiceName("s3", "S3"),
            type_annotation=ExternalImport.from_class(ServiceName),
            object_class_name="object",
        )

    def test_init(self) -> None:
        collection = self.collection
        assert collection.name == "name"
        assert collection.bases
        assert collection.boto3_doc_link

    def test_get_types(self) -> None:
        assert len(set(self.collection.iterate_types())) == 2
