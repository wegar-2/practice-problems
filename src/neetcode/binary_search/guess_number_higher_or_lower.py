# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        def bin_search(left: int, right: int) -> int:
            if left == right:
                return left
            elif left + 1 == right:
                return left if guess(left) == 0 else right # noqa
            else:
                if (g := guess(mid := (left + right) // 2)) == 0: # noqa
                    return mid
                elif g == -1:
                    return bin_search(left, mid - 1)
                else:
                    return bin_search(mid + 1, right)

        return bin_search(1, n)
