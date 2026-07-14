import random

__all__ = ["make_random_nums"]


def make_random_nums(
        n: int,
        a: int = 1,
        b: int = 101
) -> list[int]:
    return [random.randint(a, b) for _ in range(n)]
