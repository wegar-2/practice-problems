from string import ascii_uppercase

from src.dsa.parsing.utils import conjunction, make_atomic_formulae


def test_conjunction():
    assert conjunction("A", "B") == "(A&B)"
    assert conjunction("(A&B)", "C") == "((A&B)&C)"


def test_make_atomic_formulae_low_num():
    assert make_atomic_formulae(5) == {"A", "B", "C", "D", "E"}


def test_make_atomic_formulae_all_ascii_uppercase():
    assert (make_atomic_formulae(len(ascii_uppercase)) ==
            {l for l in ascii_uppercase})

def test_make_atomic_formulae_all_ascii_uppercase_plus_one():
    s = {l for l in ascii_uppercase}
    s.update({"A_0"})
    assert make_atomic_formulae(len(ascii_uppercase) + 1) == s
