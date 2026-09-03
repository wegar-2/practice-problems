from typing import List
from collections import defaultdict


class Solution:
    """
    Brute-force suboptimal solution.
    """
    def majorityElement(self, nums: List[int]) -> int:
        counts: defaultdict[int, int] = defaultdict(int)
        for x in nums:
            counts[x] += 1
        max_count: int = max(counts.values())
        return [
            k for k, v in counts.items() if v == max_count
        ][0]
