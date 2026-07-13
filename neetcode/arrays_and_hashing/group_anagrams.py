from typing import List

from string import ascii_lowercase
from collections import defaultdict


class Solution:

    def _word_to_tuple(self, word: str) -> tuple[int, ...]:
        letter_counts = {l: 0 for l in ascii_lowercase}
        for l in word:
            letter_counts[l] += 1
        return tuple(letter_counts.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped_words = defaultdict(list)

        for word in strs:
            key: tuple[int, ...] = self._word_to_tuple(word)
            grouped_words[key].append(word)

        return [list(v) for v in grouped_words.values()]


if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    s = Solution()
    print(s.groupAnagrams(strs))
