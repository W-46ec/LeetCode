
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

# # Works for full binary trees
# def initTree(lst, idx = 0):
#     if idx < 0 or idx >= len(lst):
#         return None
#     if len(lst) == 0:
#         return TreeNode(None)
#     tree = TreeNode(lst[idx])
#     if 2 * idx + 1 < len(lst) and lst[2 * idx + 1] != None:
#         tree.left = initTree(lst, 2 * idx + 1)
#     if 2 * idx + 2 < len(lst) and lst[2 * idx + 2] != None:
#         tree.right = initTree(lst, 2 * idx + 2)
#     return tree

# WIP
def initTree(lst, idx = 0):
    if idx < 0 or idx >= len(lst) or lst[idx] == None:
        return None
    tree = TreeNode(lst[idx])
    if 2 * idx + 1 < len(lst) and lst[2 * idx + 1] != None:
        tree.left = initTree(lst, 2 * idx + 1)
        tree.right = initTree(lst, 2 * idx + 2)
    else:
        tree.right = initTree(lst[2 * idx + 2 : ])
    return tree


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


