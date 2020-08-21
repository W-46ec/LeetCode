
"""
# Reorder List

Given a singly linked list *L*: *L0→L1→…→Ln-1→Ln,* 
reorder it to: *L0→Ln→L1→Ln-1→L2→Ln-2→…* 

You may **not** modify the values in the list's nodes, only nodes itself may be changed.

**Example 1:** 
```
Given 1->2->3->4, reorder it to 1->4->2->3.
```

**Example 2:** 
```
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys
sys.path.append('../../')

from util import ListNode, initList, printList

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # O(N) solution

        # Measure the length and find the mid point of the list
        length, curr, mid, mid_pre = 0, head, head, None
        while curr:
            length += 1
            curr = curr.next
            if length % 2 == 0:
                mid_pre, mid = mid, mid.next
        if mid_pre:
            mid_pre.next = None

        # Reverse the second half of the list
        reversed_tail = None
        while mid:
            nxt = mid.next
            mid.next = reversed_tail
            reversed_tail = mid
            mid = nxt

        # Merge the first half and the reversed second half of the list
        pre, curr = None, head
        while curr and reversed_tail:
            nxt_front, nxt_tail = curr.next, reversed_tail.next
            pre = curr.next = reversed_tail
            reversed_tail.next = nxt_front
            curr, reversed_tail = nxt_front, nxt_tail
        if reversed_tail:
            pre.next = reversed_tail


llst = initList([1, 2, 3, 4])
Solution().reorderList(llst)
printList(llst)


llst = initList([1, 2, 3, 4, 5])
Solution().reorderList(llst)
printList(llst)

llst = initList([1])
Solution().reorderList(llst)
printList(llst)

llst = initList([1, 2])
Solution().reorderList(llst)
printList(llst)

