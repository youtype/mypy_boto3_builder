"""
Main entrypoint for module.

Copyright 2024 Vlad Emelianov
"""

from mypy_boto3_builder.logger import enable_logger
from mypy_boto3_builder.main import main

if __name__ == "__main__":
    enable_logger()
    main()
