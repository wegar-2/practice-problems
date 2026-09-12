from src.dsa.parsing.utils import arithmetic_eval


# def parse_pn(tokens: list[str]) -> int:
#     stck: list[int] = []
#
#     for token in tokens[::-1]:
#         try:
#             num = int(token)
#         except ValueError:
#             arithmetic_eval()
#         else:
#             pass
#
#     return stck[0]


def parse_rpn(tokens: list[str]) -> int:
    stck: list[int] = []

    for token in tokens:
        try:
            num = int(token)
        except ValueError:
            r, l = stck.pop(), stck.pop()
            stck.append(arithmetic_eval(l, r, token))
        else:
            stck.append(num)

    return stck[0]
