
/*
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
*/

#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> S;
        unordered_map<string, int (*)(const int &x, const int&y)> operations;
        operations[string("+")] = [](const int &x, const int&y) { return x + y; };
        operations[string("-")] = [](const int &x, const int&y) { return x - y; };
        operations[string("*")] = [](const int &x, const int&y) { return x * y; };
        operations[string("/")] = [](const int &x, const int&y) { return x / y; };
        for (unsigned i = 0; i < tokens.size(); i++) {
            if (operations.find(tokens[i]) != operations.end()) {
                int y = S.top();
                S.pop();
                int x = S.top();
                S.pop();
                S.push(operations[tokens[i]](x, y));
            } else {
                int sign = 1, val = 0;
                for (unsigned j = 0; j < tokens[i].length(); j++) {
                    if (tokens[i][j] == '-') {
                        sign = -1;
                    } else {
                        val = val * 10 + tokens[i][j] - 48;
                    }
                }
                S.push(val * sign);
            }
        }
        return S.top();
    }
};

int main(int argc, char *argv[]) {
    Solution obj;

    // 9
    vector<string> vec = {"2", "1", "+", "3", "*"};
    cout << obj.evalRPN(vec) << endl;

    // 6
    vec = vector<string> {"4", "13", "5", "/", "+"};
    cout << obj.evalRPN(vec) << endl;

    // 22
    vec = vector<string> {"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"};
    cout << obj.evalRPN(vec) << endl;

    // -1
    vec = vector<string> {"3", "-4", "+"};
    cout << obj.evalRPN(vec) << endl;

    return 0;
}

