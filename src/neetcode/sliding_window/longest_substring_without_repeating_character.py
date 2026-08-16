from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        letters: set[str] = {s[0]}
        queue: deque[str] = deque([s[0]])

        j = 1
        max_len = 1
        for i in range(len(s)):

            while j < len(s):
                if s[j] not in letters:
                    letters.add(s[j])
                    queue.append(s[j])
                    if len(letters) > max_len:
                        max_len = len(letters)
                    j += 1
                else:
                    while (l := queue.popleft()) != s[j]:
                        letters.remove(l)
                    letters.remove(l)

        return max_len
