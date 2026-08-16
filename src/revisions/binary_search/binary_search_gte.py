from typing import Optional


def binary_search_gte(
        nums: list[int],
        target: int,
        left: int = 0,
        right: Optional[int] = None
) -> int:
    """
    An implementation of binary search for first element in sorted list that
    is greater than or equal to target.
    """

    if not nums:
        return -1

    if right is None:
        right = len(nums) - 1

    if left == right:
        if nums[left] >= target:
            return left
        else:
            return -1

    if left + 1 == right:
        if nums[left] >= target:
            return left
        elif nums[right] >= target:
            return right
        else:
            return -1

    mid = (left + right) // 2

    if nums[mid] >= target:
        return binary_search_gte(nums, target, left, mid)
    else:
        return binary_search_gte(nums, target, mid + 1, right)


if __name__ == "__main__":

    # nums = [12]
    # nums = [12]
    nums = [1, 2, 5, 9, 13, 15, 19, 23, 123, 323, 909, 100001]
    target = 20

    print(f"{binary_search_gte(nums, target)=}")
