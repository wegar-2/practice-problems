import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        h: list[int] = []

        for x in nums:

            if len(h) < k:
                heapq.heappush(h, x)
            else:
                if h[0] < x:
                    heapq.heappop(h)
                    heapq.heappush(h, x)
                else:
                    pass

        return h[0]
