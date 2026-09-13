from pytest import raises

from src.dsa.parsing.wff import parse_wff
from src.dsa.parsing.formula import AtomicFrml, CompoundFrml
from src.dsa.parsing.exceptions import InvalidAtomicFormula


def test_parse_wff_atomic():
    assert parse_wff("A") == AtomicFrml("A")
    assert parse_wff("A_123") == AtomicFrml("A_123")
    with raises(InvalidAtomicFormula):
        parse_wff("A_0123")
    with raises(InvalidAtomicFormula):
        parse_wff("A_")


def test_parse_wff1():
    assert (parse_wff("(A&B)") ==
            CompoundFrml("&", AtomicFrml("A"), AtomicFrml("B")))
    assert (parse_wff("(A|B)") ==
            CompoundFrml("|", AtomicFrml("A"), AtomicFrml("B")))
    assert (parse_wff("(A>B)") ==
            CompoundFrml(">", AtomicFrml("A"), AtomicFrml("B")))
    assert (parse_wff("(~A)") == CompoundFrml("~", AtomicFrml("A"), None))


def test_parse_wff2():
    assert (parse_wff("((A&B)|C)") ==
            CompoundFrml("&", AtomicFrml("A"), AtomicFrml("B")))
    assert (parse_wff("((~A)|(~B))") ==
            CompoundFrml("|", AtomicFrml("A"), AtomicFrml("B")))
    assert (parse_wff("(A>B)") ==
            CompoundFrml(">", AtomicFrml("A"), AtomicFrml("B")))
    assert (parse_wff("(~A)") == CompoundFrml("~", AtomicFrml("A"), None))


# def test_parse_wff_compound_conj():
#     assert parse_wff("(A&B)") == CompoundFrml(
#         "&",
#         AtomicFrml("A"),
#         AtomicFrml("B")
#     )
#     assert parse_wff("((A&B)&C)") == CompoundFrml(
#         "&",
#         CompoundFrml(
#             "&",
#             AtomicFrml("A"),
#             AtomicFrml("B")
#         ),
#         AtomicFrml("C")
#     )
#     assert parse_wff("(D&((A&B)&C))") == CompoundFrml(
#         "&",
#         AtomicFrml("D"),
#         CompoundFrml(
#             "&",
#             CompoundFrml(
#                 "&",
#                 AtomicFrml("A"),
#                 AtomicFrml("B")
#             ),
#             AtomicFrml("C")
#         )
#     )
#
#
# def test_parse_wff_compound_disj():
#     assert parse_wff("(A|B)") == CompoundFrml(
#         "|",
#         AtomicFrml("A"),
#         AtomicFrml("B")
#     )
#     assert parse_wff("((A|B)|C)") == CompoundFrml(
#         "|",
#         CompoundFrml(
#             "|",
#             AtomicFrml("A"),
#             AtomicFrml("B")
#         ),
#         AtomicFrml("C")
#     )
#     assert parse_wff("(D|((A|B)|C))") == CompoundFrml(
#         "|",
#         AtomicFrml("D"),
#         CompoundFrml(
#             "|",
#             CompoundFrml(
#                 "|",
#                 AtomicFrml("A"),
#                 AtomicFrml("B")
#             ),
#             AtomicFrml("C")
#         )
#     )
