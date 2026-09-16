from typing import List


class Solution:
    """First of the solution"""
    
    def findDuplicate(self, nums: List[int]) -> int:

        if len(nums) == 2:
            return nums[0]

        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
        else:
            slow = 0
            while nums[slow] != nums[fast]:
                slow, fast = nums[slow], nums[fast]
            else:
                return nums[slow]
