
"""
# Add and Search Word - Data structure design

Design a data structure that supports the following two operations:
```
void addWord(word)
bool search(word)
```

search(word) can search a literal word or a regular expression string containing only letters `a-z` or `.`. A `.` means it can represent any one letter.

**Example:** 
```
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```

**Note:** 
You may assume that all words are consist of lowercase letters `a-z`.

**Hint #1** 
You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.
"""


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.null = '\0'
        self.tree = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tree = self.tree
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        tree[self.null] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def traverse(tree, idx = 0):
            if idx >= len(word):
                return self.null in tree
            elif word[idx] == '.':
                return any([traverse(tree[key], idx + 1) for key in tree])
            elif word[idx] in tree:
                return traverse(tree[word[idx]], idx + 1)
            return False
            
        return traverse(self.tree)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))    # False
print(obj.search("bad"))    # True
print(obj.search(".ad"))    # True
print(obj.search("b.."))    # True

