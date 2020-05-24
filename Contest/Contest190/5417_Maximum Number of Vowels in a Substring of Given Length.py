
"""
# Maximum Number of Vowels in a Substring of Given Length

Given a string `s` and an integer `k`.

Return *the maximum number of vowel letters* in any substring of `s` with length `k`.

**Vowel letters** in English are (a, e, i, o, u).


**Example 1:** 
```
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
```

**Example 2:** 
```
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
```

**Example 3:** 
```
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
```

**Example 4:** 
```
Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.
```

**Example 5:** 
```
Input: s = "tryhard", k = 4
Output: 1
```

**Constraints:** 
    - `1 <= s.length <= 10^5` 
    - `s` consists of lowercase English letters.
    - `1 <= k <= s.length` 
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels, currMax = "aeiou", 0
        currMax = 0
        for c in s[ : k]:
            if c in vowels:
                currMax += 1
        ans = currMax
        for i in range(1, len(s) - k + 1):
            if s[i - 1] in vowels:
                currMax -= 1
            if s[i + k - 1] in vowels:
                currMax += 1
            ans = max(ans, currMax)
        return ans

print(Solution().maxVowels("abciiidef", 3))     # 3
print(Solution().maxVowels("aeiou", 2))         # 2
print(Solution().maxVowels("leetcode", 3))      # 2
print(Solution().maxVowels("rhythms", 4))       # 0
print(Solution().maxVowels("tryhard", 4))       # 1
print(Solution().maxVowels("ibpbhixfiouhdljnjfflpapptrxgcomvnb", 33))   # 7

