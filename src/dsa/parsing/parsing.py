

def _parse_wff():
    pass


def parse_wff(
        expr: str,
        atomic_formulae: set[str]
):
    pointer: int = 0

    if any(expr[pointer:].startswith(x) for x in atomic_formulae):
        pass

    if expr[pointer] == "(":
        pass


if __name__ == "__main__":
    e = "(B&((A&A)&B))"
