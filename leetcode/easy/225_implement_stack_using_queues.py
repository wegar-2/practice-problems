from collections import deque


class MyStack:
    """
    Implementation here allows for O(1) push and O(n) pop
    """

    def __init__(self):
        self._d: dict[int, deque] = {
            0: deque([]),
            1: deque([])
        }
        self._active: int = 0

    def _switch_active(self):
        self._active = 1 - self._active

    def push(self, x: int) -> None:
        self._d[self._active].append(x)

    def _switch_queues(self) -> int:
        while len(self._d[self._active]) > 1:
            self._d[1 - self._active].append(self._d[self._active].popleft())
        out: int = self._d[self._active].popleft()
        self._switch_active()
        return out

    def pop(self) -> int:
        return self._switch_queues()

    def top(self) -> int:
        out = self._switch_queues()
        self._d[self._active].append(out)
        return out

    def empty(self) -> bool:
        return len(self._d[0]) == 0 and len(self._d[1]) == 0
