
"""
# Permutation in String

Given two strings `s1` and `s2`, return *`true` if `s2` contains a permutation of `s1`, or `false` otherwise*.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.


**Example 1:** 
```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:** 
```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

**Constraints:** 
    - `1 <= s1.length, s2.length <= 10^4` 
    - `s1` and `s2` consist of lowercase English letters.
"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Sliding window"""
        
        # The frequency table for s1.
        # We need to find a substring in s2 with the same 
        # character frequencies as that of s1.
        freq = Counter(s1)
        
        # Move the window from left to right
        for i, c in enumerate(s2):
            # When a character is being popped out from the window,
            # increase the freq by 1, meaning that the need for that
            # character is increased.
            if i - len(s1) >= 0:
                freq[s2[i - len(s1)]] += 1
            
            # When a new character is added to the window, decrease
            # the corresponding freq by 1, meaning that the need for
            # that character is decreased.
            freq[c] -= 1
            
            # At any point, if all the values in the freq table
            # become 0, it means the substring corresponding to the
            # current window has the same character frequencies with s1.
            # Therefore, we can return True immediately.
            if not any(freq.values()):
                return True
        
        # We cannot find a substring in s2 with the same 
        # character frequencies as that of s1.
        return False

# True
print(Solution().checkInclusion("ab", "eidbaooo"))

# False
print(Solution().checkInclusion("ab", "eidboaoo"))

# True
print(Solution().checkInclusion("adc", "dcda"))

# True
print(Solution().checkInclusion("trinitrophenylmethylnitramine", "dinitrophenylhydrazinetrinitrophenylmethylnitramine"))

