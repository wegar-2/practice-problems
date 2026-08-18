from typing import List


class Solution:
    """
    Key observation - when moving the pointer rightward once
    I encounter a single observation breaking monotnicity,
    I have to start anew
    """

    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        best_len = 1
        left = 0
        for right in range(len(nums)):
            if right > left:
                if nums[right] > nums[right - 1]:
                    best_len = max(best_len, right - left + 1)
                else:
                    left = right
        left = 0
        for right in range(len(nums)):
            if right > left:
                if nums[right] < nums[right - 1]:
                    best_len = max(best_len, right - left + 1)
                else:
                    left = right

        return best_len
