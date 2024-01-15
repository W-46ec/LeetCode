
"""
# Stream of Characters

Implement the `StreamChecker` class as follows:
    - `StreamChecker(words)`: Constructor, init the data structure with the given words.
    - `query(letter)`: returns true if and only if for some `k >= 1`, the last `k` characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.


**Example:** 
```
StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
```

**Note:** 
    - `1 <= words.length <= 2000` 
    - `1 <= words[i].length <= 2000` 
    - Words will only consist of lowercase English letters.
    - Queries will only consist of lowercase English letters.
    - The number of queries is at most 40000.

**Hint #1** 
Put the words into a trie, and manage a set of pointers within that trie.
"""

class StreamChecker:
    def __init__(self, words):
        self.buffer = ""
        self.tree = {}
        self.null = '\0'
        for w in words:
            self.insert(w[::-1])

    def query(self, letter):
        self.buffer = letter + self.buffer
        curr = self.tree
        for c in self.buffer:
            if c in curr:
                curr = curr[c]
                if self.null in curr:
                    return True
            else:
                break
        return False

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


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

