
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



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def initTree(lst):
    if not lst:
        return None
    root = TreeNode(lst.pop(0))
    Q = [root]
    while Q:
        node = Q.pop(0)
        if lst:
            val = lst.pop(0)
            node.left = TreeNode(val) if val != None else None
            Q += [node.left] if node.left else []
        if lst:
            val = lst.pop(0)
            node.right = TreeNode(val) if val != None else None
            Q += [node.right] if node.right else []
    return root

def levelOrderTraverse(tree):
    if not tree:
        return []
    lst, queue = [], [tree]
    while queue:
        node = queue.pop(0)
        lst.append(node.val)
        queue += [node.left] if node.left else []
        queue += [node.right] if node.right else []
    return lst



