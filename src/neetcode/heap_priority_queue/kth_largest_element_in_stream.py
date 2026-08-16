import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._heap: list[int] = []
        self._k: int = k
        for i, x in enumerate(nums):
            if i < k:
                heapq.heappush(self._heap, nums[i])
            else:
                if x > self._heap[0]:
                    heapq.heappop(self._heap)
                    heapq.heappush(self._heap, x)

    def add(self, val: int) -> int:
        if len(self._heap) < self._k:
            heapq.heappush(self._heap, val)
        else:
            if val > self._heap[0]:
                heapq.heappop(self._heap)
                heapq.heappush(self._heap, val)
        return self._heap[0]
