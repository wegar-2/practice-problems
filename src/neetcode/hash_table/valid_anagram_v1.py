from collections import Counter

class Solution:
    """
    Super-naive solution using collections.Counter.
    Exploits - implicitly - the fact that in this problem, only lowercase
    English latter are allowed in the strings being compared,
    so there is a hard cap of 26 on the number of elements in a Counter
    which is O(c) memory
    """

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
