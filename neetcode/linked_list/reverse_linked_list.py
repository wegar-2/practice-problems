from typing import Optional
from neetcode.linked_list.list_node import ListNode


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev_ = head
        if head is None:
            return None
        next_ = prev_.next

        head.next = None

        while next_ is not None:
            temp = next_.next

            next_.next = prev_

            prev_ = next_
            next_ = temp

        return prev_
