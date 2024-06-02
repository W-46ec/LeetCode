
/*
# Reverse String

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with `O(1)` extra memory.


**Example 1:** 
```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Example 2:** 
```
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

**Constraints:** 
    - `1 <= s.length <= 10^5` 
    - `s[i]` is a [printable ascii character](https://en.wikipedia.org/wiki/ASCII#Printable_characters).
*/

#include <iostream>
#include <vector>
#include "util.h"

using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
        for (unsigned i = 0; i < s.size() / 2; i++) {
            char tmp = s[i];
            s[i] = s[s.size() - i - 1];
            s[s.size() - i - 1] = tmp;
        }
    }
};

int main(int argc, char *argv[]) {
    Solution obj;
    vector<char> s = {'h', 'e', 'l', 'l', 'o'};
    obj.reverseString(s);
    print<char>(s, "\n", '\''); // {'o', 'l', 'l', 'e', 'h'}


    s = vector<char>{'H', 'a', 'n', 'n', 'a', 'h'};
    obj.reverseString(s);
    print<char>(s, "\n", '\''); // {'h', 'a', 'n', 'n', 'a', 'H'}

    return 0;
}

