
/*
# First Unique Character in a String

Given a string `s`, *find the first non-repeating character in it and return its index*. If it does not exist, return `-1`.


**Example 1:** 
```
Input: s = "leetcode"
Output: 0
```

**Example 2:** 
```
Input: s = "loveleetcode"
Output: 2
```

**Example 3:** 
```
Input: s = "aabb"
Output: -1
```

**Constraints:** 
    - `1 <= s.length <= 10^5` 
    - `s` consists of only lowercase English letters.
*/

#include <iostream>
#include <string>
#include <cstring>

using namespace std;

class Solution {
private:
    unsigned counter[26];
public:
    int firstUniqChar(string s) {
        memset(counter, 0, sizeof(unsigned) * 26);
        for (unsigned i = 0; i < s.length(); i++) {
            counter[s[i] - 97]++;
        }
        for (unsigned i = 0; i < s.length(); i++) {
            if (counter[s[i] - 97] == 1) {
                return i;
            }
        }
        return -1;
    }
};

int main(int argc, char *argv[]) {
    Solution obj;
    cout << obj.firstUniqChar(string("leetcode")) << endl;      // 0
    cout << obj.firstUniqChar(string("loveleetcode")) << endl;  // 2
    cout << obj.firstUniqChar(string("aabb")) << endl;          // -1
    cout << obj.firstUniqChar(string("aadadaad")) << endl;      // -1
    return 0;
}
