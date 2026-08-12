import random

from utils.aliases import Alphabet
from utils.constants import ALPHABETS

__all__ = [
    "make_random_nums",
    "make_random_string"
]


def make_random_nums(
        n: int,
        a: int = 1,
        b: int = 101
) -> list[int]:
    return [random.randint(a, b) for _ in range(n)]


def make_random_string(
        n: int = 50,
        alphabet: Alphabet = "ascii_letters"
) -> str:
    return "".join(random.choices(population=ALPHABETS[alphabet], k=n))
