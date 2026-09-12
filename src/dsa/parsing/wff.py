from src.dsa.parsing.aliases import Frml, AtomicFrml, CompoundFrml


def _parse_wff(expr: str) -> Frml:
    pass


def parse_wff(expr: str) -> Frml:
    pointer: int = 0

    if expr[pointer] == "(":
        pass
