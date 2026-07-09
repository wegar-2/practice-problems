

def isPalindrome(s: str) -> bool:

    l, r = 0, len(s) - 1

    while l < len(s) and r > -1:

        while True:
            if l >= len(s) or s[l].isalnum():
                break
            else:
                l += 1

        while True:
            if r < 0 or s[r].isalnum():
                break
            else:
                r -= 1

        if l >= len(s):
            return True

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True

if __name__ == "__main__":
    res = isPalindrome(s="tab a cat")
    print(res)
