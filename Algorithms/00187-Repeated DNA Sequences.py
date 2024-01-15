
"""
# Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as `'A'`, `'C'`, `'G'`, and `'T'`, for example: `"ACGAATTCCG"`. When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.


**Example 1:** 
```
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
```

**Example 2:** 
```
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
```

**Constraints:** 
    - `0 <= s.length <= 10^5` 
    - `s[i]` is `'A'`, `'C'`, `'G'`, or `'T'`.
"""

from typing import List
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = defaultdict(int)
        for i in range(len(s) - 9):
            d[s[i : i + 10]] += 1
        return [key for key in d if d[key] > 1]


# ['AAAAACCCCC', 'CCCCCAAAAA']
print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

# ['AAAAAAAAAA']
print(Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA"))

