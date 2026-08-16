

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        counts: dict[str, int] = {"B": 0, "W": 0}
        min_: int = -1

        for i in range(len(blocks) - k + 1):
            if i == 0:
                for j in range(k):
                    counts[blocks[j]] += 1
                    min_ = k - counts["B"]
            else:
                counts[blocks[i - 1]] -= 1
                counts[blocks[i + k - 1]] += 1
                min_ = min(k - counts["B"], min_)

        return min_
