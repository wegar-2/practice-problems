from src.dsa.parsing.pn import eval_pn, eval_rpn


def test_parse_pn1():
    assert eval_pn(["+", "10", "3"]) == 13
    assert eval_pn(["-", "10", "3"]) == 7
    assert eval_pn(["//", "10", "3"]) == 3
    assert eval_pn(["*", "10", "3"]) == 30


def test_parse_pn2():
    tokens = ["-", "+", "10", "3", "*", "2", "3"]
    assert eval_pn(tokens) == 7
    assert eval_pn(["*", "//", "10", "5"] + tokens) == 14


def test_parse_rpn1():
    assert eval_rpn(["10", "3", "+"]) == 13
    assert eval_rpn(["10", "3", "-"]) == 7
    assert eval_rpn(["10", "3", "//"]) == 3
    assert eval_rpn(["10", "3", "*"]) == 30


def test_parse_rpn2():
    tokens = ["10", "3", "+", "2", "3", "*", "-"]
    assert eval_rpn(tokens) == 7
    assert eval_rpn(tokens + ["10", "5", "//", "*"]) == 14
