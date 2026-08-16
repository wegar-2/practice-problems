

def _make_subsets(nums: list[int], inclusions: list[bool]) -> list[list[int]]:
    out: list[list[int]] = []

    if len(nums) == len(inclusions):
        return [[
            nums[i] for i in range(len(nums)) if inclusions[i]
        ]]

    inclusions.append(False)
    print(f"{inclusions=}")
    out += _make_subsets(nums, inclusions)
    inclusions.pop()
    inclusions.append(True)
    print(f"{inclusions=}")
    out += _make_subsets(nums, inclusions)
    inclusions.pop()

    return out

def make_subsets(nums: list[int]) -> list[list[int]]:
    out: list[list[int]] = []
    out += _make_subsets(nums, [False])
    out += _make_subsets(nums, [True])
    return out


if __name__ == "__main__":
    res = make_subsets(nums=[1, 2, 3])
    print(res)