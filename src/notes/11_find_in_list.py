

if __name__ == "__main__":

    nums = [12, 5, 123, 7, 5, 323, 1233, 100, 65, 5, 3232]

    # find position of first occurrence of 5 in the list
    pos5 = nums.index(5)
    print(f"{nums[pos5]=}")

    # find positions all occurrences of 5 in the list in one shot
    positions5 = [i for i, x in enumerate(nums) if x == 5]
    print(f"{positions5=}")

    # filter list by condition - usual list comprehension
    values_below10 = [x < 10 for x in nums]
    print(f"{values_below10=}")

    # positions of values satisfying a condition
    positions_below10 = [i for i, x in enumerate(nums) if x < 10]
    print(f"{positions_below10=}")

    # generator of values satisfying a condition
    gen_find5 = (i for i, x in enumerate(nums) if x == 5)
    for j, pos in enumerate(gen_find5):
        print(f"{j}-th 5 at position: {pos}")

    values = [5, 1, 23, 19, 43, 11, 2, 7, 123]
    res = next((i for i, x in enumerate(values) if x < 0), -1)
    print(f"{res=}")
