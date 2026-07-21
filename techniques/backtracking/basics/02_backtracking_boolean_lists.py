

def _make_boolean_lists(n: int, l: list[bool]) -> list[list[bool]]:
    if len(l) == n:
        return [l]
    out: list[list[bool]] = []
    out += _make_boolean_lists(n, l + [False])
    out += _make_boolean_lists(n, l + [True])
    return out



def make_boolean_lists(n: int) -> list[list[bool]]:
    return _make_boolean_lists(n, l=[])


if __name__ == "__main__":
    res = make_boolean_lists(n=4)
    print(res)
