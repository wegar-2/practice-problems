from typing import TypeAlias

from src.dsa.parsing.formula import AtomicFrml, CompoundFrml


Frml: TypeAlias = AtomicFrml | CompoundFrml
