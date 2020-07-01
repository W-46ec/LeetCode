
"""
# First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

**Examples:** 
```
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
```

**Note:** You may assume the string contain only lowercase letters.
"""


from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d, pool = OrderedDict(), set()
        for i in range(len(s)):
            if s[i] not in d and s[i] not in pool:
                d[s[i]] = i
            elif s[i] in d:
                d.pop(s[i])
                pool.add(s[i])
        return next(iter(d.items()))[1] if len(d) > 0 else -1

print(Solution().firstUniqChar("leetcode"))         # 0
print(Solution().firstUniqChar("loveleetcode"))     # 2
print(Solution().firstUniqChar("aaaaa"))            # -1
print(Solution().firstUniqChar("aadadaad"))         # -1

