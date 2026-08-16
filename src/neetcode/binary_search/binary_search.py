

def binary_search(
        values: list[int],
        target: int,
        left: int,
        right: int
) -> int:

    if left == right:
        if values[left] == target:
            return left
        else:
            return -1

    mid = (left + right) // 2
    if (midval := values[mid]) == target:
        return mid
    elif midval > target:
        return binary_search(values, target, left, mid - 1)
    else:
        return binary_search(values, target, mid + 1, right)


if __name__ == "__main__":

    values = [1, 5, 12, 13, 17, 20, 22, 26, 29, 31, 45, 101, 203, 445]

    # print(binary_search(values, 6, left=0, right=len(values)))
    # print(binary_search(values, 203, left=0, right=len(values)))
    print(binary_search(values, 203, left=0, right=len(values)))
