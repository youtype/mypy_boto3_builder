"""
Profiling entrypoint.

Copyright 2024 Vlad Emelianov
"""

from pathlib import Path

from mypy_boto3_builder.cli_parser import CLINamespace
from mypy_boto3_builder.enums.output_type import OutputType
from mypy_boto3_builder.enums.product import Product
from mypy_boto3_builder.main import run


def main() -> None:
    """
    Profiling entrypoint.
    """
    args = CLINamespace(
        log_level=0,
        output_path=Path("./mypy_boto3_output"),
        service_names=["acm"],
        build_version="1.0.0",
        output_types=[OutputType.package],
        products=[Product.boto3_services],
        list_services=False,
        partial_overload=False,
        skip_published=False,
        disable_smart_version=True,
        download_static_stubs=False,
    )
    run(args)


if __name__ == "__main__":
    main()
