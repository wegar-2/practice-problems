import random


if __name__ == "__main__":

    len_ = random.randint(11, 20)

    nums = list(range(1, len_ + 1))

    # print non-empty slices starting at consecutive positions and reaching
    # until end of the array
    for start in range(len(nums)):
        print(f"{start}: {nums[start:]}")

    # symmetric case: shorten from the right
    for end in range(l := len(nums)):
        print(f"{end}: {nums[:l-end]}")

    # sliding window of fixed size using pointers
    w = 3 # size of the window
    for start in range(len(nums) - w + 1):
        print(f"{start=} ===> {nums[start:start+w]}")
    # why is the range above correct? take it in the following steps:
    # (1) give a slice starting at pos left and ending at right (both inclusive)
    # its width is:
    # w = right - left + 1 (*)
    # (2) you want slice of fixed size: w - fixed
    # (3) last window ends at right = l - 1
    # (4) using the formula (*) to get left:
    #     left = l - w + 1
    # (5) which works since for:
    # left = l - w
    # right = l - 1
    # right - left + 1 = l - 1 - l + w = w
    # l - w + (w - 1) = l - 1