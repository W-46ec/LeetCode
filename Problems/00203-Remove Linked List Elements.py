
"""
# Remove Linked List Elements

Remove all elements from a linked list of integers that have value **val**.

**Example:** 
```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```
"""

from util import ListNode, initList, printList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev, curr = None, head
        while curr:
            if curr.val == val:
                if curr == head:
                    head = head.next
                    prev, curr = None, head
                    continue
                prev.next = curr.next
                curr = curr.next
                continue
            prev, curr = curr, curr.next
        return head

printList(Solution().removeElements(initList([1, 2, 6, 3, 4, 5, 6]), 6))    # 1 -> 2 -> 3 -> 4 -> 5
printList(Solution().removeElements(initList([6, 6, 6]), 6))                # (None)
printList(Solution().removeElements(initList([1]), 1))                      # (None)
printList(Solution().removeElements(initList([1, 2, 2, 1]), 2))             # 1 -> 1

