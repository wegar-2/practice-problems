from itertools import product
import random
from string import ascii_uppercase
from typing import Optional

from src.dsa.parsing.constants import BINARY_LOGICAL_OPERATORS
from src.dsa.parsing.exceptions import InvalidAtomicFormula


def arithmetic_eval(l: int, r: int, operator: str) -> int:
    match operator:
        case "+":
            return l + r
        case "-":
            return l - r
        case "//":
            return l // r
        case "*":
            return l * r
    raise ValueError(f"Unhandled operator {operator=}")


def make_atomic_formulae(n: int = 10) -> set[str]:
    """
    Creates atomic formulae using the following schedule:
    (1) firstly, ascii_uppercase letters without index are used
    (2) then, ascii_uppercase are juxtaposed with indexes 0, 1, ...
        using the schema: LETTER_N until the number n of formulae is reached

    :param n: number of atomic formulae to create
    :return: set of strings
    """
    if n < 0:
        raise ValueError(f"Invalid number of required symbols: {n=}")
    m: int = min(n, len(ascii_uppercase))
    out: set[str] = set(list(ascii_uppercase[:m]))
    if n > len(ascii_uppercase):
        q, r = divmod(n, len(ascii_uppercase))
        more: set[str] = set([])
        if q > 1:
            more.update({
                f"{l}_{idx}"
                for l, idx in product(ascii_uppercase, range(q - 1))
            })
        if r > 0:
            more.update({f"{l}_{q-1}" for l in ascii_uppercase[:r]})
        out.update(more)
    return out


def make_random_formula(
        atomic_formulae: set[str],
        num_connectives: int = 5,
        seed: int = 123_456
) -> str:

    random.seed(seed)

    def get_atomic_formula() -> str:
        return random.choices(list(atomic_formulae), k=1)[0]

    out: str = ""
    for i in range(num_connectives):
        if i == 0:
            out = f"({get_atomic_formula()}&{get_atomic_formula()})"
        else:
            l, r = out, get_atomic_formula()
            if random.uniform(0, 1) > 0.5:
                l, r = r, l
            out = f"({l}&{r})"

    return out


def validate_atomic_formula_index(digits: str) -> None:
    if digits[0] == "0":
        raise InvalidAtomicFormula(digits)


def retrieve_atomic_formula(
        expr: str,
        atomic_formulae: Optional[set[str]] = None
) -> str:
    if expr[0] not in ascii_uppercase:
        raise ValueError(f"Invalid string passed!")

    if len(expr) == 1:
        return expr

    if expr[1] in BINARY_LOGICAL_OPERATORS or expr[1] == ")":
        return expr[0]
    else:
        if expr[1] != "_":
            raise InvalidAtomicFormula(expr)

    if len(expr) == 2:
        raise InvalidAtomicFormula(expr)

    idx: int = 2
    while expr[idx].isnumeric() and idx < len(expr):
        idx += 1
    validate_atomic_formula_index(expr[2:idx])

    if atomic_formulae is None:
        return expr[:idx]
    elif (out := expr[:idx]) not in atomic_formulae:
        raise InvalidAtomicFormula(expr)
    else:
        return out
