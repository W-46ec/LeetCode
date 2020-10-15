
"""
# Buddy Strings

Given two strings `A` and `B` of lowercase letters, return `true` *if you can swap two letters in* `A` so the result is equal to `B`, otherwise, return `false`*.

Swapping letters is defined as taking two indices `i` and `j` (0-indexed) such that `i != j` and swapping the characters at `A[i]` and `A[j]`. For example, swapping at indices `0` and `2` in `"abcd"` results in `"cbad"`.


**Example 1:** 
```
Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
```

**Example 2:** 
```
Input: A = "ab", B = "ab"
Output: false
Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.
```

**Example 3:** 
```
Input: A = "aa", B = "aa"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.
```

**Example 4:** 
```
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
```

**Example 5:** 
```
Input: A = "", B = "aa"
Output: false
```

**Constraints:** 
    - `0 <= A.length <= 20000` 
    - `0 <= B.length <= 20000` 
    - `A` and `B` consist of lowercase letters.
"""

from collections import Counter

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            freq = Counter(A)
            return any([freq[key] >= 2 for key in freq])
        else:
            count, i = 0, 0
            while i < len(A):
                if A[i] != B[i]:
                    count += 1
                    break
                i += 1
            j = i + 1
            while j < len(A):
                if A[j] != B[j]:
                    count += 1
                    break
                j += 1
            if count == 2:
                return A[i] == B[j] and A[j] == B[i] and A[j + 1 : ] == B[j + 1 : ]
            return False


print(Solution().buddyStrings("ab", "ba"))                  # True
print(Solution().buddyStrings("ab", "ab"))                  # False
print(Solution().buddyStrings("aa", "aa"))                  # True
print(Solution().buddyStrings("aaaaaaabc", "aaaaaaacb"))    # True
print(Solution().buddyStrings("", "a"))                     # False
print(Solution().buddyStrings("", ""))                      # False

