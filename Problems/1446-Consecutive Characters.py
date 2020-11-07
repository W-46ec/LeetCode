
"""
# Consecutive Characters

Given a string `s`, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return *the power* of the string.


**Example 1:** 
```
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
```

**Example 2:** 
```
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
```

**Example 3:** 
```
Input: s = "triplepillooooow"
Output: 5
```

**Example 4:** 
```
Input: s = "hooraaaaaaaaaaay"
Output: 11
```

**Example 5:** 
```
Input: s = "tourist"
Output: 1
```

**Constraints:** 
    - `1 <= s.length <= 500` 
    - `s` contains only lowercase English letters.

**Hint #1** 
Keep an array power where power[i] is the maximum power of the i-th character.

**Hint #2** 
The answer is max(power[i]).
"""

class Solution:
    def maxPower(self, s: str) -> int:
        ans, i = 0 if len(s) > 1 else len(s), 0
        while i < len(s) - 1:
            curr = 1
            while i < len(s) - 1 and s[i] == s[i + 1]:
                curr, i = curr + 1, i + 1
            ans, i = max(ans, curr), i + 1
        return ans


print(Solution().maxPower("leetcode"))              # 2
print(Solution().maxPower("abbcccddddeeeeedcba"))   # 5
print(Solution().maxPower("triplepillooooow"))      # 5
print(Solution().maxPower("hooraaaaaaaaaaay"))      # 11
print(Solution().maxPower("tourist"))               # 1
print(Solution().maxPower("ccbccbb"))               # 2
print(Solution().maxPower("j"))                     # 1

