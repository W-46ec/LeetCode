
"""
# Implement Rand10() Using Rand7()

Given a function `rand7` which generates a uniform random integer in the range 1 to 7, write a function `rand10` which generates a uniform random integer in the range 1 to 10.

Do NOT use system's `Math.random()`.


**Example 1:** 
```
Input: 1
Output: [7]
```

**Example 2:** 
```
Input: 2
Output: [8,4]
```

**Example 3:** 
```
Input: 3
Output: [8,1,10]
```

**Note:** 
```
rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.
```

**Follow up:** 
    1. What is the expected value for the number of calls to `rand7()` function?
    2. Could you minimize the number of calls to `rand7()`?
"""

from random import randint

def rand7():
    return randint(1, 7)

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row, column = rand7(), rand7()
            num = column + (row - 1) * 7
            if num <= 40:
                break
        return 1 + (num % 10)

print(Solution().rand10())
