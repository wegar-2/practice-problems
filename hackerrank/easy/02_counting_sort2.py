
def countingSort(arr):

    out: list[int] = [None] * len(arr)

    M = max(arr)
    counts = [0] * (M + 1)
    for x in arr:
        counts[x] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[ i -1]

    for x in reversed(arr):
        out[counts[x] - 1] = x
        counts[x] -= 1

    return out
