from __future__ import annotations
from dataclasses import dataclass

from src.dsa.parsing.constants import BINARY_LOGICAL_OPERATORS


@dataclass(frozen=True)
class AtomicFrml:
    formula: str


@dataclass(frozen=True)
class CompoundFrml:
    operator: str
    left: AtomicFrml | CompoundFrml
    right: AtomicFrml | CompoundFrml | None

    def __post_init__(self):
        if (self.operator not in BINARY_LOGICAL_OPERATORS and
                self.operator != "~"):
            raise ValueError(
                f"Invalid logical operator encountered: {self.operator}")
