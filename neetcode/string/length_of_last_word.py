

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        start = len(s) - 1
        while start >= 0:
            if s[start] != " ":
                break
            else:
                start -= 1

        if start == -1:
            return 0

        end = start
        while end >= 0:
            if s[end] == " ":
                end += 1
                break
            else:
                end -= 1

        if end == -1:
            return start + 1

        return start - end + 1
