from typing import List


class Solution:
    """
    pointers based solution implemented more elegantly
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return 0

        w = strs[0]

        for i, x in enumerate(w):
            for s in strs[1:]:
                if len(s) == i or s[i] != w[i]:
                    return w[:i]

        return w
