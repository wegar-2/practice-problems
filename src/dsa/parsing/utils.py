from itertools import product
import random
from string import ascii_uppercase


def conjunction(l: str, r: str) -> str:
    return f"({l}&{r})"


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
        return random.choices(list(atomic_formulae), k=1)

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
