
"""
# Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different `order`. The `order` of the alphabet is some permutation of lowercase letters.

Given a sequence of `words` written in the alien language, and the `order` of the alphabet, return `true` if and only if the given `words` are sorted lexicographically in this alien language.


**Example 1:** 
```
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
```

**Example 2:** 
```
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
```

**Example 3:** 
```
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
```

**Constraints:** 
    - `1 <= words.length <= 100` 
    - `1 <= words[i].length <= 20` 
    - `order.length == 26` 
    - All characters in `words[i]` and `order` are English lowercase letters.
"""

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # The indices of each character in the dictionary (i.e., `order`)
        indices = { order[idx]: idx for idx in range(len(order)) }

        # Iterate through the list of words and compare every two consecutive words
        for i in range(len(words) - 1):
            j, w1, w2 = 0, words[i], words[i + 1]
            # Compare characters of the two consecutive words
            while j < min(len(w1), len(w2)):
                if indices[w1[j]] > indices[w2[j]]:
                    # Case 1: current character of w1 is greater than that of w2;
                    #         then w1 is greater than w2;
                    #         `words` are not sorted lexicographically;
                    return False
                elif indices[w1[j]] < indices[w2[j]]:
                    # Case 2: current character of w1 is smaller than that of w2;
                    #         then w1 is smaller than w2;
                    #         We may ignore the rest of the characters
                    break
                else:
                    # Case 3: current character of w1 is the same as that of w2;
                    #         Update pointer `j` and compare the next character
                    j += 1

            # If w1 is longer than w2 and w2 matches the first part of w1, w1 is greater.
            if len(w1) > j and j == len(w2):
                return False

        return True

# True
print(Solution().isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))

# False
print(Solution().isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))

# False
print(Solution().isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
