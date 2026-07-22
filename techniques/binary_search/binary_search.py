import random

from utils.utils import make_random_nums


def _check_sorted(nums: list[int]) -> None:
    for i in range(1, len(nums)):
        if nums[i-1] > nums[i]:
            raise ValueError("nums passed are not sorted ascending")


def binary_search(nums: list[int], target: int) -> int:
    _check_sorted(nums)

    left, right = 0, len(nums) - 1
    mid = len(nums) // 2

    while left <= right:
        if left == right:
            return -1 if nums[left] != target else left
        elif left + 1 == right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                return -1
        else:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid


if __name__ == "__main__":
    nums = sorted(make_random_nums(20))
    print(f"{nums=}")
    pos = random.randint(0, len(nums))
    target = nums[pos]
    print(f"{target=}")

    res = binary_search(nums, target)
    print(f"{res=}")
    print(f"{nums[res]=}")
