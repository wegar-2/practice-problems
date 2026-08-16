from collections import deque
from queue import Queue


if __name__ == "__main__":

    # 1. stack - can only add on top and pop from top; proverbial stack of
    # plates in canteen; FIFO queue
    stck: list[int] = [] # noqa

    stck.append(1)
    stck.append(3)
    stck.pop()
    stck.pop()


    # 2. queue: LIFO queue - using python's queue.Queue
    queue: Queue[int] = Queue()

    # adding to queue: .put aka enqueue
    queue.put(1)
    queue.put(10)
    queue.put(3)

    # taking off the queue: .get aka dequeue
    while queue:
        print(f"{queue.get()=}")


    # 3. deque: supports adding and removing from both ends
    # using python's collections.deque
    deq: deque[int] = deque([])
    deq.append(3)
    deq.append(10)
    deq.appendleft(9)
    print(f"{deq.popleft()=}")
    print(f"{deq.pop()=}")
