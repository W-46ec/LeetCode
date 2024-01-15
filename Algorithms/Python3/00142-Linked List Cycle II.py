
"""
# Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

**Notice** that you **should not modify** the linked list.


**Example 1:** 
![142_circularlinkedlist](./img/142_circularlinkedlist.png)
```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

**Example 2:** 
![142_circularlinkedlist_test2](./img/142_circularlinkedlist_test2.png)
```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

**Example 3:** 
![142_circularlinkedlist_test3](./img/142_circularlinkedlist_test3.png)
```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

**Constraints:** 
    - The number of the nodes in the list is in the range `[0, 10^4]`.
    - `-10^5 <= Node.val <= 10^5` 
    - `pos` is `-1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?
"""

import sys
sys.path += ['.', '../', '../../']

from util import ListNode, deserializeList
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# # O(n) space
# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         seen, ptr = set(), head
#         while ptr:
#             if ptr in seen:
#                 return ptr
#             seen.add(ptr)
#             ptr = ptr.next
#         return None

# O(1) space
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
                    D3
                /-------\
                |       |
                |       |
                v       |
        |-----> . ----> .
        o  D1   p  D2  p'

        Maintain two pointers (i.e., fast, slow). The fast pointer moves twice as fast as 
        the slow pointer. If there exists a cycle, the fast pointer will eventally catch up
        with the slow pointer at some point in the cycle (let's name it p', and we assume p
        is the starting point of the cycle).

        When the fast pointer catches up with the slow pointer at p', the fast pointer has
        travelled a distance equal to D1 + D2 + D3 + D2. And the slow pointer has travelled
        D1 + D2. Since the fast pointer is two times faster than the slow pointer, we should
        have: 2 * (D1 + D2) = (D1 + D2 + D3 + D2). After cancellation, we should get D1 = D3.

        Therefore, when the two pointers meet at p', we simply send the slow pointer back to the
        start of the linked list (i.e., o), and set the speed of the fast pointer (which is 
        located at p' right now) to be the same as the slow pointer. If we keep traversing, they
        will eventually meet again at p (because D1 is equal to D3 as we just proved).
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while slow and fast and slow != fast:
                    slow, fast = slow.next, fast.next
                return slow
        return None




def _search_node_pos(head: ListNode, target: ListNode) -> int:
    if not head or not target:
        return -1
    pos = 0
    while head and head.val != target.val:
        pos += 1
        head = head.next
    return pos

head, pos = deserializeList("[3, 2, 0, -4]"), 1
node, tail = head, head
for _ in range(pos):
    node = node.next
while tail and tail.next:
    tail = tail.next
if tail and pos >= 0:
    tail.next = node
print(_search_node_pos(head, Solution().detectCycle(head)))     # 1


head, pos = deserializeList("[1, 2]"), 0
node, tail = head, head
for _ in range(pos):
    node = node.next
while tail and tail.next:
    tail = tail.next
if tail and pos >= 0:
    tail.next = node
print(_search_node_pos(head, Solution().detectCycle(head)))     # 0


head, pos = deserializeList("[1]"), -1
node, tail = head, head
for _ in range(pos):
    node = node.next
while tail and tail.next:
    tail = tail.next
if tail and pos >= 0:
    tail.next = node
print(_search_node_pos(head, Solution().detectCycle(head)))     # -1
