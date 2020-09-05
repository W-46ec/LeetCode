
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

def tree2List(tree):
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

def serializeTree(tree):
    return str(tree2List(tree)).replace('None', 'null')

def deserializeTree(string):
    try:
        string = string.strip().replace('null', 'None')
        if len(string) < 2 or string[0] != '[' or string[-1] != ']':
            raise Exception("Parsing Error!")
        lst = list(map(
            lambda x: int(x) if x != 'None' else None, 
            [x.strip() for x in string[1 : -1].split(',')]
        )) if string != '[]' else []
    except:
        raise Exception("Parsing Error!")
    return initTree(lst)

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

def preOrderTraverse(tree):
    if not tree:
        return []
    lst, stack = [], [tree]
    while stack:
        node = stack.pop()
        lst += [node.val]
        stack += [node.right] if node.right else []
        stack += [node.left] if node.left else []
    return lst


