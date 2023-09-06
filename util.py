
# util.py

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def initList(lst: List) -> ListNode:
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return ListNode(lst[0])
    else:
        lNode = ListNode(lst[0])
        head = lNode
        for i in range(1, len(lst)):
            lNode.next = ListNode(lst[i])
            lNode = lNode.next
        return head

def serializeList(head: ListNode) -> List:
    lst = []
    while head:
        lst, head = lst + [head.val], head.next
    return "[%s]" % ", ".join(map(str, lst))

def deserializeList(string: str) -> ListNode:
    try:
        string = string.strip().replace('null', 'None')
        if len(string) < 2 or string[0] != '[' or string[-1] != ']':
            raise Exception("There was a problem parsing the string")
        lst = list(map(
            lambda x: int(x) if x != 'None' else None, 
            [x.strip() for x in string[1 : -1].split(',')]
        )) if string != '[]' else []
    except:
        raise Exception("There was a problem parsing the string")
    return initList(lst)

def printList(lst: ListNode) -> None:
    while lst != None:
        print(lst.val, end = ' -> ')
        lst = lst.next
    print('NULL')



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def initTree(lst: List) -> TreeNode:
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

def tree2List(tree: TreeNode) -> List:
    if not tree:
        return []
    lst, queue = [], [tree]
    while queue:
        node = queue.pop(0)
        lst += [node.val] if node else [node]
        queue += [node.left] if node else []
        queue += [node.right] if node else []
    while lst and lst[-1] == None:
        lst.pop()
    return lst

def serializeTree(tree: TreeNode) -> str:
    return str(tree2List(tree)).replace('None', 'null')

def deserializeTree(string: str) -> TreeNode:
    try:
        string = string.strip().replace('null', 'None')
        if len(string) < 2 or string[0] != '[' or string[-1] != ']':
            raise Exception("There was a problem parsing the string")
        lst = list(map(
            lambda x: int(x) if x != 'None' else None, 
            [x.strip() for x in string[1 : -1].split(',')]
        )) if string != '[]' else []
    except:
        raise Exception("There was a problem parsing the string")
    return initTree(lst)

def levelOrderTraverse(tree: TreeNode) -> List:
    if not tree:
        return []
    lst, queue = [], [tree]
    while queue:
        node = queue.pop(0)
        lst.append(node.val)
        queue += [node.left] if node.left else []
        queue += [node.right] if node.right else []
    return lst

def preOrderTraverse(tree: TreeNode) -> List:
    if not tree:
        return []
    lst, stack = [], [tree]
    while stack:
        node = stack.pop()
        lst += [node.val]
        stack += [node.right] if node.right else []
        stack += [node.left] if node.left else []
    return lst


