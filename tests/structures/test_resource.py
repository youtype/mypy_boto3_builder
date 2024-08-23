from mypy_boto3_builder.service_name import ServiceNameCatalog
from mypy_boto3_builder.structures.collection import Collection
from mypy_boto3_builder.structures.resource import Resource


class TestResource:
    resource: Resource

    def setup_method(self):
        self.resource = Resource(
            name="Name",
            service_name=ServiceNameCatalog.s3,
        )

    def test_init(self) -> None:
        assert self.resource.name == "Name"
        assert self.resource.service_name == ServiceNameCatalog.s3

    def test_boto3_doc_link(self) -> None:
        assert (
            self.resource.boto3_doc_link
            == "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.Name"
        )

    def test_iterate_types(self) -> None:
        assert set(self.resource.iterate_types()) == {self.resource.bases[0]}
        collection = Collection(
            name="Collection",
            attribute_name="name",
            parent_name="parent",
            service_name=ServiceNameCatalog.s3,
            type_annotation=self.resource.bases[0],
            object_class_name="Object",
        )
        self.resource.collections.append(collection)
        assert set(self.resource.iterate_types()) == {
            self.resource.bases[0],
            collection.bases[0],
        }
