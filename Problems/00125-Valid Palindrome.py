
"""
# Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

**Note:** For the purpose of this problem, we define empty string as valid palindrome.

**Example 1:** 
```
Input: "A man, a plan, a canal: Panama"
Output: true
```

**Example 2:** 
```
Input: "race a car"
Output: false
```

**Constraints:** 
    - `s` consists only of printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [c for c in s.lower() if c.isalpha() or c.isnumeric()]
        return lst == lst[::-1]

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))    # True
print(Solution().isPalindrome("race a car"))        # False
