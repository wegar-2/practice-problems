from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        else:
            return False
