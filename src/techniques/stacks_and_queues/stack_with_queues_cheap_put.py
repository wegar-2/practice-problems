from collections import deque


class IntStackCheapPut:

    def __init__(self):
        self._d: dict[int, deque[int]] = {0: deque([]), 1: deque([])}
        self._active: int = 0

    @property
    def values(self) -> list[int]:
        return [x for x in self._d[self._active]]

    def __len__(self):
        pass

    def _switch_active(self):
        self._active = 1 - self._active

    def put(self, x: int) -> None:
        self._d[self._active].append(x)

    def get(self) -> int | None:

        # special case - if the currently active queue contains
        # no elements - return None
        if len(self._d[self._active]) == 0:
            return None

        # move all but last element from the active queue to the other queue
        while len(self._d[self._active]) > 1:
            self._d[1 - self._active].append(self._d[self._active].popleft())
        out: int = self._d[self._active].popleft()

        # make the other the one that's currently active
        self._switch_active()

        return out


if __name__ == "__main__":
    stck = IntStackCheapPut()
    stck.put(10)
    stck.put(12)
    stck.put(1)
    stck.put(4)
    stck.put(7)

    print(f"{stck.values=}")
    print(f"{stck.get()=}")

    print(f"{stck.values=}")
    print(f"{stck.get()=}")

    print(f"{stck.values=}")
    print(f"{stck.get()=}")

    print(f"{stck.values=}")
    print(f"{stck.get()=}")

    print(f"{stck.values=}")
    print(f"{stck.get()=}")

    print(f"{stck.values=}")
    print(f"{stck.get()=}")
