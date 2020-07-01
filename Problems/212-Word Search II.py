
"""
# Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.


**Example:** 
```
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
```

**Note:** 
    - All inputs are consist of lowercase letters `a-z`.
    - The values of `words` are distinct.

**Hint #1** 
You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

**Hint #2** 
If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.
"""

# Reference: https://leetcode.com/problems/word-search-ii/discuss/712733/Python-Trie-solution-with-dfs-explained

from typing import List

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}
        self.null = '\0'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.tree
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        tree[self.null] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.tree
        for c in word:
            if c not in tree:
                return False
            tree = tree[c]
        if self.null not in tree:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.tree
        for c in prefix:
            if c not in tree:
                return False
            tree = tree[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visited, tree, ans = [[False] * len(board[0]) for _ in board], Trie(), []

        # Build a prefix tree
        for w in words:
            tree.insert(w)

        # Define DFS
        def dfs(x, y, prefix):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return
            if tree.startsWith(prefix) and not visited[x][y]:
                prefix += board[x][y]
                visited[x][y] = True
                if tree.search(prefix) and prefix not in ans:
                    ans.append(prefix)
                for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    dfs(x + i, y + j, prefix)
                visited[x][y] = False

        # Run DFS for every letter on the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, "")
        return ans

print(Solution().findWords([
    ['o', 'a', 'a', 'n'], 
    ['e', 't', 'a', 'e'], 
    ['i', 'h', 'k', 'r'], 
    ['i', 'f', 'l', 'v']
], ["oath", "pea", "eat", "rain"]))

print(Solution().findWords([
    ['a', 'a']
], ["a"]))
