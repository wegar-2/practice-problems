# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        heap: list[int] = []
        out: ListNode | None = None
        head: ListNode | None = None

        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        while heap:
            new_val, i = heapq.heappop(heap)
            if out is None:
                out = ListNode(new_val)
                head = out
            else:
                out.next = ListNode(new_val)
                out = out.next

            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        return head
