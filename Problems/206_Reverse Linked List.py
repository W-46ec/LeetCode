
"""
# Reverse Linked List

Reverse a singly linked list.

**Example:** 
```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

**Follow up:** 
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

import sys
sys.path = ['.', '../', '../../'] + sys.path

from util import ListNode, initList, printList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # O(n) time & O(1) space
        ptr = None
        while head:
            ptr, head.next, head = head, ptr, head.next
        return ptr
        
        # # O(n) time & O(n) space
        # queue, ptr = [], head
        # while ptr:
        #     queue.append(ptr)
        #     ptr = ptr.next
        # while queue:
        #     node = queue.pop(0)
        #     node.next, ptr = ptr, node
        # return ptr

        # # O(n) Recursive
        # if not head or not head.next:
        #     return head
        # tail = self.reverseList(head.next)
        # head.next.next, head.next = head, None
        # return tail

# 5 -> 4 -> 3 -> 2 -> 1 -> NULL
printList(Solution().reverseList(initList([1, 2, 3, 4, 5])))

# NULL
printList(Solution().reverseList(initList([])))

# 1 -> NULL
printList(Solution().reverseList(initList([1])))

# 2 -> 1 -> NULL
printList(Solution().reverseList(initList([1, 2])))

