from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_set: set[int] = set()

        if k >= len(nums):
            for i in range(len(nums)):
                if nums[i] not in nums_set:
                    nums_set.add(nums[i])
                else:
                    return True
            return False

        for i in range(len(nums) - k):
            if i == 0:
                for j in range(0, k + 1):
                    if nums[j] not in nums_set:
                        nums_set.add(nums[j])
                    else:
                        return True
            else:
                nums_set.remove(nums[i - 1])
                if nums[i + k] not in nums_set:
                    nums_set.add(nums[i + k])
                else:
                    return True
        return False
