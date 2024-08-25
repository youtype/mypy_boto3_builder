import tempfile
from pathlib import Path

from mypy_boto3_builder.writers.ruff_formatter import RuffFormatter


class TestRuffFormatter:
    def test_format(self) -> None:
        formatter = RuffFormatter(
            known_first_party=["local"],
            known_third_party=["extra", "local"],
        )
        with tempfile.NamedTemporaryFile("+w") as f:
            f.write("import os\n")
            f.write("import datetime\n")
            f.write("import black\n")
            f.write("import local\n")
            f.write("import extra.new\n")
            f.write("a   =datetime.datetime.now()\n")
            f.flush()
            formatter.format_python([Path(f.name)])
            assert Path(f.name).read_text() == (
                "import datetime\n"
                "import os\n"
                "\n"
                "import black\n"
                "import extra.new\n"
                "\n"
                "import local\n"
                "\n"
                "a = datetime.datetime.now()\n"
            )

    def test_format_markdown(self) -> None:
        formatter = RuffFormatter()
        assert formatter.format_markdown("") == ""
        assert (
            formatter.format_markdown("# a\ntest\n## b\n## c\ntest2")
            == "# a\ntest\n## b\n## c\ntest2"
        )
        assert formatter.format_markdown("# a\n```python\na=5\n```") == "# a\n```python\na = 5\n```"
        assert formatter.format_markdown("# a\n```bash\na=5\n```") == "# a\n```bash\na=5\n```"
