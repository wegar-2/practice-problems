from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_valid = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[next_valid] = nums[j]
                next_valid += 1

        if next_valid < len(nums):
            for j in range(next_valid, max(next_valid + 1, len(nums))):
                nums[j] = None

        return next_valid
