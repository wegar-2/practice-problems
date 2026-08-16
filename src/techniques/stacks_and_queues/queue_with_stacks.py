

class IntQueue:
    """
    Implementation of queue using two stacks.
    Yields average O(1) complexity of enqueue and dequeue operations.
    """

    def __init__(self):
        self._stack_in: list[int] = []
        self._stack_out: list[int] = []

    def enqueue(self, x: int) -> None:
        self._stack_in.append(x)

    def dequeue(self) -> int | None:

        if self._stack_out:
            return self._stack_out.pop()
        else:
            if self._stack_in:
                while self._stack_in:
                    self._stack_out.append(self._stack_in.pop())
                return self._stack_out.pop()
            else:
                print("Empty queue...")
                return None


if __name__ == "__main__":

    q = IntQueue()
    q.enqueue(10)
    q.enqueue(20)
    print(f"{q.dequeue()}")
    print(f"{q.dequeue()}")
    print(f"{q.dequeue()}")

    q.enqueue(1)
    q.enqueue(2)
    print(f"{q.dequeue()}")
    q.enqueue(3)
    print(f"{q.dequeue()}")
    print(f"{q.dequeue()}")
    print(f"{q.dequeue()}")
