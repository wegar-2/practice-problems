# https://stackoverflow.com/questions/62903377/python3-bytes-vs-bytearray-and-converting-to-and-from-strings
from string import ascii_letters


if __name__ == "__main__":
    print(f"{ascii_letters=}")

    bytes_letters: bytes = bytes([ord(l) for l in ascii_letters])
    print(f"{bytes_letters=}")

    ba_letters: bytearray = bytearray([0] * len(ascii_letters))
    for i, l in enumerate(ascii_letters):
        ba_letters[i] = ord(l)
    print(f"{ba_letters=}")

    try:
        bytes_letters[2] = 123
    except TypeError as exc:
        print(f"Caught {exc=}")

    str_: str = "qwerty"
    str_ascii = str_.encode("ASCII")
    print(f"{str_ascii=}")