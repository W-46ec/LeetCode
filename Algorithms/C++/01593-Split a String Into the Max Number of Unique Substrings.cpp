
/*
# Split a String Into the Max Number of Unique Substrings

Given a string `s`, return *the maximum number of unique substrings that the given string can be split into*.

You can split string `s` into any list of **non-empty substrings**, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are **unique**.

A **substring** is a contiguous sequence of characters within a string.


**Example 1:** 
```
Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
```

**Example 2:** 
```
Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
```

**Example 3:** 
```
Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
```

**Constraints:** 
    `1 <= s.length <= 16` 
*/

#include <iostream>
#include <unordered_set>

using namespace std;

class Solution {
private:
    unordered_set<string> seen;
    int max_count;

    void solve(const string &s, unsigned i = 0, int count = 0) {
        if (i >= s.length()) {
            max_count = max(max_count, count);
        }
        for (unsigned j = i + 1; j <= s.length(); j++) {
            string sub_str = s.substr(i, j - i);
            if (seen.find(sub_str) == seen.end()) {
                seen.insert(sub_str);
                solve(s, j, count + 1);
                seen.erase(sub_str);
            }
        }
    }

public:
    int maxUniqueSplit(string s) {
        this -> max_count = 1;
        this -> solve(s);
        return this -> max_count;
    }
};


int main(int argc, char *argv[]) {
    Solution obj;

    string s = "ababccc";
    cout << obj.maxUniqueSplit(s) << endl;  // 5

    s = "aba";
    cout << obj.maxUniqueSplit(s) << endl;  // 2

    s = "aa";
    cout << obj.maxUniqueSplit(s) << endl;  // 1

    s = "abcdefgghhh";
    cout << obj.maxUniqueSplit(s) << endl;  // 9

    return 0;
}
