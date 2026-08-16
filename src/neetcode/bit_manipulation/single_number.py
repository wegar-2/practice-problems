

def single_number(nums: list[int]):
    out = nums[0]
    for x in nums[1:]:
        out = out ^ x
    return out


if __name__ == "__main__":
    print(single_number(nums=[2, 3, 3]))