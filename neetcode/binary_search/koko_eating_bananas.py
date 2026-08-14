from typing import List
import math


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eating_time(piles: List[int], k: int) -> int:
            return sum(math.ceil(x / k) for x in piles)

        left, right = 1, max(piles)
        best_rate: int = right

        while left <= right:

            if left == right:
                rate = left
                t = eating_time(piles, rate)
                if t <= h and rate < best_rate:
                    best_rate = rate
                break
            elif left + 1 == right:

                if eating_time(piles, right) <= h:
                    if right < best_rate:
                        best_rate = right

                if eating_time(piles, left) <= h:
                    if left < best_rate:
                        best_rate = left

                break
            else:
                rate = (left + right) // 2
                t = eating_time(piles, rate)
                if t <= h:
                    right = rate
                    if rate < best_rate:
                        best_rate = rate
                else:
                    left = rate

        return best_rate
