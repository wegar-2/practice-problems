from collections import deque


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_dict = {}
        for l in s1:
            if l in s1_dict:
                s1_dict[l] += 1
            else:
                s1_dict[l] = 1

        sdq = deque()
        s2_dict = {}

        for i, l in enumerate(s2):

            sdq.append(l)
            if l in s2_dict:
                s2_dict[l] += 1
            else:
                s2_dict[l] = 1

            if i > len(s1) - 1:
                letter_out = sdq.popleft()

                s2_dict[letter_out] -= 1
                if s2_dict[letter_out] == 0:
                    del s2_dict[letter_out]

            if s1_dict == s2_dict:
                return True

        return False
