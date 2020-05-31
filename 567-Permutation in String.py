
"""
# Permutation in String

Given two strings **s1** and **s2**, write a function to return true if **s2** contains the permutation of **s1**. In other words, one of the first string's permutations is the **substring** of the second string.


**Example 1:** 
```
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:** 
```
Input:s1= "ab" s2 = "eidboaoo"
Output: False
```

**Note:** 
    1. The input strings only contain lower case letters.
    2. The length of both given strings is in range [1, 10,000].
"""


from collections import OrderedDict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        map_s1, map_s2 = OrderedDict(), OrderedDict()
        slice2 = s2[ : len(s1)]
        for i in range(len(s1)):
            map_s1[s1[i]] = s1.count(s1[i])
            map_s2[s2[i]] = slice2.count(s2[i])
        i = 0
        while i < len(s2) - len(s1) + 1:
            if i != 0:
                if s2[i + len(s1) - 1] in map_s2:
                    map_s2[s2[i + len(s1) - 1]] += 1
                else:
                    map_s2[s2[i + len(s1) - 1]] = 1
            equal = True
            for k in map_s1:
                if k not in map_s2 or map_s1[k] != map_s2[k]:
                    equal = False
                    break
            if equal:
                return True
            if map_s2[s2[i]] > 1:
                map_s2[s2[i]] -= 1
            else:
                map_s2.pop(s2[i])
            i += 1
        return False

print(Solution().checkInclusion("ab", "eidbaooo"))
print(Solution().checkInclusion("ab", "eidboaoo"))
print(Solution().checkInclusion("adc", "dcda"))
print(Solution().checkInclusion("trinitrophenylmethylnitramine", "dinitrophenylhydrazinetrinitrophenylmethylnitramine"))

