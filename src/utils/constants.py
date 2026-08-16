from string import (
    ascii_letters,
    ascii_lowercase,
    ascii_uppercase,
    printable,
    punctuation,
    digits
)

from utils.aliases import Alphabet

__all__ = ["ALPHABETS"]


ALPHABETS: dict[Alphabet, str] = {
    "ascii_lowercase": ascii_lowercase,
    "ascii_uppercase": ascii_uppercase,
    "ascii_letters": ascii_letters,
    "ascii_digits": digits,
    "ascii_symbols": printable,
    "ascii_punctuation": punctuation,
}
