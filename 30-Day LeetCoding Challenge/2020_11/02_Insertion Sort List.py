
"""
# Insertion Sort List

Sort a linked list using insertion sort.

![02_Insertion-sort-example-300px](02_Insertion-sort-example-300px.gif)

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list


**Algorithm of Insertion Sort:** 
    1. Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
    2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
    3. It repeats until no input elements remain.

**Example 1:** 
```
Input: 4->2->1->3
Output: 1->2->3->4
```

**Example 2:** 
```
Input: -1->5->3->4->0
Output: -1->0->3->4->5
```
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys
sys.path  = sys.path = ['.', '../', '../../'] + sys.path

from util import ListNode, initList, printList

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        sortedList = None
        while head:
            ptr, head = head, head.next
            prev, curr = None, sortedList
            while curr and ptr.val > curr.val:
                prev, curr = curr, curr.next
            if prev:
                ptr.next = prev.next
                prev.next = ptr
            elif curr:
                ptr.next = sortedList
                sortedList = ptr
            else:
                ptr.next = None
                sortedList = ptr
        return sortedList

# 1 -> 2 -> 3 -> 4 -> NULL
printList(Solution().insertionSortList(initList([4, 2, 1, 3])))

# -1 -> 0 -> 3 -> 4 -> 5 -> NULL
printList(Solution().insertionSortList(initList([-1, 5, 3, 4, 0])))

