from collections import Counter, defaultdict
import heapq


class KLargest:

     def __init__(self, k: int):
          self._k: int = k
          self._k_largest: dict[int, int] = {}
          self._min: int | None = None

     def insert(self, x: int) -> None:
          if len(self._k_largest) < self._k:
               pass
          else:
               pass

     @property
     def min(self) -> int | None:
          return self._min


def top_k_counts(nums: list[int], k: int):

     counts = Counter(nums)
     l = []

     for v, c in counts.items():
          heapq.heappush(l, (c, v))

     return [x[1] for x in heapq.nlargest(k, l)]
