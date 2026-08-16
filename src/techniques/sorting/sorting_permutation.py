

def make_sorting_dict(nums: list[int]) -> dict[int, int]:
    srtd = sorted([(i, x) for i, x in enumerate(nums)], key=lambda x: x[1])
    return {i: srtd[i][0] for i in range(len(nums))}


def make_sorting_perm(nums: list[int]) -> list[int]:
    srtd = sorted([(i, x) for i, x in enumerate(nums)], key=lambda x: x[1])
    return [x[0] for x in srtd]


if __name__ == "__main__":

    # example 1:
    nums = [10, 3, 7, 5, 2, 31]
    nums = [(i, x) for i, x in enumerate(nums)]

    sorted_nums = sorted(nums, key = lambda x: x[1])
    print(sorted_nums)

    sorting_permutation = [x[0] for x in sorted_nums]
    sorting_dict = dict(zip(
        [i for i in range(len(sorting_permutation))], sorting_permutation))

    print(f"{nums=}")
    print(f"{sorting_permutation=}")

    print("Sorting permutation")
    for k, v in sorting_dict.items():
        print(f"{k} -----> {v} -----> {nums[v][1]}")

    # using two-line function to calculate sorting permutations
    nums = [10, 3, 7, 5, 2, 31]
    print(f"{make_sorting_perm(nums)=}")
    print(f"{make_sorting_dict(nums)=}")