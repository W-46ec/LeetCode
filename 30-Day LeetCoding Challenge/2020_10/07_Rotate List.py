
"""
# Rotate List

Given a linked list, rotate the list to the right by *k* places, where *k* is non-negative.

**Example 1:** 
```
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
```

**Example 2:** 
```
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
```
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys
sys.path = ['.', '../', '../../'] + sys.path

from util import ListNode, initList, printList

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # O(n) solution
        if not head:
            return None

        # Count the length of linked list
        # Find the tail of the linked list
        length, ptr, tail = 0, head, head
        while ptr:
            tail = tail.next if tail.next else tail
            length, ptr = length + 1, ptr.next

        # Calculate the offset
        offset, prev, ptr = k % length, None, head
        if offset == 0:     # Remains unchanged
            return head

        # Find the head of the new linked list
        for i in range(length - offset):
            prev, ptr = ptr, ptr.next
        newHead = ptr

        # Link the original tail to original head
        # Update new tail
        tail.next, prev.next = head, None

        return newHead

# 4 -> 5 -> 1 -> 2 -> 3
printList(Solution().rotateRight(initList([1, 2, 3, 4, 5]), 2))

# 2 -> 0 -> 1
printList(Solution().rotateRight(initList([0, 1, 2]), 4))

# None
printList(Solution().rotateRight(initList([]), 0))

# 1
printList(Solution().rotateRight(initList([1]), 1))

