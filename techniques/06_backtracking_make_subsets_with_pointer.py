from typing import List


def _make_subsets(
        nums: List[int],
        all_subsets: List[List[int]],
        subset: List[int],
        pointer: int
) -> List[List[int]]:

    if pointer == len(nums):
        all_subsets.append([x for x in subset])
        return all_subsets

    all_subsets = _make_subsets(nums, all_subsets, subset, pointer + 1)
    subset.append(nums[pointer])
    all_subsets = _make_subsets(nums, all_subsets, subset, pointer + 1)
    subset.pop()

    return [x for x in all_subsets]


def make_subsets(nums: List[int]) -> List[List[int]]:
    return _make_subsets(nums, [], [], 0)


if __name__ == "__main__":
    print(make_subsets(nums=[1, 2]))