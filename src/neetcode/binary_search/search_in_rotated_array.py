from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # ROTATIONS OF 1...6 ARRAY
        # (1): 1 2 3 4 5 6
        # (2): 6 1 2 3 4 5
        # (3): 5 6 1 2 3 4
        # (4): 4 5 6 1 2 3
        # (5): 3 4 5 6 1 2
        # (6): 2 3 4 5 6 1
        left, right = 0, len(nums) - 1

        while left <= right:

            if left == right:
                if nums[left] == target:
                    return left

            if left + 1 == right:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right

            mid_idx = (left + right) // 2

            if nums[mid_idx] == target:
                return mid_idx

            if nums[left] <= nums[mid_idx - 1]:
                if nums[left] <= target <= nums[mid_idx - 1]:
                    right = mid_idx - 1
                else:
                    left = mid_idx + 1
            else:
                if target >= nums[mid_idx]:
                    left = mid_idx + 1
                else:
                    right = mid_idx - 1

        return -1

