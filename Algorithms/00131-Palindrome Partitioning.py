
"""
# Palindrome Partitioning

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return all possible palindrome partitioning of `s`.

A **palindrome** string is a string that reads the same backward as forward.

**Example 1:** 
```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

**Example 2:** 
```
Input: s = "a"
Output: [["a"]]
```

**Constraints:** 
    - `1 <= s.length <= 16` 
    - `s` contains only lowercase English letters.
"""

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, length = [], len(s)
        def backtracking(lo = 0, curr_lst = []):
            if lo >= length:
                ans.append(curr_lst.copy())
            for hi in range(lo + 1, length + 1):
                curr_str = s[lo : hi]
                if curr_str == curr_str[::-1]:
                    curr_lst.append(curr_str)
                    backtracking(hi, curr_lst)
                    curr_lst.pop()
        backtracking()
        return ans


# [['a', 'a', 'b'], ['aa', 'b']]
print(Solution().partition("aab"))

# [['a']]
print(Solution().partition("a"))

# [['a', 'a', 'a'], ['a', 'aa'], ['aa', 'a'], ['aaa']]
print(Solution().partition("aaa"))

