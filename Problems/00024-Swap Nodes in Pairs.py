
"""
# Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


**Example 1:** 
![024_swap_ex1](./img/024_swap_ex1.jpg)
```
Input: head = [1,2,3,4]
Output: [2,1,4,3]
```

**Example 2:** 
```
Input: head = []
Output: []
```

**Example 3:** 
```
Input: head = [1]
Output: [1]
```

**Constraints**:
    - The number of nodes in the list is in the range `[0, 100]`.
    - `0 <= Node.val <= 100` 
"""

import sys
sys.path += ['.', '../', '../../']

from typing import Optional
from util import ListNode, initList, printList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # # Iterative approach
    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     # Initialization
    #     dummy_head, prev, curr = ListNode(0, head), ListNode(0, head), head

    #     while curr:
    #         nxt = curr.next
    #         # If the next node is None, it means we have reached the last element of the list
    #         if nxt:
    #             # Swap nodes
    #             prev.next, curr.next, nxt.next = nxt, nxt.next, curr
    #             # Obtain the head of the new list
    #             if curr == head:
    #                 dummy_head.next = nxt
    #             # Proceed to the next iteration
    #             prev, curr = curr, curr.next
    #         else:
    #             break

    #     return dummy_head.next

    # Recursive approach
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr, nxt = head, head.next
        nxt.next, curr.next = curr, self.swapPairs(nxt.next)
        return nxt

# NULL
printList(Solution().swapPairs(initList([])))

# 1 -> NULL
printList(Solution().swapPairs(initList([1])))

# 2 -> 1 -> NULL
printList(Solution().swapPairs(initList([1, 2])))

# 2 -> 1 -> 3 -> NULL
printList(Solution().swapPairs(initList([1, 2, 3])))

# 2 -> 1 -> 4 -> 3 -> NULL
printList(Solution().swapPairs(initList([1, 2, 3, 4])))
