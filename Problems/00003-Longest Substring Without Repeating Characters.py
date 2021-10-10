
"""
# Longest Substring Without Repeating Characters

Given a string `s`, find the length of the **longest substring** without repeating characters.


**Example 1:** 
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:** 
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:** 
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Example 4:** 

Input: s = ""
Output: 0
```

**Constraints:** 
    - `0 <= s.length <= 5 * 10^4` 
    - `s` consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n) solution
        # Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/732681/Sliding-Window-with-Easy-Explanation
        ans, lo, curr = 0, 0, set()
        for hi in range(len(s)):

            # Found a duplicate character.
            # Start popping out elements in the front, until that 
            # duplicated character is being popped out
            while s[hi] in curr:
                curr.remove(s[lo])
                lo += 1

            # Keep adding characters to the current set, until we 
            # find duplicate element
            curr.add(s[hi])

            ans = max(ans, hi - lo + 1)
        return ans

        # # O(n^2) solution
        # ans = 0
        # for i in range(len(s)):
        #     curr = set()
        #     for j in range(i, len(s)):
        #         if s[j] not in curr:
        #             curr.add(s[j])
        #         else:
        #             break
        #     ans = max(ans, len(curr))
        # return ans

print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
print(Solution().lengthOfLongestSubstring("bbbbb"))     # 1
print(Solution().lengthOfLongestSubstring("pwwkew"))    # 3
print(Solution().lengthOfLongestSubstring(""))          # 0

