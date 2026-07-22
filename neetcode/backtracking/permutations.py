from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        out: List[List[int]] = []
        used: List[bool] = [False for _ in range(len(nums))]
        current: List[int] = []

        def _recurse():
            if len(current) == len(nums):
                out.append([x for x in current])
            else:
                for i in range(len(nums)):
                    if not used[i]:
                        current.append(nums[i])
                        used[i] = True
                        _recurse()
                        current.pop()
                        used[i] = False

        _recurse()

        return out
