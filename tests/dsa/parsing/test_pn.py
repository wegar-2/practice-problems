from src.dsa.parsing.pn import parse_pn, parse_rpn


def test_parse_pn1():
    assert parse_pn(["+", "10", "3"]) == 13
    assert parse_pn(["-", "10", "3"]) == 7
    assert parse_pn(["//", "10", "3"]) == 3
    assert parse_pn(["*", "10", "3"]) == 30


def test_parse_pn2():
    tokens = ["-", "+", "10", "3", "*", "2", "3"]
    assert parse_pn(tokens) == 7
    assert parse_pn(["*", "//", "10", "5"] + tokens) == 14


def test_parse_rpn1():
    assert parse_rpn(["10", "3", "+"]) == 13
    assert parse_rpn(["10", "3", "-"]) == 7
    assert parse_rpn(["10", "3", "//"]) == 3
    assert parse_rpn(["10", "3", "*"]) == 30


def test_parse_rpn2():
    tokens = ["10", "3", "+", "2", "3", "*", "-"]
    assert parse_rpn(tokens) == 7
    assert parse_rpn(tokens + ["10", "5", "//", "*"]) == 14
