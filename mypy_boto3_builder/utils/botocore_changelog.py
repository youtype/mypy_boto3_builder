"""
Parser for boto3 changelog.
"""
import re
from functools import cache

import requests


class BotocoreChangelog:
    """
    Parser for boto3 changelog.
    """

    URL = "https://raw.githubusercontent.com/boto/botocore/develop/CHANGELOG.rst"

    @cache
    def _get_changelog(self) -> str:
        return requests.get(self.URL).content.decode()

    def _get_section(self, version: str) -> str:
        result: list[str] = []
        changelog = self._get_changelog()
        found = False
        for line in changelog.splitlines():
            if line == version:
                found = True
                continue
            if found and result and line.startswith("==="):
                break
            if found:
                result.append(line)

        return "\n".join(result[1:-1])

    def get_updated_service_names(self, version: str) -> list[str]:
        """
        Get a list of service names updated in `version` release.
        """
        result: list[str] = []
        section = self._get_section(version)
        for match in re.findall(r"``(\S+)``", section):
            if match not in result:
                result.append(match)

        return result
