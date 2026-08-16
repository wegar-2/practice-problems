from array import array
import heapq
from typing import List


class Solution:

    _MIN: int = -1_000
    _MAX: int = 1_000

    @classmethod
    def _to_idx(cls, x: int) -> int:
        return x - cls._MIN

    @classmethod
    def _from_idx(cls, i: int) -> int:
        return i + cls._MIN

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ar = array("i", [0] * (self._MAX - self._MIN + 1))
        for x in nums:
            ar[self._to_idx(x)] += 1

        k_largest_counts = []
        for i, el in enumerate(ar):
            if len(k_largest_counts) < k:
                heapq.heappush(k_largest_counts, (el, self._from_idx(i)))
            else:
                if el > k_largest_counts[0][0]:
                    heapq.heappop(k_largest_counts)
                    heapq.heappush(k_largest_counts, (el, self._from_idx(i)))

        return k_largest_counts
