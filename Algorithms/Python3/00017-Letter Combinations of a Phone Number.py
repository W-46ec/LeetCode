
"""
# Letter Combinations of a Phone Number

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
![017_1200px-telephone-keypad2svg](./img/017_1200px-telephone-keypad2svg.png)

**Example 1:** 
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Example 2:** 
```
Input: digits = ""
Output: []
```

**Example 3:** 
```
Input: digits = "2"
Output: ["a","b","c"]
```

**Constraints:** 
    - `0 <= digits.length <= 4` 
    - `digits[i]` is a digit in the range `['2', '9']`.
"""

from typing import List
from functools import reduce

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        # digit_map[idx] corresponds to digit (idx + 2)
        digit_map = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        combinations = ['']
        for idx in range(len(digits) - 1, -1, -1):
            letters = digit_map[int(digits[idx]) - 2]
            mat = [combinations.copy() for _ in range(len(letters))]
            for i, lst in enumerate(mat):
                for j in range(len(lst)):
                    lst[j] = letters[i] + lst[j]
            combinations = reduce(lambda x, y: x + y, mat)
        return combinations

# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print(Solution().letterCombinations("23"))

# []
print(Solution().letterCombinations(""))

# ['a', 'b', 'c']
print(Solution().letterCombinations("2"))
