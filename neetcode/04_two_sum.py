from collections import defaultdict


def two_sum(nums: list[int], target: int):

    needs_for_target = defaultdict(list)

    for i, x in enumerate(nums):
        if x in needs_for_target:
            return [needs_for_target[x][0], i]
        needs_for_target[target-x].append(i)

