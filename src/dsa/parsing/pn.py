from src.dsa.parsing.utils import binary_arithmetic_eval


def parse_rpn(tokens: list[str]) -> int:
    stck: list[int] = []

    for token in tokens:
        try:
            num = int(token)
        except ValueError:
            r, l = stck.pop(), stck.pop()
            stck.append(binary_arithmetic_eval(l, r, token))
        else:
            stck.append(num)

    return stck[0]
