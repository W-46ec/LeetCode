
"""
# Linked List Cycle

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return *`true` if there is a cycle in the linked list. Otherwise, return `false`*.


**Example 1:** 
![141_circularlinkedlist](./img/141_circularlinkedlist.png)
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

**Example 2:** 
![141_circularlinkedlist_test2](./img/141_circularlinkedlist_test2.png)
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

**Example 3:** 
![141_circularlinkedlist_test3](./img/141_circularlinkedlist_test3.png)
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

**Constraints:** 
    - The number of the nodes in the list is in the range `[0, 10^4]`.
    - `-10^5 <= Node.val <= 10^5` 
    - `pos` is `-1` or a **valid index** in the linked-list.

**Follow up**: Can you solve it using `O(1)` (i.e. constant) memory?
"""

import sys
sys.path += ['.', '../', '../../']

from util import ListNode, deserializeList
from typing import Optional
from collections import defaultdict

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # # O(n) space
        # # Keep track of the visited nodes.
        # # Return True if we see a visited node for a second time.
        # visited = defaultdict(int)
        # while head:
        #     if visited[head]:
        #         return True
        #     visited[head], head = visited[head] + 1, head.next
        # return False

        # O(1) space
        # Maintain two pointers 'fast' and 'slow'. The fast pointer
        # moves two times faster than the slow pointer.
        # If there exists a cycle, the fast pointer will always 
        # catch the slow pointer at some point.
        # If the fast pointer reaches the tail, then no cycles are detected.
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


head, pos = deserializeList("[3, 2, 0, -4]"), 1
node, tail = head, head
for _ in range(pos):
    node = node.next
while tail and tail.next:
    tail = tail.next
if tail and pos >= 0:
    tail.next = node
print(Solution().hasCycle(head))    # True


head, pos = deserializeList("[1, 2]"), 0
node, tail = head, head
for _ in range(pos):
    node = node.next
while tail and tail.next:
    tail = tail.next
if tail and pos >= 0:
    tail.next = node
print(Solution().hasCycle(head))    # True


head, pos = deserializeList("[1]"), -1
node, tail = head, head
for _ in range(pos):
    node = node.next
while tail and tail.next:
    tail = tail.next
if tail and pos >= 0:
    tail.next = node
print(Solution().hasCycle(head))    # False


head, pos = deserializeList("[]"), -1
node, tail = head, head
for _ in range(pos):
    node = node.next
while tail and tail.next:
    tail = tail.next
if tail and pos >= 0:
    tail.next = node
print(Solution().hasCycle(head))    # False
