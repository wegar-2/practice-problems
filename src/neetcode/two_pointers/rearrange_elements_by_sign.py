from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        next_pos = 0
        next_neg = 1
        out = [None for _ in nums]

        for x in nums:
            if x > 0:
                out[next_pos] = x
                next_pos += 2
            else:
                out[next_neg] = x
                next_neg += 2

        return out
