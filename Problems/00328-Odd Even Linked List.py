
"""
# Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

**Example 1:** 
```
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
```

**Example 2:** 
```
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
```

**Note:** 
    - The relative order inside both the even and odd groups should remain as it was in the input.
    - The first node is considered odd, the second node even and so on ...
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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        # A flag that indicates odd or even node
        odd = 1
        
        # ptr1 points to the last node of the odd linked list
        # ptr2 points to the first node of the even linked list
        ptr1, ptr2 = head, head.next
        
        # Pointers that are used to iterate through the linked list
        prev, curr = None, head
        
        # Traverse the linked list
        while curr != None:

            # It is an odd node and it is not the head node
            if odd == 1 and prev != None:
                
                # Remove current node from the list
                prev.next = curr.next
                ptr1.next = curr
                curr.next = ptr2
                
                # Insert it to the end of odd linked list
                ptr1 = ptr1.next
                
                # Update curr pointer
                curr = prev.next
                
                # Now curr should be an even node
                odd *= -1
                continue
            prev, curr = curr, curr.next
            odd *= -1
        return head

printListNode(Solution().oddEvenList(initListNode([1, 2, 3, 4, 5])))        # 1 -> 3 -> 5 -> 2 -> 4
printListNode(Solution().oddEvenList(initListNode([2, 1, 3, 5, 6, 4, 7])))  # 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4

