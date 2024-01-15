
"""
# Add Two Numbers II

You are given two **non-empty** linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Follow up:** 
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

**Example:** 
```
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
```
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys
sys.path  += ['.', '../', '../../']

from util import ListNode, initList, printList
from typing import Optional

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # O(n) time & O(1) space
        ptr = None
        while head:
            ptr, head.next, head = head, ptr, head.next
        return ptr

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reverse_l1, reverse_l2 = self.reverseList(l1), self.reverseList(l2)
        head, carry, digit = None, 0, 0
        while reverse_l1 and reverse_l2:
            digit = (carry + reverse_l1.val + reverse_l2.val) % 10
            carry = (carry + reverse_l1.val + reverse_l2.val) // 10
            head = ListNode(digit, head)
            reverse_l1, reverse_l2 = reverse_l1.next, reverse_l2.next
        for lst in [reverse_l1, reverse_l2]:
            while lst:
                digit = (carry + lst.val) % 10
                carry = (carry + lst.val) // 10
                head = ListNode(digit, head)
                lst = lst.next
        if carry != 0:
            head = ListNode(carry, head)
        return head

# 7 -> 8 -> 0 -> 7 -> NULL
printList(Solution().addTwoNumbers(initList([7, 2, 4, 3]), initList([5, 6, 4])))

# 1 -> 0 -> NULL
printList(Solution().addTwoNumbers(initList([5]), initList([5])))

# 5 -> NULL
printList(Solution().addTwoNumbers(initList([]), initList([5])))

# NULL
printList(Solution().addTwoNumbers(initList([]), initList([])))

# 1 -> 0 -> 0 -> 0 -> NULL
printList(Solution().addTwoNumbers(initList([9, 9, 9]), initList([1])))

