"""
Parser for boto3 changelog.

Copyright 2024 Vlad Emelianov
"""

import re

import requests

from mypy_boto3_builder.constants import REQUEST_TIMEOUT
from mypy_boto3_builder.exceptions import BuildEnvError


class BotocoreChangelog:
    """
    Parser for boto3 changelog.
    """

    URL = "https://raw.githubusercontent.com/boto/botocore/develop/CHANGELOG.rst"
    SERVICE_NAME_RE = re.compile(r"``(\S+)``")

    def __init__(self) -> None:
        self._changelog: str = ""

    @classmethod
    def _get_changelog(cls) -> str:
        response = requests.get(cls.URL, timeout=REQUEST_TIMEOUT)
        if not response.ok:
            raise BuildEnvError(
                f"Cannot retrieve {cls.URL}: {response.status_code} {response.text}",
            ) from None

        return response.text

    def _get_section(self, version: str) -> str:
        result: list[str] = []
        self._changelog = self._changelog or self._get_changelog()
        found = False
        for line in self._changelog.splitlines():
            if line == version:
                found = True
                continue
            if found and result and line.startswith("==="):
                result.pop()
                break
            if found:
                result.append(line)

        return "\n".join(result[1:])

    def fetch_updated(self, version: str) -> list[str]:
        """
        Get a list of service names updated in `version` release.
        """
        result: list[str] = []
        section = self._get_section(version)
        for match in self.SERVICE_NAME_RE.findall(section):
            if match not in result:
                result.append(match)

        return result
