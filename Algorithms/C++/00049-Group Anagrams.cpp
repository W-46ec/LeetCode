
/*
# Group Anagrams

Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


**Example 1:** 
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2:** 
```
Input: strs = [""]
Output: [[""]]
```

**Example 3:** 
```
Input: strs = ["a"]
Output: [["a"]]
```

**Constraints:** 
    - `1 <= strs.length <= 10^4` 
    - `0 <= strs[i].length <= 100` 
    - `strs[i]` consists of lowercase English letters.
*/

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include "util.h"

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams;
        for (unsigned i = 0; i < strs.size(); i++) {
            string key = strs[i];
            sort(key.begin(), key.end());
            anagrams[key].push_back(strs[i]);
        }
        vector<vector<string>> groups;
        for (auto it = anagrams.begin(); it != anagrams.end(); it++) {
            groups.push_back(it -> second);
        }
        return groups;
    }
};


int main(int argc, char *argv[]) {
    Solution obj;

    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    // {{"bat"}, {"tan", "nat"}, {"eat", "tea", "ate"}}
    print<string>(obj.groupAnagrams(strs), "\n", '"');

    strs = vector<string>{""};
    // {{""}}
    print<string>(obj.groupAnagrams(strs), "\n", '"');

    strs = vector<string>{"a"};
    // {{"a"}}
    print<string>(obj.groupAnagrams(strs), "\n", '"');

    return 0;
}
