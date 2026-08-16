from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(
            self,
            headA: ListNode,
            headB: ListNode
    ) -> Optional[ListNode]:

        def get_len(head: ListNode) -> int:
            len_: int = 1
            while head.next:
                head = head.next
                len_ += 1
            return len_

        def get_last(head: ListNode) -> ListNode:
            while head.next:
                head = head.next
            return head

        def reverse_ll(head: ListNode) -> ListNode:
            prv, nxt = head, head.next
            prv.next = None
            while nxt:
                temp = nxt.next
                nxt.next = prv
                prv, nxt = nxt, temp
            return prv

        # return None if lls dont intersect
        if get_last(headA) is not get_last(headB):
            return None

        S = get_len(headA) + get_len(headB)
        headA = reverse_ll(headA)

        headB = reverse_ll(headB)
        L = get_len(headB)
        p = (S + 1 - L) / 2

        i = 1
        out: ListNode = headA

        while i < p:
            out = out.next
            i += 1

        # restore the original form
        reverse_ll(headB)
        reverse_ll(headA)

        return out
