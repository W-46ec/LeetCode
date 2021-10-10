
"""
# Word Pattern

Given a `pattern` and a string `str`, find if `str` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `str`.

**Example 1:** 
```
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
```

**Example 2:** 
```
Input:pattern = "abba", str = "dog cat cat fish"
Output: false
```

**Example 3:** 
```
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
```

**Example 4:** 
```
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
```

**Notes:** 
You may assume `pattern` contains only lowercase letters, and `str` contains lowercase letters that may be separated by a single space.
"""

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        lst, mapping, images = str.split(' '), {}, set()
        if len(pattern) != len(lst):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in mapping:
                if lst[i] in images:
                    return False
                mapping[pattern[i]] = lst[i]
                images.add(lst[i])
            else:
                if mapping[pattern[i]] != lst[i]:
                    return False
        return True


print(Solution().wordPattern("abba", "dog cat cat dog"))	# True
print(Solution().wordPattern("abba", "dog cat cat fish"))	# False
print(Solution().wordPattern("aaaa", "dog cat cat dog"))	# False
print(Solution().wordPattern("abba", "dog dog dog dog"))	# False
