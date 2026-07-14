from typing import List

from collections import defaultdict


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        single_num_waiting_for: defaultdict[int, int] = defaultdict(int)
        pairs_waiting_for: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)

        out: dict[tuple[int, int, int], int] = {}

        for i, x in enumerate(nums):

            if i > 0:
                if x in pairs_waiting_for :
                    for p in pairs_waiting_for[x]:
                        triplet = (p[0], p[1], x)
                        if triplet not in out:
                            out[tuple(sorted(triplet))] = 1

                for k, v in single_num_waiting_for.items():
                    # if x == 2:
                    #     print("halt")
                    # if -(x + v) not in pairs_waiting_for:
                    pairs_waiting_for[-(v + x)].append((
                        min(v, x),
                        max(v, x)
                    ))

                if 0 in single_num_waiting_for:
                    pairs_waiting_for[-x].append((
                        min(0, x),
                        max(0, x)
                    ))


            single_num_waiting_for[-x] = x

        return [list(k) for k in out]


if __name__ == "__main__":
    nums = [0, 1, 1]
    # nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(nums))
