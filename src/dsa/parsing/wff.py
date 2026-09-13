from src.dsa.parsing.aliases import Frml, AtomicFrml, CompoundFrml
from src.dsa.parsing.utils import retrieve_atomic_formula
from src.dsa.parsing.exceptions import NotWellFormedFormula


class _WFFParser:

    def __init__(self, expr: str):
        self._expr: str = expr
        self._idx: int = 0

    def _consume(self) -> str:
        self._idx += 1
        return self._expr[self._idx - 1]

    def _peek(self) -> str:
        return self._expr[self._idx]

    def _end_reached(self) -> bool:
        return True if self._idx == len(self._expr) else False

    def _parse_compound(self) -> CompoundFrml:
        left: Frml = self._parse_compound()
        operator: str = self._consume()
        right: Frml = self._parse_compound()
        if self._consume() != ")":
            raise NotWellFormedFormula
        return CompoundFrml(operator, left, right)

    def _parse_atomic(self) -> AtomicFrml:
        return AtomicFrml(retrieve_atomic_formula(self._expr[self._idx:]))

    def parse(self) -> Frml:
        if self._peek() == "(":
            return self._parse_compound()
        else:
            return self._parse_atomic()


def parse_wff(expr: str) -> Frml:
    return _WFFParser(expr).parse()
