
"""
# Add Two Numbers

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


**Example 1:** 
![12_addtwonumber1](./img/12_addtwonumber1.jpg)
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Example 2:** 
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3:** 
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

**Constraints:** 
    - The number of nodes in each linked list is in the range `[1, 100]`.
    - `0 <= Node.val <= 9` 
    - It is guaranteed that the list represents a number that does not have leading zeros.
"""

import sys
sys.path = ['.', '../', '../../'] + sys.path

from util import ListNode, initList, printList

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry, head, tail = 0, None, None
        while l1 or l2 or carry:
            d1, d2 = l1.val if l1 else 0, l2.val if l2 else 0
            if not head:
                head = ListNode((d1 + d2 + carry) % 10)
                tail = head
            else:
                tail.next = ListNode((d1 + d2 + carry) % 10)
                tail = tail.next
            carry = (d1 + d2 + carry) // 10
            l1, l2 = l1.next if l1 else l1, l2.next if l2 else l2
        return head


# 0 -> 1 -> NULL
ll1, ll2 = initList([5]), initList([5])
printList(Solution().addTwoNumbers(ll1, ll2))

# 1 -> 8 -> NULL
ll1, ll2 = initList([1, 8]), initList([0])
printList(Solution().addTwoNumbers(ll1, ll2))

# 0 -> 0 -> 0 -> 1 -> NULL
ll1, ll2 = initList([9, 9, 9]), initList([1])
printList(Solution().addTwoNumbers(ll1, ll2))

