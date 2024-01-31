
"""
# Evaluate Reverse Polish Notation

You are given an array of strings `tokens` that represents an arithmetic expression in a [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

Evaluate the expression. Return *an integer that represents the value of the expression*.

**Note** that:
    - The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
    - Each operand may be an integer or another expression.
    - The division between two integers always **truncates toward zero**.
    - There will not be any division by zero.
    - The input represents a valid arithmetic expression in a reverse polish notation.
    - The answer and all the intermediate calculations can be represented in a **32-bit** integer.
 

**Example 1:** 
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Example 2:** 
```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

**Example 3:** 
```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

**Constraints:** 
    - `1 <= tokens.length <= 10^4` 
    - `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.
"""

import unittest
from typing import List

class Solution:
    operations = {
        '+': lambda x, y: x + y, 
        '-': lambda x, y: x - y, 
        '*': lambda x, y: x * y, 
        '/': lambda x, y: int(x / y)
    }
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in self.operations:
                l, r = stack[-2], stack[-1]
                stack[len(stack) - 2 : ] = []
                stack[len(stack) : ] = [self.operations[t](l, r)]
            else:
                stack[len(stack) : ] = [int(t)]
        return stack[0]


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.evalRPN(["2", "1", "+", "3", "*"]), 9)

    def testcase2(self):
        self.assertEqual(self.soln_obj.evalRPN(["4", "13", "5", "/", "+"]), 6)

    def testcase3(self):
        self.assertEqual(self.soln_obj.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)

    def testcase4(self):
        self.assertEqual(self.soln_obj.evalRPN(["3", "-4", "+"]), -1)


if __name__ == '__main__':
    unittest.main()

