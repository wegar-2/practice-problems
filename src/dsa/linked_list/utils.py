"""
In the remarks on complexity: n stands for length of the singly linked list
"""

from src.dsa.linked_list.node import Node

__all__ = [
    "attach_at_end",
    "interweave_lls",
    "reverse_sll",
    "sll_end",
    "sll_len",
    "split_at_mid"
]


def print_sll(head: Node) -> None:
    i = 0
    while head.next:
        print(f"node {i}: {head.val}")
        i += 1


def sll_end(node: Node) -> Node:
    """ Time complexity: O(n) """
    while node.next: # noqa
        node = node.next
    return node # noqa


def reverse_sll(head: Node) -> Node:
    """ Time complexity: O(n) """
    prev: Node = head
    nxt: Node | None = prev.next
    prev.next = None
    while nxt:
        temp = nxt.next
        nxt.next = prev
        prev, nxt = nxt, temp
    return prev


def sll_len(head: Node) -> int:
    len_: int = 1
    while head.next:
        head = head.next
        len_ += 1
    return len_


def split_at_mid(head: Node) -> tuple[Node, Node]:
    """
    Time complexity: O(n).

    """
    slow = head
    fast = head.next
    while fast:
        slow = slow.next
        if fast.next and fast.next.next:
            fast = fast.next.next
        else:
            pass
    slow.next = None
    return slow, fast


def attach_at_end(head1: Node, head2: Node):
    sll_end(head1).next = head2


def interweave_lls(head1: Node, head2: Node) -> Node:
    pass
