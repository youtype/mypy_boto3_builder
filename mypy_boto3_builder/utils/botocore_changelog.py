"""
Parser for boto3 changelog.
"""

import re
from typing import IO
from urllib.error import HTTPError
from urllib.request import urlopen


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
        try:
            response: IO[bytes]
            with urlopen(cls.URL) as response:
                return response.read().decode("utf-8")
        except HTTPError as e:
            raise RuntimeError(f"Cannot retrieve {cls.URL}: {e}") from None

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
