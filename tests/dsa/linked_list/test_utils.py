from src.dsa.linked_list.utils import sll_end, reverse_sll
from src.dsa.linked_list.node import Node

from pytest import fixture


@fixture
def sll() -> Node:
    node = Node(1)
    out = node
    for i in range(2, 6):
        node.next = Node(i)
        node = node.next
    return out


def test_sll_end(sll):
    node = sll_end(sll)
    assert node.val == 5


def test_reverse_sll(sll):
    node = reverse_sll(sll)
    for i in range(5, 0, -1):
        assert node.val == i
        node = node.next
