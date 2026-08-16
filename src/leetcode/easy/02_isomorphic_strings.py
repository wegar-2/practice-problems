# https://leetcode.com/problems/isomorphic-strings/description/


def is_isomorphic(s: str, t: str) -> bool:
    m: dict[str, str] = {}
    for i in range(len(s)):
        if s[i] not in m:
            if t[i] not in m.values():
                m[s[i]] = t[i]
            else:
                return False
        else:
            if t[i] != m[s[i]]:
                return False
    return True


if __name__ == "__main__":
    print(is_isomorphic(s="egg", t="add"))
