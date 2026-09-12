from __future__ import annotations
from dataclasses import dataclass

from src.dsa.parsing.constants import BINARY_LOGICAL_OPERATORS


@dataclass
class AtomicFrml:
    formula: str


@dataclass
class CompoundFrml:
    operator: str
    left: AtomicFrml | CompoundFrml
    left: AtomicFrml | CompoundFrml

    def __post_init__(self):
        if self.operator not in BINARY_LOGICAL_OPERATORS:
            raise ValueError(f"Invalid logical operator encountered: "
                             f"{self.operator}")
