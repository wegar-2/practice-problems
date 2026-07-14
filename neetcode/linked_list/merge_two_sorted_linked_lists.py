from neetcode.linked_list.list_node import ListNode
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head1, head2 = list1, list2
        head = None

        if head1 and head2:
            if head1.val < head2.val:
                head = head1
                head1 = head1.next
            else:
                head = head2
                head2 = head2.next
        elif head1:
            head = head1
            head1 = head1.next
        elif head2:
            head = head2
            head2 = head2.next
        else:
            return None

        node = head
        while head1 or head2:
            if head1 and head2:
                if head1.val < head2.val:
                    node.next = head1
                    head1 = head1.next
                else:
                    node.next = head2
                    head2 = head2.next
                node = node.next
            elif head1:
                node.next = head1
                head1 = head1.next
                node = node.next
            elif head2:
                node.next = head2
                head2 = head2.next
                node = node.next
            else:
                break

        return head