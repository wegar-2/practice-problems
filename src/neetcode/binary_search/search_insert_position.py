from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:

        def find(
                nums: List[int],
                target: int,
                left: int,
                right: int,
        ):
            if left == right:
                if nums[left] == target:
                    return left
                elif nums[left] > target:
                    return left
                else:
                    return left + 1
            elif left + 1 == right:
                if target < nums[left]:
                    return left
                elif target == nums[left]:
                    return left
                elif nums[left] < target < nums[right]:
                    return left + 1
                elif target == nums[right]:
                    return right
                else:
                    return right + 1
            else:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return find(nums, target, left, mid)
                else:
                    return find(nums, target, mid, right)

        return find(nums, target, 0, len(nums) - 1)
