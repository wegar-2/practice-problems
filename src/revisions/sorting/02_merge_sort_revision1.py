

def _merge(
        left: list[int],
        right: list[int]
) -> list[int]:

    l, r = 0, 0
    out: list[int] = []

    while l < len(left) or r < len(right):
        if l < len(left) and r < len(right):
            if left[l] <= right[r]:
                out.append(left[l])
                l += 1
            else:
                out.append(right[r])
                r += 1
        elif l < len(left):
            out.append(left[l])
            l += 1
        else:
            out.append(right[r])
            r += 1
    return out


def merge_sort(values: list[int]) -> list[int]:

    if len(values) <= 1:
        return values
    else:
        mid = len(values) // 2
        left = merge_sort(values[:mid])
        right = merge_sort(values[mid:])
        return _merge(left, right)


if __name__ == "__main__":

    # res = _merge(
    #     left=[1, 2, 3, 5, 10],
    #     right=[3, 4, 5, 10, 23]
    # )
    # print(f"{res=}")

    values = [19, 4, 1, 3, 8, 67, 4, 5, 3, 2, 9, 11, 23, 43, 23]
    res = merge_sort(values=values)
    print(f"{res=}")
