
"""
# Merge k Sorted Lists

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it*.


Example 1:
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

**Example 2:** 
```
Input: lists = []
Output: []
```

Example 3:
```
Input: lists = [[]]
Output: []
```

**Constraints:** 
    - `k == lists.length` 
    - `0 <= k <= 10^4` 
    - `0 <= lists[i].length <= 500` 
    - `-10^4 <= lists[i][j] <= 10^4` 
    - `lists[i]` is sorted in **ascending order**.
    - `The sum of `lists[i].length` won't exceed `10^4`.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys
sys.path += ['.', '../', '../../']

from util import ListNode, initList, printList
from typing import List
from functools import reduce

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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists:
            return reduce(lambda l1, l2: self.mergeTwoLists(l1, l2), lists)
        return None

# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> NULL
printList(Solution().mergeKLists(map(initList, [[1, 4, 5], [1, 3, 4], [2, 6]])))

# NULL
printList(Solution().mergeKLists(None))

# NULL
printList(Solution().mergeKLists(map(initList, [[]])))
