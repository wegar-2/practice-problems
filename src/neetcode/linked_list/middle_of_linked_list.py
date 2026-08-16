from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    What they are asking for in this example is something that is also
    called right middle or upper middle, i.e. middle calculated using len // 2
    """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast = head, head

        while fast:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            elif fast.next and not fast.next.next:
                # even length
                return slow.next
            else:
                # odd length, end hit
                return slow
