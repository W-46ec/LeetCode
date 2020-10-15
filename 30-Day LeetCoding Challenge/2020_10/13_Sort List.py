
"""
# Sort List

Given the `head` of a linked list, return *the list after sorting it in **ascending order***.

**Follow up**: Can you sort the linked list in `O(n logn)` time and `O(1)` memory (i.e. constant space)?


**Example 1:** 

```
Input: head = [4,2,1,3]
Output: [1,2,3,4]
```

**Example 2:** 

```
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

**Example 3:** 
```
Input: head = []
Output: []
```

**Constraints:** 
    - The number of nodes in the list is in the range `[0, 5 * 10^4]`.
    - `-10^5 <= Node.val <= 10^5` 
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
    def sortList(self, head: ListNode) -> ListNode:
        def mergeList(llst1, llst2):
            if not llst1:
                return llst2
            if not llst2:
                return llst1
            head, tail = None, None
            while llst1 and llst2:
                if llst1.val < llst2.val:
                    if not tail:
                        tail, llst1 = llst1, llst1.next
                        head = tail
                    else:
                        tail.next, llst1 = llst1, llst1.next
                        tail = tail.next
                else:
                    if not tail:
                        tail, llst2 = llst2, llst2.next
                        head = tail
                    else:
                        tail.next, llst2 = llst2, llst2.next
                        tail = tail.next
            if llst1:
                tail.next = llst1
            elif llst2:
                tail.next = llst2
            return head

        def mergeSort(head):
            if not head or not head.next:
                return head
            llst1, llst2, midPrev = head, head, None
            while llst1 and llst1.next:
                midPrev = midPrev.next if midPrev else llst1
                llst1 = llst1.next.next
            midPrev.next, llst2, llst1 = None, midPrev.next, head
            
            llst1, llst2 = mergeSort(llst1), mergeSort(llst2)
            llst = mergeList(llst1, llst2)
            return llst
        
        return mergeSort(head)

# 1 -> 2 -> 3 -> 4 -> NULL
printList(Solution().sortList(initList([4, 2, 1, 3])))

# -1 -> 0 -> 3 -> 4 -> 5 -> NULL
printList(Solution().sortList(initList([-1, 5, 3, 4, 0])))

# NULL
printList(Solution().sortList(initList([])))

