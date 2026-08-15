from typing import List


class Solution:
    """
    Naive / common sense solution
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return 0

        min_: int = min(len(s) for s in strs)

        result = True
        len_: int = 0
        for i in range(min_):
            l: str = strs[0][i]

            if len(strs) > 1:
                for s in strs[1:]:
                    result &= s[i] == l
                    if not result:
                        break

            if not result:
                break
            else:
                len_ += 1

        return strs[0][:len_]
