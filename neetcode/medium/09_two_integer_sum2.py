from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        j = len(numbers) - 1

        for i in range(len(numbers)):
            while numbers[i] + numbers[j] > target and i < j:
                j -= 1

            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            else:
                continue
