
"""
# Remove Nth Node From End of List

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

**Follow up**: Could you do this in one pass?

**Example 1:** 
![019_remove_ex1](./img/019_remove_ex1.jpg)
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Example 2:** 
```
Input: head = [1], n = 1
Output: []
```

**Example 3:** 
```
Input: head = [1,2], n = 1
Output: [1]
```

**Constraints:** 
    - The number of nodes in the list is `sz`.
    - `1 <= sz <= 30` 
    - `0 <= Node.val <= 100` 
    - `1 <= n <= sz` 

**Hint #1** 
Maintain two pointers and update one with a delay of n steps.
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev_target, target, curr, diff = None, head, head, 1
        while diff < n and curr:
            curr, diff = curr.next, diff + 1
        while curr and curr.next:
            prev_target, target, curr = target, target.next, curr.next
        if prev_target:
            prev_target.next = target.next
        elif target:
            head = head.next
        else:
            head = None
        return head

# 1 -> 2 -> 3 -> 5 -> NULL
printList(Solution().removeNthFromEnd(initList([1, 2, 3, 4, 5]), 2))

# NULL
printList(Solution().removeNthFromEnd(initList([1]), 1))

# 1 -> NULL
printList(Solution().removeNthFromEnd(initList([1, 2]), 1))

# 2 -> NULL
printList(Solution().removeNthFromEnd(initList([1, 2]), 2))
