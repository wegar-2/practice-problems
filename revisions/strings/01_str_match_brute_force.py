

def match_str_brute_force(str_: str, pattern: str) -> list[int]:

    matches: list[int] = []

    if len(str_) < len(pattern):
        return matches

    for i in range(0, len(str_) - len(pattern)):
        check = True
        for j, x in enumerate(pattern):
            if str_[i+j] != pattern[j]:
                check = False
                break
        if check:
            matches.append(i)

    return matches


if __name__ == "__main__":

    str_ = "qwerasdf gfdsgpolkobjugfojhug sdfg"
    pattern = "polkob"

    res = match_str_brute_force(str_=str_, pattern=pattern)

    print(pattern == str_[res[0]:(res[0] + len(pattern))])

    print(res)
