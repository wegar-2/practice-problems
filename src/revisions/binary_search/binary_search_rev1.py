
# idx: 0, 1, 2, 3, 4
# val: 9  2  3  4  1


def binary_search(
        nums: list[int],
        target: int,
        left: int = 0,
        right: int | None = None
) -> int:
    if not right:
        right = len(nums) - 1

    # base case 1: list of len 1
    if left == right:
        if nums[left] == target:
            return left
        else:
            return -1

    # base case 2: list of len 2
    if left + 1 == right:
        if target == nums[left]:
            return left
        elif target == nums[right]:
            return right
        else:
            return -1

    mid = (left + right) // 2
    if target == (mid_val := (nums[mid])):
        return mid
    elif target < mid_val:
        return binary_search(nums, target, left, mid - 1)
    else:
        return binary_search(nums, target, mid + 1, right)


# Observations:
# (1) start length is 2k + 1; mid = (0 + 2k) // 2 = k
# (2) start length is 2k: mid = (0 + 2k - 1) // 2 = k - 1, e.g k = 3;
#     2k - 1 = 5 ===> // 2 ====> 2
#     2*(k-1) < 2*k - 1 < 2*k
#     k-1 < k - 1/2 < 2 ====> flooring =====> k - 1
# To wrap up:
#       (a) start_len = 2k + 1 ===> mid = k
#       (b) start_len = 2k =====> mid = k - 1
#


if __name__ == "__main__":
    res = binary_search([1, 4, 10, 2323, 324444], 100)
    print(f"{res=}")