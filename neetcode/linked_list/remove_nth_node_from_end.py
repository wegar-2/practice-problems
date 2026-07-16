from typing import Optional
from neetcode.linked_list.list_node import ListNode

class Solution:

    @staticmethod
    def reverse_list(head: Optional[ListNode]) -> ListNode:

        if head is None:
            return None

        prev_ = head
        next_ = prev_.next
        head.next = None

        while next_:
            temp = next_.next
            next_.next = prev_
            prev_, next_ = next_, temp

        return prev_

    @staticmethod
    def remove_nth_node(head: ListNode, n: int) -> ListNode:
        """
        WARNING: Note that this removal is 1-indexed unlike pythonic 0-indexing!
        """
        if n == 1:
            head = head.next
            return head
        else:
            node: ListNode = head
            for i in range(1, n - 1):
                node = node.next
            if node.next is not None:
                node.next = node.next.next
            else:
                node.next = None
            return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[
        ListNode]:
        tail = self.reverse_list(head)
        tail = self.remove_nth_node(tail, n)
        return self.reverse_list(tail)
