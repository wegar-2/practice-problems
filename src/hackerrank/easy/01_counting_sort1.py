
def countingSort(arr):
    M = max(arr)
    print(f"{M=}")
    counts = [0] * 100
    for x in arr:
        counts[x] += 1
    return counts
