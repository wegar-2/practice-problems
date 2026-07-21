import random


def integer_generator(n: int, seed: int = 123_456):
    random.seed(seed)
    for _ in range(n):
        yield random.randint(1, 101)


def nested_generator(n: int, m: int, seed: int = 123_456):
    for j in range(1, m + 1):
        print(f"m={j:02}")
        yield from integer_generator(n, seed)


def make_bin_str(s: str = ""):



if __name__ == "__main__":
    # for i, x in enumerate(integer_generator(10), start=1):
    #     print(f"{i}: {x}")
    for i, x in enumerate(nested_generator(n=5, m=3), start=1):
        print(f"{i}: {x}")
