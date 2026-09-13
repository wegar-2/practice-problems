from pytest import raises

from src.dsa.parsing.wff import parse_wff
from src.dsa.parsing.formula import AtomicFrml, CompoundFrml
from src.dsa.parsing.exceptions import (
    NotWellFormedFormula, InvalidAtomicFormula)


def test_parse_wff_atomic():
    assert parse_wff("A") == AtomicFrml("A")
    assert parse_wff("A_123") == AtomicFrml("A_123")
    with raises(InvalidAtomicFormula):
        parse_wff("A_0123")
    with raises(InvalidAtomicFormula):
        parse_wff("A_")

def test_parse_wff_compound_conj():
    pass
