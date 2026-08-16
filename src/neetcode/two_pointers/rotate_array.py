from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def reverse(nums: List[int], left: int, right: int) -> None:
            if left >= right:
                return
            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # step1: reverse whole array
        reverse(nums, 0, len(nums) - 1)

        # step2: reverse slice up to k
        reverse(nums, 0, k - 1)

        # step 3 reverse slice from k up
        reverse(nums, k, len(nums) - 1)
