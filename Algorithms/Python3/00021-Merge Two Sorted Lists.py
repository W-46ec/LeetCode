
"""
# Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new **sorted** list. The new list should be made by splicing together the nodes of the first two lists.


**Example 1:** 
![021_merge_ex1](./img/021_merge_ex1.jpg)
```
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:** 
```
Input: l1 = [], l2 = []
Output: []
```

**Example 3:** 
```
Input: l1 = [], l2 = [0]
Output: [0]
```

**Constraints:** 
    - The number of nodes in both lists is in the range `[0, 50]`.
    - `-100 <= Node.val <= 100` 
    - Both `l1` and `l2` are sorted in **non-decreasing** order.
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev = dummy_head = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2
        return dummy_head.next

# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> NULL
printList(Solution().mergeTwoLists(initList([1, 2, 4]), initList([1, 3, 4])))

# NULL
printList(Solution().mergeTwoLists(initList([]), initList([])))

# 0 -> NULL
printList(Solution().mergeTwoLists(initList([]), initList([0])))

