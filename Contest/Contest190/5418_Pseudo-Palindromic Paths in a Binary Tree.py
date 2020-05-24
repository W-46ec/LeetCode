
"""
# Pseudo-Palindromic Paths in a Binary Tree

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be **pseudo-palindromic** if at least one permutation of the node values in the path is a palindrome.

*Return the number of **pseudo-palindromic** paths going from the root node to leaf nodes.* 


**Example 1:** 
![5418_palindromic_paths_1](./img/5418_palindromic_paths_1.png)
```
Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
```

**Example 2:** 
![5418_palindromic_paths_2](./img/5418_palindromic_paths_2.png)
```
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
```

**Example 3:** 
```
Input: root = [9]
Output: 1
```

**Constraints:** 
    - The given binary tree will have between `1` and `10^5` nodes.
    - Node values are digits from `1` to `9`.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        stack, ans = [], 0

        def dfs(tree):
            nonlocal stack, ans
            if tree == None:
                return
            stack.append(tree.val)
            if tree.left == None and tree.right == None:
                s = set()
                for x in stack:
                    if x in s:
                        s.remove(x)
                    else:
                        s.add(x)
                if len(s) <= 1:
                    ans += 1
            else:
                dfs(tree.left)
                dfs(tree.right)
            stack.pop()

        dfs(root)
        return ans

# # Testcases
# [2,3,1,3,1,null,1]
# [2,1,1,1,3,null,null,null,null,null,1]
# [9]
# [7,3,6,9,null,6,9,null,null,null,null,null,2,8]
# [4,null,2,9,1,null,null,2,3,3,3,null,null,5,4]
# [9,5,4,5,null,2,6,2,5,null,8,3,9,2,3,1,1,null,4,5,4,2,2,6,4,null,null,1,7,null,5,4,7,null,null,7,null,1,5,6,1,null,null,null,null,9,2,null,9,7,2,1,null,null,null,6,null,null,null,null,null,null,null,null,null,5,null,null,3,null,null,null,8,null,1,null,null,8,null,null,null,null,2,null,8,7]

# # Answers
# 2
# 1
# 1
# 1
# 0
# 1
