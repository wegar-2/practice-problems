

def is_valid_parentheses(s: str) -> bool:

    open_to_close = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    close_to_open = {v: k for k, v in open_to_close.items()}

    stck: list[str] = []

    for x in s:
        if x in open_to_close:
            stck.append(x)
        else:
            if not stck or close_to_open[x] != stck[-1]:
                return False
            else:
                stck.pop()
    if stck:
        return False
    return True