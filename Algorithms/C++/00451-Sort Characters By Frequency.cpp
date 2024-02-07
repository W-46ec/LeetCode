
/*
# Sort Characters By Frequency

Given a string `s`, sort it in **decreasing order** based on the **frequency** of the characters. The **frequency** of a character is the number of times it appears in the string.

Return *the sorted string*. If there are multiple answers, return *any of them*.


**Example 1:** 
```
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
```

**Example 2:** 
```
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
```

**Example 3:** 
```
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
```

**Constraints:** 
    - `1 <= s.length <= 5 * 10^5` 
    - `s` consists of uppercase and lowercase English letters and digits.
*/

#include <iostream>
#include <unordered_map>
#include <queue>
#include <cstring>

using namespace std;

class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, unsigned> freq;
        for (unsigned i = 0; i < s.length(); i++) {
            freq[s[i]]++;
        }

        priority_queue<pair<unsigned, char>> max_heap;
        for (auto it = freq.begin(); it != freq.end(); it++) {
            max_heap.push({it -> second, it -> first});
        }

        string res = "";
        char *buffer = new char[max_heap.top().first + 1];
        while (max_heap.size()) {
            memset(buffer, max_heap.top().second, max_heap.top().first);
            buffer[max_heap.top().first] = '\0';
            res.append(buffer);
            max_heap.pop();
        }
        delete[] buffer;
        return res;
    }
};


int main(int argc, char *argv[]) {
    Solution obj;

    // eetr
    cout << obj.frequencySort(string("tree")) << endl;

    // cccaaa
    cout << obj.frequencySort(string("cccaaa")) << endl;

    // bbaA
    cout << obj.frequencySort(string("Aabb")) << endl;

    // eeeeoollvtdc
    cout << obj.frequencySort(string("loveleetcode")) << endl;

    // sssssssffffff44444aaaa55522
    cout << obj.frequencySort(string("2a554442f544asfasssffffasss")) << endl;

    return 0;
}

