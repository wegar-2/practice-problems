import heapq
import math
from typing import List


class Solution:

    def _origin_dist(self, point: List[int]) -> float:
        x, y = point[0], point[1]
        return math.sqrt(x ** 2 + y ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        h: List[tuple[float, List[int]]] = []
        for p in points:
            point_d = self._origin_dist(p)
            if len(h) < k:
                heapq.heappush(h, (-point_d, p))
            else:
                heappoint_d, heappoint = h[0]
                heappoint_d = -heappoint_d
                if heappoint_d > point_d:
                    heapq.heappop(h)
                    heapq.heappush(h, (-point_d, p))

        return [p for _, p in h]
