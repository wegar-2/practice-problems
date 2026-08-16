

class Solution:

    def appendCharacters(self, s: str, t: str) -> int:

        if len(s) == 0:
            return len(t)

        # it's pointing at the position that's currently being scanned
        tpointer: int = 0

        for x in s:
            if t[tpointer] == x:
                tpointer += 1
                if tpointer >= len(t):
                    break

        return (len(t) - 1) - tpointer + 1
