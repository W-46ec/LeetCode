
/*
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
*/

#include <iostream>
#include <string>
#include <stack>

using namespace std;

class Solution {
public:
    bool parseBoolExpr(string expression) {
        stack<char> S;
        for (unsigned i = 0; i < expression.length(); i++) {
            if (expression[i] == ')') {
                bool has_true = false, has_false = false;
                while (S.top() == 't' || S.top() == 'f') {
                    has_true |= (S.top() == 't');
                    has_false |= (S.top() == 'f');
                    S.pop();
                }
                char op = S.top();
                S.pop();
                if (op == '!') {
                    S.push(has_false ? 't' : 'f');
                } else if (op == '&') {
                    S.push(has_false ? 'f' : 't');
                } else {
                    S.push(has_true ? 't' : 'f');
                }
            } else if (expression[i] == '!' || expression[i] == '&' || expression[i] == '|'
                    || expression[i] == 't' || expression[i] == 'f') {
                S.push(expression[i]);
            }
        }
        return S.top() == 't';
    }
};

int main(int argc, char *argv[]) {
    Solution obj;

    // 0
    string expr = "&(|(f))";
    cout << obj.parseBoolExpr(expr) << endl;

    // 1
    expr = "|(f,f,f,t)";
    cout << obj.parseBoolExpr(expr) << endl;

    // 1
    expr = "!(&(f,t))";
    cout << obj.parseBoolExpr(expr) << endl;

    // 1
    expr = "|(&(|(f,f,t),!(t)),&(t,t))";
    cout << obj.parseBoolExpr(expr) << endl;

    // 1
    expr = "!(f)";
    cout << obj.parseBoolExpr(expr) << endl;

    return 0;
}
