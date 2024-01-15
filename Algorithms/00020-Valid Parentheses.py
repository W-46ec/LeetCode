
"""
# Valid Parentheses

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

**Example 1:** 
```
Input: s = "()"
Output: true
```

**Example 2:** 
```
Input: s = "()[]{}"
Output: true
```

**Example 3:** 
```
Input: s = "(]"
Output: false
```

**Constraints:** 
    - `1 <= s.length <= 10^4` 
    - `s` consists of parentheses only `'()[]{}'`.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {
            '(': ')', 
            '{': '}', 
            '[': ']'
        }
        for c in s:
            if c in parentheses_map:
                stack += [c]
            else:
                if not stack or c != parentheses_map[stack.pop()]:
                    return False
        return True if not stack else False

testcases = [
    "()", 
    "()[]{}", 
    "(]", 
    "[", 
    ")))", 
]


# True
# True
# False
# False
# False
for test in testcases:
    print(Solution().isValid(test))


