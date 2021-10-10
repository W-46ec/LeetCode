
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
sys.path  = sys.path = ['.', '../', '../../'] + sys.path

from util import ListNode, initList, printList

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # O(n) time & O(1) space
        if not l1:
            return l2
        elif not l2:
            return l1
        num1, num2 = 0, 0
        while l1 or l2:
            num1 = num1 * 10 + l1.val if l1 else num1
            num2 = num2 * 10 + l2.val if l2 else num2
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        head, num = None, num1 + num2
        if num == 0:
            return ListNode(0)
        while num:
            head, num = ListNode(num % 10, head), num // 10
        return head


        # # O(n) time & O(n) space
        # head, stack1, stack2, carry = None, [], [], 0
        # while l1 or l2:
        #     stack1 += [l1.val] if l1 else []
        #     stack2 += [l2.val] if l2 else []
        #     l1 = l1.next if l1 else l1
        #     l2 = l2.next if l2 else l2
        # while stack1 or stack2:
        #     num = carry
        #     num += stack1.pop() if stack1 else 0
        #     num += stack2.pop() if stack2 else 0
        #     head, carry = ListNode(num % 10, head), num // 10
        # head = ListNode(carry, head) if carry else head
        # return head

# 7 -> 8 -> 0 -> 7 -> NULL
printList(Solution().addTwoNumbers(initList([7, 2, 4, 3]), initList([5, 6, 4])))

# 1 -> 0 -> NULL
printList(Solution().addTwoNumbers(initList([5]), initList([5])))

# 5 -> NULL
printList(Solution().addTwoNumbers(initList([]), initList([5])))

# NULL
printList(Solution().addTwoNumbers(initList([]), initList([])))

