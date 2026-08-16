from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        out: ListNode = head
        node: ListNode = head
        current: int = node.val
        while node.next:
            if node.next.val != current:
                current = node.next.val
                node = node.next
            else:
                node.next = node.next.next

        return out
