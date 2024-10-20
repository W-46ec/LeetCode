
"""
# Parsing A Boolean Expression

A **boolean expression** is an expression that evaluates to either `true` or `false`. It can be in one of the following shapes:
    - `'t'` that evaluates to `true`.
    - `'f'` that evaluates to `false`.
    - `'!(subExpr)'` that evaluates to **the logical NOT** of the inner expression `subExpr`.
    - `'&(subExpr1, subExpr2, ..., subExprn)'` that evaluates to **the logical AND** of the inner expressions `subExpr1, subExpr2, ..., subExprn` where `n >= 1`.
    - `'|(subExpr1, subExpr2, ..., subExprn)'` that evaluates to **the logical OR** of the inner expressions `subExpr1, subExpr2, ..., subExprn` where `n >= 1`.

Given a string `expression` that represents a **boolean expression**, return *the evaluation of that expression*.

It is **guaranteed** that the given expression is valid and follows the given rules.


**Example 1:** 
```
Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.
```

**Example 2:** 
```
Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.
```

**Example 3:** 
```
Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.
```

**Constraints:** 
    - `1 <= expression.length <= 2 * 10^4` 
    - expression[i] is one following characters: `'('`, `')'`, `'&'`, `'|'`, `'!'`, `'t'`, `'f'`, and `','`.
"""

import unittest
from functools import reduce

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        val = {'t': True, 'f': False}
        ops = {
            '!': lambda lst: not lst[0],
            '&': lambda lst: reduce(lambda x, y: x and y, lst),
            '|': lambda lst: reduce(lambda x, y: x or y, lst),
        }
        stack = []
        for c in expression:
            # A ')' indicates that we have reached the end of an expression
            # So we can start evaluating it
            if c == ')':
                args = []
                while stack[-1] in [True, False]:
                    args += [stack.pop()]
                operator = stack.pop()
                stack.append(ops[operator](args))
            elif c in val:
                stack.append(val[c])
            elif c in ops:
                stack.append(c)
        return stack[0]


class Test(unittest.TestCase):
    def setUp(self):
        self.soln_obj = Solution()

    def testcase1(self):
        self.assertEqual(self.soln_obj.parseBoolExpr("&(|(f))"), False)

    def testcase2(self):
        self.assertEqual(self.soln_obj.parseBoolExpr("|(f,f,f,t)"), True)

    def testcase3(self):
        self.assertEqual(self.soln_obj.parseBoolExpr("!(&(f,t))"), True)

    def testcase4(self):
        self.assertEqual(self.soln_obj.parseBoolExpr("|(&(|(f,f,t),!(t)),&(t,t))"), True)


if __name__ == '__main__':
    unittest.main()
