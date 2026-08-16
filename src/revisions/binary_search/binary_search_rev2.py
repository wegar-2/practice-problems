from typing import Optional


def binsearch(
        nums: list[int],
        target: int,
        left: int = 0,
        right: Optional[int] = None
) -> int:

    if right is None:
        right = len(nums) - 1

    if left == right:
        if nums[left] == target:
            return left
        else:
            return -1

    if left + 1 == right:
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1

    mid = (left + right) // 2

    if (mid_val := nums[mid]) == target:
        return mid
    elif mid_val > target:
        return binsearch(nums, target, left, mid - 1)
    else:
        return binsearch(nums, target, mid + 1, right)


if __name__ == "__main__":
    nums = [1, 4, 5, 10, 23, 32, 344, 901]
    target = 10
    print(f"{binsearch(nums, target)=}")
