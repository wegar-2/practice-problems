
class Solution:
    """This is the crude solution"""
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        lt, et, gt = [], [], []
        for x in nums:
            if x < pivot: lt.append(x)
            elif x == pivot: et.append(x)
            else: gt.append(x)
        out = [x for l in [lt, et, gt] for x in l]
        return out
