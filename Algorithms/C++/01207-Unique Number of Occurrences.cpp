
/*
# Unique Number of Occurrences

Given an array of integers `arr`, return *`true` if the number of occurrences of each value in the array is **unique** or `false` otherwise.


**Example 1:** 
```
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
```

**Example 2:** 
```
Input: arr = [1,2]
Output: false
```

**Example 3:** 
```
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
```

**Constraints:** 
    - `1 <= arr.length <= 1000` 
    - `-1000 <= arr[i] <= 1000`
*/

#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> freq;
        for (auto it = arr.begin(); it != arr.end(); it++) {
            freq[*it]++;
        }

        unordered_set<int> occurences;
        for (auto it = freq.begin(); it != freq.end(); it++) {
            occurences.insert(it -> second);
        }

        return freq.size() == occurences.size();
    }
};

int main(int argc, char *argv[]) {
    Solution soln;
    vector<int> arr = {1, 2, 2, 1, 1, 3};
    cout << soln.uniqueOccurrences(arr) << endl;    // 1

    return 0;
}
