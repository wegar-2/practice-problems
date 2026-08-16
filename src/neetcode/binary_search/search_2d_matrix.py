from bisect import bisect_left
from typing import List


class Solution:

    def _calc_row(self, matrix: List[List[int]], target) -> int:
        nums = [l[0] for l in matrix]
        pos = bisect_left(nums, target, 0, len(nums))

        if pos < len(nums) and nums[pos] <= target:
            return pos
        return pos - 1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_idx = self._calc_row(matrix, target)
        if row_idx == -1:
            return False

        row = matrix[row_idx]

        pos = bisect_left(row, target, 0, len(row))
        if pos < len(row) and row[pos] == target:
            return True
        else:
            return False
