from src.dsa.linked_list.node import Node

__all__ = [
    "sll_end",
    "reverse_ll",
    "split_at_mid",
    "attach_at_end",
    "interweave_lls"
]


def sll_end(node: Node) -> Node:
    while node.next:
        node = node.next
    return node


def reverse_ll(head: Node) -> Node:
    prev = head
    nxt = prev.next
    while nxt:
        pass
    return nxt


def split_at_mid(head: Node) -> tuple[Node, Node]:
    pass


def attach_at_end(head1: Node, head2: Node) -> Node:
    pass


def interweave_lls(head1: Node, head2: Node) -> Node:
    pass
