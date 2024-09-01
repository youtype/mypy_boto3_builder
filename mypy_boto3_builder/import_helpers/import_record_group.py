"""
Group tool for ImportRecord sets.
"""

from collections.abc import Iterable, Iterator
from typing import Final

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString


class ImportRecordGroup:
    """
    Group tool for ImportRecord sets.
    """

    _SYS_IMPORT_RECORD: Final[ImportRecord] = ImportRecord(ImportString("sys"))

    def __init__(self, records: Iterable[ImportRecord] = ()) -> None:
        self.records: set[ImportRecord] = set()
        self.add(*records)

    def add(self, *records: ImportRecord) -> None:
        """
        Add record to group.
        """
        for record in records:
            if record.source.is_builtins():
                continue
            if record.needs_sys_fallback():
                self.add(self._SYS_IMPORT_RECORD)

            self.records.add(record)

    @staticmethod
    def _render_records(records: set[ImportRecord]) -> Iterator[str]:
        sources = {x.source for x in records}
        for source in sorted(sources):
            source_records = {i for i in records if i.source == source}
            names = (x.render_name() for x in sorted(source_records))
            yield f"from {source.render()} import {', '.join(names)}"

    def _iterate_render_nameless(self) -> Iterator[str]:
        """
        Iterate over nameless import records.
        """
        nameless_records = {i for i in self.records if not i.name}
        for record in sorted(nameless_records):
            yield record.render()

    def _iterate_render_regular(self) -> Iterator[str]:
        """
        Iterate over rendered regular records with name and no fallback.
        """
        regular_records = {
            i for i in self.records if i.name and not i.min_version and not i.fallback
        }
        yield from self._render_records(regular_records)

    def _iterate_render_source_fallback(self) -> Iterator[str]:
        """
        Iterate over rendered records with fallback but no min version.
        """
        records = {i for i in self.records if i.fallback and not i.min_version}
        sources = {x.source for x in records}
        for source in sorted(sources):
            source_records = {i for i in records if i.source == source}
            fallback_records = {i.fallback for i in source_records if i.fallback}
            yield "\n".join(
                (
                    "try:",
                    *(f"    {x}" for x in self._render_records(source_records)),
                    "except ImportError:",
                    *(f"    {x}" for x in self._render_records(fallback_records)),
                )
            )

    def _iterate_render_source_min_version(self) -> Iterator[str]:
        """
        Iterate over rendered records with min version.
        """
        records = {i for i in self.records if i.min_version}
        min_versions = {i.min_version for i in records if i.min_version}
        for min_version in sorted(min_versions):
            min_version_records = {i for i in records if i.min_version == min_version}
            min_version_str = ", ".join(str(i) for i in min_version)
            fallback_records = {i.fallback for i in min_version_records if i.fallback}
            yield "\n".join(
                (
                    f"if sys.version_info >= ({min_version_str}):",
                    *(f"    {x}" for x in self._render_records(min_version_records)),
                    "else:",
                    *(f"    {x}" for x in self._render_records(fallback_records)),
                )
            )

    def __iter__(self) -> Iterator[str]:
        """
        Iterate over all records grouped by source.
        """
        yield from self._iterate_render_nameless()
        yield from self._iterate_render_regular()
        yield from self._iterate_render_source_fallback()
        yield from self._iterate_render_source_min_version()
