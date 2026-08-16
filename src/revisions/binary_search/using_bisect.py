import random
import bisect
from utils.utils import make_random_nums

def binsearch(
        nums: list[int],
        target: int,
        left: int,
        right: int
):
    idx = bisect.bisect_left(nums, target, left, right)
    if nums[idx] == target and idx < right:
        return idx
    return -1


if __name__ == "__main__":

    random.seed(123)
    nums = sorted(make_random_nums(10))
    print(f"{nums=}")

    res = bisect.bisect_left(nums, 100, 0, len(nums) - 1)
    print(f"{res=}")
