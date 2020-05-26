
"""
# Middle of the Linked List

Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.


Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.


Note:
    - The number of nodes in the given list will be between 1 and 100.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def initListNode(lst):
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

def printListNode(lst):
    while lst != None:
        if lst.next:
            print(lst.val, end = ' -> ')
        else:
            print(lst.val, end = '')
        lst = lst.next
    print()

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        middleIdx, length = 0, 0
        middle, ptr = head, head
        while ptr != None:
            length += 1
            ptr = ptr.next
            while middleIdx < length // 2:
                middleIdx += 1
                middle = middle.next
        return middle

lst1 = initListNode([1, 2, 3, 4, 5])
lst2 = initListNode([1, 2, 3, 4, 5, 6])
printListNode(Solution().middleNode(lst1))      # 3 -> 4 -> 5
printListNode(Solution().middleNode(lst2))      # 4 -> 5 -> 6

