from mypy_boto3_builder.constants import ALL
from mypy_boto3_builder.utils.lookup_dict import LookupDict


class TestLookupDict:
    def test_get(self) -> None:
        lookup_dict: LookupDict[int] = LookupDict(
            {"test": {"one": {"child1": 1}, ALL: {"child2": 10}}, ALL: {"two": {"child3": 12}}},
        )
        assert lookup_dict.get("test", "one", "child1") == 1
        assert lookup_dict.get("test", "one", "child2") == 10
        assert lookup_dict.get("test", "one", "child3") is None
        assert lookup_dict.get("test", "two", "child1") is None
        assert lookup_dict.get("test", "two", "child2") == 10
        assert lookup_dict.get("test2", "two", "child2") is None
        assert lookup_dict.get("test2", "two", "child3") == 12

    def test_static(self) -> None:
        lookup_dict: LookupDict[int] = LookupDict(
            {"test": {"one": {"child1": 1}, "two": {"child2": 10}}},
        )
        assert lookup_dict.get("test", "one", "child1") == 1
        assert lookup_dict.get("test", "one", "child2") is None
        assert lookup_dict.get("test", "two", "child1") is None
        assert lookup_dict.get("test", "two", "child2") == 10
