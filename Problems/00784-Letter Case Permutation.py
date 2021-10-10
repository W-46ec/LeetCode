
"""
# Letter Case Permutation

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return *a list of all possible strings we could create*. You can return the output in **any order**.


**Example 1:** 
```
Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
```

**Example 2:** 
```
Input: S = "3z4"
Output: ["3z4","3Z4"]
```

**Example 3:** 
```
Input: S = "12345"
Output: ["12345"]
```

**Example 4:** 
```
Input: S = "0"
Output: ["0"]
```

**Constraints:** 
    - `S` will be a string with length between `1` and `12`.
    - `S` will consist only of letters or digits.
"""

from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = ['']
        for c in S:
            if c.isalpha():
                ans = list(map(lambda x: x + c.lower(), ans.copy())) + \
                    list(map(lambda x: x + c.upper(), ans.copy()))
            else:
                ans = list(map(lambda x: x + c, ans.copy()))
        return ans

# ['a1b2', 'A1b2', 'a1B2', 'A1B2']
print(Solution().letterCasePermutation("a1b2"))

# ['3z4', '3Z4']
print(Solution().letterCasePermutation("3z4"))

# ['12345']
print(Solution().letterCasePermutation("12345"))

# ['0']
print(Solution().letterCasePermutation("0"))

