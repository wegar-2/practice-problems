from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        mru: int = 0
        min_pointer: int = 0

        for i, x in enumerate(prices):
            if prices[min_pointer] > x:
                min_pointer = i
            cru = x - prices[min_pointer]
            if cru > mru:
                mru = cru

        return mru
