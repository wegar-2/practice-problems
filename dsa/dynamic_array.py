from __future__ import annotations
from array import array

__all__ = ["DynamicIntArray"]


class DynamicIntArray:

    def __init__(self, mem_block_size: int = 16):
        self._private_len: int = mem_block_size
        self._array: array = array("i", [0 for _ in range(mem_block_size)])
        self._public_len: int = 0

    def __len__(self) -> int:
        return self._public_len

    def __setitem__(self, key: int, value):
        pass

    def __delitem__(self, key):
        pass

    def __getitem__(self, item: int) -> int:
        if item < self._public_len:
            return self._array[item]
        raise IndexError(f"Tried to reach out to the index {item} in "
                         f"array of length {self._public_len}")

    def _extend_array(self) -> None:
        pass

    def _reduce_array(self):
        pass

    def append(self, value: int) -> None:
        pass

    def pop(self, value) -> int:
        pass
