
"""
# ZigZag Conversion

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"` 

Write the code that will take a string and make this conversion given a number of rows:
```
string convert(string s, int numRows);
```

**Example 1:** 
```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

**Example 2:** 
```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```
"""

from functools import reduce

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lst, order = [[] for i in range(numRows)], [i for i in range(numRows)]
        order += order[-2 : 0 : -1]
        for i, c in enumerate(s):
            lst[order[i % len(order)]].append(c)
        return reduce(lambda x, y: x + y, ["".join(x) for x in lst])


print(Solution().convert("PAYPALISHIRING", 3))  # "PAHNAPLSIIGYIR"
print(Solution().convert("PAYPALISHIRING", 4))  # "PINALSIGYAHRPI"

