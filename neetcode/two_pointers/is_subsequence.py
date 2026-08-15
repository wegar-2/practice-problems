

class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True

        sp = -1
        for i in range(len(t)):
            if s[sp + 1] == t[i]:
                sp += 1
                if sp == len(s) - 1:
                    return True
        return False
