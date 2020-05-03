
"""
# Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

**Note:** 
You may assume that both strings contain only lowercase letters.
```
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
```
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all([ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote)])

print(Solution().canConstruct("ab", "bba"))     # True
print(Solution().canConstruct("bjaajgea", "affhiiicabhbdchbidghccijjbfjfhjeddgggbajhidhjchiedhdibgeaecffbbbefiabjdhggihccec"))  # True

