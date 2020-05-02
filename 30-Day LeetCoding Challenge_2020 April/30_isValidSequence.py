
"""
# Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

Given a binary tree where each path going from the root to any leaf form a **valid sequence**, check if a given string is a **valid sequence** in such binary tree. 
We get the given string from the concatenation of an array of integers `arr` and the concatenation of all values of the nodes along a path results in a **sequence** in the given binary tree.


Example 1:
![30_leetcode_testcase_1](./img/30_leetcode_testcase_1.png)

Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
Output: true
Explanation: 
The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
Other valid sequences are: 
0 -> 1 -> 1 -> 0 
0 -> 0 -> 0


Example 2:
![30_leetcode_testcase_2](./img/30_leetcode_testcase_2.png)

Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
Output: false 
Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.


Example 3:
![30_leetcode_testcase_3](./img/30_leetcode_testcase_3.png)

Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
Output: false
Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.


Constraints:
    - 1 <= arr.length <= 5000
    - 0 <= arr[i] <= 9
    - Each node's value is between [0 - 9].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(tree, arr, idx):
            if not tree or idx >= len(arr):
                return False
            if tree.left == None and tree.right == None and tree.val == arr[idx] and idx == len(arr) - 1:
                return True
            return arr[idx] == tree.val and (dfs(tree.left, arr, idx + 1) or dfs(tree.right, arr, idx + 1))
        return dfs(root, arr, 0)


