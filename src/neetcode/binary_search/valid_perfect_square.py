

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        def bin_search(num: int, left: int, right: int) -> bool:

            if left == right:
                if left ** 2 == num:
                    return True
                else:
                    return False
            elif left + 1 == right:
                if left ** 2 == num or right ** 2 == num:
                    return True
                else:
                    return False
            else:
                mid = (left + right) // 2
                if (sq := mid ** 2) == num:
                    return True
                elif sq > num:
                    return bin_search(num, left, mid - 1)
                else:
                    return bin_search(num, mid + 1, right)

        return bin_search(num, 0, num)
