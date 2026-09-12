from string import ascii_uppercase

from pytest import raises

from src.dsa.parsing.utils import (
    make_atomic_formulae, arithmetic_eval, retrieve_atomic_formula)
from src.dsa.parsing.exceptions import (
    NotWellFormedFormula, InvalidAtomicFormula)


def test_arithmetic_eval():
    assert arithmetic_eval(10, 2, "+") == 12
    assert arithmetic_eval(10, 2, "-") == 8
    assert arithmetic_eval(10, 2, "*") == 20
    assert arithmetic_eval(11, 2, "//") == 5


def test_make_atomic_formulae_low_num():
    assert make_atomic_formulae(5) == {"A", "B", "C", "D", "E"}


def test_make_atomic_formulae_all_ascii_uppercase():
    assert (make_atomic_formulae(len(ascii_uppercase)) ==
            {l for l in ascii_uppercase})


def test_make_atomic_formulae_all_ascii_uppercase_plus_one():
    s = {l for l in ascii_uppercase}
    s.update({"A_0"})
    assert make_atomic_formulae(len(ascii_uppercase) + 1) == s


def test_retrieve_atomic_formula1():
    assert retrieve_atomic_formula("A_123&B_434)") == "A_123"
    with raises(InvalidAtomicFormula):
        retrieve_atomic_formula("A123&B_434)")
    with raises(InvalidAtomicFormula):
        retrieve_atomic_formula("A_0123&B_434)")
