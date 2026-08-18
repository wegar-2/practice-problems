from itertools import product
from typing import List


class Solution:
    """ Brute force solution """

    def stringMatching(self, words: List[str]) -> List[str]:
        out = set()

        def match_strs(subs: str, s: str) -> bool:
            if len(subs) > len(s):
                return False
            for i in range(len(s) - len(subs) + 1):
                for j in range(len(subs)):
                    if s[i + j] != subs[j]:
                        break
                    if j == len(subs) - 1:
                        return True
            return False

        for i, j in product(range(len(words)), range(len(words))):
            if i == j:
                continue
            else:
                if match_strs(words[i], words[j]):
                    out.add(words[i])

        return list(out)
