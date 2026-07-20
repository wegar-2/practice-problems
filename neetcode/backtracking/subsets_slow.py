from typing import List


class Solution:

    def _make_subsets(self, nums: List[int], inclusions: List[bool]) -> List[List[int]]:
        out: List[List[int]] = []

        if len(nums) == len(inclusions):
            return [[
                nums[i] for i in range(len(nums)) if inclusions[i]
            ]]

        inclusions.append(False)
        print(f"{inclusions=}")
        out += self._make_subsets(nums, inclusions)
        inclusions.pop()
        inclusions.append(True)
        print(f"{inclusions=}")
        out += self._make_subsets(nums, inclusions)
        inclusions.pop()

        return out

    def subsets(self, nums: List[int]) -> List[List[int]]:
        out: List[List[int]] = []
        out += self._make_subsets(nums, [False])
        out += self._make_subsets(nums, [True])
        return out