from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # key idea: two passages through the array are required - the second one is to allow 
        # for checking for element that's greater than last element of nums
        out: list[int] = [-1 for _ in nums]
        mstack: list[tuple[int, int]] = []

        # first passage
        for i, x in enumerate(nums):
            while mstack:
                j, y = mstack[-1]
                if y < x:
                    mstack.pop()
                    out[j] = x
                else:
                    break
            mstack.append((i, x))

        for i, x in enumerate(nums):
            while mstack:
                j, y = mstack[-1]
                if y < x:
                    mstack.pop()
                    out[j] = x
                else:
                    break
            mstack.append((i, x))

        return out
