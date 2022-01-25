from mypy_boto3_builder.utils.strings import (
    get_anchor_link,
    get_class_prefix,
    get_line_with_indented,
    get_min_build_version,
    get_short_docstring,
    is_reserved,
)


class TestStrings:
    def test_get_class_prefix(self) -> None:
        assert get_class_prefix("my_func") == "MyFunc"
        assert get_class_prefix("") == ""
        assert get_class_prefix("myFunc") == "MyFunc"

    def test_get_line_with_indented(self) -> None:
        assert get_line_with_indented("a\n\nb\nc") == "a"
        assert get_line_with_indented("a\n\n b\n  c\n\n d\ne") == "a\n\n b\n  c\n\n d"
        assert get_line_with_indented(" a\n  b\n  c\n d") == " a\n  b\n  c"
        assert get_line_with_indented("") == ""
        assert get_line_with_indented("a\n\nb\n c\nd", True) == "a\n\nb\n c"
        assert get_line_with_indented(" a\n\n b\n   c\n  d\ne", True) == " a\n\n b\n   c\n   d"

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
        assert get_short_docstring("`asd\n **Request syntax**::\ntest") == "`asd`."
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

    def test_get_min_build_version(self):
        assert get_min_build_version("1.22.36") == "1.22.0"
        assert get_min_build_version("1.22.48.post13") == "1.22.0"
        assert get_min_build_version("1.13.3") == "1.13.0"
        assert get_min_build_version("1.13.2.post56") == "1.13.0"
