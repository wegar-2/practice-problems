from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def bisect(nums: List[int], left: int, right: int) -> int:

            if left == right:
                return left

            if left + 1 == right:
                if nums[left] < nums[right]:
                    return nums[left]
                else:
                    return nums[right]

            mid: int = (left + right) // 2

            left_monotonic: bool = nums[left] < nums[mid]
            right_monotonic: bool = nums[mid] < nums[right]
            if left_monotonic and right_monotonic:
                return nums[left]

            if left_monotonic:
                return bisect(nums, mid, right)
            else:
                return bisect(nums, left, mid)

        return bisect(nums, 0, len(nums) - 1)
