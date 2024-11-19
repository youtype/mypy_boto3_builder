import pytest

from mypy_boto3_builder.exceptions import BuildInternalError, TypeAnnotationError
from mypy_boto3_builder.utils.strings import (
    capitalize,
    get_anchor_link,
    get_botocore_class_name,
    get_class_prefix,
    get_copyright,
    get_pypi_link,
    get_short_docstring,
    get_type_def_name,
    is_reserved,
    textwrap,
    xform_name,
)


class TestStrings:
    def test_get_class_prefix(self) -> None:
        assert get_class_prefix("my_func") == "MyFunc"
        assert not get_class_prefix("")
        assert get_class_prefix("myFunc") == "MyFunc"

    def test_get_anchor_link(self) -> None:
        assert get_anchor_link("test") == "test"
        assert get_anchor_link("n.ew_t est") == "new_t-est"

    def test_is_reserved(self) -> None:
        assert is_reserved("lambda")
        assert is_reserved("List")
        assert is_reserved("dict")
        assert not is_reserved("myname")

    def test_get_short_docstring(self) -> None:
        assert not get_short_docstring("")
        assert not get_short_docstring("\n")
        assert get_short_docstring("`asd\n:type") == "`asd`."
        assert get_short_docstring("`as’d\n:type") == "`as'd`."
        assert (
            get_short_docstring("`asd <https://link>`\n **Request syntax**::\ntest")
            == "[asd](https://link)."
        )
        assert (
            get_short_docstring(
                """
                This action aborts a multipart
                upload. After a multipart upload is aborted,
                no additional parts can be uploaded using that upload ID. The storage
                consumed by any previously uploaded parts will be freed. However, if
                any part uploads are currently in progress, those part uploads might or might
                not succeed.
                As a result, it might be necessary to abort a given multipart upload multiple times
                in order to completely free all storage consumed by all parts.


                To verify that all parts have been removed, so you don't get charged
                for the part storage, you should call the `ListParts
                <https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html>`
                __ action and ensure that the parts list is empty.
                """,
            )
            == "This action aborts a multipart upload."
        )

    def test_get_type_def_name(self) -> None:
        assert get_type_def_name("MyClass", "my_method") == "MyClassMyMethodTypeDef"
        assert get_type_def_name("my_func") == "MyFuncTypeDef"

        with pytest.raises(TypeAnnotationError):
            get_type_def_name()

    def test_textwrap(self) -> None:
        assert textwrap("test", 12) == "test"
        assert textwrap("test", 2) == "test"
        assert textwrap("te  st words", 12) == "te  st words"
        assert textwrap("te  st words", 6) == "te\nst\nwords"
        assert textwrap("te  stwords", 12) == "te  stwords"
        assert textwrap("te  stwords new", 6) == "te\nstwords\nnew"
        assert textwrap(
            "Get all items from the collection, optionally"
            " with a custom page size and item count limit.",
        ) == (
            "Get all items from the collection, optionally with a custom page size and item"
            "\ncount limit."
        )

    def test_get_botocore_class_name(self) -> None:
        assert get_botocore_class_name({"serviceAbbreviation": "drs"}) == "Drs"
        assert (
            get_botocore_class_name({"serviceAbbreviation": "drs", "serviceFullName": "name"})
            == "Drs"
        )
        assert get_botocore_class_name({"serviceFullName": "name"}) == "Name"
        assert get_botocore_class_name({"serviceFullName": "naMe"}) == "NaMe"
        assert get_botocore_class_name({"serviceAbbreviation": "RDS"}) == "RDS"

    def test_capitalize(self) -> None:
        assert capitalize("test caps") == "Test caps"
        assert capitalize("test Caps") == "Test Caps"
        assert capitalize("TEST") == "TEST"

    def test_xform_name(self) -> None:
        assert xform_name("test") == "test"
        assert xform_name("MyClass") == "my_class"
        assert xform_name("MyClass", "-") == "my-class"
        with pytest.raises(BuildInternalError):
            xform_name("MyClass", "")

    def test_get_pypi_link(self) -> None:
        assert get_pypi_link("mypy-boto3-builder") == "https://pypi.org/project/mypy-boto3-builder/"
        with pytest.raises(BuildInternalError):
            get_pypi_link("")

    def test_get_copyright(self) -> None:
        assert "Copyright" in get_copyright()
