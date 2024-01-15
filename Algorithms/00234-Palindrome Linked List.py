
"""
# Palindrome Linked List

Given the `head` of a singly linked list, return `true` if it is a palindrome.

**Example 1:** 
![234_pal1linked-list](./img/234_pal1linked-list.jpg)
```
Input: head = [1,2,2,1]
Output: true
```

**Example 2:** 
![234_pal2linked-list](./img/234_pal2linked-list.jpg)
```
Input: head = [1,2]
Output: false
```

**Constraints:** 
    - The number of nodes in the list is in the range `[1, 10^5]`.
    - `0 <= Node.val <= 9` 

**Follow up**: Could you do it in `O(n)` time and `O(1)` space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys
sys.path = ['.', '../', '../../'] + sys.path

from util import ListNode, initList

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # O(n) time & O(1) space

        # Find the mid-point of the linked list
        curr, mid = head, head
        while curr and curr.next:
            curr, mid = curr.next.next, mid.next
        
        # Reverse the second half of the linked list
        reversed_h = None
        while mid:
            nxt = mid.next
            mid.next = reversed_h
            reversed_h = mid
            mid = nxt

        # Compare the first and the reversed second half
        while reversed_h:
            if reversed_h.val != head.val:
                return False
            head, reversed_h = head.next, reversed_h.next
        return True

# True
print(Solution().isPalindrome(initList([1, 2, 2, 1])))

# False
print(Solution().isPalindrome(initList([1, 2])))
