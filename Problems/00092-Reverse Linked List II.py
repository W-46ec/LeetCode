
"""
# Reverse Linked List II

Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return *the reversed list*.


**Example 1:** 
![092_rev2ex2](./img/092_rev2ex2.jpg)
```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

**Example 2:** 
```
Input: head = [5], left = 1, right = 1
Output: [5]
```

**Constraints:** 
    - The number of nodes in the list is `n`.
    - `1 <= n <= 500` 
    - `-500 <= Node.val <= 500` 
    - `1 <= left <= right <= n` 

**Follow up**: Could you do it in one pass?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev, curr, curr_idx = ListNode(0, head), head, 1
        while curr_idx < left:
            prev, curr, curr_idx = curr, curr.next, curr_idx + 1
        curr_head, tail = None, curr
        while curr_idx <= right:
            curr_head, curr.next, curr, curr_idx = curr, curr_head, curr.next, curr_idx + 1
        head = curr_head if prev.next == head else head
        prev.next, tail.next = curr_head, curr if tail != curr else None
        return head
