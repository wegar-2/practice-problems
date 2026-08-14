import heapq
from typing import List


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        out: list[int] = []
        heap: list[tuple[int, int]] = []

        for i, x in enumerate(nums):
            heapq.heappush(heap, (-x, i))
            if i >= k - 1:
                while heap[0][1] > i or heap[0][1] < (i - k + 1):
                    heapq.heappop(heap)
                out.append(-heap[0][0])

        return out
