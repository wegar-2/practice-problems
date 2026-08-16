
def fixed_len_bin_str_generator(n: int = 2):
    def make_str(s: str):
        if len(s) == n:
            yield s
        else:
            yield from make_str(s + "0")
            yield from make_str(s + "1")
    return make_str("")


if __name__ == "__main__":
    gen = fixed_len_bin_str_generator(3)
    for x in gen:
        print(f"{x=}")
