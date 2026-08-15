from itertools import groupby
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len: int = 0
        for s, g in groupby(nums):
            if s == 1 and (l := len(list(g))) > max_len:
                max_len = l
        return max_len
