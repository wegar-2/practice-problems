from typing import List


class Solution:
    """
    Memory intensive & dirty solution based on sets
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return 0

        word: str = strs[0]

        for i, s in enumerate(strs):
            strs[i] = {(j, l) for j, l in enumerate(s)}

        intersection: set = strs[0]
        if len(intersection) > 1:
            for tups in strs[1:]:
                intersection &= set(tups)
        intersection = {tup[0] for tup in intersection}

        out: int = 0
        for i in range(len(intersection)):
            if i in intersection:
                out += 1
            else:
                break
        return word[:out]
