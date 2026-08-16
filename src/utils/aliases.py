from typing import TypeAlias, Literal

__all__ = ["Alphabet"]


Alphabet: TypeAlias = Literal[
    "ascii_lowercase",
    "ascii_uppercase",
    "ascii_letters",
    "ascii_digits",
    "ascii_symbols",
    "ascii_punctuation",
    "ascii_digits"
]
