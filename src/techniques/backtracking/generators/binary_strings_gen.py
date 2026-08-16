from itertools import count


def make_bin_strs(n: int, prefix: str = "1"):

    def make_str(s: str):
        if len(s) == n + len(prefix):
            yield s
        else:
            yield from make_str(s + "0")
            yield from make_str(s + "1")

    yield from make_str(prefix)


def binary_strings_gen():

    inf_count = count(1)

    yield next(inf_count), "1"

    l = 1
    while True:
        gen = make_bin_strs(n=l)
        for x in gen:
            yield next(inf_count), x
        l += 1


if __name__ == "__main__":

    # for x in make_bin_strs(3):
    #     print(f"{x=}")

    j = 1
    for x in binary_strings_gen():
        print(f"{j} --> {x}")
        j += 1
        if j > 20:
            break