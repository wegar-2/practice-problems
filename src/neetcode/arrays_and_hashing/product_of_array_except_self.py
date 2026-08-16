from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_products = [nums[0]]
        right_products = [nums[-1]]

        for i in range(1, len(nums) - 1):
            left_products.append(nums[i] * left_products[-1])
            right_products.append(nums[len(nums) - 1 - i] * right_products[-1])

        right_products = right_products[::-1]

        out = []

        for i in range(len(nums)):
            if i == 0:
                out.append(right_products[i])
            elif 1 <= i <= len(nums) - 2:
                out.append(left_products[i-1] * right_products[i])
            else:
                out.append(left_products[-1])

        return out


if __name__ == "__main__":
    s = Solution()
    nums = [1, 5, 3, 1, 4, 3, 0]
    print(s.productExceptSelf(nums))