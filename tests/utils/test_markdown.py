from mypy_boto3_builder.utils.markdown import Header, TableOfContents, fix_pypi_headers


class TestTableOfContents:
    def test_render(self) -> None:
        toc = TableOfContents(
            [
                Header("a", 1),
                Header("b", 3),
                Header("c", 6),
            ],
        )
        assert toc.render() == "- [a](#a)\n    - [b](#b)"


class TestMarkdown:
    def test_fix_pypi_headers(self) -> None:
        assert (
            fix_pypi_headers("# a\ntest\n## b\n## c\ntest2")
            == '<a id="a"></a>\n\n# a\ntest\n<a id="b"></a>\n\n## b\n<a id="c"></a>\n\n## c\ntest2'
        )
        assert fix_pypi_headers("# a\n```## b```") == '<a id="a"></a>\n\n# a\n```## b```'
