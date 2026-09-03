from typing import List
from collections import Counter


class Solution:
    """
    Brute-force suboptimal solution.
    Worst case space complexity: O(n)
    Slight variation of solution 3 in which collections.Counter was not used.
    """
    def majorityElement(self, nums: List[int]) -> int:
        counts: Counter = Counter(nums)
        max_count: int = max(counts.values())
        return [k for k, v in counts.items() if v == max_count][0]
