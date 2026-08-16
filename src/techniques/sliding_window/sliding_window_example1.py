

def shortest_containing_substring(
        s: str,
        letter: str,
        k: int
) -> str:

    if len(letter) != 1:
        raise ValueError(f"Invalid {letter=} - string of len gt 1! ")

    if len(s) == 0:
        return ""

    if k <= 0:
        raise ValueError(f"{k=} has to be positive!")

    scs_i, scs_j = 0, 0
    count_: int = 0

    i = 0
    for j, x in enumerate(s):

        if x == letter:
            count_ += 1

        while count_ == k:
            if scs_j - scs_i == 0:
                scs_i, scs_j = i, j + 1
            elif j - i + 1 < scs_j - scs_i:
                scs_i, scs_j = i, j + 1

            if s[i] == letter:
                count_ -= 1
            i += 1

    return s[scs_i:scs_j]
