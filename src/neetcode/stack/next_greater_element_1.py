from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # first step - run the usual search for next greater than on nums2
        mstack: list[tuple[int, int]] = []
        nge: list[int] = [-1 for _ in nums2]
        for i, x in enumerate(nums2):
            if mstack:
                while mstack:
                    j, y = mstack.pop()
                    if y < x:
                        nge[j] = x
                    else:
                        mstack.append((j, y))
                        break
            mstack.append((i, x))

        # second step: map the results from nums2 to nums2 - this is possible
        # due to uniqueness of elements of nums2
        nums2_to_nge: dict[int, int] = {
            nums2[i]: nge[i] for i in range(len(nums2))
        }
        return [nums2_to_nge[x] for x in nums1]
