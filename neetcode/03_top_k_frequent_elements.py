from collections import Counter


def top_k_counts(nums: list[int], k: int):
    vals_by_count = [None] * 1_000

    for v, c in Counter(nums).items():
        if vals_by_count[c - 1] is None:
            vals_by_count[c - 1] = []
        vals_by_count[c - 1].append(v)

    top_k = []
    i = 999
    while len(top_k) < k and i > -1:
        if vals_by_count[i] is not None:
            top_k.extend(vals_by_count[i])
        i -= 1

    return top_k


if __name__ == "__main__":
    print(top_k_counts([1,2,2,3,3,3], 2))