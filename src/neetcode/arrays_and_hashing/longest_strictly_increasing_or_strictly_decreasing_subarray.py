from typing import List


class Solution:

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_len = 1
        dec_len = 1
        out = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc_len += 1
                dec_len = 1
            elif nums[i] < nums[i - 1]:
                inc_len = 1
                dec_len += 1
            else:
                inc_len = 1
                dec_len = 1

            out = max(out, inc_len, dec_len)

        return out
