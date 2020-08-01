
"""
# Add Digits

Given a non-negative integer `num`, repeatedly add all its digits until the result has only one digit.

**Example:** 
```
Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
```

**Follow up:** 
Could you do it without any loop/recursion in O(1) runtime?

**Hint #1** 
A naive implementation of the above process is trivial. Could you come up with other methods?

**Hint #2** 
What are all the possible results?

**Hint #3** 
How do they occur, periodically or randomly?

**Hint #4** 
You may find this Wikipedia article useful.
"""

class Solution:
    def addDigits(self, num: int) -> int:
        # # Convert to string
        # lst = list(map(int, list(str(num))))
        # while len(lst) > 1:
        #     lst = list(map(int, list(str(sum(lst)))))
        # return lst[0]

        # Number theory
        # Reference: https://leetcode.com/articles/add-digits/
        # n ≡ sum of digits of n (mod 9)
        return 0 if not num else 9 if not (num % 9) else num % 9

print(Solution().addDigits(38))     # 2

