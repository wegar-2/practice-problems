# Can be used when k = O(n) with n - array length, k - range of values in the array being sorted

def _min_max(values: list[int]) -> tuple[int, int]:
    m, M = values[0], values[0]

    for x in values[1:]:
        if x < m:
            m = x
        if x > M:
            M = x

    return m, M


def counting_sort(values: list[int]) -> list[int]:

    m, M = _min_max(values=values)
    counts: list[int] = [0] * (M - m + 1)
    out = [None] * len(values)

    for x in values:
        counts[x - m] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    for x in reversed(values):
        out[counts[x - m] - 1] = x
        counts[x - m] -= 1

    return out


if __name__ == "__main__":
    res = counting_sort(values=[1, 6, 2, 3, 4, 1, 11, 7, 1, 2])
    print(f"{res=}")
