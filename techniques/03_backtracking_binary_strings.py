

def _make_binary_strings(
        n: int,
        s: str = ""
) -> list[str]:

    if len(s) == n:
        return [s]

    out: list[str] = []
    out += [x for x in _make_binary_strings(n=n, s=s + "0")]
    out += [x for x in _make_binary_strings(n=n, s=s + "1")]

    return out


def make_binary_strings(n: int) -> list[str]:
    return _make_binary_strings(n, "")


if __name__ == "__main__":
    res = make_binary_strings(n=4)
    print(res)
