"""
Parser for boto3 changelog.
"""
import re
from urllib.request import urlopen


class BotocoreChangelog:
    """
    Parser for boto3 changelog.
    """

    URL = "https://raw.githubusercontent.com/boto/botocore/develop/CHANGELOG.rst"

    def __init__(self) -> None:
        self._changelog: str | None = None

    def _get_changelog(self) -> str:
        if self._changelog is not None:
            return self._changelog

        with urlopen(self.URL) as response:
            self._changelog = response.read().decode()

        return self._changelog

    def _get_section(self, version: str) -> str:
        result: list[str] = []
        changelog = self._get_changelog()
        found = False
        for line in changelog.splitlines():
            if line == version:
                found = True
                continue
            if found and result and line.startswith("==="):
                result.pop()
                break
            if found:
                result.append(line)

        return "\n".join(result[1:])

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
