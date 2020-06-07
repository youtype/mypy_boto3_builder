"""
Grouped by `source` import records for nicer rendering.
"""
from typing import Any, Iterable, List, Set

from mypy_boto3_builder.import_helpers.import_record import ImportRecord
from mypy_boto3_builder.import_helpers.import_string import ImportString


class ImportRecordGroup:
    """
    Grouped by `source` import records for nicer rendering.

    Arguments:
        source -- Common source for import records.
        import_records -- Grouped import records.
    """

    def __init__(self, source: ImportString, import_records: Iterable[ImportRecord]) -> None:
        self.source = source
        self.import_records = list(import_records)

    @classmethod
    def from_import_records(
        cls, import_records: Iterable[ImportRecord]
    ) -> List["ImportRecordGroup"]:
        """
        Get groups from `ImportRecord` list.

        Arguments:
            import_records -- Import records list.

        Returns:
            A list of generated `ImportRecordGroup`.
        """
        result: List[ImportRecordGroup] = []
        all_import_records: Set[ImportRecord] = set(import_records)

        for import_record in import_records:
            if import_record.fallback:
                all_import_records.add(ImportRecord(ImportString("sys")))

        for import_record in sorted(all_import_records):
            if not import_record:
                continue
            if import_record.is_builtins():
                continue
            if (
                not result
                or result[-1].source != import_record.source
                or not result[-1].import_records[0].name
                or import_record.is_standalone()
                or result[-1].import_records[0].is_standalone()
            ):
                result.append(ImportRecordGroup(import_record.source, [import_record]))
            else:
                result[-1].import_records.append(import_record)

        return result

    def is_builtins(self) -> bool:
        """
        Whether imports are from builtins.
        """
        return self.source.startswith(ImportRecord.builtins_import_string)

    def render(self) -> str:
        """
        Render to string.

        Returns:
            A valid Python import records group.
        """
        return "\n".join([i.render() for i in self.import_records])

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ImportRecordGroup):
            return False

        return self.render() == other.render()
