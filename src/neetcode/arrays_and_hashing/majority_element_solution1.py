from typing import List


class Solution:
    """
    This solution has time complexity O(n) and space complexity O(1).
    It is using the Boyer Moore voting algorithm:
    https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
    """

    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        candidate_count = 0

        for x in nums:
            if candidate is None:
                candidate = x
                candidate_count += 1
            else:
                if x == candidate:
                    candidate_count += 1
                else:
                    if candidate_count > 0:
                        candidate_count -= 1
                    else:
                        candidate = x
                        candidate_count += 1

        return candidate
