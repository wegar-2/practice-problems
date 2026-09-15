from collections import defaultdict


class Solution:
    """
    One level above naive solution: manually handle the list count and
    use the __eq__ of defaultdict.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        ds, dt = defaultdict(int), defaultdict(int)
        if len(s) != len(t):
            return False
        for ls, lt in zip(s, t):
            ds[ls] += 1
            dt[lt] += 1
        return ds == dt
