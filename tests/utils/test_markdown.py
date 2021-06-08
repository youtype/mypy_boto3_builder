from mypy_boto3_builder.utils.markdown import fix_pypi_headers


class TestMarkdown:
    def test_fix_pypi_headers(self) -> None:
        assert (
            fix_pypi_headers("# a\ntest\n## b\n## c\ntest2")
            == '<a id="a"></a>\n\n# a\ntest\n<a id="b"></a>\n\n## b\n<a id="c"></a>\n\n## c\ntest2'
        )
        assert fix_pypi_headers("# a\n") == '<a id="a"></a>\n\n# a'
