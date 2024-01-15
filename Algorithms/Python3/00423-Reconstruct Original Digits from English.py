
"""
# Reconstruct Original Digits from English

Given a **non-empty** string containing an out-of-order English representation of digits `0-9`, output the digits in ascending order.

**Note:** 
    1. Input contains only lowercase English letters.
    2. Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
    3. Input length is less than 50,000.

**Example 1:** 
```
Input: "owoztneoer"

Output: "012"
```

**Example 2:** 
```
Input: "fviefuro"

Output: "45"
```
"""


# Reference: https://leetcode.com/problems/reconstruct-original-digits-from-english/discuss/458655/linear-algebra-as-a-solution-O(N)

from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        ans = ""
        ans += '0' * count['z']
        ans += '1' * (count['o'] - count['z'] - count['w'] - count['u'])
        ans += '2' * count['w']
        ans += '3' * (count['t'] - count['w'] - count['g'])
        ans += '4' * count['u']
        ans += '5' * (count['f'] - count['u'])
        ans += '6' * count['x']
        ans += '7' * (count['s'] - count['x'])
        ans += '8' * count['g']
        ans += '9' * (count['i'] - count['x'] - count['g'] - count['f'] + count['u'])
        return ans

# "012"
print(Solution().originalDigits("owoztneoer"))

# "45"
print(Solution().originalDigits("fviefuro"))

# "0123456789"
print(Solution().originalDigits("zeroonetwothreefourfivesixseveneightnine"))

