

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = []
        i, j = 0, 0
        word1_turn = True

        while i < len(word1) or j < len(word2):
            if word1_turn:
                if i <= len(word1) - 1:
                    word.append(word1[i])
                    i += 1
                if j <= len(word2) - 1:
                    word1_turn = False
            else:
                if j <= len(word2) - 1:
                    word.append(word2[j])
                    j += 1
                if i <= len(word1) - 1:
                    word1_turn = True

        return "".join(word)
