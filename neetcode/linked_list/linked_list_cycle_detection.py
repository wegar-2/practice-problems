from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False

        fast: ListNode = head
        slow: ListNode = head

        while (
                fast is not None and
                fast.next is not None and
                fast.next.next is not None
        ):
            # move pointers
            fast = fast.next.next
            slow = slow.next
            if fast.val == slow.val:
                return True

        return False
