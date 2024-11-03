
/*
# Rotate String

Given two strings `s` and `goal`, return *`true` if and only if `s` can become `goal` after some number of **shifts** on `s`*.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

- For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.
 

**Example 1:** 
```
Input: s = "abcde", goal = "cdeab"
Output: true
```

**Example 2:** 
```
Input: s = "abcde", goal = "abced"
Output: false
```

**Constraints:** 
    - `1 <= s.length, goal.length <= 100` 
    - `s` and `goal` consist of lowercase English letters.
*/

#include <iostream>

using namespace std;

class Solution {
private:
    bool compare(const string &s1, const string &s2, unsigned idx1, unsigned idx2, unsigned len) {
        for (unsigned i = 0; i < len; i++) {
            if (s1[idx1 + i] != s2[idx2 + i]) {
                return false;
            }
        }
        return true;
    }
public:
    bool rotateString(string s, string goal) {
        if (s.length() != goal.length()) {
            return false;
        }
        unsigned i = 0;
        while (i < s.length()) {
            while (i < s.length() && s[i] != goal[0]) {
                i++;
            }
            if (compare(s, goal, i, 0, s.length() - i) 
                && compare(s, goal, 0, s.length() - i, i)) {
                return true;
            }
            i++;
        }
        return false;
    }
};


int main(int argc, char *argv[]) {
    Solution obj;
    cout << obj.rotateString(string("abcde"), string("cdeab")) << endl; // 1
    cout << obj.rotateString(string("abcde"), string("abced")) << endl; // 0
    cout << obj.rotateString(string("a"), string("aaa")) << endl;       // 0
    cout << obj.rotateString(string("abc"), string("c")) << endl;       // 0
    cout << obj.rotateString(string("abc"), string("cab")) << endl;     // 1
    cout << obj.rotateString(string("a"), string("a")) << endl;         // 1
    return 0;
}
