"""
Lookup dictionary to get values by multiple keys.
"""

import itertools
from collections.abc import Iterator, Mapping
from typing import Generic, TypeVar, cast

from mypy_boto3_builder.constants import ALL

_T = TypeVar("_T")
_V = TypeVar("_V")


class LookupDict(Generic[_V]):
    """
    Lookup dictionary to get values by multiple keys.

    Arguments:
        hash_map -- Initial hash map.
        required_keys -- Number of required keys in th end of key tuple.
    """

    def __init__(
        self,
        hash_map: Mapping[str, _T],
        required_keys: int = 1,
    ) -> None:
        self._hash_map = hash_map
        self._lookup_hash_map: dict[tuple[str, ...], _V] = {}
        self._keys_len = 0
        self._required_keys = required_keys
        self._products: tuple[tuple[bool, ...], ...] = ()

    @property
    def _lookup(self) -> dict[tuple[str, ...], _V]:
        if not self._lookup_hash_map:
            self._lookup_hash_map = self._generate_lookup(
                {str(k): v for k, v in self._hash_map.items()}, ()
            )
            self._keys_len = len(next(iter(self._lookup_hash_map)))
            self._products = tuple(
                itertools.product((True, False), repeat=self._keys_len - self._required_keys)
            )

        return self._lookup_hash_map

    def _generate_lookup(
        self, hash_map: Mapping[str, _T], keys: tuple[str, ...]
    ) -> dict[tuple[str, ...], _V]:
        result: dict[tuple[str, ...], _V] = {}
        for key, value in hash_map.items():
            if isinstance(value, Mapping):
                value = cast(Mapping[str, _T], value)  # type: ignore
                result.update(self._generate_lookup(value, (*keys, key)))
            else:
                value_v = cast(_V, value)  # type: ignore
                result[(*keys, key)] = value_v
        return result

    def _iterate_lookup_keys(self, keys: tuple[str, ...]) -> Iterator[tuple[str, ...]]:
        if len(keys) != self._keys_len:
            raise ValueError(f"Got {len(keys)}, {self._keys_len} expected: {keys}")

        optional_keys = keys[: -self._required_keys]
        required_keys = keys[-self._required_keys :]
        for product in self._products:
            yield (
                *(key if product[i] else ALL for i, key in enumerate(optional_keys)),
                *required_keys,
            )

    def get(self, *keys: str) -> _V | None:
        """
        Get value by multiple keys.
        """
        lookup = self._lookup
        for lookup_keys in self._iterate_lookup_keys(keys):
            result = lookup.get(lookup_keys)
            if result is not None:
                return result
        return None
