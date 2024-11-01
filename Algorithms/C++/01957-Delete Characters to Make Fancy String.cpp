
/*
# Delete Characters to Make Fancy String

A **fancy string** is a string where no **three consecutive** characters are equal.

Given a string `s`, delete the **minimum** possible number of characters from `s` to make it **fancy**.

Return *the final string after the deletion*. It can be shown that the answer will always be **unique**.


**Example 1:** 
```
Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
```

**Example 2:** 
```
Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
```

**Example 3:** 
```
Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
```

**Constraints:** 
    - `1 <= s.length <= 10^5` 
    - `s` consists only of lowercase English letters.
*/

#include <iostream>

using namespace std;

class Solution {
public:
    string makeFancyString(string s) {
        unsigned i = 0, j = 0;
        string ans = "";
        while (i < s.length()) {
            j = i + 1;
            while (j < s.length() && s[j] == s[i]) {
                j++;
            }
            ans += s[i];
            if (j - i > 1) {
                ans += s[i];
            }
            i = j;
        }
        return ans;
    }
};


int main(int argc, char *argv[]) {
    Solution obj;
    cout << obj.makeFancyString(string("leeetcode")) << endl;   // "leetcode"
    cout << obj.makeFancyString(string("aaabaaaa")) << endl;    // "aabaa"
    cout << obj.makeFancyString(string("aab")) << endl;         // "aab"
    cout << obj.makeFancyString(string("a")) << endl;           // "a"
    cout << obj.makeFancyString(string("aaaaaaaa")) << endl;    // "a"
    return 0;
}
