import random
from utils.utils import make_random_nums


def find_gen(nums: list[int], target: int):
    for i, x in enumerate(nums):
        if x == target:
            yield i


def find_occ_positions1(nums: list[int], value: int) -> list[int]:
    out: list[int] = []
    j: int = -1
    while True:
        try:
            offset = nums[j+1:].index(value)
        except ValueError or IndexError:
            break
        else:
            j += (1 + offset)
            out.append(j)
    return out


if __name__ == '__main__':
    random.seed(123_456)
    nums: list[int] = make_random_nums(10, 1, 20)
    print(f"{nums=}")

    target = 1

    print("using generator - v1")
    for pos in find_gen(nums, target):
        print(f"{pos=}")

    print("using generator - v2")
    for pos in (i for i, x in enumerate(nums) if x == target):
        print(f"{pos=}")

    print("using function: ")
    print(f"{find_occ_positions1(nums, target)=}")
