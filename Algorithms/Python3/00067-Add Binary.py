
"""
# Add Binary

Given two binary strings `a` and `b`, return *their sum as a binary string*.


**Example 1:** 
```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:** 
```
Input: a = "1010", b = "1011"
Output: "10101"
```

**Constraints:** 
    - `1 <= a.length, b.length <= 10^4` 
    - `a` and `b` consist only of `'0'` or `'1'` characters.
    - Each string does not contain leading zeros except for the zero itself.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # # Built-in function: Convert to bin type
        # return bin(int(a, base = 2) + int(b, base = 2))[2 : ]

        # # Compute bit by bit

        # Addition table
        add_op = {
            '0': { '0': '0', '1': '1' }, 
            '1': { '0': '1', '1': '0' }
        }

        # Add preceding zeros to make it easier to deal with
        length = max(len(a), len(b))
        a, b = a.zfill(length), b.zfill(length)

        # Current carry bit is 0
        carry, res = '0', ''
        for i in range(length - 1, -1, -1):
            resulting_bit = add_op[add_op[a[i]][b[i]]][carry]
            # Update the next carry bit
            if a[i] == b[i] == '1' or add_op[a[i]][b[i]] == carry == '1':
                carry = '1'
            else:
                carry = '0'
            res = resulting_bit + res
        return res if carry == '0' else carry + res

# "100"
print(Solution().addBinary("11", "1"))

# "10101"
print(Solution().addBinary("1010", "1011"))

