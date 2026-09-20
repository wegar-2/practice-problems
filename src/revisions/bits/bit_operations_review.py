from typing import Literal, TypeAlias

B: TypeAlias = Literal[0, 1]


def make_bit_map(n: int) -> dict[int, B]:
    """
    Bits in the output are numbered left to right starting at 0
    :param n:
    :return:
    """
    out: dict[int, B] = {}
    for sh in range(n.bit_length()):
        out[sh] = 1 & (n >> sh) # noqa
    return out

def main():

    x: int = 13
    print(f"{bin(x)=}")
    print(f"{x.bit_length()=}")
    print(f"{(x >> 1)=}")

    for sh in range(x.bit_length()):
        print(f"{((x >> sh) & 1)=}")

    x = 0b110010
    y = 0b101011
    width: int = x.bit_length()
    # bitwise complement
    print(f"{(~x)=:0{width}b}")
    # bitwise AND
    print(f"{(x & y)=:0{width}b}")
    # bitwise OR
    print(f"{(x | y)=:0{width}b}")
    # bitwise XOR
    print(f"{(x ^ y)=:0{width}b}")

    m: int = 0b1010111
    for k, v in make_bit_map(m).items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
