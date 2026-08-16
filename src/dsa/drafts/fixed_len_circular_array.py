from array import array


class FixedLenCircularArray:

    def __init__(self, max_len: int = 10):
        self._memory: array[int] = array("i", [0 for _ in range(max_len)])
        self._start: int = 0
        self._end: int = 0

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def pop(self) -> int:
        pass

    def popleft(self) -> int:
        pass
