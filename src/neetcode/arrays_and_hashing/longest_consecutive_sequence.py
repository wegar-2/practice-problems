from collections import Counter

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        d: dict[int, int] = {}

        for i, x in enumerate(nums):

            if x in d:
                continue

            if x - 1 in d and x + 1 in d:
                d[x] = d[x - 1]
                j = x + 1
                while j in d:
                    d[j] = d[x - 1]
                    j += 1
            elif x - 1 in d:
                d[x] = d[x - 1]
            elif x + 1 in d:
                d[x] = d[x + 1]
            else:
                d[x] = i

        return max(Counter(d.values()).values())
