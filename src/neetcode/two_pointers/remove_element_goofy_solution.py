from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        c = 0
        for j in range(len(nums)):
            if nums[j] == val:
                nums[j] = None
            else:
                c += 1

        if c > 0:
            l, r = 0, len(nums) - 1
            while l < r:
                while nums[l] is not None and l < len(nums) - 1:
                    l += 1
                while nums[r] is None and r > 0:
                    r -= 1

                if l > r:
                    break
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        return c
