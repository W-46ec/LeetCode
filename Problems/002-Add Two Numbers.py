
"""
# Add Two Numbers

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example:** 
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry, head, tail = 0, None, None
        while l1 or l2 or carry:
            d1, d2 = l1.val if l1 else 0, l2.val if l2 else 0
            if not head:
                head = ListNode((d1 + d2 + carry) % 10)
                tail = head
            else:
                tail.next = ListNode((d1 + d2 + carry) % 10)
                tail = tail.next
            carry = (d1 + d2 + carry) // 10
            l1, l2 = l1.next if l1 else l1, l2.next if l2 else l2
        return head

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def initList(lst):
    if len(lst) == 0:
        return ListNode(None)
    elif len(lst) == 1:
        return ListNode(lst[0])
    else:
        lNode = ListNode(lst[0])
        head = lNode
        for i in range(1, len(lst)):
            lNode.next = ListNode(lst[i])
            lNode = lNode.next
        return head

def printList(lst):
    while lst != None:
        if lst.next:
            print(lst.val, end = ' -> ')
        else:
            print(lst.val, end = '')
        lst = lst.next
    print()


ll1, ll2 = initList([5]), initList([5])
printList(Solution().addTwoNumbers(ll1, ll2))   # 0 -> 1

ll1, ll2 = initList([1, 8]), initList([0])
printList(Solution().addTwoNumbers(ll1, ll2))   # 1 -> 8

ll1, ll2 = initList([9, 9, 9]), initList([1])
printList(Solution().addTwoNumbers(ll1, ll2))   # 0 -> 0 -> 0 -> 1
