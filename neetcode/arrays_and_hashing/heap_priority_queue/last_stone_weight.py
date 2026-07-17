import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h: list[int] = []

        for x in stones:
            heapq.heappush(h, -x)

        while len(h) > 1:
            stone1 = -heapq.heappop(h)
            stone2 = -heapq.heappop(h)

            if stone1 > stone2:
                stone = stone1 - stone2
            elif stone1 < stone2:
                stone = stone2 - stone1
            else:
                stone = None

            if stone is not None:
                heapq.heappush(h, -stone)

        if len(h) == 1:
            return -h[0]
        return 0