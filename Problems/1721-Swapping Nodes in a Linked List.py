
"""
# Swapping Nodes in a Linked List

You are given the `head` of a linked list, and an integer `k`.

Return *the head of the linked list after **swapping** the values of the `kth` node from the beginning and the `kth` node from the end (the list is **1-indexed**)*.


**Example 1:** 
![1721_linked1](./img/1721_linked1.jpg)
```
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
```

**Example 2:** 
```
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
```

**Example 3:** 
```
Input: head = [1], k = 1
Output: [1]
```

**Example 4:** 
```
Input: head = [1,2], k = 1
Output: [2,1]
```

**Example 5:** 
```
Input: head = [1,2,3], k = 2
Output: [1,2,3]
```

**Constraints:** 
    - The number of nodes in the list is `n`.
    - `1 <= k <= n <= 10^5` 
    - `0 <= Node.val <= 100` 

**Hint #1**
We can transform the linked list to an array this should ease things up

**Hint #2** 
After transforming the linked list to an array it becomes as easy as swapping two integers in an array then rebuilding the linked list
"""

import sys
sys.path  = sys.path = ['.', '../', '../../'] + sys.path

from util import ListNode, initList, printList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        curr, node1, length = head, None, 0
        while curr:
            if length == k - 1:
                node1 = curr
            curr, length = curr.next, length + 1
        node2 = head
        for _ in range(length - k):
            node2 = node2.next
        node1.val, node2.val = node2.val, node1.val
        return head

# 5 -> 2 -> 3 -> 4 -> 1 -> NULL
printList(Solution().swapNodes(initList([1, 2, 3, 4, 5]), 1))

# 1 -> 4 -> 3 -> 2 -> 5 -> NULL
printList(Solution().swapNodes(initList([1, 2, 3, 4, 5]), 2))

# 1 -> 2 -> 3 -> 4 -> 5 -> NULL
printList(Solution().swapNodes(initList([1, 2, 3, 4, 5]), 3))

# 1 -> 4 -> 3 -> 2 -> 5 -> NULL
printList(Solution().swapNodes(initList([1, 2, 3, 4, 5]), 4))

# 5 -> 2 -> 3 -> 4 -> 1 -> NULL
printList(Solution().swapNodes(initList([1, 2, 3, 4, 5]), 5))
