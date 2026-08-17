

class Solution:
    def mySqrt(self, x: int) -> int:

        def bins(target: int, left: int, right: int) -> int:
            if left == right:
                return left
            elif left + 1 == right:
                if right * right <= target:
                    return right
                else:
                    return left
            else:
                mid = (left + right) // 2
                if target == mid * mid:
                    return mid
                elif target < mid * mid:
                    return bins(target, left, mid)
                else:
                    return bins(target, mid, right)

        return bins(x, 1, x)
