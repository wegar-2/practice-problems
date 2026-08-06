from typing import Any, Optional


__all__ = ["rotate1"]


def reverse_list_in_place(
        values: list[Any],
        left: int = 0,
        right: Optional[int] = None
) -> None:
    if right is None:
        right = len(values) - 1
    if left >= right:
        return
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1


def rotate1(nums: list[int], degree: int) -> list[int]:
    """
    Suboptimal solution
    """

    if degree < 0:
        raise ValueError(f"Invalid degree - negative number {degree}")
    if degree == 0:
        return nums
    degree = degree % len(nums)

    nums = nums[::-1]
    return nums[:degree][::-1] + nums[degree:][::-1]


def rotate2(nums: list[int], degree: int) -> None:

    if degree < 0:
        raise ValueError(f"Invalid degree - negative number {degree}")
    if degree == 0:
        return
    degree = degree % len(nums)

    # invert whole list in place
    reverse_list_in_place(nums)
    reverse_list_in_place(nums, left=0, right=degree - 1)
    reverse_list_in_place(nums, left=degree, right=len(nums) - 1)


if __name__ == "__main__":
    # nums = list(range(1, 11, 1))
    nums = list(range(1, 3, 1))
    # res = rotate1(nums, degree=3)
    # res = rotate2(nums, degree=3)
    res = rotate2(nums, degree=1)
    # reverse_list_in_place(nums)
    print(f"{nums=}")
    # print(f"{res=}")

