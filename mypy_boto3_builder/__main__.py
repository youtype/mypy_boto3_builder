"""
Main entrypoint for module.
"""

import sys

from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.main import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger = get_logger()
        logger.warning("Interrupted by user")
        sys.exit(1)
