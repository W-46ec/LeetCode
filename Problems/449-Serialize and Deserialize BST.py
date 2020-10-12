
"""
# Serialize and Deserialize BST

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a **binary search tree**. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

**The encoded string should be as compact as possible.** 


**Example 1:** 
```
Input: root = [2,1,3]
Output: [2,1,3]
```

**Example 2:** 
```
Input: root = []
Output: []
```

**Constraints:** 
    - The number of nodes in the tree is in the range `[0, 10^4]`.
    - `0 <= Node.val <= 10^4` 
    - The input tree is **guaranteed** to be a binary search tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return "[]"
        lst, queue = [], [root]
        while queue:
            node = queue.pop(0)
            lst += [node.val] if node else [node]
            queue += [node.left] if node else []
            queue += [node.right] if node else []
        while lst and lst[-1] == None:
            lst.pop()
        return str(lst)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        # Parse data into a list
        lst = list(map(
            lambda x: int(x) if x != 'None' else None, 
            [x.strip() for x in data[1 : -1].split(',')]
        )) if data != "[]" else []

        # Reconstruct the tree
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


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
