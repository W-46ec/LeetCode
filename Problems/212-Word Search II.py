
"""
# Word Search II

Given an `m x n` `board` of characters and a list of strings `words`, return *all words on the board*.

Each word must be constructed from letters of sequentially adjacent cells, where **adjacent cells** are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.


**Example 1:** 
![212_search1](./img/212_search1.jpg)
```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

**Example 2:** 
![212_search2](./img/212_search2.jpg)
```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

**Constraints:** 
    - `m == board.length` 
    - `n == board[i].length` 
    - `1 <= m, n <= 12` 
    - `board[i][j]` is a lowercase English letter.
    - `1 <= words.length <= 3 * 10^4` 
    - `1 <= words[i].length <= 10` 
    - `words[i]` consists of lowercase English letters.
    - All the strings of `words` are unique.

**Hint #1** 
You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

**Hint #2** 
If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.
"""

# Reference: https://leetcode.com/problems/word-search-ii/discuss/712733/Python-Trie-solution-with-dfs-explained

from typing import List
from collections import defaultdict

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        ans = []

        # Build a prefix tree
        prefix_tree = {}
        for word in words:
            tree = prefix_tree
            for c in word:
                if c not in tree:
                    tree[c] = {}
                tree = tree[c]
            tree['\0'] = {}

        # Define DFS
        def dfs(x, y, tree, prefix):
            visited[x][y] = True
            if '\0' in tree:
                tree.pop('\0')
                ans.append(prefix)
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= x + dx < m and 0 <= y + dy < n \
                        and board[x + dx][y + dy] in tree \
                        and not visited[x + dx][y + dy]:
                    dfs(
                        x + dx, y + dy, 
                        tree[board[x + dx][y + dy]], 
                        prefix + board[x + dx][y + dy]
                    )
            visited[x][y] = False

        # Run DFS for every letter on the board
        for i in range(m):
            for j in range(n):
                if board[i][j] in prefix_tree and len(ans) < len(words):
                    dfs(i, j, prefix_tree[board[i][j]], board[i][j])
        return ans


# ['oath', 'eat']
print(Solution().findWords([
    ['o', 'a', 'a', 'n'], 
    ['e', 't', 'a', 'e'], 
    ['i', 'h', 'k', 'r'], 
    ['i', 'f', 'l', 'v']
], ["oath", "pea", "eat", "rain"]))


# []
print(Solution().findWords([
    ["a", "b"], 
    ["c", "d"]
], ["abcb"]))


# ['a']
print(Solution().findWords([
    ['a', 'a']
], ["a"]))


# ['oa', 'oaa']
print(Solution().findWords([
    ['o', 'a', 'b', 'n'], 
    ['o', 't', 'a', 'e'], 
    ['a', 'h', 'k', 'r'], 
    ['a', 'f', 'l', 'v']
], ["oa", "oaa"]))


# ['oath', 'eat', 'hklf', 'hf']
print(Solution().findWords([
    ['o', 'a', 'a', 'n'], 
    ['e', 't', 'a', 'e'], 
    ['i', 'h', 'k', 'r'], 
    ['i', 'f', 'l', 'v']
], ['oath', 'pea', 'eat', 'rain', 'hklf', 'hf']))


# ['abcdefg', 'befa', 'eaabcdgfa', 'gfedcbaaa']
print(Solution().findWords([
    ['a', 'b', 'c'], 
    ['a', 'e', 'd'], 
    ['a', 'f', 'g']
], ['abcdefg', 'gfedcbaaa', 'eaabcdgfa', 'befa', 'dgc', 'ade']))


# ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']
print(Solution().findWords([
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
], ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']))

