
"""
# Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Example:** 
```
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
```

**Clarification:** The above format is the same as [how LeetCode serializes a binary tree](https://leetcode.com/faq/#binary-tree). You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

**Note:** Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
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
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
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
# codec = Codec()
# codec.deserialize(codec.serialize(root))        


codec = Codec()

# "[1, 2, 3, None, None, 4, 5]"
print(codec.serialize(codec.deserialize("[1,2,3,None,None,4,5]")))

