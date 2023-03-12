
"""
# String Compression

Given an array of characters `chars`, compress it using the following algorithm:

Begin with an empty string `s`. For each group of consecutive repeating characters in `chars`:
    - If the group's length is `1`, append the character to `s`.
    - Otherwise, append the character followed by the group's length.

The compressed string `s` **should not be returned separately**, but instead, be stored **in the input character array `chars`**. Note that group lengths that are `10` or longer will be split into multiple characters in `chars`.

After you are done **modifying the input array**, return *the new length of the array*.

You must write an algorithm that uses only constant extra space.


**Example 1:** 
```
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
```

**Example 2:** 
```
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
```

**Example 3:** 
```
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
```

**Constraints:** 
    - `1 <= chars.length <= 2000` 
    - `chars[i]` is a lowercase English letter, uppercase English letter, digit, or symbol.
"""

from typing import List
from math import floor, log10

class Solution:
    def compress(self, chars: List[str]) -> int:
        # Accepted, but not constant extra space
        s, idx = "", 0
        while idx < len(chars):
            curr_char, curr_count = chars[idx], 1
            while idx + curr_count < len(chars) and chars[idx + curr_count] == curr_char:
                curr_count += 1
            s += curr_char
            s += str(curr_count) if curr_count > 1 else ""
            idx += curr_count
        chars[ : ] = list(s)
        return len(s)


# 6
# ["a", "2", "b", "2", "c", "3"]
lst = ["a", "a", "b", "b", "c", "c", "c"]
print(Solution().compress(lst))
print(lst)

# 1
# ["a"]
lst = ["a"]
print(Solution().compress(lst))
print(lst)

# 4
# ["a", "b", "1", "2"]
lst = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(Solution().compress(lst))
print(lst)

# 3
# ["a", "1", "0"]
lst = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
print(Solution().compress(lst))
print(lst)

# 6
# ["a", "3", "b", "2", "a", "2"]
lst = ["a", "a", "a", "b", "b", "a", "a"]
print(Solution().compress(lst))
print(lst)
