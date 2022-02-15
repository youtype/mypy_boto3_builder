from mypy_boto3_builder.utils.version import get_min_build_version


class TestStrings:
    def test_get_min_build_version(self):
        assert get_min_build_version("1.22.36") == "1.22.0"
        assert get_min_build_version("1.22.48.post13") == "1.22.0"
        assert get_min_build_version("1.13.3") == "1.13.0"
        assert get_min_build_version("1.13.2.post56") == "1.13.0"
