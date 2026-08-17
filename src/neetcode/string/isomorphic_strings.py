

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        char_map: dict[str, str] = {}
        mapped_chars: set[str] = set()

        for i in range(len(s)):
            if s[i] not in char_map:
                if t[i] not in mapped_chars:
                    char_map[s[i]] = t[i]
                    mapped_chars.add(t[i])
                else:
                    return False
            else:
                if char_map[s[i]] != t[i]:
                    return False

        return True
