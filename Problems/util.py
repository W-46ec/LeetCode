
# util.py

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
