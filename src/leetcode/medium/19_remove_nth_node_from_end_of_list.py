from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Formula-based solution"""

    def removeNthFromEnd(
            self,
            head: Optional[ListNode],
            n: int
    ) -> Optional[ListNode]:

        l = 1
        node = head
        while node.next:
            node = node.next
            l += 1

        if l == 1:
            return None

        pos = l - n + 1  # 1-indexed position in the list from start
        node = head

        if pos == 1:
            head = head.next

        for j in range(1, pos - 1):
            node = node.next

        if node.next:
            node.next = node.next.next

        return head
