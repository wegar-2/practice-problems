from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Remark1: we know that the lists are not of length 0! -- not necessary to handle this
    """

    def addTwoNumbers(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        def get_ll_len(ll: Optional[ListNode]) -> int:
            len_: int = 1
            while ll.next:
                ll = ll.next
                len_ += 1
            return len_

        l1_len = get_ll_len(l1)
        l2_len = get_ll_len(l2)

        # ensure that l1 always longer
        if l2_len > l1_len:
            l1, l2 = l2, l1

        out: ListNode | None = None
        node: ListNode | None = None

        carry: int = 0
        while l1 is not None or carry > 0:
            if l1 is not None:
                val = l1.val + carry
            else:
                val = carry

            if l2:
                val += l2.val
                l2 = l2.next
            carry, digit = divmod(val, 10)

            if l1 is not None:
                l1 = l1.next

            if out is None:
                out = ListNode(digit)
                node = out
            else:
                node.next = ListNode(digit)
                node = node.next

        return out
