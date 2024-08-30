import pytest

from mypy_boto3_builder.exceptions import TypeAnnotationError
from mypy_boto3_builder.utils.strings import (
    capitalize,
    get_anchor_link,
    get_botocore_class_name,
    get_class_prefix,
    get_short_docstring,
    get_type_def_name,
    is_reserved,
    textwrap,
)


class TestStrings:
    def test_get_class_prefix(self) -> None:
        assert get_class_prefix("my_func") == "MyFunc"
        assert get_class_prefix("") == ""
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
        assert get_short_docstring("") == ""
        assert get_short_docstring("\n") == ""
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
                any part uploads are currently in progress, those part uploads might or might not succeed. As a result, it might be necessary to abort a given multipart upload multiple times in order to completely free all storage consumed by all parts. 

                
                To verify that all parts have been removed, so you don't get charged
                for the part storage, you should call the `ListParts
                <https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html>`
                __ action and ensure that the parts list is empty.
                """
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
