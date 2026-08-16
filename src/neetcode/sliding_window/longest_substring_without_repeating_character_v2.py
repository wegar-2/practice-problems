from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        max_len: int = 0
        symbols: set[str] = set()
        queue: deque[str] = deque([])

        for x in s:
            if x in symbols:
                while x in symbols:
                    symbols.remove(queue.popleft())
            symbols.add(x)
            queue.append(x)
            if len(queue) > max_len:
                max_len = len(queue)

        return max_len
