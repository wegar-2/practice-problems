from typing import List


class Solution:
    """More succinct implementation"""
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while (slow := nums[slow]) != (fast := nums[nums[fast]]):
            pass
        slow = 0
        while (slow := nums[slow]) != (fast := nums[fast]):
            pass
        return slow
