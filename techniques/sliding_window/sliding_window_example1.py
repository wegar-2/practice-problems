import random

from utils.utils import make_random_string


def shortest_containing_substring(
        s: str,
        letter: str,
        k: int
) -> str:

    # Complexity wise - I am using the notation:
    # len(s) = n

    if len(letter) > 1:
        raise ValueError(f"Invalid {letter=} - string of len gt 1! ")

    if len(s) == 0:
        return ""

    # this is O(n) - not very nice, although this does not change the complexity!
    if letter not in s:
        return ""

    scs: str = ""
    count_: int = 0

    i = 0
    for j, x in enumerate(s):

        if x == letter:
            count_ += 1

        if count_ == k:
            if scs == "":
                scs = s[i:j+1]
            else:
                if j - i + 1 < len(scs):
                    scs = s[i:j + 1]

        while count_ == k:
            if s[i] == letter:
                count_ -= 1
            i += 1
            if count_ == k and j - i + 1 < len(scs):
                scs = s[i:j + 1]

    return scs
