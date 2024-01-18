
/*
# Climbing Stairs

You are climbing a stair case. It takes *n* steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Example 1:** 
```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2:** 
```
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

**Constraints:** 
    - `1 <= n <= 45` 

**Hint #1** 
To reach nth step, what could have been your previous steps? (Think about the step sizes)
*/

#include <iostream>

using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        long a = 1, b = 2;
        for (int i = 1; i < n; i++) {
            long c = a + b;
            a = b;
            b = c;
        }
        return a;
    }
};

int main(int argc, char *argv[]) {
    Solution obj;
    for (int i = 1; i <= 45; i++) {
        cout << "climbStairs(" << i << "): " << obj.climbStairs(i) << endl;
    }
    return 0;
}
