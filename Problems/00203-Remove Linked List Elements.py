
"""
# Remove Linked List Elements

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return *the new head*.


**Example 1:** 
![203_removelinked-list](./img/203_removelinked-list.jpg)
```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
```

**Example 2:** 
```
Input: head = [], val = 1
Output: []
```

**Example 3:** 
```
Input: head = [7,7,7,7], val = 7
Output: []
```

**Constraints:** 
    - The number of nodes in the list is in the range `[0, 10^4]`.
    - `1 <= Node.val <= 50` 
    - `0 <= val <= 50` 
"""

import sys
sys.path += ['.', '../', '../../']

from util import ListNode, initList, printList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(0, head)
        prev, curr = dummy_head, head
        while curr:
            if curr.val == val:
                curr = prev.next = curr.next
            else:
                prev, curr = curr, curr.next
        return dummy_head.next

# 1 -> 2 -> 3 -> 4 -> 5 -> NULL
printList(Solution().removeElements(initList([1, 2, 6, 3, 4, 5, 6]), 6))    # 1 -> 2 -> 3 -> 4 -> 5

# NULL
printList(Solution().removeElements(initList([6, 6, 6]), 6))                # (None)

# NULL
printList(Solution().removeElements(initList([1]), 1))                      # (None)

# 1 -> 1 -> NULL
printList(Solution().removeElements(initList([1, 2, 2, 1]), 2))             # 1 -> 1

