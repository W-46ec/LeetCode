
"""
# Remove Duplicates from Sorted List II

Given the `head` of a sorted linked list, *delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list*. Return *the linked list **sorted** as well*.


**Example 1:** 
![05_linkedlist1](./img/05_linkedlist1.jpg)
```
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
```

**Example 2:** 
![05_linkedlist2](./img/05_linkedlist2.jpg)
```
Input: head = [1,1,1,2,3]
Output: [2,3]
```

**Constraints:** 
    - The number of nodes in the list is in the range `[0, 300]`.
    - `-100 <= Node.val <= 100` 
    - The list is guaranteed to be **sorted** in ascending order.
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr and curr.next:
            if curr.val == curr.next.val:
                val = curr.val
                while curr and curr.val == val:
                    if prev:
                        prev.next = curr.next
                    else:
                        head = curr.next
                    curr = curr.next
            else:
                prev, curr = curr, curr.next
        return head

# 2 -> 3 -> NULL
printList(Solution().deleteDuplicates(initList([1, 1, 1, 2, 3])))

# NULL
printList(Solution().deleteDuplicates(initList([1, 1, 1])))

# 1 -> NULL
printList(Solution().deleteDuplicates(initList([1])))

