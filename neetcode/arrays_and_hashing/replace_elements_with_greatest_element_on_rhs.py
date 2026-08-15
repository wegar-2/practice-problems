from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        maxval: int = -1
        for i in range(len(arr) - 1, -1, -1):

            if i == len(arr) - 1:
                maxval = arr[-1]
                arr[-1] = -1
                continue

            prev = arr[i]
            arr[i] = maxval
            maxval = max(prev, maxval)

        return arr
