from typing import List


class Solution:
    """
    this is a suboptimal solution.
    It can be improved upon by making use of the fact that search for the
    least number greater than the val on the left of first drop
    can be simplified by using the monotonicity of all the elements to the
    right of that value
    """

    def nextPermutation(self, nums: List[int]) -> None:

        if len(nums) == 1:
            return

        # step 1: find first drop from the right
        pointer: int = len(nums) - 2
        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -= 1

        if pointer == -1:
            nums.reverse()
            return

        # step 2: determine the value to insert into position pointer
        new_val_pos: int = pointer + 1
        new_val: int = nums[pointer + 1]
        for i in range(pointer + 1, len(nums)):
            if new_val > nums[i] > nums[pointer]:
                new_val = nums[i]
                new_val_pos = i
        # replace the value at pointer with new_va
        old_val: int = nums[pointer]
        nums[pointer] = new_val
        nums[new_val_pos] = old_val

        # step 3: ensure that pointer+1 to the end is ordered descending
        for i in range(pointer + 1, len(nums) - 2):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        # step 4: reverse order of positions pointer+1 until end
        left, right = pointer + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
