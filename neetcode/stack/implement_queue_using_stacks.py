
class MyQueue:

    def __init__(self):
        self._stack_in: list[int] = []
        self._stack_out: list[int] = []

    def push(self, x: int) -> None:
        self._stack_in.append(x)

    def pop(self) -> int:
        if not self._stack_out:
            while self._stack_in:
                self._stack_out.append(self._stack_in.pop())
        return self._stack_out.pop()

    def peek(self) -> int:
        if self._stack_out:
            return self._stack_out[-1]
        else:
            return self._stack_in[0]

    def empty(self) -> bool:
        return not self._stack_in and not self._stack_out
