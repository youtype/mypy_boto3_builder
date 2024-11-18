from mypy_boto3_builder.package_data import Boto3StubsPackageData
from mypy_boto3_builder.structures.package_url import PackageURL


class TestPackageURL:
    package_url: PackageURL

    def setup_method(self) -> None:
        self.package_url = PackageURL("name", Boto3StubsPackageData)

    def test_init(self) -> None:
        assert self.package_url.pypi_name == "name"
        assert self.package_url.data == Boto3StubsPackageData

        assert self.package_url.pypi_badge == "https://img.shields.io/pypi/v/name.svg?color=blue"
        assert (
            self.package_url.pyversions_badge
            == "https://img.shields.io/pypi/pyversions/name.svg?color=blue"
        )
        assert (
            self.package_url.rtd_badge
            == "https://img.shields.io/readthedocs/boto3-stubs.svg?color=blue"
        )
        assert self.package_url.pepy_badge == "https://static.pepy.tech/badge/name"
        assert (
            self.package_url.montly_downloads_badge
            == "https://img.shields.io/pypi/dm/name?color=blue"
        )
        assert self.package_url.pypi == "https://pypi.org/project/name/"
        assert self.package_url.library_pypi == "https://pypi.org/project/boto3/"
        assert self.package_url.stubs_pypi == "https://pypi.org/project/boto3-stubs/"
        assert self.package_url.stubs_lite_pypi == "https://pypi.org/project/boto3-stubs-lite/"
        assert self.package_url.stubs_full_pypi == "https://pypi.org/project/boto3-stubs-full/"
        assert self.package_url.pepy == "https://pepy.tech/project/name"
        assert self.package_url.pypistats == "https://pypistats.org/packages/name"
        assert self.package_url.docs == "https://youtype.github.io/boto3_stubs_docs/"
